from django.urls import path, include, re_path
from rest_framework import routers
from .views import IndexTemplateView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('userdata/', views.userdata, name='userdata'),
    path('annualreports/', views.AnnualReportList.as_view()),
    path('annualreports/<int:pk>/', views.AnnualReportDetail.as_view()),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]
