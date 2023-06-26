import credentials.config

import 

steam_api_key = credentials.config.steam_api_key


def get_profile_games(profile_id):
    my_api = steam_api.SteamAPIController(api_key=steam_api_key, profile_id=profile_id)
    my_games_response = my_api.owned_game_request()
