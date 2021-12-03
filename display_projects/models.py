from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class project(models.Model):
    creator = models.ForeignKey(
        User, blank=True, null=True, related_name="creator", on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    screenshot = models.ImageField(upload_to="screenshots")
    description = models.TextField(default="Enter the description here")
    link = models.URLField(blank=True, null=True)
    likes = models.PositiveSmallIntegerField(default=0)
    dislikes = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.creator.username + " - " + self.title
