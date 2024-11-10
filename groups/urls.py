from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.CreateGroupView.as_view()),
    path('all/', views.AllGroupView.as_view()),
    path('edit/<int:id>/', views.EditGroupView.as_view()),
    path('coadmin/', views.AddCoAdminView.as_view()),
    path('demote/coadmin/<int:id>/<int:group_id>/', views.DemoteCoadmin)
]