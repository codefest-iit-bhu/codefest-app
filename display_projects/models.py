from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class ProjectModel(models.Model):
    # TODO: change to teams later
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
        return 'Rating \'{}\' by \'{}\' on \'{}\''.format(self.rating, self.user, self.project)


class ProjectComment(models.Model):
    user = models.ForeignKey(
        User, related_name='user_comment', on_delete=models.CASCADE)
    project = models.ForeignKey(
        ProjectModel, related_name='commented_project', on_delete=models.CASCADE)
    comment = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return 'Comment by \'{}\' on \'{}\' at \'{}\''.format(self.user, self.project, self.created)
