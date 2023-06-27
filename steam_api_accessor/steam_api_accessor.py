import credentials.config
import steam_api_wrapper.steam_api_controller as steam_api
import steam_api_wrapper.games_manager as games_manager

steam_api_key = credentials.config.steam_api_key


def get_profile_games(profile_id):
    api_connection = steam_api.SteamAPIController(api_key=steam_api_key, profile_id=profile_id)
    my_games_response = api_connection.owned_game_request()
    return games_manager.get_games_dict(my_games_response)
