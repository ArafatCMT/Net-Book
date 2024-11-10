from rest_framework import serializers
from . import models

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ['id', 'name', 'image_url', 'description', 'group_status', 'post_status', 'admin']
        read_only_fields = ['admin']

class CoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoAdmin
        fields = ['id', 'group', 'account']

