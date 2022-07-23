from riotwatcher import LolWatcher, ApiError
import collect_match as c
#timeline_by_match()


#' Collects timeline from a given match for a given player
#' 
#' Pulls match timeline from Riot API and focuses on a given player's actions
#' 
#' @param my_region region of player
#' @param summoner_name name of player
#' @param champion_name champion's name to pull matches of
#' @param matches number of matches to scrape 
#' @param api_key api key to pull off the riot API
#'
#' @return a list of strings (match IDs)
#'
#' @export
#'
#' @examples
#' collect('na1', 'PrawnJ', 'Shen', 1, 'RGAPI-xxxxx')