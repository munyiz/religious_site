from django.urls import path
from .views import (
    home_view, live_meeting, signup_view, login_view, logout_view, post_question, post_story,
    questions_list, stories_list, add_comment, like_post, user_profile,
    about_view, profile_view, contact_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('post-question/', post_question, name='post_question'),
    path('post-story/', post_story, name='post_story'),
    path('questions/', questions_list, name='questions_list'),
    path('stories/', stories_list, name='stories_list'),
    path('add-comment/<str:post_type>/<int:post_id>/', add_comment, name='add_comment'),
    path('like/<str:post_type>/<int:post_id>/', like_post, name='like_post'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('about/', about_view, name='about'),
    path('profile/', profile_view, name='profile'),
    path('contact/', contact_view, name='contact'),
    path("meet/", live_meeting, name="meet"),
]
