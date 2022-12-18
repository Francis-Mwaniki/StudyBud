from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room, Messages
from .serializers import RoomSerializer, MessagesSerializer
@api_view(['GET'])
def getRoutes(request):
    routes = [
    'GET /api',   
    'GET /api/rooms',
    'GET /api/room/:id'
]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    room = Room.objects.all()
    serializer = RoomSerializer(room,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getMessages(request):
    messages = Messages.objects.all()
    serializer = MessagesSerializer(messages,many=True)
    return Response(serializer.data)

