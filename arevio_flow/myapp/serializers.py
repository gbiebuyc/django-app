from django.contrib.auth.models import User, Group
from . import models
from rest_framework import serializers
from django.conf import settings
import os
import shutil

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

    def create(self, validated_data):
        obj = super().create(validated_data)
        shutil.copy(
            os.path.join(settings.BASE_DIR, 'xbrl_reports', 'empty-qrs.xbrl.original'),
            os.path.join(settings.BASE_DIR, 'xbrl_reports', f'{obj.id}.xbrl'),
        )
        return obj
