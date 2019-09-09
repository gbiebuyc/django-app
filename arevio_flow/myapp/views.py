from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexTemplateView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        # if settings.DEBUG:
        #     template_name = 'index-dev.html'
        # else:
        #     template_name = 'index.html'
        template_name = 'index-dev.html'
        return template_name


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from . import serializers, models


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer

    def get_object(self):
        if self.kwargs.get('pk') == 'me':
            self.kwargs['pk'] = self.request.user.pk
        return super().get_object()


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = models.Profile.objects.all()
#     serializer_class = serializers.ProfileSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CurrentUserView(APIView):
    def get(self, request):
        if (request.user.is_authenticated == False):
            return Response({'error': 'not authenticated'})
        serializer = serializers.UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)

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
