"""
URL configuration for pollsapp project.

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
from django.http import HttpResponse
from django.urls import path, include

def hello(request, num):
    html = ''
    for i in range(10):
        html += f"<p>{ i + 1 } * { num } = { (i + 1) * num }</p>"
    return HttpResponse("<h1>Hello!</h1>" + html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<int:num>/', hello, name='hello'),
    path('', include('polls.urls'))
]