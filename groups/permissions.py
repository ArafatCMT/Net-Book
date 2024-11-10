from rest_framework import permissions
from accounts import models
from groups.models import Group

class IsAuthorOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            account = models.Account.objects.get(user = request.user)
            return obj.admin == account
        
        
        