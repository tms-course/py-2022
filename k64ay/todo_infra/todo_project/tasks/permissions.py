from rest_framework import permissions

class IsOwnerPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user