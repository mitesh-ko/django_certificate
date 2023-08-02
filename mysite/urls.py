from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
  
def gotoQuestion(request):
    return HttpResponse('<a href="/polls/1/vote">Answer to the Ultimate Question</a>')

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('hello/', include('hello.urls')),
    path('', gotoQuestion),
    # path('', HttpResponse('<a href="/polls/1/vote">Answer to the Ultimate Question</a>'))
]


