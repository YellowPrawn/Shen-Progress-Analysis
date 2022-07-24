import pytest
from riotwatcher import LolWatcher, ApiError
import sys

sys.path.append(".")
from src.get_participantId import get_participantId

api_key = 'RGAPI-xxxx'
watcher = LolWatcher(api_key)

# tests if the given puuid is present in the given matchId
def test_correct_puuid_or_matchId():
    participantId = get_participantId('na1', 'DKJpLKoGsLmWP5btU6O4ZlPYKLwITUmf9pF921BIbf4q5vd9ioWDKGpP34qYWaDiRH-zuyHR3lxFng', 'NA1_4323386823', watcher)
    expected = 10
    assert expected == participantId

# tests that the given puuid is not present in the given matchId
def test_incorrect_puuid_or_matchId():
    with pytest.raises(Exception):
        get_participantId('na1', 'RQ5zvRFguY0jhlsZBUwLteHUcvWpJ2rwBF9Y_Qwu241RRvGDySkK7q2BwDRuhsIaCAX1Gu7-txCZTQ', 'NA1_4322190232', watcher)