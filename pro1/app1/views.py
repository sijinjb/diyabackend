from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from app1.models import Blog, Image
from app1.serializers import BlogSerializer, ImageSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()  # All images in the database
    serializer_class = ImageSerializer

    # Custom action for fetching image details (optional)
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        image = self.get_object()  # Get the image by primary key
        serializer = self.get_serializer(image)
        return Response(serializer.data)
        

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        blog = self.get_object()
        serializer = self.get_serializer(blog)
        return Response(serializer.data)