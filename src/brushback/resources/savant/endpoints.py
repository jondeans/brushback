"""Fetching data from BaseballSavant.com"""

import pandas as pd

from loguru import logger
from endpointer import Endpoint


class BaseballSavant(Endpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            url="https://baseballsavant.mlb.com",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            },
            **kwargs,
        )


class Gamefeed(BaseballSavant):
    """This endpoint doesn't seem to contain much useful information."""

    def __init__(self, game_pk: int = None, *args, **kwargs):
        super().__init__(*args, endpoint="gamefeed", params={"gamePk": game_pk}, **kwargs)


class GamefeedJson(BaseballSavant):
    def __init__(self, game_pk: int = None, *args, **kwargs):
        super().__init__(*args, endpoint="gf", params={"game_pk": game_pk}, **kwargs)

    def load_response(self) -> pd.DataFrame:
        """Load the JSON results into a DataFrame."""

        if not self._response:
            logger.warning(
                f"No response found for {self._endpoint!r}. Did you get your request yet?"
            )
            return pd.DataFrame()

        return self._response.json()


class Schedule(BaseballSavant):
    def __init__(
        self,
        sport_id: int = None,
        date: str = None,
        game_pk: int = None,
        use_latest_games: int = None,
        hydrate: int = None,
        *args,
        **kwargs,
    ):
        super().__init__(
            *args,
            endpoint="schedule",
            params={
                "sportId": sport_id,
                "date": date,
                "gamePk": game_pk,
                "useLatestGames": use_latest_games,
                "hydrate": hydrate,
            },
            **kwargs,
        )
