from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    """
    Entry point view for the frontend.
    """
    def get_template_names(self):
        # if settings.DEBUG:
        #     template_name = 'index-dev.html'
        # else:
        #     template_name = 'index.html'
        template_name = 'index-dev.html'
        return template_name


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from . import serializers, models, permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.UserViewPermission,)

    def get_object(self):
        if self.kwargs.get('pk') == 'me':
            self.kwargs['pk'] = self.request.user.pk
        return super().get_object()


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = (permissions.CompanyViewPermission,)

class AnnualReportViewSet(viewsets.ModelViewSet):
    queryset = models.AnnualRapport.objects.all().order_by("-created_at")
    serializer_class = serializers.AnnualReportSerializer
    permission_classes = (permissions.AnnualReportViewPermission,)

    def get_queryset(self):
        # Gets all reports from all companies the user has access to.
        companies = models.Company.objects.all()
        if not self.request.user.is_superuser:
            companies = companies.filter(users=self.request.user)
        return self.queryset.filter(company__in=companies)

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('entry-point')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
