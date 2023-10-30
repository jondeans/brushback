"""Tests for the `Gamefeed` endpoint."""

from src.brushback.resources.savant import endpoints
from loguru import logger


def test_gamefeed():
    params = {"gamePk": 717187}

    gamefeed = endpoints.Gamefeed()
    gamefeed.update_params(params)

    logger.debug(f"{gamefeed=}")

    assert gamefeed.params == params
    assert gamefeed.endpoint == "gamefeed"


def test_gamefeedjson():
    params = {"game_pk": 717187}

    gf = endpoints.GamefeedJson()
    gf.update_params(params)

    logger.debug(f"{gf=}")

    assert gf.params == params
    assert gf.endpoint == "gf"


def test_schedule():
    params = {
        "sportId": None,
        "date": None,
        "gamePk": None,
        "useLatestGames": None,
        "hydrate": None,
    }

    schedule = endpoints.Schedule()
    schedule.update_params(params)

    logger.debug(f"{schedule=}")

    assert schedule.params == params
    assert schedule.endpoint == "schedule"
