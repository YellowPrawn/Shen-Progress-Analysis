import pytest
from riotwatcher import LolWatcher, ApiError
import sys

sys.path.append(".")
from src.get_shrooms_created import get_shrooms_created

api_key = open("api_key.txt", "r").readline()
print(api_key)
watcher = LolWatcher(api_key)

timeline = watcher.match.timeline_by_match('na1', 'NA1_4323386823')

# test if correct number of shrooms placed was recorded
def test_shrooms_created():
    count = 0
    for f in timeline['info']['frames']:
        count = count + get_shrooms_created(10, f)
    assert count == 70

