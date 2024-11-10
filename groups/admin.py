from django.contrib import admin
from groups import models
# Register your models here.

class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'admin', 'group_status', 'post_status']

class MemberRequestAdmin(admin.ModelAdmin):
    list_display = ['group', 'account']

class MemberAdmin(admin.ModelAdmin):
    list_display = ['group', 'account']

class CoAdminModelAdmin(admin.ModelAdmin):
    list_display = ['group', 'account']

class AddGroupAdmin(admin.ModelAdmin):
    list_display = ['group', 'sender', 'receiver']

class GroupPostAdmin(admin.ModelAdmin):
    list_display = ['group', 'account', 'img_url', 'description', 'created_on']

class PendingPostAdmin(admin.ModelAdmin):
    list_display = ['group', 'account', 'img_url', 'description', 'created_on']


class BanAdmin(admin.ModelAdmin):
    list_display = ['group', 'account']


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ['Post',  'comment_body', 'comment_by', 'created_on']
    
    def Post(self, obj):
        return obj.post.img_url
    
    def comment_by(self, obj):
        return obj.account
    
    def comment_body(self, obj):
        return obj.body
    

class PostLikeAdmin(admin.ModelAdmin):
    list_display = ['Post', 'like_by']

    def Post(self, obj):
        return obj.post.img_url
    
    def like_by(self, obj):
        return obj.account

admin.site.register(models.Group, GroupModelAdmin)
admin.site.register(models.MemberRequest, MemberRequestAdmin)
admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.CoAdmin, CoAdminModelAdmin)
admin.site.register(models.Add_Group, AddGroupAdmin)
admin.site.register(models.GroupPost, GroupPostAdmin)
admin.site.register(models.PendingPost, PendingPostAdmin)
admin.site.register(models.Ban, BanAdmin)
admin.site.register(models.PostComment, PostCommentAdmin)
admin.site.register(models.PostLike, PostLikeAdmin)

