import pytest
from riotwatcher import LolWatcher, ApiError
import sys

sys.path.append(".")
from src.get_shrooms_destroyed import get_shrooms_destroyed

api_key = open("api_key.txt", "r").readline()
watcher = LolWatcher(api_key)

timeline = watcher.match.timeline_by_match('na1', 'NA1_4323386823')

# test if correct number of shrooms placed was recorded
def test_shrooms_destroyed():
    count = 0
    for f in timeline['info']['frames']:
        count = count + get_shrooms_destroyed(f)
    assert count == 13

