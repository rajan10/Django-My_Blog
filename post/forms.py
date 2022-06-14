from django import forms
from django.forms import ModelForm, Textarea
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','image','content']
        # overriding the default fields
        #  ModelForm gives you the flexibility of changing the form field for a given model.
        widgets ={

            'content':Textarea(attrs={'cols':50, 'rows':10}),
                    }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        widgets={
            'content':Textarea(attrs={'cols':50, 'rows':10}),
        }

# class CommentForm(forms.Form):
#
#     # model view  content only
#     commentor=forms.CharField(required=True)
#     post=forms.CharField(required=True)
#     content=forms.CharField(required=True)


