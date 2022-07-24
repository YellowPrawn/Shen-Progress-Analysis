from riotwatcher import LolWatcher, ApiError
#' Checks a match where a specified champion was played
#' 
#' Checks a match where a specified champion was played
#' code based on https://towardsdatascience.com/how-to-use-riot-api-with-python-b93be82dbbd6
#' this function is not feasibly testable as player match history is not static
#' 
#' @param my_region region of player
#' @param puuid puuid of player
#' @param champion_name champion's name to pull matches of
#' @param i number of matches to scrape 
#' @param my_matches DTO of matches under given player
#' @param watcher LolWatcher object
#'
#' @return a string representing a match ID
#'
#' @export
#'
#' @examples
#' check('na1', 'PrawnJ', 'DKJpLKoGsLmWP5btU6O4ZlPYKLwITUmf9pF921BIbf4q5vd9ioWDKGpP34qYWaDiRH-zuyHR3lxFng', 'Shen', 1, my_matches, watcher)
def check(my_region, puuid, champion_name, i, my_matches, watcher):
    # fetch ith match detail
    match_detail = watcher.match.by_id(my_region, my_matches[i])
    players = match_detail['info']['participants']
    for p in players:
        if p['puuid'] == puuid:
            if p['championName'] == champion_name:
                return match_detail['metadata']['matchId']