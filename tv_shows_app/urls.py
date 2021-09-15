"""tv_shows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('shows', views.shows),
    path('shows/new', views.new_form),
    path('shows/new_show', views.new_show),
    path('shows/<show_id>', views.info_show),
    path('shows/<show_id>/edit', views.edit_form),
    path('shows/<show_id>/edit_show', views.edit_show),
    path('shows/<show_id>/delete', views.delete_show),
]
