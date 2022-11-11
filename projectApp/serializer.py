from .models import ProductMain,ProductColor,productImage
from rest_framework import serializers

class ProductMainSerializer(serializers.ModelSerializer):
    colors = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    class Meta:
        model = ProductMain
        fields = '__all__'
    def get_colors(self, obj):
        data = ProductColorSerializer(obj.color.all(), many=True).data
        return data
    def get_images(self, obj):
        data = ProductImageSerializer(obj.image.all(), many=True).data
        return data    

class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = productImage
        fields = '__all__'
    