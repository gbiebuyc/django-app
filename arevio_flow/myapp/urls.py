from django.urls import path, include, re_path
from rest_framework import routers
from .views import IndexTemplateView
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]