from rest_framework import serializers


from .models import Timeline , Comments , Notifications , Members , FriendsReq ,Markets
from user.serializers import UserSerializer

# Serializers define the API representation.
class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('__all__')

class MembersLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('id','name','pic')

class TimelineSerializer(serializers.ModelSerializer):

    # name = UserSerializer(required=False)
    name = MembersLinkSerializer(required=False)
    name_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Timeline
        fields = ('id','name','status','like','name_id')

    def create(self, validated_data):
        # name_by_id = validated_data.get('name_by_id')
        # validated_data.pop('name_by_id',None)

        timeline = Timeline(**validated_data)
        
        #related name
        # members = Members.objects.filter(id=name_by_id).first()
        # timeline.name = members
        timeline.save()

        return timeline


class CommentsSerializer(serializers.ModelSerializer):

    timeline = TimelineSerializer(required=False)
    comment_by = MembersLinkSerializer(required=False)

    timeline_by_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    comment_by_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    
    class Meta:
        model = Comments
        fields = (
            'id',
            'comment',

            'timeline',
            'comment_by',
            
            'timeline_by_id',
            'comment_by_id',
            )

    def get_custom_validated_data(self, validated_data):
        timeline_by_id = validated_data.get('timeline_by_id')
        validated_data.pop('timeline_by_id', None)
        if timeline_by_id:
            timelineid = Timeline.objects.get(id=timeline_by_id)
            validated_data['timeline'] = timelineid

        comment_by_id = validated_data.get('comment_by_id')
        validated_data.pop('comment_by_id', None)
        if comment_by_id:
            koment = Members.objects.get(id=comment_by_id)
            validated_data['comment_by'] = koment

        return validated_data

    def create(self, validated_data):
        validated_data = self.get_custom_validated_data(validated_data)
        branch = Comments.objects.create(**validated_data)
        return branch

    def update(self, instance, validated_data):
        validated_data = self.get_custom_validated_data(validated_data)
        branch = Comments.objects.filter(id=instance.id)
        branch.update(**validated_data)
        return branch.get()

    # def create(self, validated_data):
    #     validated_data.pop('timeline_by_id',None)
    #     timeline_by_id = validated_data.get('timeline_by_id')
        
    #     timelineId = Comments(**validated_data)

    #     data_filter = Timeline.objects.filter(id=timeline_by_id)
    #     timelineId.timeline = data_filter
    #     timelineId.save(force_insert=True)

    #     return timelineId 

    # def create(self, validated_data):
    #     comment_by_id = validated_data.get('comment_by_id')
    #     validated_data.pop('comment_by_id',None)

    #     getname = Comments(**validated_data)
        
    #     #related name
    #     comment = Members.objects.filter(id=comment_by_id)
    #     getname.comment_by = comment
    #     getname.save(force_insert=True)

    #     return getname

class NotificationsSerializer(serializers.ModelSerializer):

    member = MembersLinkSerializer(required=False)
    member_by_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Notifications
        fields = (
            'id',
            'notif_content',
            'member',

            'member_by_id',
            )

    def create(self, validated_data):
        member_by_id = validated_data.get('member_by_id')
        validated_data.pop('member_by_id',None)

        notifications = Notifications(**validated_data)
        
        #related name
        members = Members.objects.filter(id=member_by_id).first()
        notifications.member = members
        notifications.save()

        return notifications

class FriendsReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendsReq
        fields = ('__all__')

class MarketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Markets
        fields = ('__all__')