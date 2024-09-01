# Contains the code associated with portion of the game related to the "aware hero" dialogue.

default aware_hero_number = 0

label aware_hero:
    $ aware_hero_number += 1

    if aware_hero_number == 1:
        jump aware_hero_first
    elif aware_hero_number == 2:
        jump aware_hero_second
    elif aware_hero_number == 3:
        jump aware_hero_third
    else:
        jump aware_hero_fourth


label aware_hero_first:
    $ aware_hero_met = True
    return

label aware_hero_second:
    return

label aware_hero_third:
    return

label aware_hero_fourth:
    $ game_done = True
    return