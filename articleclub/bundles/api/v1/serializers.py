from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer

from ...models import Bundle, Link, BundleLink


class CuratorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ('title', 'url', 'is_public', 'read_time', 'published_at', )


class BundleLinkSerializer(ModelSerializer):
    link = LinkSerializer()
    curator = CuratorSerializer()

    class Meta:
        model = BundleLink
        fields = ('link', 'curator', 'comfort_level', )


class BundleSerializer(ModelSerializer):
    link_list = BundleLinkSerializer(many=True)

    class Meta:
        model = Bundle
        fields = ('link_list', 'title', 'description', )
