from pyexpat import model
from rest_framework import serializers
from .models import Reply


class ReplySerializers(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'user', 'comment', 'text']
        depth = 1
