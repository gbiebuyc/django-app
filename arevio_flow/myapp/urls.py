from django.contrib import admin
from django.urls import path, include, re_path
from .views import IndexTemplateView

urlpatterns = [
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]