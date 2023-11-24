from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['nomeFilme', 'opiniao', 'categories']
        widgets = {'categories': forms.CheckboxSelectMultiple}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
