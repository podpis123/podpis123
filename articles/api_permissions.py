from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read only is allowed for anyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write is allowed only for author
        return obj.author == request.user