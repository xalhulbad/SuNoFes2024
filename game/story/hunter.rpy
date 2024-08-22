# Contains the code associated with portion of the game related to the "hunter" second villain encounter.

# Default variables


# Flags for unlockable options

label hu_start:
    n "The forest’s dense canopy loomed overhead as the princess and the hero cautiously moved forward, the familiar tension thickening the air. It felt as if the forest itself was holding its breath."
    n "The princess and hero could see the kingdom now, a sign that they were getting close."
    n "A twig snapped beneath the hero’s foot, sending a flock of birds scattering into the sky. The sudden noise only served to heighten the tension between them."
    n "The hero tightened his grip on his sword, scanning the surroundings with a wary gaze. His instincts told him that danger was near, and he wasn’t wrong."
    n "From the shadows, a figure emerged, cloaked in the dark hues of the forest."
    n "His presence was as ominous as ever, and the bow in his hand gleamed with a readiness that set both the princess and hero on edge."
    hu "You’ve ventured deep into the forest again. It seems you haven’t learned your lesson."

    if hu_times_gotten == 1:
        pt "The Hunter again… I was hoping we wouldn’t have to run into him a second time."
    
    elif hu_times_gotten == 2:
        pt "Another encounter with the hunter… Will things go differently this time?"

    else:
        pt "Let’s just get this over with."

    n "The Hunter stepped closer, his movements deliberate and precise. The hero instinctively moved to place himself between the princess and The Hunter, ready to defend her with his life."
    h "Stay back, princess. We won’t back down, but we don’t want to fight."
    hu "How predictable. But the forest demands respect, and you are trespassing. Prepare yourselves—your choices have consequences."


    # Level 1 of choice tree
    label hu_choices_1:
        # Initial branch
        menu:
            "(Act) Tell hero to brandish sword":
                jump hu_choices_2_1

            "(Act) Try to reason with The Hunter":
                jump hu_choices_2_2
        

    # Level 2 of choice tree
    label hu_choices_2_1:
        # Branching from "(Act) Tell hero to brandish sword"
        menu:
            "(Act) Charge at The Hunter":
                jump hu_choices_3_1

            "(Act) Wait for him to make a move":
                jump hu_choices_3_2

    label hu_choices_2_2:
        # Branching from "(Act) Try to reason with The Hunter"
        menu:
            "(Act) Appeal to The Hunter's morality":
                jump hu_choices_3_3

            "(Act) Offer a bargain":
                jump hu_choices_3_4


    # Level 3 of choice tree
    label hu_choices_3_1:
        # Branching from "(Act) Charge at The Hunter"
        menu:
            "(Act) Strike with precision":
                jump hu_choices_4_1

            "(Act) Use the environment":
                jump hu_choices_4_2

    label hu_choices_3_2:
        # Branching from "(Act) Wait for him to make a move"
        menu:
            "(Act) Shoot an arrow":
                jump hu_choices_4_3

            "(Act) Look for an escape route":
                jump hu_choices_4_4

    label hu_choices_3_3:
        # Branching from "(Act) Appeal to The Hunter's morality"
        menu:
            "(Act) Invoke his sense of duty":
                jump hu_choices_4_5

            "(Act) Challenge his honor":
                jump hu_choices_4_6

    label hu_choices_3_4:
        # Branching from "(Act) Offer a bargain"
        menu:
            "(Act) Offer yourself in exchange":
                jump hu_choices_4_7

            "(Act) Promise him freedom in the kingdom":
                jump hu_choices_4_8


    # Level 4 of choice tree
    label hu_choices_4_1:
        # Branching from "(Act) Strike with precision"
        menu:
            "(Act) Disarm The Hunter":
                jump hu_choices_5_1

            "(Act) Strike and retreat":
                jump hu_choices_5_2

    label hu_choices_4_2:
        # Branching from "(Act) Use the environment"
        menu:
            "(Act) Lure the Hunter into a trap":
                jump hu_choices_5_3

            "(Act) Create a distraction with magic" if chose_magic:
                jump hu_choices_5_4

    label hu_choices_4_3:
        # Branching from "(Act) Shoot an arrow"
        menu:
            "(Act) Nock another arrow":
                jump hu_choices_5_5

            "(Act) Switch to a different tactic":
                jump hu_choices_5_6

    label hu_choices_4_4:
        # Branching from "(Act) Look for an escape route"
        menu:
            "(Act) Escape using magic" if chose_magic:
                jump hu_choices_5_7

            "(Act) Distract him":
                jump hu_choices_5_8

    label hu_choices_4_5:
        # Branching from "(Act) Invoke his sense of duty"
        menu:
            "(Act) Remind him of his vows":
                jump hu_choices_5_9

            "(Act) Make him rethink his mission":
                jump hu_choices_5_10

    label hu_choices_4_6:
        # Branching from "(Act) Challenge his honor"
        menu:
            "(Act) Confront him about his methods" if not chose_magic:
                jump hu_choices_5_11

            "(Act) Accuse him of cowardice":
                jump hu_choices_5_12

    label hu_choices_4_7:
        # Branching from "(Act) Offer yourself in exchange"
        menu:
            "(Act) Sacrifice yourself" if not chose_magic:
                jump hu_choices_5_13

            "(Act) Feign submission and use magic" if chose_magic:
                jump hu_choices_5_14

    label hu_choices_4_8:
        # Branching from "(Act) Promise him freedom in the kingdom"
        menu:
            "(Act) Convince him to abandon his mission" if not chose_magic:
                jump hu_choices_5_15

            "(Act) Betray him":
                jump hu_choices_5_16


    # Level 5 of choice tree
    label hu_choices_5_1:
        # Branching from "(Act) Disarm The Hunter"
        menu:
            "(Act) Use the hero's sword":
                jump saved_hero

            "(Act) Fire a spell at the hunter" if chose_magic:
                jump corrupted_hero

    label hu_choices_5_2:
        # Branching from "(Act) Strike and retreat"
        menu:
            "(Act) Deal a decisive blow and escape":
                jump inherited_throne

            "(Act) Strike with magic and escape" if chose_magic:
                jump corrupted_hero

    label hu_choices_5_3:
        # Branching from "(Act) Lure the Hunter into a trap"
        menu:
            "(Act) Use a snare trap" if not chose_magic:
                jump sacrificed_hero

            "(Act) Trap him using magic" if chose_magic:
                jump happily_ever_after

    label hu_choices_5_4:
        # Branching from "(Act) Create a distraction with magic"
        menu:
            "(Act) Use a flashy spell to blind him":
                jump happily_ever_after

            "(Act) Start a fire to get his attention":
                jump forest_curse
    
    label hu_choices_5_5:
        # Branching from "(Act) Nock another arrow"
        menu:
            "(Act) Jump in front of the hero":
                jump sacrificed_princess

            "(Act) Light the area on fire with magic" if chose_magic:
                jump forest_curse

    label hu_choices_5_6:
        # Branching from "(Act) Switch to a different tactic"
        menu:
            "(Act) Charge at him with sword":
                jump inherited_throne

            "(Act) Try to use magic" if chose_magic:
                jump unfulfilled_love

    label hu_choices_5_7:
        # Branching from "(Act) Escape using magic"
        menu:
            "(Act) Teleport away using magic":
                jump happily_ever_after

            "(Act) Light the trees on fire":
                jump forest_curse

    label hu_choices_5_8:
        # Branching from "(Act) Distract him"
        menu:
            "(Act) Catch him off guard with magic" if chose_magic:
                jump unfulfilled_love

            "(Act) Escape while you can":
                jump inherited_throne

    label hu_choices_5_9:
        # Branching from "(Act) Remind him of his vows"
        menu:
            "(Act) Change his mind about magic" if chose_magic:
                jump unfulfilled_love

            "(Act) Create a path for his redemption" if not chose_magic:
                jump sacrificed_princess

    label hu_choices_5_10:
        # Branching from "(Act) Make him rethink his mission"
        menu:
            "(Act) Change his mind about magic" if chose_magic:
                jump unfulfilled_love

            "(Act) Persuade him to leave the forest" if not chose_magic:
                jump saved_hero

    label hu_choices_5_11:
        # Branching from "(Act) Confront him about his methods"
        menu:
            "(Act) Make him doubt his actions":
                jump saved_hero

            "(Act) Anger him":
                jump sacrificed_hero

    label hu_choices_5_12:
        # Branching from "(Act) Accuse him of cowardice"
        menu:
            "(Act) Force him into a corner":
                jump saved_hero

            "(Act) Use magic to overpower him" if chose_magic:
                jump corrupted_hero

    label hu_choices_5_13:
        # Branching from "(Act) Sacrifice yourself"
        menu:
            "(Act) Give in to the Hunter":
                jump sacrificed_princess

            "(Act) Feign surrender":
                jump inherited_throne
    
    label hu_choices_5_14:
        # Branching from "(Act) Feign submission and use magic"
        menu:
            "(Act) Teleport away":
                jump happily_ever_after

            "(Act) Shoot a fireball at him":
                jump forest_curse

    label hu_choices_5_15:
        # Branching from "(Act) Convince him to abandon his mission"
        menu:
            "(Act) Offer a path to freedom outside the forest":
                jump sacrificed_princess

            "(Act) Promise a new life, only to betray him":
                jump sacrificed_hero

    label hu_choices_5_16:
        # Branching from "(Act) Betray him"
        menu:
            "(Act) Strike while he has his guard down":
                jump sacrificed_hero

            "(Act) Turn the tables with a magic-assisted ruse" if chose_magic:
                jump corrupted_hero