from django.urls import path
from polls import views
urlpatterns = [
    path('<int:question_id>/vote/', views.vote, name='vote'),
]