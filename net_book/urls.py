from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), #
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('likes/', include('likes.urls')),
    path('comments/', include('comments.urls')),
    path('groups/', include('groups.urls')), #
]
