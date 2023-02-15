from rest_framework import permissions

<<<<<<< HEAD

class IsOwnerPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view, obj):
        pass
        return
=======
class IsOwnerPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
>>>>>>> bdde28e3ae4d20ec23f8fa3a00a2ac590ab4db85
