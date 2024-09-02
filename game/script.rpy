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

define aware_hero_routes = [3, 6, 8]

# Background images
image bg blackscreen = "base_backgrounds/bg blackscreen.png"
image bg Tower = "base_backgrounds/bg Tower.png"
image bg Forest1 = "base_backgrounds/bg Forest1.png"
image bg Forest2 = "base_backgrounds/bg Forest2.png"
image bg Cryptic = "base_backgrounds/bg Cryptic.png"
image bg Villain = "base_backgrounds/bg Villain.png"
image bg Meadow = "base_backgrounds/bg Meadow.jpeg"


# The game starts here.
label start:
    window hide # Don't hide dialogue box

    stop music fadeout 0.5

    # scene bg blackscreen

    pause 1
    # Give time for title screen music to stop

    while not game_done:

        if routes_completed + 1 in aware_hero_routes: # Aware hero route
            call aware_hero_route

        else: # Not aware hero route

            # Tower
            call tower_start

            # Forest (and first villain encounter)
            call forest_start
            
            # Cryptic Stonehenge
            call cryptic_start

            # Meadow
            call meadow_start

            # Second Villain Encounter
            call second_villain_start

        $ routes_completed += 1


    # This ends the game.
    return
