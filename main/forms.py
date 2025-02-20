from django import forms
from django.contrib.auth.models import User
from .models import Question, Story, Comment

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

