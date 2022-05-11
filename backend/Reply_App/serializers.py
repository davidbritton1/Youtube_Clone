from rest_framework import serializers
from .models import Reply


class ReplySerializers(serializers.ModelSerializer):
    class Meta:
        user = Reply
        fields = ['id', 'user', 'comment', 'text']
        depth = 1
