from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True if request.method in permissions.SAFE_METHODS else False

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        return object.author == request.user

# NOTE TODO SECURITY ??
class AllowAny(permissions.BasePermission):
    def has_permission(self, request, view):
        return True