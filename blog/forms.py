from django import forms
from .models import Post, Comment, Menu

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('menu','parent_title','index_title','title','period','text')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('author','text')
