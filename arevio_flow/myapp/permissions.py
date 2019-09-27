from rest_framework import permissions
from django.shortcuts import get_object_or_404
from . import models

class CompanyViewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action == 'retrieve' or request.user.is_superuser
    def has_object_permission(self, request, view, companyObj):
        return (request.user in companyObj.users.all() or
            request.user.is_superuser)

class UserViewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action == 'retrieve' or request.user.is_superuser
    def has_object_permission(self, request, view, userObj):
        return request.user == userObj or request.user.is_superuser

class AnnualReportViewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if view.action == 'retrieve':
            return True
        if view.action != 'list':
            return False
        companyId = request.query_params.get('company')
        if companyId is None:
            return False
        company = get_object_or_404(models.Company, pk=companyId)
        if request.user not in company.users.all():
            return False
        return True                
        
    def has_object_permission(self, request, view, reportObj):
        return (request.user in reportObj.company.users.all() or
            request.user.is_superuser)
