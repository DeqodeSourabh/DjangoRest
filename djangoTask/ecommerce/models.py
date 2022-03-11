from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Singer(models.Model):
#     name = models.CharField(max_length=40)
#     gender = models.CharField(max_length=10)
#     def __str__(self):
#         return self.name

class Song(models.Model):
    title = models.CharField(max_length=30)
    # singer1 = models.ForeignKey(
    #     User, on_delete=models.CASCADE, 
    #     related_name='sungby1', null=True, blank=True)

    cloths = models.ForeignKey(
        'self', on_delete=models.CASCADE, 
        related_name='sungby', null=True, blank=True)

    def __str__(self):
        return self.title
   