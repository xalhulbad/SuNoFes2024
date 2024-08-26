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

    jump dml_choices_1

    # Level 1 of choice tree
    label dml_choices_1:
        # Initial branch
        menu:
            "(Act) Challenge his authority":
                jump dml_choices_2_1

            "(Act) Attempt to reason with him":
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
        # Branching from "(Act) Challenge his authority"
        menu:
            "(Act) Engage in direct combat":
                jump dml_choices_3_1
            "(Act) Use magic to weaken his power" if chose_magic:
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
        # Branching from "(Act) Attempt to reason with him"
        menu:
            "(Act) Appeal to his lost humanity":
                jump dml_choices_3_3
            "(Act) Bargain for information":
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
        # Branching from "(Act) Engage in direct combat"
        menu:
            "(Act) Strike with the hero’s sword" if not chose_magic:
                jump dml_choices_4_1
            "(Act) Create an opening with a magic blast" if chose_magic:
                jump dml_choices_4_2

    label dml_choices_3_2:
        # Branching from "(Act) Use magic to weaken his power"
        menu:
            "(Act) Seal his dark magic with a counterspell":
                jump dml_choices_4_3
            "(Act) Overwhelm him with a burst of light":
                jump dml_choices_4_4

    label dml_choices_3_3:
        # Branching from "(Act) Appeal to his lost humanity"
        menu:
            "(Act) Remind him of his past":
                jump dml_choices_4_5
            "(Act) Challenge him to confront his own corruption":
                jump dml_choices_4_6

    label dml_choices_3_4:
        # Branching from "(Act) Bargain for information"
        menu:
            "(Act) Offer him something of value" if chose_magic:
                jump dml_choices_4_7
            "(Act) Feign submission and plan a counterattack":
                jump dml_choices_4_8

    
    # Level 4 of choice tree
    label dml_choices_4_1:
        # Branching from "(Act) Strike with the hero’s sword"
        menu:
            "(Act) Go for a decisive blow":
                jump dml_choices_5_1
            "(Act) Use the environment to gain an advantage":
                jump dml_choices_5_2

    label dml_choices_4_2:
        # Branching from "(Act) Create an opening with a magic blast"
        menu:
            "(Act) Follow up with a powerful strike":
                jump dml_choices_5_3
            "(Act) Distract him and go invisible":
                jump dml_choices_5_4

    label dml_choices_4_3:
        # Branching from "(Act) Seal his dark magic with a counterspell"
        menu:
            "(Act) Contain him in a magic circle":
                jump dml_choices_5_5
            "(Act) Counter his curse":
                jump dml_choices_5_6

    label dml_choices_4_4:
        # Branching from "(Act) Overwhelm him with a burst of light"
        menu:
            "(Act) Channel all your magic into a final spell":
                jump dml_choices_5_7
            "(Act) Bind his power and offer a truce":
                jump dml_choices_5_8

    label dml_choices_4_5:
        # Branching from "(Act) Remind him of his past"
        menu:
            "(Act) Appeal to his sense of honor":
                jump dml_choices_5_9
            "(Act) Remind him of the loved ones he lost":
                jump dml_choices_5_10

    label dml_choices_4_6:
        # Branching from "(Act) Challenge him to confront his own corruption"
        menu:
            "(Act) Make him see the consequences of his actions" if chose_magic:
                jump dml_choices_5_11
            "(Act) Push him to redeem himself" if not chose_magic:
                jump dml_choices_5_12

    label dml_choices_4_7:
        # Branching from "(Act) Offer him something of value"
        menu:
            "(Act) Offer to share forbidden knowledge":
                jump dml_choices_5_13
            "(Act) Offer to combine your powers":
                jump dml_choices_5_14

    label dml_choices_4_8:
        # Branching from "(Act) Feign submission and plan a counterattack"
        menu:
            "(Act) Wait for the perfect moment to strike" if not chose_magic:
                jump dml_choices_5_15
            "(Act) Manipulate him into lowering his guard":
                jump dml_choices_5_16


    # Level 5 of choice tree
    label dml_choices_5_1:
        # Branching from "(Act) Go for a decisive blow"
        menu:
            "(Act) Strike at his heart":
                jump sacrificed_princess
            "(Act) Overpower him with raw strength":
                jump inherited_throne

    label dml_choices_5_2:
        # Branching from "(Act) Use the environment to gain an advantage"
        menu:
            "(Act) Lure him into a trap":
                jump inherited_throne
            "(Act) Have the hero distract him":
                jump sacrificed_princess

    label dml_choices_5_3:
        # Branching from "(Act) Follow up with a powerful strike"
        menu:
            "(Act) Channel dark energy for a finishing blow":
                jump corrupted_hero
            "(Act) Use his own magic against him":
                jump love_beyond_death

    label dml_choices_5_4:
        # Branching from "(Act) Distract him and go invisible"
        menu:
            "(Act) Strike from the shadows":
                jump forest_curse
            "(Act) Bind his magic permanently":
                jump forest_protectors

    label dml_choices_5_5:
        # Branching from "(Act) Contain him in a magic circle"
        menu:
            "(Act) Trap him within the circle forever":
                jump forest_curse
            "(Act) Purify the dark magic within him":
                jump forest_protectors

    label dml_choices_5_6:
        # Branching from "(Act) Counter his curse"
        menu:
            "(Act) Seal the curse within yourself":
                jump corrupted_hero
            "(Act) Redirect the curse into the environment":
                jump forest_curse

    label dml_choices_5_7:
        # Branching from "(Act) Channel all your magic into a final spell"
        menu:
            "(Act) Release all your power at once":
                jump unfulfilled_love
            "(Act) Sacrifice your life to end the darkness":
                jump sacrificed_princess

    label dml_choices_5_8:
        # Branching from "(Act) Bind his power and offer a truce"
        menu:
            "(Act) Accept a temporary alliance":
                jump unfulfilled_love
            "(Act) Force him into a magical vow":
                jump forest_protectors

    label dml_choices_5_9:
        # Branching from "(Act) Appeal to his sense of honor"
        menu:
            "(Act) Challenge him to a duel of skill":
                jump sacrificed_hero
            "(Act) Offer him a path to redemption":
                jump inherited_throne

    label dml_choices_5_10:
        # Branching from "(Act) Remind him of the loved ones he lost"
        menu:
            "(Act) Make him relive his past mistakes":
                jump sacrificed_hero
            "(Act) Offer him peace and forgiveness":
                jump love_beyond_death

    label dml_choices_5_11:
        # Branching from "(Act) Make him see the consequences of his actions"
        menu:
            "(Act) Show him the destruction he caused":
                jump love_beyond_death
            "(Act) Persuade him to change his ways":
                jump forest_protectors

    label dml_choices_5_12:
        # Branching from "(Act) Push him to redeem himself"
        menu:
            "(Act) Offer him a chance to make amends":
                jump inherited_throne
            "(Act) Convince him to give up on his ideology":
                jump sacrificed_hero

    label dml_choices_5_13:
        # Branching from "(Act) Offer to share forbidden knowledge"
        menu:
            "(Act) Unlock hidden power together":
                jump corrupted_hero
            "(Act) Betray him at the last moment":
                jump unfulfilled_love

    label dml_choices_5_14:
        # Branching from "(Act) Offer to combine your powers"
        menu:
            "(Act) Fuse your magic with his":
                jump corrupted_hero
            "(Act) Create a powerful but unstable bond":
                jump forest_curse

    label dml_choices_5_15:
        # Branching from "(Act) Wait for the perfect moment to strike"
        menu:
            "(Act) Ambush him when he’s vulnerable ":
                jump sacrificed_hero
            "(Act) Strike him down with no hesitation":
                jump sacrificed_princess

    label dml_choices_5_16:
        # Branching from "(Act) Manipulate him into lowering his guard"
        menu:
            "(Act) Turn his own power against him" if chose_magic:
                jump unfulfilled_love
            "(Act) Catch him off guard with an attack" if not chose_magic:
                jump love_beyond_death


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