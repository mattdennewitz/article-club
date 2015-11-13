from rest_framework.serializers import ModelSerializer

from ...models import Bundle, Link, BundleLink


class BundleSerializer(ModelSerializer):
    class Meta:
        fields = ('title', 'description', )
        model = Bundle


class LinkSerializer(ModelSerializer):
    class Meta:
        fields = ('title', 'url', 'is_public', 'read_time', 'published_at', )
        model = Link


class BundleLink(ModelSerializer):
    link = LinkSerializer()
    bundle = BundleSerializer()

    class Meta:
        fields = ('link', 'bundle', 'comfort_level', )
