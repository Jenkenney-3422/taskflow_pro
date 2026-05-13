from django.db import models
from cloudinary.models import CloudinaryField

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    # Cloudinary handles the image/file upload
    attachment = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.title