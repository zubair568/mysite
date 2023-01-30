from django import forms
from .models import Member, Post

class Form(forms.ModelForm):
      class Meta:
         model = Member
         fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
