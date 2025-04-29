"""
URL configuration for Python_OnlineStore_Radygina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from users.views import goods_list, good_detail, clients_list, client_detail, register
from django.contrib.auth import views as auth_views
from users.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("goods/", goods_list, name='goods_list'),
    path("goods/int:pk", good_detail, name='good_detail'),
    path("clients/", clients_list, name='clients_list'),
    path("clients/int:pk", client_detail, name='client_detail'),
    path('register/', register, name='register'),
    path('', home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
