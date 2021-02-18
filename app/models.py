from django.db import models

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=50)
    comment = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos")
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
