from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    image_file = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True, null=True)  # Add a 'name' field

    def save(self, *args, **kwargs):
        if not self.name:
            # Automatically set the name field to the name of the uploaded file if it's not provided
            self.name = self.image_file.name.split('/')[-1]  # Extracts the name of the image file
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Ensure this line exists

    def __str__(self):
        return self.title
