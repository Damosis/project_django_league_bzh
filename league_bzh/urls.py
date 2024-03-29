from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('participant/<int:participant_id>/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('add-match/', views.add_match, name='add_match'),
    path('matches/', views.matches, name='matches'),
    path('rank/<int:league_id>/', views.rank, name='rank'),
]
