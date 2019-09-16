from django.contrib.auth.models import User, Group
from . import models
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'


# class ProfileSerializer(serializers.HyperlinkedModelSerializer):
#     company = CompanySerializer(many=True)
#     class Meta:
#         model = Profile
#         exclude = ['url', 'user']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # profile = ProfileSerializer()
    companies = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'companies', 'is_staff']

    def get_companies(self, obj):
        return CompanySerializer(obj.company_set.all(), many=True).data


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AnnualReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnnualRapport
        fields = '__all__'
