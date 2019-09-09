from django.urls import path, include, re_path
from rest_framework import routers
from .views import IndexTemplateView
from . import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'profiles', views.ProfileViewSet)
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/me/', views.CurrentUserView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]
