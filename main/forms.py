from django import forms
from django.contrib.auth.models import User
from .models import Question, Story, Comment

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password',]

class QuestionForm(forms.ModelForm):
    private = forms.BooleanField(required=False, label="Make this question private")

    class Meta:
        model = Question
        fields = ['title', 'content', 'private']

class StoryForm(forms.ModelForm):
    private = forms.BooleanField(required=False, label="Make this story private")

    class Meta:
        model = Story
        fields = ['title', 'content', 'private']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

