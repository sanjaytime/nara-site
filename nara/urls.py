"""nara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

# router = routers.DefaultRouter()                      # add this
# router.register(r'todos', views.TodoView, 'todo')     # add this

# urlpatterns = [
#     path('admin/', admin.site.urls),         path('api/', include(router.urls))                # add this
# ]
# urlpatterns = patterns('',
# url(r'^admin/', include(admin.site.urls)),
# url(r'^polls/', include('todo.urls')),
# )


urlpatterns = [
    path('',include('stills.urls')),
    path('projects/', include('projects.urls')),
    path('admin/', admin.site.urls),
    # path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path('beats/', include('beats.urls')),
    path("markdownx/", include('markdownx.urls')),
]
# noinspection PyPackageRequirements
