# Contains the code associated with portion of the game related to the "vengeful spirit" second villain encounter.

    # Level 1 of choice tree
    label vs_choices_1:
        # Initial branch
        menu:
            "(Act) Prepare for combat":
                jump vs_choices_2_1

            "(Act) Try to reason with him":
                jump vs_choices_2_2


    # Level 2 of choice tree
    label vs_choices_2_1:
        # Branching from ""
        menu:
            "":
                jump vs_choices_3_1
            "":
                jump vs_choices_3_2

    label vs_choices_2_2:
        # Branching from ""
        menu:
            "":
                jump vs_choices_3_3
            "":
                jump vs_choices_3_4


    # Level 3 of choice tree
    label vs_choices_3_1:
        # Branching from ""
        menu:
            "":
                jump vs_choices_4_1
            "":
                jump vs_choices_4_2

    label vs_choices_3_2:
        # Branching from ""
        menu:
            "":
                jump vs_choices_4_3
            "":
                jump vs_choices_4_4

    label vs_choices_3_3:
        # Branching from ""
        menu:
            "":
                jump vs_choices_4_5
            "":
                jump vs_choices_4_6

    label vs_choices_3_4:
        # Branching from ""
        menu:
            "":
                jump vs_choices_4_7
            "":
                jump vs_choices_4_8

    
    # Level 4 of choice tree
    label vs_choices_4_1:
        # Branching from ""
        menu:
            "":
                jump vs_choices_5_1
            "":
                jump vs_choices_5_2

    label vs_choices_4_2:
        # Branching from ""
        menu:
            "":
                jump vs_choices_5_3
            "":
                jump vs_choices_5_4

    label vs_choices_4_3:
        # Branching from ""
        menu:
            "":
                jump vs_choices_5_5
            "":
                jump vs_choices_5_6

    label vs_choices_4_4:
        # Branching from ""
        menu:
            "":
                jump vs_choices_5_7
            "":
                jump vs_choices_5_8

    label vs_choices_4_5:
        # Branching from ""
        menu:
            "":
                jump vs_choices_5_9
            "":
                jump vs_choices_5_10

    label vs_choices_4_6:
        # Branching from ""
        menu:
            "":
                jump vs_choices_5_11
            "":
                jump vs_choices_5_12

    label vs_choices_4_7:
        # Branching from ""
        menu:
            "":
                jump vs_choices_5_13
            "":
                jump vs_choices_5_14

    label vs_choices_4_8:
        # Branching from ""
        menu:
            "":
                jump vs_choices_5_15
            "":
                jump vs_choices_5_16


    # Level 5 of choice tree
    label vs_choices_5_1:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_2:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_3:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_4:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_5:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_6:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_7:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_8:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_9:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_10:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_11:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_12:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_13:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_14:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_15:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump

    label vs_choices_5_16:
        # Branching from ""
        menu:
            "":
                jump
            "":
                jump