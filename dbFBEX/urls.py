"""dbFBEX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from fb.views import TimelineViewSet,CommentsViewSet,NotificationsViewSet,MembersViewSet,MarketsViewSet,FriendsReqViewSet

router = routers.DefaultRouter()

router.register('timeline', TimelineViewSet),
router.register('comments', CommentsViewSet),
router.register('notifications', NotificationsViewSet),
router.register('Members', MembersViewSet),
router.register('friendsreq', FriendsReqViewSet),
router.register('markets', MarketsViewSet),

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
