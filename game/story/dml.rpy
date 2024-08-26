# Contains the code associated with portion of the game related to the "dark magic lord" second villain encounter.

# Default Variables


# Flags for unlockable options

default dml_chose_who_are_you = False
default dml_chose_why_do_you = False
default dml_chose_what_do_you = False
default dml_chose_how_did_you = False
default dml_chose_what_drives_your = False
default dml_chose_do_you_not = False
default dml_chose_what_is_your = False
default dml_chose_do_you_really = False
default dml_chose_how_do_you = False
default dml_chose_why_cant_you = False
default dml_chose_is_there_nothing = False
default dml_chose_what_would_happen = False

label dml_who_are_you:
    return
label dml_why_do_you:
    return
label dml_what_do_you:
    return
label dml_how_did_you:
    return
label dml_what_drives_your:
    return
label dml_do_you_not:
    return
label dml_what_is_your:
    return
label dml_do_you_really:
    return
label dml_how_do_you:
    return
label dml_why_cant_you:
    return
label dml_is_there_nothing:
    return
label dml_what_would_happen:
    return



label dml_start:
    $ dml_chose_who_are_you = False
    $ dml_chose_why_do_you = False
    $ dml_chose_what_do_you = False
    $ dml_chose_how_did_you = False
    $ dml_chose_what_drives_your = False
    $ dml_chose_do_you_not = False
    $ dml_chose_what_is_your = False
    $ dml_chose_do_you_really = False
    $ dml_chose_how_do_you = False
    $ dml_chose_why_cant_you = False
    $ dml_chose_is_there_nothing = False
    $ dml_chose_what_would_happen = False

    # Leading text
    n "The forest's atmosphere grew heavier as the princess and the hero ventured deeper, an unnatural darkness creeping in from all sides. The air was thick with the stench of decay, and the once vibrant trees were now withered and lifeless."
    n "The hero’s hand hovered over his sword, eyes narrowing as the oppressive energy weighed down on them. He could sense it—an evil force lurking nearby, draining the life from everything it touched."
    n "From the shadows, a figure materialized, cloaked in dark robes that seemed to absorb the light around them. His eyes glowed with a malevolent energy, and a twisted smile spread across his face as he observed the pair."
    dml "Ah, the kingdom’s pawns have arrived. Come to witness the grandeur of true power? You’re just in time to see the culmination of my work!"
    
    if dml_times_gotten == 1: 
        pt "The Dark Magic Lord again… He's the source of all this corruption. We have to stop him before it’s too late." 
    
    elif dml_times_gotten == 2: 
        pt "We’ve faced him before. We know his tricks, but he’s more dangerous than ever. We can’t let our guard down." 
    
    else: 
        pt "It’s him again… We know what to expect, but we can’t underestimate him. This has to end soon..."
    
    n "The Dark Magic Lord stepped forward, his presence exuding an overwhelming aura of arrogance and delusion. The hero instinctively moved in front of the princess, his stance protective but tense."
    h "Stay back, princess. His power may be great, but it’s born of madness. We must be careful."
    dml "Madness? You dare call my work madness? This forest was dying long before I arrived. I am its salvation, its rebirth! But of course, you’re too blind to see the truth."
    n "The Dark Magic Lord raised his hand, dark tendrils of magic swirling around his fingers, ready to strike at a moment’s notice. The air buzzed with dangerous energy, and the forest seemed to tremble under his influence."
    dml "Enough talk. If you’re so determined to stand in my way, then witness the power of the one true savior of this world!"


    # Level 1 of choice tree
    label dml_choices_1:
        # Initial branch
        menu:
            "":
                jump dml_choices_2_1

            "":
                jump dml_choices_2_2

            
            # Dialogue pool options

            "(Speak) Who are you?" if not dml_chose_who_are_you:
                $ dml_chose_who_are_you = True
                call dml_who_are_you
                jump dml_choices_1

            "(Speak) Why do you claim to be a hero?" if not dml_chose_why_do_you and dml_chose_who_are_you:
                $ dml_chose_why_do_you = True
                call dml_why_do_you
                jump dml_choices_1

            "(Speak) What do you truly seek?" if not dml_chose_what_do_you and dml_chose_why_do_you:
                $ dml_chose_what_do_you = True
                call dml_what_do_you
                jump dml_choices_1

            "(Speak) How did you come to wield such power?" if not dml_chose_how_did_you:
                $ dml_chose_how_did_you = True
                call dml_how_did_you
                jump dml_choices_1

            "(Speak) What drives your obsession with magic?" if not dml_chose_what_drives_your and dml_chose_how_did_you:
                $ dml_chose_what_drives_your = True
                call dml_what_drives_your
                jump dml_choices_1

            "(Speak) Do you not understand the consequences of your actions?" if not dml_chose_do_you_not and dml_chose_what_drives_your:
                $ dml_chose_do_you_not = True
                call dml_do_you_not
                jump dml_choices_1
            
            "(Speak) What is your end goal?" if not dml_chose_what_is_your:
                $ dml_chose_what_is_your = True
                call dml_what_is_your
                jump dml_choices_1

            "(Speak) Do you really believe this will save the world?" if not dml_chose_do_you_really and dml_chose_what_is_your:
                $ dml_chose_do_you_really = True
                call dml_do_you_really
                jump dml_choices_1

            "(Speak) How do you justify the suffering you’ve caused?" if not dml_chose_how_do_you and dml_chose_do_you_really:
                $ dml_chose_how_do_you = True
                call dml_how_do_you
                jump dml_choices_1

            "(Speak) Why can’t you stop overusing magic?" if not dml_chose_why_cant_you:
                $ dml_chose_why_cant_you = True
                call dml_why_cant_you
                jump dml_choices_1

            "(Speak) Is there nothing that would change your mind?" if not dml_chose_is_there_nothing and dml_chose_why_cant_you:
                $ dml_chose_is_there_nothing = True
                call dml_is_there_nothing
                jump dml_choices_1

            "(Speak) What would happen if you did stop?" if not dml_chose_what_would_happen and dml_chose_is_there_nothing:
                $ dml_chose_what_would_happen = True
                call dml_what_would_happen
                jump dml_choices_1


    # Level 2 of choice tree
    label dml_choices_2_1:
        # Branching from ""
        menu:
            "":
                jump dml_choices_3_1
            "":
                jump dml_choices_3_2

            
            # Dialogue pool options

            "(Speak) Who are you?" if not dml_chose_who_are_you:
                $ dml_chose_who_are_you = True
                call dml_who_are_you
                jump dml_choices_2_1

            "(Speak) Why do you claim to be a hero?" if not dml_chose_why_do_you and dml_chose_who_are_you:
                $ dml_chose_why_do_you = True
                call dml_why_do_you
                jump dml_choices_2_1

            "(Speak) What do you truly seek?" if not dml_chose_what_do_you and dml_chose_why_do_you:
                $ dml_chose_what_do_you = True
                call dml_what_do_you
                jump dml_choices_2_1

            "(Speak) How did you come to wield such power?" if not dml_chose_how_did_you:
                $ dml_chose_how_did_you = True
                call dml_how_did_you
                jump dml_choices_2_1

            "(Speak) What drives your obsession with magic?" if not dml_chose_what_drives_your and dml_chose_how_did_you:
                $ dml_chose_what_drives_your = True
                call dml_what_drives_your
                jump dml_choices_2_1

            "(Speak) Do you not understand the consequences of your actions?" if not dml_chose_do_you_not and dml_chose_what_drives_your:
                $ dml_chose_do_you_not = True
                call dml_do_you_not
                jump dml_choices_2_1
            
            "(Speak) What is your end goal?" if not dml_chose_what_is_your:
                $ dml_chose_what_is_your = True
                call dml_what_is_your
                jump dml_choices_2_1

            "(Speak) Do you really believe this will save the world?" if not dml_chose_do_you_really and dml_chose_what_is_your:
                $ dml_chose_do_you_really = True
                call dml_do_you_really
                jump dml_choices_2_1

            "(Speak) How do you justify the suffering you’ve caused?" if not dml_chose_how_do_you and dml_chose_do_you_really:
                $ dml_chose_how_do_you = True
                call dml_how_do_you
                jump dml_choices_2_1

            "(Speak) Why can’t you stop overusing magic?" if not dml_chose_why_cant_you:
                $ dml_chose_why_cant_you = True
                call dml_why_cant_you
                jump dml_choices_2_1

            "(Speak) Is there nothing that would change your mind?" if not dml_chose_is_there_nothing and dml_chose_why_cant_you:
                $ dml_chose_is_there_nothing = True
                call dml_is_there_nothing
                jump dml_choices_2_1

            "(Speak) What would happen if you did stop?" if not dml_chose_what_would_happen and dml_chose_is_there_nothing:
                $ dml_chose_what_would_happen = True
                call dml_what_would_happen
                jump dml_choices_2_1

    label dml_choices_2_2:
        # Branching from ""
        menu:
            "":
                jump dml_choices_3_3
            "":
                jump dml_choices_3_4

            
            # Dialogue pool options

            "(Speak) Who are you?" if not dml_chose_who_are_you:
                $ dml_chose_who_are_you = True
                call dml_who_are_you
                jump dml_choices_2_2

            "(Speak) Why do you claim to be a hero?" if not dml_chose_why_do_you and dml_chose_who_are_you:
                $ dml_chose_why_do_you = True
                call dml_why_do_you
                jump dml_choices_2_2

            "(Speak) What do you truly seek?" if not dml_chose_what_do_you and dml_chose_why_do_you:
                $ dml_chose_what_do_you = True
                call dml_what_do_you
                jump dml_choices_2_2

            "(Speak) How did you come to wield such power?" if not dml_chose_how_did_you:
                $ dml_chose_how_did_you = True
                call dml_how_did_you
                jump dml_choices_2_2

            "(Speak) What drives your obsession with magic?" if not dml_chose_what_drives_your and dml_chose_how_did_you:
                $ dml_chose_what_drives_your = True
                call dml_what_drives_your
                jump dml_choices_2_2

            "(Speak) Do you not understand the consequences of your actions?" if not dml_chose_do_you_not and dml_chose_what_drives_your:
                $ dml_chose_do_you_not = True
                call dml_do_you_not
                jump dml_choices_2_2
            
            "(Speak) What is your end goal?" if not dml_chose_what_is_your:
                $ dml_chose_what_is_your = True
                call dml_what_is_your
                jump dml_choices_2_2

            "(Speak) Do you really believe this will save the world?" if not dml_chose_do_you_really and dml_chose_what_is_your:
                $ dml_chose_do_you_really = True
                call dml_do_you_really
                jump dml_choices_2_2

            "(Speak) How do you justify the suffering you’ve caused?" if not dml_chose_how_do_you and dml_chose_do_you_really:
                $ dml_chose_how_do_you = True
                call dml_how_do_you
                jump dml_choices_2_2

            "(Speak) Why can’t you stop overusing magic?" if not dml_chose_why_cant_you:
                $ dml_chose_why_cant_you = True
                call dml_why_cant_you
                jump dml_choices_2_2

            "(Speak) Is there nothing that would change your mind?" if not dml_chose_is_there_nothing and dml_chose_why_cant_you:
                $ dml_chose_is_there_nothing = True
                call dml_is_there_nothing
                jump dml_choices_2_2

            "(Speak) What would happen if you did stop?" if not dml_chose_what_would_happen and dml_chose_is_there_nothing:
                $ dml_chose_what_would_happen = True
                call dml_what_would_happen
                jump dml_choices_2_2


    # Level 3 of choice tree
    label dml_choices_3_1:
        # Branching from ""
        menu:
            "":
                jump dml_choices_4_1
            "":
                jump dml_choices_4_2

    label dml_choices_3_2:
        # Branching from ""
        menu:
            "":
                jump dml_choices_4_3
            "":
                jump dml_choices_4_4

    label dml_choices_3_3:
        # Branching from ""
        menu:
            "":
                jump dml_choices_4_5
            "":
                jump dml_choices_4_6

    label dml_choices_3_4:
        # Branching from ""
        menu:
            "":
                jump dml_choices_4_7
            "":
                jump dml_choices_4_8

    
    # Level 4 of choice tree
    label dml_choices_4_1:
        # Branching from ""
        menu:
            "":
                jump dml_choices_5_1
            "":
                jump dml_choices_5_2

    label dml_choices_4_2:
        # Branching from ""
        menu:
            "":
                jump dml_choices_5_3
            "":
                jump dml_choices_5_4

    label dml_choices_4_3:
        # Branching from ""
        menu:
            "":
                jump dml_choices_5_5
            "":
                jump dml_choices_5_6

    label dml_choices_4_4:
        # Branching from ""
        menu:
            "":
                jump dml_choices_5_7
            "":
                jump dml_choices_5_8

    label dml_choices_4_5:
        # Branching from ""
        menu:
            "":
                jump dml_choices_5_9
            "":
                jump dml_choices_5_10

    label dml_choices_4_6:
        # Branching from ""
        menu:
            "":
                jump dml_choices_5_11
            "":
                jump dml_choices_5_12

    label dml_choices_4_7:
        # Branching from ""
        menu:
            "":
                jump dml_choices_5_13
            "":
                jump dml_choices_5_14

    label dml_choices_4_8:
        # Branching from ""
        menu:
            "":
                jump dml_choices_5_15
            "":
                jump dml_choices_5_16


    # Level 5 of choice tree
    label dml_choices_5_1:
        # Branching from ""
        menu:
            "":
                jump sacrificed_princess
            "":
                jump inherited_throne

    label dml_choices_5_2:
        # Branching from ""
        menu:
            "":
                jump inherited_throne
            "":
                jump sacrificed_princess

    label dml_choices_5_3:
        # Branching from ""
        menu:
            "":
                jump corrupted_hero
            "":
                jump love_beyond_death

    label dml_choices_5_4:
        # Branching from ""
        menu:
            "":
                jump forest_curse
            "":
                jump forest_protectors

    label dml_choices_5_5:
        # Branching from ""
        menu:
            "":
                jump forest_curse
            "":
                jump forest_protectors

    label dml_choices_5_6:
        # Branching from ""
        menu:
            "":
                jump corrupted_hero
            "":
                jump forest_curse

    label dml_choices_5_7:
        # Branching from ""
        menu:
            "":
                jump unfulfilled_love
            "":
                jump sacrificed_princess

    label dml_choices_5_8:
        # Branching from ""
        menu:
            "":
                jump unfulfilled_love
            "":
                jump forest_protectors

    label dml_choices_5_9:
        # Branching from ""
        menu:
            "":
                jump sacrificed_hero
            "":
                jump inherited_throne

    label dml_choices_5_10:
        # Branching from ""
        menu:
            "":
                jump sacrificed_hero
            "":
                jump love_beyond_death

    label dml_choices_5_11:
        # Branching from ""
        menu:
            "":
                jump love_beyond_death
            "":
                jump forest_protectors

    label dml_choices_5_12:
        # Branching from ""
        menu:
            "":
                jump inherited_throne
            "":
                jump sacrificed_hero

    label dml_choices_5_13:
        # Branching from ""
        menu:
            "":
                jump corrupted_hero
            "":
                jump unfulfilled_love

    label dml_choices_5_14:
        # Branching from ""
        menu:
            "":
                jump corrupted_hero
            "":
                jump forest_curse

    label dml_choices_5_15:
        # Branching from ""
        menu:
            "":
                jump sacrificed_hero
            "":
                jump sacrificed_princess

    label dml_choices_5_16:
        # Branching from ""
        menu:
            "":
                jump unfulfilled_love
            "":
                jump love_beyond_death