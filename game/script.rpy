﻿# Contains the main script used to run the game.

# Make dialogue stay on screen when choice menu appears
define config.choice_empty_window = extend

# Default variables
default routes_completed = 0
default aware_hero_met = False
default romance = 50
default chose_magic = None

default hu_times_gotten = 0
default ff_times_gotten = 0
default vs_times_gotten = 0
default dml_times_gotten = 0
default fh_times_gotten = 0

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
    window show

    stop music fadeout 0.5

    # scene bg blackscreen

    pause 1
    # Give time for title screen music to stop

    call hu_start
    
    call tower_start

    call forest_start

    call cryptic_start

    # This ends the game.
    return
