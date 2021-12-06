from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class ProjectModel(models.Model):
    creator = models.ForeignKey(
        User, blank=True, null=True, related_name="creator", on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    screenshot = models.ImageField(upload_to="screenshots")
    description = models.TextField(default="Enter the description here")
    link = models.URLField(blank=True, null=True)
    # likes = models.PositiveSmallIntegerField(default=0)
    # dislikes = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.creator.username + " - " + self.title


class ProjectRating(models.Model):
    user = models.ForeignKey(
        User, related_name="user_rating", on_delete=CASCADE)
    project = models.ForeignKey(
        ProjectModel, related_name="rated_project", on_delete=CASCADE)

    # like -> true, dislike -> false, neither -> null/delete row.
    rating = models.BooleanField(null=True)

    class Meta:
        unique_together = ("user", "project")

    def __str__(self) -> str:
        return self.user.username + " - " + self.project.title + str(self.rating)
