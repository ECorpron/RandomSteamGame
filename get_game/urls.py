from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /profile_id
    path("<int:profile_id>", views.get_account_games, name="get_account_game")
]
