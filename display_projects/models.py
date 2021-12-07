from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class ProjectModel(models.Model):
    creator = models.ForeignKey(User, blank=True, null=True, related_name="creator", on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    screenshot = models.ImageField(upload_to="screenshots")
    description = models.TextField(default="Enter the description here")
    link = models.URLField(blank=True, null=True)
    likes_count = models.PositiveIntegerField(default=0)
    views_count = models.PositiveIntegerField(default=0)



    def __str__(self) -> str:
        return self.creator.username + " - " + self.title


class ProjectRating(models.Model):
    user = models.ForeignKey(
        User, related_name="user_rating", on_delete=CASCADE)
    project = models.ForeignKey(
        ProjectModel, related_name="rated_project", on_delete=CASCADE)
    like = models.BooleanField(default=False)
    view = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "project")

    def __str__(self) -> str:
        return self.user.username + " - " + self.project.title +" rating model"

class Comment(models.Model): 
    post = models.ForeignKey(ProjectModel,on_delete=models.CASCADE,related_name='comments')
    comment=models.CharField(max_length=100,null=False)
    commentor = models.ForeignKey(User, related_name='commentor', null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    likes_count = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.commentor, self.post) 
    
class CommentRating(models.Model):
    user = models.ForeignKey(User, related_name="user_comment", on_delete=CASCADE)
    comment = models.ForeignKey(Comment, related_name="rated_comment", on_delete=CASCADE)
    like = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "comment")

    def __str__(self) -> str:
        return self.user.username + " - " + self.project.title +" comment model"