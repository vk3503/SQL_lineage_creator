from django.db import models

# Create your models here.
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')  # Files will be saved in the 'uploads/' directory
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name