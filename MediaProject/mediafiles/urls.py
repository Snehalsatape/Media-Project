from django.urls import path
from . import views

urlpatterns = [
    path('', views.media_list, name='media_list'),  # This handles the root path for the media app
]
