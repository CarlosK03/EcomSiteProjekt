from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', include('test1.urls')),
    path('admin/', admin.site.urls),
]