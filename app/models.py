from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=50)
    comment = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
