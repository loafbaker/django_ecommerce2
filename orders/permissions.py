from rest_framework.permissions import BasePermission


class isOwnerAndAuth(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user_checkout and obj.user_checkout.user == request.user

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
