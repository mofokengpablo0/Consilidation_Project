from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsJournalist(BasePermission):
    """Permission for journalist users only."""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == "journalist"


class IsEditor(BasePermission):
    """Permission for editor users only."""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == "editor"


class IsReader(BasePermission):
    """Permission for reader users only."""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == "reader"


class IsPublisher(BasePermission):
    """Permission for publisher users only."""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == "publisher"


class IsEditorOrReadOnly(BasePermission):
    """Editors can edit, others can only read."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == "editor"


class IsArticleAuthorOrEditor(BasePermission):
    """Article author or any editor can edit/delete article."""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user or (
            request.user.is_authenticated and request.user.role == "editor"
        )


class CanApproveArticle(BasePermission):
    """Permission to approve articles - editors only."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "editor"


class IsNewsletterAuthorOrEditor(BasePermission):
    """Newsletter author or editor can edit."""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user or (
            request.user.is_authenticated and request.user.role == "editor"
        )
