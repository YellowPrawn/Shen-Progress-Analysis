from riotwatcher import LolWatcher, ApiError

#' Computes player kill participation in a given match
#' 
#' @param my_region region of player
#' @param puuid puuid of player
#' @param matchId ID of match 
#' @param watcher LolWatcher object
#'
#' @return an integer
#'
#' @export
#'
#' @examples
#' get_kill_participation('na1', 'DKJpLKoGsLmWP5btU6O4ZlPYKLwITUmf9pF921BIbf4q5vd9ioWDKGpP34qYWaDiRH-zuyHR3lxFng', 'NA1_4323386823', watcher)

def get_kill_participation(my_region, puuid, matchId, watcher):
    match_detail = watcher.match.by_id(my_region, matchId)
    players = match_detail['info']['participants']
    total_team_kills = 0
    player_takedowns = 0
    for p in players:
        total_team_kills = total_team_kills + p['kills']
        if p['puuid'] == puuid:
            player_takedowns = p['kills'] + p['assists']
    return player_takedowns / total_team_kills