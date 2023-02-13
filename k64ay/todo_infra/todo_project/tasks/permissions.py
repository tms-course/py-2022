from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view, obj):
        pass
        return
