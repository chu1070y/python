"""python_ch3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# from python_ch3 import helloworld
import helloworld.views as helloworld_views
import robot.views as robot_views
import emaillist.views as emaillist_views

urlpatterns = [
    path('emaillist/', emaillist_views.index),
    path('emaillist/form', emaillist_views.form),
    path('robot/', robot_views.robot),
    path('helloworld/', helloworld_views.hello),
    path('admin/', admin.site.urls),
]