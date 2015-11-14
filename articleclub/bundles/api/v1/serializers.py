from rest_framework.serializers import ModelSerializer

from ...models import Bundle, Link, BundleLink


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ('title', 'url', 'is_public', 'read_time', 'published_at', )


class BundleSerializer(ModelSerializer):
    links = LinkSerializer(many=True)

    class Meta:
        model = Bundle
        fields = ('links', 'title', 'description', )


class BundleLinkSerializer(ModelSerializer):
    link = LinkSerializer()
    bundle = BundleSerializer()

    class Meta:
        model = BundleLink
        fields = ('link', 'bundle', 'comfort_level', )
