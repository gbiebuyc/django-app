from django.contrib.auth.models import User, Group
from . import models
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Companies are nested in UserSerializer to save HTTP requests.
    companies = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'companies', 'is_staff']

    def get_companies(self, obj):
        # Admin can access all companies of the database
        if obj.is_superuser:
            companies = models.Company.objects.all()
        else:
            companies = obj.company_set.all()
        return CompanySerializer(companies, many=True).data


class AnnualReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnnualRapport
        fields = '__all__'
