"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from django_test import views
from django_test.views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserList)
router.register(r'users', views.UserDetail)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/music/', include('music.urls')),
    path('api/me/', views.CurrentUserDetail.as_view()),
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register', views.register, name='register'),
    path('accounts/profile/', views.profile),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', CustomObtainAuthToken.as_view()),
]
