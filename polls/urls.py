from django.urls import path
from polls import views
urlpatterns = [
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),
]