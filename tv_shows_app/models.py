from django.db import models

# Create your models here.
class Show(models.Model):
     title = models.CharField(max_length=32)
     network = models.CharField(max_length=16)
     release_date = models.DateField()
     description = models.TextField(max_length=255)
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)

     def __str__(self) -> str:
         return self.title

     def __repr__(self) -> str:
         return self.title

