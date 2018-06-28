from django.shortcuts import render

# from django.contrib.auth.models import User 
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

from .models import Timeline , Comments , Notifications , Members ,  FriendsReq , Markets
from .serializers import TimelineSerializer , CommentsSerializer , NotificationsSerializer , MembersSerializer , MarketsSerializer , FriendsReqSerializer


# Create your views here.

class TimelineViewSet(viewsets.ModelViewSet):

    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    

    def create(self, request, *args, **kwargs,):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED) 

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    filter_fields = ('timeline',)

    def create(self, request, *args, **kwargs,):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
     

class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer

    def create(self, request, *args, **kwargs,):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED) 

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

class FriendsReqViewSet(viewsets.ModelViewSet):
    queryset = FriendsReq.objects.all()
    serializer_class = FriendsReqSerializer

class MarketsViewSet(viewsets.ModelViewSet):
    queryset = Markets.objects.all()
    serializer_class = MarketsSerializer