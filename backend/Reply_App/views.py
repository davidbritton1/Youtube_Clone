from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Reply
from .serializers import ReplySerializers



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reply_detail(request, pk):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    
    replys = get_object_or_404(Reply, pk=pk)
    
    if request.method == 'GET':
        replys = Reply.objects.filter(user_id=request.user.id)
        serializer = ReplySerializers(replys, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_record(request):
    if request.method == 'POST':
        serializer = ReplySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)