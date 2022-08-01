#' Scrapes events in frames to generate a sum of the damage dealt by shrooms in a kill participation
#' 
#' Scrapes events in frames to generate a sum of the damage dealt by shrooms in a kill participation
#' 
#' @param frame dictionary of frames from a match timeline
#'
#' @return a sum of the damage dealt with shrooms
#'
#' @export
#'
#' @examples
#' get_shroom_damage(frames)
def get_shroom_damage(frames):
    i = 0
    for e in frames['events']:
        try:
            for v in e['victimDamageReceived']:
                if v['spellName'] == 'teemorcast' and v['name'] == 'Teemo':
                    i = i + v['magicDamage']
        except KeyError:
                pass
    return i