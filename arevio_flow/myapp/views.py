from django.views.generic.base import TemplateView
from django.conf import settings

class IndexTemplateView(TemplateView):

    def get_template_names(self):
        # if settings.DEBUG:
        #     template_name = 'index-dev.html'
        # else:
        #     template_name = 'index.html'
        template_name = 'index-dev.html'
        return template_name


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_object(self):
        if self.kwargs.get('pk') == 'me':
            self.kwargs['pk'] = self.request.user.pk
        return super().get_object()


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
