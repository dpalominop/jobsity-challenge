from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'rooms', views.RoomViewSet)
router.register(r'posts', views.PostViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:room_id>', views.index, name='index_room'),
    path('post_message', views.post_message, name='post_message'),
    path('get_posts', views.get_posts, name='get_posts'),
    path('command_status', views.command_status, name='command_status'),
    path('api/', include(router.urls)),
]
