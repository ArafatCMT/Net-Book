from django.db import models
from accounts.models import Account

# Create your models here.

GROUP_STATUS = [
    ('Public', 'Public'),
    ('Private', 'Private'),
]

GROUP_POST_STATUS = [
    ('Approval Required', 'Approval Required'),
    ('Public Post', 'Public Post'),
]

class Group(models.Model):
    name = models.CharField(max_length=30)
    image_url = models.CharField(max_length=250, default='https://ibb.co.com/txxyPY4')
    admin = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    group_status = models.CharField(choices=GROUP_STATUS, max_length=15, default='Public')
    post_status = models.CharField(choices=GROUP_POST_STATUS, max_length=30, default='Public Post')
    
    def __str__(self):
        return f'{self.name}'
    

class CoAdmin(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account.user.username}'

class Member(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account.user.first_name} {self.account.user.last_name}'

class PendingPost(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"post id: {self.id}"

class GroupPost(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"post id: {self.id}"

class MemberRequest(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account.user.username}'

class Add_Group(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sender_user')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='receiver_user')

    def __str__(self):
        return f"{self.receiver.user.first_name} {self.receiver.user.last_name}"
    

class Ban(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account.user.first_name} {self.account.user.last_name}' 
    
class PostComment(models.Model):
    post = models.ForeignKey(GroupPost, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"comment by : {self.account.user.first_name}"
    

class PostLike(models.Model):
    post = models.ForeignKey(GroupPost, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.description}"
    






