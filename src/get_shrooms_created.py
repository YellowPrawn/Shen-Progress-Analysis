#' Scrapes events in frames to generate a count of shrooms created
#' 
#' Scrapes events in frames to generate a count of shrooms created
#' 
#' @param participant_id participant id in match (between 1 and 10)
#' @param frame dictionary of frames from a match timeline
#'
#' @return a number of shrooms placed
#'
#' @export
#'
#' @examples
#' get_shrooms_created(10, frames)

def get_shrooms_created(participant_id, frames):
    i = 0
    for e in frames['events']:
        try:
            if e['creatorId'] == participant_id and e['wardType'] == 'TEEMO_MUSHROOM':
                i = i + 1
        except KeyError:
            pass
    return i