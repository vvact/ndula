from rest_framework import serializers
from django.utils.timesince import timesince
from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'thumbnail']

    def get_image(self, obj):
        # Full image URL
        return obj.image.url if obj.image else None

    def get_thumbnail(self, obj):
        # Cloudinary thumbnail version (faster loading)
        try:
            return obj.image.build_url(width=400, height=400, crop="fill")
        except Exception:
            return obj.image.url if obj.image else None


class ProductSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True, read_only=True)
    formatted_price = serializers.SerializerMethodField()
    created_ago = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'price',
            'formatted_price',
            'main_image',
            'sizes',
            'images',
            'created_at',
            'created_ago',
            'updated_at',
        ]

    def get_main_image(self, obj):
        # Return the full Cloudinary URL for the main image
        return obj.main_image.url if obj.main_image else None

    def get_formatted_price(self, obj):
        # Example: KSh 1,000.00
        return f"KSh {obj.price:,.2f}"

    def get_created_ago(self, obj):
        # Example: "3 hours ago"
        return timesince(obj.created_at) + " ago"

    def to_representation(self, instance):
        """
        Optional cleanup — ensure sizes are sorted numerically.
        """
        data = super().to_representation(instance)
        if isinstance(data.get('sizes'), list):
            try:
                data['sizes'] = sorted(data['sizes'])
            except Exception:
                pass
        return data
