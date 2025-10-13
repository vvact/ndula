from rest_framework import serializers
from .models import Sneaker, SneakerImage

class SneakerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SneakerImage
        fields = ['id', 'image_url']


class SneakerSerializer(serializers.ModelSerializer):
    images = SneakerImageSerializer(many=True, read_only=True)

    class Meta:
        model = Sneaker
        fields = [
            'id', 'name', 'brand', 'price', 'description',
            'main_image', 'sizes', 'available', 'created_at', 'images'
        ]
