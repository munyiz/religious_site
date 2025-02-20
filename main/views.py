
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CommentForm, SignupForm
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, StoryForm
from .models import Question, Story, User, Like
from .models import BibleBook, BibleChapter, BibleVerse


def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash password
            user.save()
            login(request, user)  # Auto login after signup
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def post_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('questions_list')
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})

@login_required
def post_story(request):
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.save()
            return redirect('stories_list')
    else:
        form = StoryForm()
    return render(request, 'post_story.html', {'form': form})

def questions_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'questions_list.html', {'questions': questions})

def stories_list(request):
    stories = Story.objects.all().order_by('-created_at')
    return render(request, 'stories_list.html', {'stories': stories})




def bible_view(request):
    books = BibleBook.objects.all()
    selected_book = request.GET.get("book", books.first().name if books else "")
    chapters = BibleChapter.objects.filter(book__name=selected_book)
    selected_chapter = request.GET.get("chapter", 1)
    verses = BibleVerse.objects.filter(chapter__book__name=selected_book, chapter__chapter_number=selected_chapter)

    return render(request, 'bible.html', {
        'books': books,
        'chapters': chapters,
        'selected_book': selected_book,
        'selected_chapter': selected_chapter,
        'verses': verses,
    })
    
@login_required
def add_comment(request, post_type, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user

            if post_type == "question":
                comment.question = Question.objects.get(id=post_id)
            elif post_type == "story":
                comment.story = Story.objects.get(id=post_id)

            comment.save()
            return redirect(request.META.get("HTTP_REFERER", "home"))
    return redirect("home")

@login_required
def like_post(request, post_type, post_id):
    if post_type == "question":
        post = Question.objects.get(id=post_id)
    else:
        post = Story.objects.get(id=post_id)

    like, created = Like.objects.get_or_create(user=request.user, question=post if post_type == "question" else None, story=post if post_type == "story" else None)

    if not created:
        like.delete()

    return redirect(request.META.get("HTTP_REFERER", "home"))

@login_required
def user_profile(request, username):
    profile_user = User.objects.get(username=username)
    questions = Question.objects.filter(user=profile_user)
    stories = Story.objects.filter(user=profile_user)
    liked_questions = Question.objects.filter(like__user=profile_user)
    liked_stories = Story.objects.filter(like__user=profile_user)

    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'questions': questions,
        'stories': stories,
        'liked_questions': liked_questions,
        'liked_stories': liked_stories
    })
    

def about_view(request):
    return render(request, 'about.html')

def profile_view(request):
    return render(request, 'profile.html')


def contact_view(request):
    return render(request, 'contact.html') 










