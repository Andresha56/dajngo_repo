from django.db import models
# Create your models here.

class Image(models.Model):
    name=models.CharField(max_length=25)
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='image')
