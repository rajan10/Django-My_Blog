from django.db import models
from django.contrib.auth.models import User

# for ckeditor

from ckeditor.fields import RichTextField



class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="authors")
    title=models.CharField(max_length=100, help_text='Type any title')
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    # content=models.CharField(max_length=1000)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True,)
    # posts is a psedo-column here      post.posts.all()   for that post, get all the comment
    class Meta:
        ordering=['-created_date']

    def __str__(self):
        return f"{self.author.username}:{self.title}"

class Comment(models.Model):
    commentor=models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentors")
    # posts=comments from reverse relationship
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    content=models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    # authors is a pseduoocolumn here     comment.authors.all()   >>>for that comment get the author name eg rajan

    class Meta:
        ordering=['-created_date']

    def __str__(self):
        return f"{self.commentor.username}:{self.content}"