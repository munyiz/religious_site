from django import views
from django.urls import path
from .views import add_comment, home_view, signup_view, login_view, logout_view,  post_question, post_story, questions_list, stories_list, bible_view, like_post, user_profile
from . import views


urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('post-question/', post_question, name='post_question'),
    path('post-story/', post_story, name='post_story'),
    path('questions/', questions_list, name='questions_list'),
    path('stories/', stories_list, name='stories_list'),
    path('bible/', bible_view, name='bible'),
    path('add-comment/<str:post_type>/<int:post_id>/', add_comment, name='add_comment'),
    path('like/<str:post_type>/<int:post_id>/', like_post, name='like_post'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('profile/', views.profile_view, name='profile'),
    path('contact/', views.contact_view, name='contact'),  # ✅ Add this line


]

    



