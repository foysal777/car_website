from django import forms
from .models import CommentModel

class comment_form(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name' , 'email' , 'comment_here']
