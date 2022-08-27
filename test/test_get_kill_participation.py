import pytest
from riotwatcher import LolWatcher, ApiError
import sys

sys.path.append(".")
from src.get_kill_participation import get_kill_participation

api_key = open("api_key.txt", "r").readline()
watcher = LolWatcher(api_key)

# tests if correct kill participation was calculated
def test_correct_kill_participation():
    kill_participation = get_kill_participation('na1', 'DKJpLKoGsLmWP5btU6O4ZlPYKLwITUmf9pF921BIbf4q5vd9ioWDKGpP34qYWaDiRH-zuyHR3lxFng', 'NA1_4323386823', watcher)
    expected = 0.14285714285714285
    assert expected == kill_participation
