from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Room, Post
from .serializers import RoomSerializer, PostSerializer, PostListSerializer
from django.contrib.auth.decorators import login_required


@login_required
def index(request, room_id=None):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    if not room_id:
        room_id = Room.objects.all()[0:1].get().id
    room = Room.objects.get(id=room_id)
    context['room'] = room
    return render(request, "chat.html", context)


@login_required
def post_message(request):
    if request.method == 'POST':
        print(request.POST)
        room_id = request.POST['room_id']
        message = request.POST['message']
        room = Room.objects.get(pk=room_id)
        post = Post.objects.create(room=room, message=message, author=request.user)
        post.save()
        return redirect('index_room', room_id=room_id)


@api_view(['POST'])
def get_posts(request):
    room_id = request.POST['room_id']
    room = Room.objects.get(pk=room_id)
    posts_data = Post.objects.filter(room=room).order_by('-created')[:50]
    for post_data in posts_data:
        post_data.created_date = post_data.created.strftime('%Y-%m-%d')
        post_data.created_time = post_data.created.strftime('%H:%M')
    posts = PostListSerializer(posts_data, many=True)
    return Response(posts.data)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
