from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == "POST":
        data = request.POST
        profile_id = data.get("profile_submit")
    return render(request, 'get_game/index.html')


def get_account_games(request, profile_id):
    return HttpResponse("You're looking for games from account %s." % profile_id)
