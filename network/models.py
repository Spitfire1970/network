from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.ManyToManyField("self", blank = True, symmetrical= False, related_name= "people_followed_by")
    following = models.ManyToManyField("self", blank = True, symmetrical= False, related_name= "people_who_follow")
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creators", null=True)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True, blank=True)
    time_modified = models.DateTimeField(auto_now=True, blank=True)
    likes = models.ManyToManyField(User, blank = True)
class Comment(models.Model):
    description = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)