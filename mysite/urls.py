from django.shortcuts import HttpResponse

def index_method(request):
    return HttpResponse("Hello, world. 25461651 is the polls owner.")


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_method),
    path('polls/', include('polls.urls'))
]


