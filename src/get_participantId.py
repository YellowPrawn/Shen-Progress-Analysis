from riotwatcher import LolWatcher, ApiError
#' Gets participant ID in a given match 
#' 
#' Gets participant ID in a given match 
#' 
#' @param my_region region of player
#' @param puuid puuid of player
#' @param matchId ID of match 
#' @param watcher LolWatcher object
#'
#' @return a string representing a participantID 
#'
#' @export
#'
#' @examples
#' get_participantId('na1', 'DKJpLKoGsLmWP5btU6O4ZlPYKLwITUmf9pF921BIbf4q5vd9ioWDKGpP34qYWaDiRH-zuyHR3lxFng', 'NA1_4323386823', watcher)
def get_participantId(my_region, puuid, matchId, watcher):
    timeline = watcher.match.timeline_by_match(my_region, matchId)
    participants = timeline['info']['participants']
    for p in participants: 
        if p['puuid'] == puuid:
            return p['participantId']
    raise Exception('Participant Not Found... (hint: PUUID or matchId may be incorrect)')
        