"""demo5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from app01.views import login, index, logout

from rest_framework.authtoken import views
from app01.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login.html', login),
    path('index.html', index),
    path('logout.html', logout),
    # drf自带的Token认证模式
    path('api-token-auth/', views.obtain_auth_token),
    path('index/', IndexView.as_view(), name='index'),
]
