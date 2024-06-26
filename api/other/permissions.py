from rest_framework import permissions

class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it,
    but allow anyone to read it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object or admin users (or you're creating a new obj)
        return request.user.is_staff or request.method == "POST"

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.user == request.user or request.user.is_staff
