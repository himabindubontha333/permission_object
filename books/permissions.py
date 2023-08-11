from rest_framework import permissions

class IsEditorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('books.editor_permission'):
            return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.has_perm('books.editor_permission'):
            return True
        return request.method in permissions.SAFE_METHODS or (
            request.method in ['PUT', 'PATCH', 'DELETE'] and
            obj.author == request.user
        )

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('books.admin_permission'):
            return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.has_perm('books.admin_permission'):
            return True
        return request.method in permissions.SAFE_METHODS or (
            request.method in ['PUT', 'PATCH', 'DELETE']
        )


class IsViewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('books.viewer_permission')

class IsCreatorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('books.creator_permission'):
            return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.has_perm('books.creator_permission'):
            return True
        return request.method in permissions.SAFE_METHODS
