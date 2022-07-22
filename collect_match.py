import argparse
import pandas as pd
from riotwatcher import LolWatcher, ApiError

#' Collects data from a given match where a given player plays Shen
#' 
#' Pulls match data from Riot API and filters for only matches where player plays Shen.
#' 
#' @param my_region region of player
#' @param summoner_name name of player
#' @param api_key api key to pull off the riot API
#' @param champion_name champion's name to pull matches of
#'
#' @return creates a file based off the dataset from 'source' and saves it at/as 'path'
#'
#' @export
#'
#' @examples
#' collect('na1', 'PrawnJ', RGAPI-xxxxx)
def collect(my_region, summoner_name, api_key, champion_name):
    # global variables
    watcher = LolWatcher(api_key)

    me = watcher.summoner.by_name(my_region, summoner_name)
    my_matches = watcher.match.matchlist_by_puuid(my_region, me['puuid'])
    shen_matches = []

    # fetch last match detail
    match_detail = watcher.match.by_id(my_region, my_matches[0])
    
    players = match_detail['info']['participants']
    for p in players:
        if p['puuid'] == me['puuid'] and p['championName'] == champion_name:
            shen_matches.append(match_detail['metadata']['matchId'])
    print(shen_matches)