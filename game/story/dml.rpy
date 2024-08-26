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

    # Level 1 of choice tree
    label dml_choices_1:
        # Initial branch
        menu:
            "":
                jump dml_choices_2_1

            "":
                jump dml_choices_2_2


    # Level 2 of choice tree
    label dml_choices_2_1:
        # Branching from ""
        menu:
            "":
                jump dml_choices_3_1
            "":
                jump dml_choices_3_2

    label dml_choices_2_2:
        # Branching from ""
        menu:
            "":
                jump dml_choices_3_3
            "":
                jump dml_choices_3_4


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
                jump
            "":
                jump

    label dml_choices_5_2:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_3:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_4:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_5:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_6:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_7:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_8:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_9:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_10:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_11:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_12:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_13:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_14:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_15:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label dml_choices_5_16:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump