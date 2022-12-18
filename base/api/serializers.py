from rest_framework.serializers import ModelSerializer
from base.models import Room, Messages

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class MessagesSerializer(ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'