from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from app1.models import Blog, Image, Scooter
from app1.serializers import BlogSerializer, ImageSerializer, ScooterSerializer

# ViewSet for Image
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()  # Fetch all images
    serializer_class = ImageSerializer

    # Optional custom action to get details of an image
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        image = self.get_object()  # Get the image by primary key
        serializer = self.get_serializer(image)
        return Response(serializer.data)


# ViewSet for Blog
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()  # Fetch all blogs
    serializer_class = BlogSerializer

    # Optional custom action to get details of a blog
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        blog = self.get_object()
        serializer = self.get_serializer(blog)
        return Response(serializer.data)


# # APIView for Scooter List
# class ScooterListView(APIView):
#     def get(self, request, *args, **kwargs):
#         scooters = Scooter.objects.all()  # Fetch all scooters
#         serializer = ScooterSerializer(scooters, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class ScooterViewSet(viewsets.ModelViewSet):
    queryset = Scooter.objects.all()  # Fetch all images
    serializer_class = ScooterSerializer

    # Optional custom action to get details of an image
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        Scooter = self.get_object()  # Get the image by primary key
        serializer = self.get_serializer(Scooter)
        return Response(serializer.data)

