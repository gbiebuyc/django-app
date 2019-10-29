from rest_framework import permissions

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
        return (view.action == 'retrieve' or
                view.action == 'list' or
                request.user.is_superuser)        
    def has_object_permission(self, request, view, reportObj):
        return (request.user in reportObj.company.users.all() or
            request.user.is_superuser)
