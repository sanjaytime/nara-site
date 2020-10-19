from django.urls import path
from . import views

urlpatterns = [
	path('', views.beats_index, name='music_index'),
]