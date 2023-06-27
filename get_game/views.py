from django.shortcuts import render
from django.http import HttpResponse

import steam_api.steam_api_accessor as steam_api


# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, 'get_game/index.html')
    elif request.method == "POST":
        # return HttpResponse("Made it here")
        profile_id = request.POST.get("profile_id")

        request.session["profile_id"] = int(profile_id)

        return render(request, 'get_game/get_random_game.html')
    else:
        return HttpResponse("Not a GET or POST request")


def random_game(request):
    if request.method != "GET":
        return HttpResponse("ERROR")
    profile_id = request.session.get("profile_id")
    user_games = steam_api.get_profile_games(profile_id)
    rand_game = steam_api.get_random_game(user_games)
    request.session["game_name"] = rand_game.name

    return render(request, 'get_game/random_game.html')
