# Contains the main script used to run the game.

# Default variables
default routes_completed = 2


# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    call tower_choices1_start

    # This ends the game.
    return
