from django.shortcuts import HttpResponse

def owner(request):
    return HttpResponse("Hello, world. 25461651 is the polls owner.")

def gotoQuestion(request):
    return HttpResponse('<a href="/polls/1/vote">Answer to the Ultimate Question</a>')


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner/', owner),
    path('polls/', include('polls.urls')),
    path('', gotoQuestion),
]


