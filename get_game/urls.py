from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /profile_id
    path('random_game/', views.random_game, name="random_game")
]
