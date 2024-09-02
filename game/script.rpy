# Contains the main script used to run the game.

# Make dialogue stay on screen when choice menu appears
define config.choice_empty_window = extend

# Default variables
default routes_completed = 0
default aware_hero_met = False
default romance = 50
default chose_magic = None
default game_done = False

default v_type = None # Variable used for revealing villain type
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
image bg Cryptic_Touching = "base_backgrounds/bg Cryptic_Touching.png"
image bg Villain = "base_backgrounds/bg Villain.png"
image bg Meadow = "base_backgrounds/bg Meadow.png"
image bg Boulder = "base_backgrounds/bg Boulder.png"


# The game starts here.
label start:
    window hide # Don't hide dialogue box

    stop music fadeout 0.5

    # scene bg blackscreen

    pause 1
    # Give time for title screen music to stop

    call credits

    call true_ending_monologue

    # while not game_done:

    #     if routes_completed + 1 in aware_hero_routes: # Aware hero route
    #         call aware_hero_route

    #     else: # Not aware hero route

    #         # Tower
    #         call tower_start

    #         # Forest (and first villain encounter)
    #         call forest_start
            
    #         # Cryptic Stonehenge
    #         call cryptic_start

    #         # Meadow
    #         call meadow_start

    #         # Second Villain Encounter
    #         call second_villain_start

    #     $ routes_completed += 1

    # call credits

    # This ends the game.
    return


# Credits courtesy of https://lemmasoft.renai.us/forums/viewtopic.php?t=22481
label credits:
    $ credits_speed = 60 #scrolling speed in seconds
    scene bg blackscreen #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    play music "audio/Credits - Credits 1.mp3" loop volume 1.0 fadein 0.5
    show cred at Move((0.5, 10.85), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    stop music fadeout 1.5
    pause 1.5
    scene bg blackscreen
    return

init python:
    credits = ('Lead Designer', 'William Liu'), ('Lead Programmer', 'Abdullah Safi'), ('Developer', 'Hamin Lee'), ('Character Artist', 'William Liu'), ('Environment Artist', 'Sion'), ('UI/UX Designers', 'William Liu'), ('UI/UX Designers', 'Hamin Lee'), ('Story Writers', 'Abdullah Safi'), ('Story Writers', 'Ben Ni'), ('Story Writers', 'William Liu'), ('Composer', 'Kyle Sung'), ('Special Thanks', 'Storytime')
    credits_s = "{size=160}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n\n\n\n\n\n\n\n\n"
            credits_s += "\n{size=80}" + c[0] + "\n"
            credits_s += "{size=120}" + c[1] + "\n"
        else:
            credits_s += "{size=120}" + c[1] + "\n"
        c1=c[0]
    
    credits_s += "\n\n\n\n\n\n\n\n\n"
    credits_s += "\n{size=80}Engine\n{size=120}" + renpy.version()
    credits_s += "\n\n\n\n\n\n\n\n\n"
    credits_s += "\n{size=80}Play by Play Games\n"
    credits_s += "\n\n\n\n\n\n\n\n\n"
    credits_s += "\n{size=80}With Love\n"
    
init:
    # image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=160}We found our happily ever after.", text_align=0.5)
    image thanks = Text("{size=160}Thanks for Playing!", text_align=0.5)