from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from accounts.views import UserRegistrationView
from links.views import HomeView, NewSubmissionView, SubmissionDetailView, NewCommentView,                         NewCommentReplyView, UpvoteSubmissionView, RemoveUpvoteFromSubmissionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(),
         kwargs={'template_name': 'login.html'}, name='login'),
    path('logout/', LogoutView.as_view(),
         kwargs={'next_page': '/login/'}, name='logout'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),

    path('new-submission/', NewSubmissionView.as_view(), name='new-submission'),
    path('submission/<int:pk>/', SubmissionDetailView.as_view(),
         name='submission-detail'),
    path('new-comment/', NewCommentView.as_view(), name='new-comment'),
    path('new-comment-reply/', NewCommentReplyView.as_view(),
         name='new-comment-reply'),

    path('upvote/<int:link_pk>/', UpvoteSubmissionView.as_view(),
         name='upvote-submission'),
    path('upvote/<int:pk>/remove/',
         RemoveUpvoteFromSubmissionView.as_view(), name='remove-upvote'),
]
