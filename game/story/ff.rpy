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
            "(Act) Play her game":
                jump ff_choices_2_1

            "(Act) Engage her directly":
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
        # Branching from "(Act) Play her game"
        menu:
            "(Act) Flatter her and pretend to be impressed":
                jump ff_choices_3_1
            "(Act) Feign weakness and vulnerability":
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
        # Branching from "(Act) Engage her directly"
        menu:
            "(Act) Have the hero charge with his sword":
                jump ff_choices_3_3
            "(Act) Confront her about her deception":
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
        # Branching from "(Act) Flatter her and pretend to be impressed"
        menu:
            "(Act) Compliment her cunning":
                jump ff_choices_4_1
            "(Act) Question her motives subtly" if chose_magic:
                jump ff_choices_4_2

    label ff_choices_3_2:
        # Branching from "(Act) Feign weakness and vulnerability"
        menu:
            "(Act) Appear desperate for her help":
                jump ff_choices_4_3
            "(Act) Ask for guidance in using magic" if chose_magic:
                jump ff_choices_4_4

    label ff_choices_3_3:
        # Branching from "(Act) Have the hero charge with his sword"
        menu:
            "(Act) Aim for her weak spots" if not chose_magic:
                jump ff_choices_4_5
            "(Act) Distract her and strike when she lunges":
                jump ff_choices_4_6

    label ff_choices_3_4:
        # Branching from "(Act) Confront her about her deception"
        menu:
            "(Act) Accuse her of hiding something":
                jump ff_choices_4_7
            "(Act) Challenge her to prove her superiority":
                jump ff_choices_4_8

    
    # Level 4 of choice tree
    label ff_choices_4_1:
        # Branching from "(Act) Compliment her cunning"
        menu:
            "(Act) Offer to join forces with her" if chose_magic:
                jump ff_choices_5_1
            "(Act) Lure her into overconfidence and trap her":
                jump ff_choices_5_2

    label ff_choices_4_2:
        # Branching from "(Act) Question her motives subtly"
        menu:
            "(Act) Pretend to agree with her goals":
                jump ff_choices_5_3
            "(Act) Provoke her to reveal her true intentions":
                jump ff_choices_5_4

    label ff_choices_4_3:
        # Branching from "(Act) Appear desperate for her help"
        menu:
            "(Act) Beg her for protection":
                jump ff_choices_5_5
            "(Act) Pretend to surrender":
                jump ff_choices_5_6

    label ff_choices_4_4:
        # Branching from "(Act) Ask for guidance in using magic"
        menu:
            "(Act) Learn her techniques and betray her":
                jump ff_choices_5_7
            "(Act) Use her own spells against her":
                jump ff_choices_5_8

    label ff_choices_4_5:
        # Branching from "(Act) Aim for her weak spots"
        menu:
            "(Act) Strike at her unarmored side":
                jump ff_choices_5_9
            "(Act) Go for a quick, decisive blow":
                jump ff_choices_5_10

    label ff_choices_4_6:
        # Branching from "(Act) Distract her and strike when she lunges"
        menu:
            "(Act) Let her tire herself out before countering":
                jump ff_choices_5_11
            "(Act) Knock her off balance and disarm her" if not chose_magic:
                jump ff_choices_5_12

    label ff_choices_4_7:
        # Branching from "(Act) Accuse her of hiding something"
        menu:
            "(Act) Challenge her to reveal her secrets" if chose_magic:
                jump ff_choices_5_13
            "(Act) Force her to admit her weaknesses":
                jump ff_choices_5_14

    label ff_choices_4_8:
        # Branching from "(Act) Challenge her to prove her superiority"
        menu:
            "(Act) Goad her into a one-on-one duel":
                jump ff_choices_5_15
            "(Act) Pretend to be impressed, then strike when she’s distracted" if not chose_magic:
                jump ff_choices_5_16


    # Level 5 of choice tree
    label ff_choices_5_1:
        # Branching from "(Act) Offer to join forces with her"
        menu:
            "(Act) Betray her at the last moment":
                jump unfulfilled_love
            "(Act) Teleport away once she’s distracted":
                jump happily_ever_after

    label ff_choices_5_2:
        # Branching from "(Act) Lure her into overconfidence and trap her"
        menu:
            "(Act) Use a snare trap" if not chose_magic:
                jump sacrificed_hero
            "(Act) Trap her with her own poison":
                jump saved_hero

    label ff_choices_5_3:
        # Branching from "(Act) Pretend to agree with her goals"
        menu:
            "(Act) Reverse the magic she’s using":
                jump forest_protectors
            "(Act) Escape with a sudden teleport":
                jump happily_ever_after

    label ff_choices_5_4:
        # Branching from "(Act) Provoke her to reveal her true intentions"
        menu:
            "(Act) Turn her ambition against her":
                jump unfulfilled_love
            "(Act) Shoot a fireball while she's distracted":
                jump forest_curse

    label ff_choices_5_5:
        # Branching from "(Act) Beg her for protection"
        menu:
            "(Act) Pretend to serve her, then backstab her":
                jump sacrificed_princess
            "(Act) Strike her with a fireball while she's distracted":
                jump forest_curse

    label ff_choices_5_6:
        # Branching from "(Act) Pretend to surrender"
        menu:
            "(Act) Feign weakness and strike back" if not chose_magic:
                jump sacrificed_princess
            "(Act) Lure her into a vulnerable position":
                jump love_beyond_death

    label ff_choices_5_7:
        # Branching from "(Act) Learn her techniques and betray her"
        menu:
            "(Act) Use what you’ve learned to outmaneuver her":
                jump forest_protectors
            "(Act) Exploit her hubris and escape":
                jump unfulfilled_love

    label ff_choices_5_8:
        # Branching from "(Act) Use her own spells against her"
        menu:
            "(Act) Reflect her spell back at her":
                jump forest_curse
            "(Act) Shatter her control with a counterspell":
                jump happily_ever_after

    label ff_choices_5_9:
        # Branching from "(Act) Strike at her unarmored side"
        menu:
            "(Act) Exploit her pain to secure a win":
                jump sacrificed_princess
            "(Act) Hesitate, showing mercy":
                jump love_beyond_death

    label ff_choices_5_10:
        # Branching from "(Act) Go for a quick, decisive blow"
        menu:
            "(Act) Strike her down immediately":
                jump love_beyond_death
            "(Act) Overwhelm her and retreat":
                jump sacrificed_hero

    label ff_choices_5_11:
        # Branching from "(Act) Let her tire herself out before countering"
        menu:
            "(Act) Strike her with magic" if chose_magic:
                jump forest_protectors
            "(Act) Deflect her attack and disarm her" if not chose_magic:
                jump sacrificed_hero

    label ff_choices_5_12:
        # Branching from "(Act) Knock her off balance and disarm her"
        menu:
            "(Act) Strike while she’s vulnerable":
                jump saved_hero
            "(Act) Give her a chance to surrender":
                jump love_beyond_death

    label ff_choices_5_13:
        # Branching from "(Act) Challenge her to reveal her secrets"
        menu:
            "(Act) Shoot a fireball at her":
                jump forest_curse
            "(Act) Teleport away":
                jump happily_ever_after

    label ff_choices_5_14:
        # Branching from "(Act) Force her to admit her weaknesses"
        menu:
            "(Act) Manipulate her into a reckless move":
                jump unfulfilled_love
            "(Act) Use her moment of doubt to strike":
                jump saved_hero

    label ff_choices_5_15:
        # Branching from "(Act) Goad her into a one-on-one duel"
        menu:
            "(Act) Strike her with magic" if chose_magic:
                jump forest_protectors
            "(Act) Use her own poison against her" if not chose_magic:
                jump sacrificed_hero

    label ff_choices_5_16:
        # Branching from "(Act) Pretend to be impressed, then strike when she’s distracted"
        menu:
            "(Act) Use the hero’s sword to land a fatal blow":
                jump saved_hero
            "(Act) Escape while she’s distracted":
                jump sacrificed_princess