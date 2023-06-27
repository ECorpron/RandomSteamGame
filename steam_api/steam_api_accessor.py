import credentials.config
import steam_api_wrapper.steam_api_controller as steam_api
import steam_api_wrapper.games_manager as games_manager
import steam_api_wrapper.classes as api_classes

steam_api_key = credentials.config.steam_api_key


def get_profile_games(profile_id):
    api_connection = steam_api.SteamAPIController(api_key=steam_api_key, profile_id=profile_id)
    user_games_response = api_connection.owned_game_request()
    user_games_data = games_manager.unwrap_user_game_response(user_games_response)
    return games_manager.get_games_dict(user_games_data)


def get_random_game(games_dict):
    rand_game_data = games_manager.get_random_game(games_dict)
    rand_game = api_classes.Game(rand_game_data.get("appid"),
                                 rand_game_data.get("name"),
                                 rand_game_data.get("playtime_forever"))
    return rand_game
