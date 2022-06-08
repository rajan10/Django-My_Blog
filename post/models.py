from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="authors")
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    content=models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}:{self.title}"


class Comment(models.Model):
    commentor=models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentors")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    content=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.commentor.username}:{self.content}"