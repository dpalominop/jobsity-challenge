from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_then_login),
]
