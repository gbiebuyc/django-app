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
    updated_by_user = serializers.SerializerMethodField()

    class Meta:
        model = models.AnnualReport
        fields = '__all__'

    def get_updated_by_user(self, obj):
        if not obj.updated_by_user:
            return 'n/a'
        return obj.updated_by_user.username
