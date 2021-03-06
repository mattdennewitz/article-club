import collections
import itertools
import operator

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

import urltools
import bundles.alchemy_utils

from ...models import COMFORT_LEVELS, Bundle, Link, BundleLink
from .serializers import (BundleSerializer, LinkSerializer,
                          BundleLinkSerializer)


class CreateBundleView(generics.CreateAPIView):
    """Creates a new bundle
    """
    serializer_class = BundleSerializer

    def create(self, request, *a, **kw):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(curator_id=1)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


@api_view(http_method_names=['POST'])
def add_link_to_bundle(request, bundle_id):
    """Adds a URL to an existing bundle.

    1. Ensure bundle exists or raise 404
    2. Get or create `Link` object for URL
    3. Add `Link` object to bundle (if not already a member)
    4. Return empty `201 Created` response
    """

    # ensure bundle exists
    bundle = get_object_or_404(Bundle, id=bundle_id)

    # get/create link for given url
    url = request.data.get('url', None)

    # validate url is a url
    v = URLValidator()

    try:
        v(url)
    except ValidationError as exc:
        # the user must be joking
        return Response({'error': True, 'msg': 'Invalid URL'}, status=400)

    # assert that "comfort_level" is specified.
    # this is validated outside of the `Link` fields handled by
    # DRF serializer validation.
    comfort_level = int(request.data.get('comfort_level', None))
    if comfort_level not in [i[0] for i in COMFORT_LEVELS]:
        return Response({'error': True,
                        'msg': 'Please specify a reader comfort level'
                        })

    url = urltools.normalize(url)

    try:
        # fetch existing link
        link = Link.objects.get(url=url)
    except Link.DoesNotExist:
        # create a new link
        link_serializer = LinkSerializer(data=request.data)
        link_serializer.is_valid(raise_exception=True)
        link = link_serializer.save()

    # add link to bundle
    if not BundleLink.objects.filter(bundle=bundle, link=link).exists():
        # call alchemy util to fetch concepts for URL
        concepts = bundles.alchemy_utils.get_concepts(url)
        this_bundle = BundleLink.objects.create(bundle=bundle,
                                  link=link,
                                  comfort_level=comfort_level,
                                  curator_id=1)
        for concept in concepts:
            this_bundle.tags.add(concept)

    return Response('', status=201)

@api_view(http_method_names=['GET'])
def find_bundles_for_url(request):
    """Fetches existing bundles for a user-specified URL.

    1. Attempt to fetch `Link` with given URL
    2. Search for any link-bundle membership with `BundleLink`
    3. Return serialized collection of bundles containing this `Link`
    """

    # get/create link for given url
    url = request.query_params.get('url', None)

    # validate url is a url
    v = URLValidator()

    try:
        v(url)
    except ValidationError as exc:
        # the user must be joking
        return Response({'error': True, 'msg': 'Invalid URL'}, status=400)

    # normalize url for tidyness
    url = urltools.normalize(url)

    try:
        link = Link.objects.get(url=url)
    except Link.DoesNotExist:
        return Response([])

    # find all bundle memberships for this link
    memberships = (BundleLink.objects
                   .filter(link=link)
                   .only('bundle_id')
                   .distinct())

    # fetch all bundle-link pairs for bundles containing this link
    bundle_ids = [m.bundle_id for m in memberships]
    all_links = (BundleLink.objects
                 .filter(bundle_id__in=bundle_ids)
                 .select_related('bundle', 'link', 'curator'))

    # group bundlelinks by bundle - <bundle: [bundlelink, ...]>
    grouped = itertools.groupby(all_links, key=operator.attrgetter('bundle'))

    output = []

    for bundle, link_list in grouped:
        setattr(bundle, 'link_list', link_list)
        serialized = BundleSerializer(bundle)
        output.append(serialized.data)

    return Response(output)
