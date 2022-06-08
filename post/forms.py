from django import forms
from .models import Post, Comment



class PostForm(forms.Form):
    author=forms.CharField(required=True)
    title=forms.CharField(required=True)
    image=forms.ImageField()
    content=forms.CharField(required=True)
    created_date=forms.DateTimeField()

class CommentForm(forms.Form):
    commentor=forms.CharField(required=True)
    post=forms.CharField(required=True)
    content=forms.CharField(required=True)



