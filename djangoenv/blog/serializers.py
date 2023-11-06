from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'text', 'created_date', 'published_date', 'image_url')

    def get_image_url(self, post):
        request = self.context.get('request')
        image_url = post.image.url if post.image else None
        return request.build_absolute_uri(image_url) if image_url else None

