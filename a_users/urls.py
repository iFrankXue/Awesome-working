from django.urls import path
from .views import *

urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit/', profile_edit_view, name='profile-edit'),
    path('delete/', profile_delete_view, name='profile-delete'),
    path('<str:username>/', profile_view, name='user-profile'),
]
