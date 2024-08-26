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


# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    call tower_start

    call forest_start

    call cryptic_start

    # This ends the game.
    return
