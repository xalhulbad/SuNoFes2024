# Contains the code associated with portion of the game related to the "vengeful spirit" second villain encounter.

# Default Variables


# Flags for unlockable options

default vs_chose_who_are_you = False
default vs_chose_why_do_you_seek = False
default vs_chose_can_you_ever = False
default vs_chose_what_do_you = False
default vs_chose_why_do_you_blame = False
default vs_chose_isnt_there_a = False
default vs_chose_why_cant_you = False
default vs_chose_do_you_not = False
default vs_chose_cant_you_find = False
default vs_chose_what_will_you = False
default vs_chose_will_your_vengeance = False
default vs_chose_what_then = False

label vs_who_are_you:
    return
label vs_why_do_you_seek:
    return
label vs_can_you_ever:
    return
label vs_what_do_you:
    return
label vs_why_do_you_blame:
    return
label vs_isnt_there_a:
    return
label vs_why_cant_you:
    return
label vs_do_you_not:
    return
label vs_cant_you_find:
    return
label vs_what_will_you:
    return
label vs_will_your_vengeance:
    return
label vs_what_then:
    return


label vs_start:
    $ vs_chose_who_are_you = False
    $ vs_chose_why_do_you_seek = False
    $ vs_chose_can_you_ever = False
    $ vs_chose_what_do_you = False
    $ vs_chose_why_do_you_blame = False
    $ vs_chose_isnt_there_a = False
    $ vs_chose_why_cant_you = False
    $ vs_chose_do_you_not = False
    $ vs_chose_cant_you_find = False
    $ vs_chose_what_will_you = False
    $ vs_chose_will_your_vengeance = False
    $ vs_chose_what_then = False

    # Level 1 of choice tree
    label vs_choices_1:
        # Initial branch
        menu:
            "":
                jump vs_choices_2_1

            "":
                jump vs_choices_2_2
            

            # Dialogue pool options

            "(Speak) Who are you?" if not vs_chose_who_are_you:
                $ vs_chose_who_are_you = True
                call vs_who_are_you
                jump vs_choices_1

            "(Speak) Why do you seek vengeance?" if not vs_chose_why_do_you_seek and vs_chose_who_are_you:
                $ vs_chose_why_do_you_seek = True
                call vs_why_do_you_seek
                jump vs_choices_1

            "(Speak) Can you ever be at peace?" if not vs_chose_can_you_ever and vs_chose_why_do_you_seek:
                $ vs_chose_can_you_ever = True
                call vs_can_you_ever
                jump vs_choices_1

            "(Speak) What do you want from us?" if not vs_chose_what_do_you:
                $ vs_chose_what_do_you = True
                call vs_what_do_you
                jump vs_choices_1

            "(Speak) Why do you blame us for the kingdom’s sins?" if not vs_chose_why_do_you_blame and vs_chose_why_do_you_blame:
                $ vs_chose_why_do_you_blame = True
                call vs_why_do_you_blame
                jump vs_choices_1

            "(Speak) Isn’t there a way to break this cycle of hatred?" if not vs_chose_isnt_there_a and vs_chose_isnt_there_a:
                $ vs_chose_isnt_there_a = True
                call vs_isnt_there_a
                jump vs_choices_1
            
            "(Speak) Why can’t you let go of your anger?" if not vs_chose_why_cant_you:
                $ vs_chose_why_cant_you = True
                call vs_why_cant_you
                jump vs_choices_1

            "(Speak) Do you not see the destruction your rage causes?" if not vs_chose_do_you_not and vs_chose_why_cant_you:
                $ vs_chose_do_you_not = True
                call vs_do_you_not
                jump vs_choices_1

            "(Speak) Can’t you find peace in the forest’s renewal?" if not vs_chose_cant_you_find and vs_chose_cant_you_find:
                $ vs_chose_cant_you_find = True
                call vs_cant_you_find
                jump vs_choices_1

            "(Speak) What will you do if you destroy us?" if not vs_chose_what_will_you:
                $ vs_chose_what_will_you = True
                call vs_what_will_you
                jump vs_choices_1

            "(Speak) Will your vengeance ever be enough?" if not vs_chose_will_your_vengeance and vs_chose_what_will_you:
                $ vs_chose_will_your_vengeance = True
                call vs_will_your_vengeance
                jump vs_choices_1

            "(Speak) What then? Will the forest be at peace?" if not vs_chose_what_then and vs_chose_will_your_vengeance:
                $ vs_chose_what_then = True
                call vs_what_then
                jump vs_choices_1


    # Level 2 of choice tree
    label vs_choices_2_1:
        # Branching from ""
        menu:
            "":
                jump vs_choices_3_1
            "":
                jump vs_choices_3_2


            # Dialogue pool options

            "(Speak) Who are you?" if not vs_chose_who_are_you:
                $ vs_chose_who_are_you = True
                call vs_who_are_you
                jump vs_choices_2_1

            "(Speak) Why do you seek vengeance?" if not vs_chose_why_do_you_seek and vs_chose_who_are_you:
                $ vs_chose_why_do_you_seek = True
                call vs_why_do_you_seek
                jump vs_choices_2_1

            "(Speak) Can you ever be at peace?" if not vs_chose_can_you_ever and vs_chose_why_do_you_seek:
                $ vs_chose_can_you_ever = True
                call vs_can_you_ever
                jump vs_choices_2_1

            "(Speak) What do you want from us?" if not vs_chose_what_do_you:
                $ vs_chose_what_do_you = True
                call vs_what_do_you
                jump vs_choices_2_1

            "(Speak) Why do you blame us for the kingdom’s sins?" if not vs_chose_why_do_you_blame and vs_chose_why_do_you_blame:
                $ vs_chose_why_do_you_blame = True
                call vs_why_do_you_blame
                jump vs_choices_2_1

            "(Speak) Isn’t there a way to break this cycle of hatred?" if not vs_chose_isnt_there_a and vs_chose_isnt_there_a:
                $ vs_chose_isnt_there_a = True
                call vs_isnt_there_a
                jump vs_choices_2_1
            
            "(Speak) Why can’t you let go of your anger?" if not vs_chose_why_cant_you:
                $ vs_chose_why_cant_you = True
                call vs_why_cant_you
                jump vs_choices_2_1

            "(Speak) Do you not see the destruction your rage causes?" if not vs_chose_do_you_not and vs_chose_why_cant_you:
                $ vs_chose_do_you_not = True
                call vs_do_you_not
                jump vs_choices_2_1

            "(Speak) Can’t you find peace in the forest’s renewal?" if not vs_chose_cant_you_find and vs_chose_cant_you_find:
                $ vs_chose_cant_you_find = True
                call vs_cant_you_find
                jump vs_choices_2_1

            "(Speak) What will you do if you destroy us?" if not vs_chose_what_will_you:
                $ vs_chose_what_will_you = True
                call vs_what_will_you
                jump vs_choices_2_1

            "(Speak) Will your vengeance ever be enough?" if not vs_chose_will_your_vengeance and vs_chose_what_will_you:
                $ vs_chose_will_your_vengeance = True
                call vs_will_your_vengeance
                jump vs_choices_2_1

            "(Speak) What then? Will the forest be at peace?" if not vs_chose_what_then and vs_chose_will_your_vengeance:
                $ vs_chose_what_then = True
                call vs_what_then
                jump vs_choices_2_1

    label vs_choices_2_2:
        # Branching from ""
        menu:
            "":
                jump vs_choices_3_3
            "":
                jump vs_choices_3_4


            # Dialogue pool options

            "(Speak) Who are you?" if not vs_chose_who_are_you:
                $ vs_chose_who_are_you = True
                call vs_who_are_you
                jump vs_choices_2_2

            "(Speak) Why do you seek vengeance?" if not vs_chose_why_do_you_seek and vs_chose_who_are_you:
                $ vs_chose_why_do_you_seek = True
                call vs_why_do_you_seek
                jump vs_choices_2_2

            "(Speak) Can you ever be at peace?" if not vs_chose_can_you_ever and vs_chose_why_do_you_seek:
                $ vs_chose_can_you_ever = True
                call vs_can_you_ever
                jump vs_choices_2_2

            "(Speak) What do you want from us?" if not vs_chose_what_do_you:
                $ vs_chose_what_do_you = True
                call vs_what_do_you
                jump vs_choices_2_2

            "(Speak) Why do you blame us for the kingdom’s sins?" if not vs_chose_why_do_you_blame and vs_chose_why_do_you_blame:
                $ vs_chose_why_do_you_blame = True
                call vs_why_do_you_blame
                jump vs_choices_2_2

            "(Speak) Isn’t there a way to break this cycle of hatred?" if not vs_chose_isnt_there_a and vs_chose_isnt_there_a:
                $ vs_chose_isnt_there_a = True
                call vs_isnt_there_a
                jump vs_choices_2_2
            
            "(Speak) Why can’t you let go of your anger?" if not vs_chose_why_cant_you:
                $ vs_chose_why_cant_you = True
                call vs_why_cant_you
                jump vs_choices_2_2

            "(Speak) Do you not see the destruction your rage causes?" if not vs_chose_do_you_not and vs_chose_why_cant_you:
                $ vs_chose_do_you_not = True
                call vs_do_you_not
                jump vs_choices_2_2

            "(Speak) Can’t you find peace in the forest’s renewal?" if not vs_chose_cant_you_find and vs_chose_cant_you_find:
                $ vs_chose_cant_you_find = True
                call vs_cant_you_find
                jump vs_choices_2_2

            "(Speak) What will you do if you destroy us?" if not vs_chose_what_will_you:
                $ vs_chose_what_will_you = True
                call vs_what_will_you
                jump vs_choices_2_2

            "(Speak) Will your vengeance ever be enough?" if not vs_chose_will_your_vengeance and vs_chose_what_will_you:
                $ vs_chose_will_your_vengeance = True
                call vs_will_your_vengeance
                jump vs_choices_2_2

            "(Speak) What then? Will the forest be at peace?" if not vs_chose_what_then and vs_chose_will_your_vengeance:
                $ vs_chose_what_then = True
                call vs_what_then
                jump vs_choices_2_2


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
                jump sacrificed_princess
            "":
                jump saved_hero

    label vs_choices_5_2:
        # Branching from ""
        menu:
            "":
                jump inherited_throne
            "":
                jump happily_ever_after

    label vs_choices_5_3:
        # Branching from ""
        menu:
            "":
                jump saved_hero
            "":
                jump inherited_throne

    label vs_choices_5_4:
        # Branching from ""
        menu:
            "":
                jump love_beyond_death
            "":
                jump saved_hero

    label vs_choices_5_5:
        # Branching from ""
        menu:
            "":
                jump sacrificed_princess
            "":
                jump inherited_throne

    label vs_choices_5_6:
        # Branching from ""
        menu:
            "":
                jump inherited_throne
            "":
                jump saved_hero

    label vs_choices_5_7:
        # Branching from ""
        menu:
            "":
                jump corrupted_hero
            "":
                jump happily_ever_after

    label vs_choices_5_8:
        # Branching from ""
        menu:
            "":
                jump unfulfilled_love
            "":
                jump love_beyond_death

    label vs_choices_5_9:
        # Branching from ""
        menu:
            "":
                jump sacrificed_princess
            "":
                jump love_beyond_death

    label vs_choices_5_10:
        # Branching from ""
        menu:
            "":
                jump forest_protectors
            "":
                jump happily_ever_after

    label vs_choices_5_11:
        # Branching from ""
        menu:
            "":
                jump forest_protectors
            "":
                jump corrupted_hero

    label vs_choices_5_12:
        # Branching from ""
        menu:
            "":
                jump forest_protectors
            "":
                jump unfulfilled_love

    label vs_choices_5_13:
        # Branching from ""
        menu:
            "":
                jump corrupted_hero
            "":
                jump unfulfilled_love

    label vs_choices_5_14:
        # Branching from ""
        menu:
            "":
                jump corrupted_hero
            "":
                jump unfulfilled_love

    label vs_choices_5_15:
        # Branching from ""
        menu:
            "":
                jump sacrificed_princess
            "":
                jump love_beyond_death

    label vs_choices_5_16:
        # Branching from ""
        menu:
            "":
                jump forest_protectors
            "":
                jump happily_ever_after