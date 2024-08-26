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
    # Reset dialogue pool flags
    $ ff_chose_who_are_you = False
    $ ff_chose_why_doing_this = False
    $ ff_chose_what_you_gain = False
    $ ff_chose_why_enjoy_manipulating = False
    $ ff_chose_isnt_there_more = False
    $ ff_chose_do_you_not = False
    $ ff_chose_how_did_you = False
    $ ff_chose_was_there_ever = False
    $ ff_chose_do_you_think = False
    $ ff_chose_what_do_you = False
    $ ff_chose_is_this_just = False
    $ ff_chose_when_will_it = False

    # Level 1 of choice tree
    label ff_choices_1:
        # Initial branch
        menu:
            "":
                jump ff_choices_2_1

            "":
                jump ff_choices_2_2


            # Dialogue pool options

            "(Speak) Who are you?" if not ff_chose_who_are_you:
                $ ff_chose_who_are_you = True
                call ff_who_are_you
                jump ff_choices_1

            "(Speak) Why are you doing this?" if not ff_chose_why_doing_this and ff_chose_who_are_you:
                $ ff_chose_why_doing_this = True
                call ff_why_doing_this
                jump ff_choices_1

            "(Speak) What do you gain from tormenting others?" if not ff_chose_what_you_gain and ff_chose_why_doing_this:
                $ ff_chose_what_you_gain = True
                call ff_what_you_gain
                jump ff_choices_1

            "(Speak) Why do you enjoy manipulating people?" if not ff_chose_why_enjoy_manipulating:
                $ ff_chose_why_enjoy_manipulating = True
                call ff_why_enjoy_manipulating
                jump ff_choices_1

            "(Speak) Isn’t there more to life than games and deceit?" if not ff_chose_isnt_there_more and ff_chose_why_enjoy_manipulating:
                $ ff_chose_isnt_there_more = True
                call ff_isnt_there_more
                jump ff_choices_1

            "(Speak) Do you not care about the harm you cause?" if not ff_chose_do_you_not and ff_chose_isnt_there_more:
                $ ff_chose_do_you_not = True
                call ff_do_you_not
                jump ff_choices_1
            
            "(Speak) How did you become like this?" if not ff_chose_how_did_you:
                $ ff_chose_how_did_you = True
                call ff_how_did_you
                jump ff_choices_1

            "(Speak) Was there ever a time when you cared about anyone?" if not ff_chose_was_there_ever and ff_chose_how_did_you:
                $ ff_chose_was_there_ever = True
                call ff_was_there_ever
                jump ff_choices_1

            "(Speak) Do you think you can ever change?" if not ff_chose_do_you_think and ff_chose_was_there_ever:
                $ ff_chose_do_you_think = True
                call ff_do_you_think
                jump ff_choices_1

            "(Speak) What do you really want from us?" if not ff_chose_what_do_you:
                $ ff_chose_what_do_you = True
                call ff_what_do_you
                jump ff_choices_1

            "(Speak) Is this just a game to you?" if not ff_chose_is_this_just and ff_chose_what_do_you:
                $ ff_chose_is_this_just = True
                call ff_is_this_just
                jump ff_choices_1

            "(Speak) When will it end?" if not ff_chose_when_will_it and ff_chose_is_this_just:
                $ ff_chose_when_will_it = True
                call ff_when_will_it
                jump ff_choices_1


    # Level 2 of choice tree
    label ff_choices_2_1:
        # Branching from ""
        menu:
            "":
                jump ff_choices_3_1
            "":
                jump ff_choices_3_2

            
            # Dialogue pool options

            "(Speak) Who are you?" if not ff_chose_who_are_you:
                $ ff_chose_who_are_you = True
                call ff_who_are_you
                jump ff_choices_2_1

            "(Speak) Why are you doing this?" if not ff_chose_why_doing_this and ff_chose_who_are_you:
                $ ff_chose_why_doing_this = True
                call ff_why_doing_this
                jump ff_choices_2_1

            "(Speak) What do you gain from tormenting others?" if not ff_chose_what_you_gain and ff_chose_why_doing_this:
                $ ff_chose_what_you_gain = True
                call ff_what_you_gain
                jump ff_choices_2_1

            "(Speak) Why do you enjoy manipulating people?" if not ff_chose_why_enjoy_manipulating:
                $ ff_chose_why_enjoy_manipulating = True
                call ff_why_enjoy_manipulating
                jump ff_choices_2_1

            "(Speak) Isn’t there more to life than games and deceit?" if not ff_chose_isnt_there_more and ff_chose_why_enjoy_manipulating:
                $ ff_chose_isnt_there_more = True
                call ff_isnt_there_more
                jump ff_choices_2_1

            "(Speak) Do you not care about the harm you cause?" if not ff_chose_do_you_not and ff_chose_isnt_there_more:
                $ ff_chose_do_you_not = True
                call ff_do_you_not
                jump ff_choices_2_1
            
            "(Speak) How did you become like this?" if not ff_chose_how_did_you:
                $ ff_chose_how_did_you = True
                call ff_how_did_you
                jump ff_choices_2_1

            "(Speak) Was there ever a time when you cared about anyone?" if not ff_chose_was_there_ever and ff_chose_how_did_you:
                $ ff_chose_was_there_ever = True
                call ff_was_there_ever
                jump ff_choices_2_1

            "(Speak) Do you think you can ever change?" if not ff_chose_do_you_think and ff_chose_was_there_ever:
                $ ff_chose_do_you_think = True
                call ff_do_you_think
                jump ff_choices_2_1

            "(Speak) What do you really want from us?" if not ff_chose_what_do_you:
                $ ff_chose_what_do_you = True
                call ff_what_do_you
                jump ff_choices_2_1

            "(Speak) Is this just a game to you?" if not ff_chose_is_this_just and ff_chose_what_do_you:
                $ ff_chose_is_this_just = True
                call ff_is_this_just
                jump ff_choices_2_1

            "(Speak) When will it end?" if not ff_chose_when_will_it and ff_chose_is_this_just:
                $ ff_chose_when_will_it = True
                call ff_when_will_it
                jump ff_choices_2_1

    label ff_choices_2_2:
        # Branching from ""
        menu:
            "":
                jump ff_choices_3_3
            "":
                jump ff_choices_3_4


            # Dialogue pool options

            "(Speak) Who are you?" if not ff_chose_who_are_you:
                $ ff_chose_who_are_you = True
                call ff_who_are_you
                jump ff_choices_2_2

            "(Speak) Why are you doing this?" if not ff_chose_why_doing_this and ff_chose_who_are_you:
                $ ff_chose_why_doing_this = True
                call ff_why_doing_this
                jump ff_choices_2_2

            "(Speak) What do you gain from tormenting others?" if not ff_chose_what_you_gain and ff_chose_why_doing_this:
                $ ff_chose_what_you_gain = True
                call ff_what_you_gain
                jump ff_choices_2_2

            "(Speak) Why do you enjoy manipulating people?" if not ff_chose_why_enjoy_manipulating:
                $ ff_chose_why_enjoy_manipulating = True
                call ff_why_enjoy_manipulating
                jump ff_choices_2_2

            "(Speak) Isn’t there more to life than games and deceit?" if not ff_chose_isnt_there_more and ff_chose_why_enjoy_manipulating:
                $ ff_chose_isnt_there_more = True
                call ff_isnt_there_more
                jump ff_choices_2_2

            "(Speak) Do you not care about the harm you cause?" if not ff_chose_do_you_not and ff_chose_isnt_there_more:
                $ ff_chose_do_you_not = True
                call ff_do_you_not
                jump ff_choices_2_2
            
            "(Speak) How did you become like this?" if not ff_chose_how_did_you:
                $ ff_chose_how_did_you = True
                call ff_how_did_you
                jump ff_choices_2_2

            "(Speak) Was there ever a time when you cared about anyone?" if not ff_chose_was_there_ever and ff_chose_how_did_you:
                $ ff_chose_was_there_ever = True
                call ff_was_there_ever
                jump ff_choices_2_2

            "(Speak) Do you think you can ever change?" if not ff_chose_do_you_think and ff_chose_was_there_ever:
                $ ff_chose_do_you_think = True
                call ff_do_you_think
                jump ff_choices_2_2

            "(Speak) What do you really want from us?" if not ff_chose_what_do_you:
                $ ff_chose_what_do_you = True
                call ff_what_do_you
                jump ff_choices_2_2

            "(Speak) Is this just a game to you?" if not ff_chose_is_this_just and ff_chose_what_do_you:
                $ ff_chose_is_this_just = True
                call ff_is_this_just
                jump ff_choices_2_2

            "(Speak) When will it end?" if not ff_chose_when_will_it and ff_chose_is_this_just:
                $ ff_chose_when_will_it = True
                call ff_when_will_it
                jump ff_choices_2_2


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