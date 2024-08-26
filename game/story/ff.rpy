# Contains the code associated with portion of the game related to the "femme fatale" second villain encounter.

# Default Variables


# Flags for unlockable options
default ff_chose_who_are_you = False
default ff_chose_why_doing_this = False
default ff_chose_what_you_gain = False
default ff_chose_why_enjoy_manipulating = False
default ff_chose_isnt_there_more = False
default ff_chose_do_you_not = False
default ff_chose_how_did_you = False
default ff_chose_was_there_ever = False
default ff_chose_do_you_think = False
default ff_chose_what_do_you = False
default ff_chose_is_this_just = False
default ff_chose_when_will_it = False

label ff_who_are_you:
    return
label ff_why_doing_this:
    return
label ff_what_you_gain:
    return
label ff_why_enjoy_manipulating:
    return
label ff_isnt_there_more:
    return
label ff_do_you_not:
    return
label ff_how_did_you:
    return
label ff_was_there_ever:
    return
label ff_do_you_think:
    return
label ff_what_do_you:
    return
label ff_is_this_just:
    return
label ff_when_will_it:
    return


label ff_start:

    # Level 1 of choice tree
    label ff_choices_1:
        # Initial branch
        menu:
            "":
                jump ff_choices_2_1

            "":
                jump ff_choices_2_2


    # Level 2 of choice tree
    label ff_choices_2_1:
        # Branching from ""
        menu:
            "":
                jump ff_choices_3_1
            "":
                jump ff_choices_3_2

    label ff_choices_2_2:
        # Branching from ""
        menu:
            "":
                jump ff_choices_3_3
            "":
                jump ff_choices_3_4


    # Level 3 of choice tree
    label ff_choices_3_1:
        # Branching from ""
        menu:
            "":
                jump ff_choices_4_1
            "":
                jump ff_choices_4_2

    label ff_choices_3_2:
        # Branching from ""
        menu:
            "":
                jump ff_choices_4_3
            "":
                jump ff_choices_4_4

    label ff_choices_3_3:
        # Branching from ""
        menu:
            "":
                jump ff_choices_4_5
            "":
                jump ff_choices_4_6

    label ff_choices_3_4:
        # Branching from ""
        menu:
            "":
                jump ff_choices_4_7
            "":
                jump ff_choices_4_8

    
    # Level 4 of choice tree
    label ff_choices_4_1:
        # Branching from ""
        menu:
            "":
                jump ff_choices_5_1
            "":
                jump ff_choices_5_2

    label ff_choices_4_2:
        # Branching from ""
        menu:
            "":
                jump ff_choices_5_3
            "":
                jump ff_choices_5_4

    label ff_choices_4_3:
        # Branching from ""
        menu:
            "":
                jump ff_choices_5_5
            "":
                jump ff_choices_5_6

    label ff_choices_4_4:
        # Branching from ""
        menu:
            "":
                jump ff_choices_5_7
            "":
                jump ff_choices_5_8

    label ff_choices_4_5:
        # Branching from ""
        menu:
            "":
                jump ff_choices_5_9
            "":
                jump ff_choices_5_10

    label ff_choices_4_6:
        # Branching from ""
        menu:
            "":
                jump ff_choices_5_11
            "":
                jump ff_choices_5_12

    label ff_choices_4_7:
        # Branching from ""
        menu:
            "":
                jump ff_choices_5_13
            "":
                jump ff_choices_5_14

    label ff_choices_4_8:
        # Branching from ""
        menu:
            "":
                jump ff_choices_5_15
            "":
                jump ff_choices_5_16


    # Level 5 of choice tree
    label ff_choices_5_1:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_2:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_3:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_4:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_5:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_6:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_7:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_8:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_9:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_10:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_11:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_12:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_13:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_14:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_15:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label ff_choices_5_16:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump