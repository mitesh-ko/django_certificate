from django.urls import path
from polls import views
from django.shortcuts import HttpResponse

def owner(request):
    return HttpResponse("Hello, world. a797b6a1 is the polls owner.")

urlpatterns = [    
    path('owner/', owner),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),
]