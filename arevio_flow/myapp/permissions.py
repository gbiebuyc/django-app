from rest_framework import permissions

class AnnualReportViewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (view.action == 'retrieve' or
                view.action == 'list' or
                view.action == 'create' or
                request.user.is_superuser)        
    def has_object_permission(self, request, view, reportObj):
        return (request.user in reportObj.company.users.all() or
            request.user.is_superuser)
