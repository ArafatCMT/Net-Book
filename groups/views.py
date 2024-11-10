from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.views import APIView
from accounts.models import Account
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.http import Http404
from .permissions import IsAuthorOrReadonly
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

class CreateGroupView(APIView):
    serializer_class = serializers.GroupSerializer

    def get_objects(self, user):
        try:
            account = Account.objects.get(user = user)
            return account
        except(Account.DoesNotExist):
            return None

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            account = self.get_objects(request.user)
            serializer.save(admin = account)
            return Response({'details': 'group create successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EditGroupView(APIView):
    permission_classes = [IsAuthorOrReadonly]
    serializer_class = serializers.GroupSerializer

    def get_objects(self, id):
        try:
            group = models.Group.objects.get(id=id)
            return group
        except(models.Group.DoesNotExist):
           return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id, format=None):
        group = self.get_objects(id)
        serializer = self.serializer_class(group)
        return Response(serializer.data)
    
    # group er details update ba modify korar jonno
    def put(self, request, id, format=None):
        group = self.get_objects(id)
        serializer = self.serializer_class(group, data=request.data)

        account = Account.objects.get(user = request.user)
        print(account)

        if serializer.is_valid():
            # print(serializer.validated_data['name'], serializer.validated_data['image_url'],
            #  serializer.validated_data['description'], serializer.validated_data['group_status'],
            # serializer.validated_data['post_status'])
            serializer.save(admin = account)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # shudu group photo upload korar jonno
    def patch(self, request, id, format=None):
        group = self.get_objects(id)
        serializer = self.serializer_class(group, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'details': 'Group Edit successfully'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpecificGroupForAdmin(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        account_id = request.query_params.get('account_id')
        # print(account_id)
        if account_id :
            return queryset.filter(admin = account_id)
        return queryset
    
class AllGroupView(ListAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    filter_backends = [SpecificGroupForAdmin]

class AddCoAdminView(APIView):
    serializer_class = serializers.CoAdminSerializer

    def get_objects(self, group, account):
        try:
            queryset = models.Member.objects.filter(account = account)
            
            try:
                member = queryset.get(group=group)
                return member
            except(models.Member.DoesNotExist):
                return None
        except(models.Member.DoesNotExist):
                return None

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            group = serializer.validated_data['group']
            account = serializer.validated_data['account']
            # print(group, account)
            member = self.get_objects(group, account)
            
            # print(member)
            if member:
                # print("member:- ", member)
                serializer.save()
                member.delete()
                return Response({'details': 'CoAdmin added successfully'},status=status.HTTP_201_CREATED)
            else:
                return Response({'details': "This user isn’t a member of the group, so they can’t be a co-admin. Only group members can become co-admins."},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def DemoteCoadmin(request, id, group_id):
    
    try:
        admin = Account.objects.get(user=request.user)
        group = models.Group.objects.get(id = group_id)
    except(models.Group.DoesNotExist):
        return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
    if admin != group.admin:
        return Response({'message': 'This action is only allowed for the group admin.'}, status=status.HTTP_400_BAD_REQUEST)
    else:

        try:
            account = Account.objects.get(id = id)
        except(Account.DoesNotExist):
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                obj = models.CoAdmin.objects.get(group=group, account=account)
            except(models.CoAdmin.DoesNotExist):
                return Response({'error': 'coadmin not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                print("delete")
                obj.delete()
                models.Member.objects.create(group=group, account=account)
                    
                print("member")
                return Response({'details': 'Demote Coadmin Successfully'}, status=status.HTTP_200_OK)
    
        







