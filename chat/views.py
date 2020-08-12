from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.decorators import api_view
from .models import Room, Post
from .serializers import RoomSerializer, PostSerializer, PostListSerializer
from django.contrib.auth.decorators import login_required
from datetime import datetime
import json
from . import bot


@login_required
def index(request, room_id=None):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    if not room_id:
        room_id = Room.objects.all()[0:1].get().id
    for room in Room.objects.all():
        room.users.remove(request.user)
    room = Room.objects.get(id=room_id)
    room.users.add(request.user)
    context['room'] = room
    return render(request, "chat.html", context)


@login_required
@api_view(['POST'])
def post_message(request):
    room_id = request.POST['room_id']
    message = request.POST['message']
    if message[:1] == '/':
        response = bot.execute_command(message[1:])
    else:
        room = Room.objects.get(pk=room_id)
        post = Post.objects.create(room=room, message=message, author=request.user)
        post.save()
        response = {'status': 'ok'}
    return JsonResponse(response)


@login_required
@api_view(['POST'])
def command_status(request):
    job_id = request.POST.get('job_id', False)
    if job_id:
        return JsonResponse(bot.command_status(job_id))


@login_required
@api_view(['POST'])
def get_posts(request):
    previus_check = None
    if request.POST['last_check'] != '':
        previus_check = datetime.strptime(request.POST['last_check'], '%Y-%m-%d %H:%M:%S.%f')
    last_check = str(datetime.now())
    room_id = request.POST['room_id']
    room = Room.objects.get(pk=room_id)
    if previus_check:
        try:
            posts_data = Post.objects.filter(Q(room=room), Q(created__gt=previus_check)).order_by('-created')[: 50]
        except Post.DoesNotExist:
            return JsonResponse({'last_check': last_check, 'posts': None})
    else:
        posts_data = Post.objects.filter(room=room).order_by('-created')[:50]
    for post_data in posts_data:
        post_data.created_date = post_data.created.strftime('%Y-%m-%d')
        post_data.created_time = post_data.created.strftime('%H:%M')
    posts = PostListSerializer(posts_data, many=True)
    users = list(room.users.values_list('username', flat=True))
    response = {
        'last_check': last_check,
        'posts': posts.data,
        'users': json.dumps(users),
    }
    return JsonResponse(response)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
