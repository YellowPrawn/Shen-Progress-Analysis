#' Scrapes events in frames to generate a count of shrooms destroyed
#' 
#' Scrapes events in frames to generate a count ofshrooms destroyed
#' 
#' @param frame dictionary of frames from a match timeline
#'
#' @return a number of shrooms destroyed
#'
#' @export
#'
#' @examples
#' get_shroom_updates(frames)

def get_shrooms_destroyed(frames):
    i = 0
    for e in frames['events']:
        try:
            if e['type'] == 'WARD_KILL' and e['wardType'] == 'TEEMO_MUSHROOM':
                i = i + 1
        except KeyError:
            pass
    return i