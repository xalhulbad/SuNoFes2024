# Contains the code associated with portion of the game related to the "fallen hero" second villain encounter.

# Default variables


# Flags for unlockable options
default fh_chose_who_are_you = False
default fh_chose_why_hold_grudge = False
default fh_chose_things_have_changed = False
default fh_chose_what_happened = False
default fh_chose_why_kingdom_turn = False
default fh_chose_really_believe_revenge = False
default fh_chose_why_hunt_us = False
default fh_chose_killing_us_satisfy = False
default fh_chose_what_would_you_do = False
default fh_chose_why_cant_pass = False
default fh_chose_change_your_mind = False
default fh_chose_not_like_those = False

label fh_start:
    # Reset dialogue pool flags
    $ fh_chose_who_are_you = False
    $ fh_chose_why_hold_grudge = False
    $ fh_chose_things_have_changed = False
    $ fh_chose_what_happened = False
    $ fh_chose_why_kingdom_turn = False
    $ fh_chose_really_believe_revenge = False
    $ fh_chose_why_hunt_us = False
    $ fh_chose_killing_us_satisfy = False
    $ fh_chose_what_would_you_do = False
    $ fh_chose_why_cant_pass = False
    $ fh_chose_change_your_mind = False
    $ fh_chose_not_like_those = False

    # Leading text
    n "The forest seemed darker than before, the shadows deeper and more menacing as the princess and hero retraced their steps."
    n "Each rustling leaf and distant creak of branches felt like the forest itself was holding its breath. The princess and hero could see the kingdom now, a sign that they were getting close."
    n "The hero’s grip tightened on his sword as they ventured further, his eyes scanning every shadow for signs of movement."
    n "He could feel it—the tension in the air that signaled they were not alone. The princess’s thoughts raced as they drew closer and closer to their destination."
    n "As they pressed forward, a familiar figure stepped out from the shadows. The Fallen Hero’s presence was as foreboding as ever, his scarred face a mask of bitterness and fury."
    n "His sword remained sheathed, but the tension in his stance made it clear that any peace was fragile and fleeting."

    if fh_times_gotten == 1:
        pt "It’s him… the warrior who lost everything. Can we find a way through this without bloodshed?"

    elif fh_times_gotten == 2:
        pt "We meet again. Maybe this time, I can reach him—if there’s still a part of him left that wants peace."

    else:
        pt "No more running. Let’s put an end to this cycle, one way or another."
    
    fh "So, we meet again. I’ve decided that you must pay for the kingdom’s past sins. Did you think the forest would forget? Or perhaps you thought you could change what’s already been broken?"
    n "The hero instinctively moved to shield the princess, his stance guarded but ready for battle."
    n "He knew that any misstep could lead to bloodshed, and the Fallen Hero’s rage had only grown since their last encounter."
    h "We don’t want to fight, but we’ll defend ourselves if we have to. There’s still a chance to end this without more pain."
    fh "Pain? You speak of pain as if you understand it. But you’re nothing more than pawns of the kingdom that turned its back on me."
    fh "No matter what words you offer, they’re all tainted by lies."
    n "The Fallen Hero’s hand drifted to the hilt of his blade, his eyes locked onto the princess with a gaze that was both accusatory and conflicted."
    n "The air crackled with unspoken threats as the forest seemed to darken around them."
    fh "Enough of this. Your fate was sealed the moment you chose to serve a kingdom built on betrayal."
    fh "Now, let’s see if you can back up your convictions with steel."

    jump fh_choices_1

    # Level 1 of choice tree
    label fh_choices_1:
        # Initial branch
        menu:
            "(Act) Prepare for combat":
                jump fh_choices_2_1

            "(Act) Try to reason with him":
                jump fh_choices_2_2


    # Level 2 of choice tree
    label fh_choices_2_1:
        # Branching from ""
        menu:
            "":
                jump fh_choices_3_1
            "":
                jump fh_choices_3_2

    label fh_choices_2_2:
        # Branching from ""
        menu:
            "":
                jump fh_choices_3_3
            "":
                jump fh_choices_3_4


    # Level 3 of choice tree
    label fh_choices_3_1:
        # Branching from ""
        menu:
            "":
                jump fh_choices_4_1
            "":
                jump fh_choices_4_2

    label fh_choices_3_2:
        # Branching from ""
        menu:
            "":
                jump fh_choices_4_3
            "":
                jump fh_choices_4_4

    label fh_choices_3_3:
        # Branching from ""
        menu:
            "":
                jump fh_choices_4_5
            "":
                jump fh_choices_4_6

    label fh_choices_3_4:
        # Branching from ""
        menu:
            "":
                jump fh_choices_4_7
            "":
                jump fh_choices_4_8

    
    # Level 4 of choice tree
    label fh_choices_4_1:
        # Branching from ""
        menu:
            "":
                jump fh_choices_5_1
            "":
                jump fh_choices_5_2

    label fh_choices_4_2:
        # Branching from ""
        menu:
            "":
                jump fh_choices_5_3
            "":
                jump fh_choices_5_4

    label fh_choices_4_3:
        # Branching from ""
        menu:
            "":
                jump fh_choices_5_5
            "":
                jump fh_choices_5_6

    label fh_choices_4_4:
        # Branching from ""
        menu:
            "":
                jump fh_choices_5_7
            "":
                jump fh_choices_5_8

    label fh_choices_4_5:
        # Branching from ""
        menu:
            "":
                jump fh_choices_5_9
            "":
                jump fh_choices_5_10

    label fh_choices_4_6:
        # Branching from ""
        menu:
            "":
                jump fh_choices_5_11
            "":
                jump fh_choices_5_12

    label fh_choices_4_7:
        # Branching from ""
        menu:
            "":
                jump fh_choices_5_13
            "":
                jump fh_choices_5_14

    label fh_choices_4_8:
        # Branching from ""
        menu:
            "":
                jump fh_choices_5_15
            "":
                jump fh_choices_5_16


    # Level 5 of choice tree
    label fh_choices_5_1:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_2:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_3:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_4:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_5:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_6:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_7:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_8:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_9:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_10:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_11:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_12:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_13:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_14:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_15:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label fh_choices_5_16:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump
    



label fh_who_are_you:
    return

label fh_why_hold_grudge:
    return

label fh_things_have_changed:
    return

label fh_what_happened:
    return

label fh_why_kingdom_turn:
    return

label fh_really_believe_revenge:
    return

label fh_why_hunt_us:
    return

label fh_killing_us_satisfy:
    return

label fh_what_would_you_do:
    return

label fh_why_cant_pass:
    return

label fh_change_your_mind:
    return

label fh_not_like_those:
    return

