from django.contrib.auth.models import User, Group
from .models import Profile, Company
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer(many=True)
    class Meta:
        model = Profile
        exclude = ['url', 'user']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'profile']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
