from django.contrib.auth.models import User, Group
from . import models
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'


class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Taxonomy
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'is_staff']


class AnnualReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnnualReport
        fields = '__all__'
