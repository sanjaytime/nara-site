from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<title>/", views.post_detail, name="post_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]