"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myproject.views import saludo, get_date, get_name, get_data, session_5, session_6, session_7

urlpatterns = [
    path('admin/', admin.site.urls),
    path('session2greet/', saludo),
    path('session2date/', get_date),
    path('session3/', get_name),
    path('session4/', get_data),
    path('session5/', session_5),
    path('session6/', session_6),
    path('session7/', session_7),
]
