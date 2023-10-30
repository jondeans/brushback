""""""

import pandas as pd

from src.brushback.resources.savant.endpoints import GamefeedJson


class Game:
    def __init__(self, game_id: int = None):
        gf = GamefeedJson(game_pk=game_id, fetch=True)
        self._gamefeed_json = gf.load_response()

        # Single value keys
        self.game_status_code: str = self._gamefeed_json["game_status_code"]
        self.game_status: str = self._gamefeed_json["game_status"]
        self.gameday_type: str = self._gamefeed_json["gamedayType"]
        self.game_date: str = self._gamefeed_json["game_date"]
        self.venue_id: int = self._gamefeed_json["venue_id"]
        self.team_home_id: int = self._gamefeed_json["team_home_id"]
        self.team_away_id: int = self._gamefeed_json["team_away_id"]
        self.players: list = self._gamefeed_json["players"]
        self.away_lineup: list[int] = self._gamefeed_json["away_lineup"]
        self.home_lineup: list[int] = self._gamefeed_json["home_lineup"]
        self.away_pitcher_lineup: list[int] = self._gamefeed_json["away_pitcher_lineup"]
        self.home_pitcher_lineup: list[int] = self._gamefeed_json["home_pitcher_lineup"]
        self.cache_key: str = self._gamefeed_json["cacheKey"]
        self.cache_hit: str = self._gamefeed_json["cache_hit"]

        # Multi-value keys
        self.scoreboard: pd.DataFrame = pd.DataFrame(self._gamefeed_json["scoreboard"])
        self.home_team_data: pd.DataFrame = pd.DataFrame(self._gamefeed_json["home_team_data"])
        self.away_team_data: pd.DataFrame = pd.DataFrame(self._gamefeed_json["away_team_data"])
        self.team_home: pd.DataFrame = pd.DataFrame(self._gamefeed_json["team_home"])
        self.team_away: pd.DataFrame = pd.DataFrame(self._gamefeed_json["team_away"])
        self.home_pitchers: dict = self._gamefeed_json["home_pitchers"]
        self.away_pitchers: dict = self._gamefeed_json["away_pitchers"]
        self.home_batters: dict = self._gamefeed_json["home_batters"]
        self.away_batters: dict = self._gamefeed_json["away_batters"]
        self.exit_velocity: pd.DataFrame = pd.DataFrame(self._gamefeed_json["exit_velocity"])
        self.boxscore: dict = self._gamefeed_json["boxscore"]

    def __str__(self):
        return "Game"

    def __repr__(self):
        return "Game"
