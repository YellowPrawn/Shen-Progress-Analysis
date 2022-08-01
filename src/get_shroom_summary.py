from riotwatcher import LolWatcher, ApiError
import get_match as gm
import get_participantId as gp
import get_shrooms_created as gsc
import get_shrooms_destroyed as gsde
import get_shroom_damage as gsd
import pandas as pd
import numpy as np
import argparse

#' Collects timeline from a given teemo match for a given player
#' 
#' Pulls match timeline from Riot API and extracts number of shrooms placed and destroyed
#' this script is not feasibly testable as player match history is not static
#' 
#' @param my_region region of player
#' @param summoner_name name of player
#' @param matches number of matches to scrape 
#'
#' @return a number of shrooms placed, number of shrooms destroyed
#'
#' @export
#'
#' @examples
#' python ./src/get_shroom_summary.py "na1" "PrawnJ" 6 
parser = argparse.ArgumentParser(description='Makes summary table of teemo shroom data')
parser.add_argument('region', metavar='source', type=str, help='region of player')
parser.add_argument('summoner_name', metavar='path', type=str, help='username of player')
parser.add_argument('matches', metavar='path', type=int, help='number of matches to be scraped')

args = parser.parse_args()
my_region = args.region
summoner_name = args.summoner_name
matches = args.matches

api_key = open("api_key.txt", "r").readline()
watcher = LolWatcher(api_key)
teemo_matches, puuid = gm.get_match(my_region, summoner_name, 'Teemo', matches, watcher)
    
summary_table = pd.DataFrame(columns=['matchId','shrooms_created','shrooms_destroyed','shroom_damage'])

for m in teemo_matches:
    timeline = watcher.match.timeline_by_match(my_region, m)
    participant_id = gp.get_participantId(my_region, puuid, m, watcher)

    shrooms_created = 0
    shrooms_destroyed = 0 
    shroom_damage = 0
        
    for f in timeline['info']['frames']:
        shrooms_created = shrooms_created + gsc.get_shrooms_created(participant_id, f)
        shrooms_destroyed = shrooms_destroyed + gsde.get_shrooms_destroyed(f)
        shroom_damage = shroom_damage + gsd.get_shroom_damage(f)
    
    match_summary = pd.DataFrame({'matchId': [m], 
                                'shrooms_created': [shrooms_created], 
                                'shrooms_destroyed': [shrooms_destroyed], 
                                'shroom_damage': [shroom_damage]})
                                
    summary_table = pd.concat([summary_table, match_summary])
summary_table.to_csv('./data/summary.data', index = None, header=True)
        