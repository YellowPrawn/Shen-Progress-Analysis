from riotwatcher import LolWatcher, ApiError
import get_match as gm
import get_participantId as gp
import get_shrooms_created as gsc
import get_shrooms_destroyed as gsde
import get_shroom_damage as gsd

#' Collects timeline from a given teemo match for a given player
#' 
#' Pulls match timeline from Riot API and extracts number of shrooms placed and destroyed
#' this function is not feasibly testable as player match history is not static
#' 
#' @param my_region region of player
#' @param summoner_name name of player
#' @param matches number of matches to scrape 
#' @param api_key api key to pull off the riot API
#'
#' @return a number of shrooms placed, number of shrooms destroyed
#'
#' @export
#'
#' @examples
#' get_shroom_summary('na1', 'PrawnJ', 1, 'RGAPI-xxxxx')
def get_shroom_summary(my_region, summoner_name, matches, api_key):
    watcher = LolWatcher(api_key)
    teemo_matches, puuid = gm.get_match(my_region, summoner_name, 'Teemo', matches, watcher)
    
    for m in teemo_matches:
        timeline = watcher.match.timeline_by_match(my_region, m)
        participant_id = gp.get_participantId(my_region, puuid, m, watcher)

        for f in timeline['info']['frames']:
            shrooms_created = gsc.get_shrooms_created(participant_id, f)
            shrooms_destroyed = gsde.get_shroom_destroyed(f)
            shroom_damage = gsd.get_shroom_damage(f)
            #TODO: add this data into numpy table
        