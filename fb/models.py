from django.db import models
from django.contrib.auth.models import User 



# Create your models here.

class Members(models.Model):

    class Meta:
        db_table: 'members'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=True , null=True ,)
    gender = models.CharField(max_length=25)
    pic = models.CharField(max_length=100,null=True)

class Timeline(models.Model):

    class Meta:
        db_table = 'timeline'

    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Members,on_delete=models.CASCADE,db_index=False, blank=True , null=True ,) 
    status = models.TextField()
    like = models.IntegerField(default=0)
    
    

class Comments(models.Model):

    class Meta:
        db_table = 'comments'

    id = models.AutoField(primary_key=True,)
    comment = models.TextField(null=True)
    timeline = models.ForeignKey(Timeline,on_delete=models.CASCADE,db_index=False, blank=True , null=True)
    comment_by = models.ForeignKey(Members, on_delete=models.CASCADE,db_index=False, blank=True , null=True)


class Notifications(models.Model):

    class Meta:
        db_table = 'notifications'

    id = models.AutoField(primary_key=True)
    notif_content = models.TextField()
    member = models.ForeignKey(Members,on_delete=models.CASCADE,db_index=False, blank=True , null=True ,) 


class FriendsReq(models.Model):

    class Meta:
        db_table = 'friendsreq'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=25)
    pic = models.CharField(max_length=100,null=True)

class Markets(models.Model):

    class Meta:
        db_table = 'markets'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    pic = models.CharField(max_length=100,null=True)