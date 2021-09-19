from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # read only permissions are allowed for any user
        if request.method in permissions.SAFE_METHODS:
            return True

        # write only permissions are allowed to the author of the post
        return obj.author == request.user