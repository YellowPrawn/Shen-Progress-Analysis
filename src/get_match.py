from riotwatcher import LolWatcher, ApiError
import check_match as c

#' Collects data from a given match where a given player plays a given champion
#' 
#' Pulls match data from Riot API and filters for only matches where player plays a given champion.
#' code based on https://towardsdatascience.com/how-to-use-riot-api-with-python-b93be82dbbd6
#' this function is not practically testable since code is obtained through a tested source
#' 
#' @param my_region region of player
#' @param summoner_name name of player
#' @param champion_name champion's name to pull matches of
#' @param matches number of matches to scrape 
#' @param api_key api key to pull off the riot API
#' @param watcher LolWater object
#'
#' @return a list of strings (match IDs) and player puuid
#'
#' @export
#'
#' @examples
#' get_match('na1', 'PrawnJ', 'Shen', 1, 'RGAPI-xxxxx')
def get_match(my_region, summoner_name, champion_name, matches, watcher):
    # global variables
    me = watcher.summoner.by_name(my_region, summoner_name)
    my_matches = watcher.match.matchlist_by_puuid(my_region, me['puuid'], count = 100)
    champion_matches = []
    for i in range(matches): 
        # fetch ith match detail
        try:
            matchID = c.check(my_region, me['puuid'], champion_name, i, my_matches, watcher)
        except IndexError:
            pass
        if matchID is not None:
            champion_matches.append(matchID)
    return champion_matches, me['puuid']