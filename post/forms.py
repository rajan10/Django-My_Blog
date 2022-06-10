from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','image','content']



class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']

# class CommentForm(forms.Form):
#
#     # model view  content only
#     commentor=forms.CharField(required=True)
#     post=forms.CharField(required=True)
#     content=forms.CharField(required=True)


