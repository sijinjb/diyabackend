from rest_framework import serializers
from app1.models import Image, Blog

class ImageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='image.name', read_only=True)  # Add name field for image

    class Meta:
        model = Image
        fields = '__all__'  # Keep all existing fields
        # Alternatively, you can specify explicit fields if you want only specific ones
        # fields = ['id', 'image', 'name'] 

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
