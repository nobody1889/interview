from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'text', 'message_id', 'type_', 'is_bot', 'created_at']
        read_only_fields = ['id', 'is_bot', 'created_at']
