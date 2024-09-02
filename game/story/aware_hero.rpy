# Contains the code associated with portion of the game related to the "aware hero" dialogue.

default aware_hero_number = 0

label aware_hero:
    $ aware_hero_number += 1

    scene bg blackscreen with Dissolve(1.0)

    h "Deja vu."
    play music "audio/6 The Aware Hero 4.mp3"
    
    h "ITS BEEN SO LONG SINCE I LAST HAVE SEEN MY SON"

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
    stop music fadeout 1.5
    return

label aware_hero_second:
    stop music fadeout 1.5
    return

label aware_hero_third:
    stop music fadeout 1.5
    return

label aware_hero_fourth:
    $ game_done = True
    stop music fadeout 1.5
    return

label aware_hero_route:
    
    # Tower
    call tower_start


    # Forest (and first villain encounter)
    call forest_start

    if renpy.random.randint(1, 10) <= 2: # 2/10 chance to trigger aware hero
        call aware_hero
        return
    

    # Cryptic Stonehenge
    call cryptic_start

    if renpy.random.randint(1, 10) <= 4: # 4/10 chance to trigger aware hero
        call aware_hero
        return


    # Meadow
    call meadow_start

    if renpy.random.randint(1, 10) <= 7: # 7/10 chance to trigger aware hero
        call aware_hero
        return


    # Second Villain Encounter
    call second_villain_start
    return