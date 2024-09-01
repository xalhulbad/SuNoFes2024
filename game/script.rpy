# Contains the main script used to run the game.

# Make dialogue stay on screen when choice menu appears
define config.choice_empty_window = extend

# Default variables
default routes_completed = 0
default aware_hero_met = False
default romance = 50
default chose_magic = None
default game_done = False

default hu_times_gotten = 0
default ff_times_gotten = 0
default vs_times_gotten = 0
default dml_times_gotten = 0
default fh_times_gotten = 0

define aware_hero_routes = [3, 6, 8, 9]

# Background images
image bg blackscreen = "bg blackscreen.png"
image bg Tower = "bg Tower.png"
image bg Forest1 = "bg Forest1.png"
image bg Forest2 = "bg Forest2.png"
image bg Cryptic = "bg Cryptic.png"
image bg Villain = "bg Villain.png"
image bg Meadow = "bg Meadow.jpeg"


# The game starts here.
label start:
    window hide # Don't hide dialogue box

    stop music fadeout 0.5

    # scene bg blackscreen

    pause 1
    # Give time for title screen music to stop

    while not game_done:

        # Tower
        call tower_start


        # Forest (and first villain encounter)
        call forest_start

        if routes_completed + 1 in aware_hero_routes: # 2/10 chance to trigger aware hero
            if renpy.random.randint(1, 10) <= 2:
                jump aware_hero
        

        # Cryptic Stonehenge
        call cryptic_start

        if routes_completed + 1 in aware_hero_routes: # 4/10 chance to trigger aware hero
            if renpy.random.randint(1, 10) <= 4:
                jump aware_hero


        # Meadow
        call meadow_start

        if routes_completed + 1 in aware_hero_routes: # 7/10 chance to trigger aware hero
            if renpy.random.randint(1, 10) <= 7:
                jump aware_hero


        # Second Villain Encounter
        call second_villain_start


        $ routes_completed += 1
    

    # This ends the game.
    return
