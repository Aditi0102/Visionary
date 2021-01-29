from django.db import models

class Document(models.Model):
    vid = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.uploaded_at)
# Create your models here.
