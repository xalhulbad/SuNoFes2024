# Contains the main script used to run the game.

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


# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg blackscreen

    call tower_start

    call forest_start

    call cryptic_start

    # This ends the game.
    return
