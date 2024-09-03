# Contains the main script used to run the game.

# Make dialogue stay on screen when choice menu appears
define config.choice_empty_window = extend

# Default variables
default routes_completed = 0
default aware_hero_met = False
default romance = 50
default chose_magic = None
default game_done = False
default ending = None

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

image main_menu_animated:
    "gui/main_menu_design1.png"
    pause 0.55
    "gui/main_menu_design2.png"
    pause 0.55
    "gui/main_menu_design3.png"
    pause 0.55
    "gui/main_menu_design2.png"
    pause 0.55
    repeat

# The game starts here.
label start:
    window hide # Don't hide dialogue box

    stop music fadeout 0.5

    pause 1
    # Give time for title screen music to stop

    while not game_done: # Main game loop

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


    if ending == "bad":
        call reset_default_vars
        jump start

    elif ending == "good":
        call credits

    else: # ending == "true"
        call credits
        call true_ending_monologue


    return # This ends the game.


label splashscreen:
    scene black
    with Pause(1)

    show text "{size=160}Play By Play Games" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return


# Credits courtesy of https://lemmasoft.renai.us/forums/viewtopic.php?t=22481
label credits:
    $ credits_speed = 52 #scrolling speed in seconds
    scene bg blackscreen #replace this with a fancy background

    if ending == "true":
        image theend = Text("{size=160}We found our happily ever after.", text_align=0.5)
    else: # ending == "good"
        image theend = Text("{size=160}I found my happily ever after.", text_align=0.5)

    show theend with dissolve:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with Pause(1.5)
    hide theend with dissolve
    show cred at Move((0.5, 10.7), (0.5, 0.625), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    pause 4.65
    play music "audio/Credits - Credits 2.mp3" noloop volume 1.0 fadein 0.5
    with Pause(credits_speed - 6)
    pause 3
    scene bg blackscreen with dissolve
    window hide
    pause 1.5
    return

init python:
    preferences.set_mixer("sfx", 0.8)
    credits = ('Lead Game Designer', 'William Liu'), ('Lead Programmer', 'Abdullah Safi'), ('Developer', 'Hamin Lee'), ('Character Artist', 'William Liu'), ('Environment Artist', 'Sion Jeong'), ('UI/UX Designers', 'William Liu'), ('UI/UX Designers', 'Hamin Lee'), ('Story Writers', 'Abdullah Safi'), ('Story Writers', 'Ben Ni'), ('Story Writers', 'William Liu'), ('Composer', 'Kyle Sung'), ('Special Thanks', 'Storytime')
    credits_s = "{size=160}Credits"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n\n\n\n\n\n\n\n\n"
            credits_s += "\n{size=80}" + c[0] + "\n"
            credits_s += "{size=120}" + c[1] + "\n"
        else:
            credits_s += "{size=120}" + c[1] + "\n"
        c1=c[0]
    
    credits_s += "\n\n\n\n"
    credits_s += "\n{size=80}Engine\n{size=120}" + renpy.version()
    credits_s += "\n\n\n\n\n\n"
    credits_s += "\n{size=210}Play By Play Games\n"
    credits_s += "\n\n\n\n\n\n"
    credits_s += "\n{size=160}With Love\n"
    
init:
    image cred = Text(credits_s, text_align=0.5)
    image thanks = Text("{size=160}With Love", text_align=0.5)