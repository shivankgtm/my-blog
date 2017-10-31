from django import forms

from .models import Post, Comment
# get used to it.
# now getting used to it .... 
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        Eyehek
