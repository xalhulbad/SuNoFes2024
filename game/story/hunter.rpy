# Contains the code associated with portion of the game related to the "hunter" second villain encounter.

# Default variables


# Flags for unlockable options
default hu_chose_who_are_you = False
default hu_chose_why_after_us = False
default hu_chose_kingdom_abolished_magic = False
default hu_chose_what_your_mission = False
default hu_chose_why_guard_forest = False
default hu_chose_how_become_hunter = False
default hu_chose_why_cant_let_us_pass = False
default hu_chose_have_you_always_been_alone = False
default hu_chose_how_long_been_here = False
default hu_chose_why_didnt_chase_us_before = False
default hu_chose_we_went_by_mistake = False

label hu_start:
    # Reset dialogue pool flags
    $ hu_chose_who_are_you = False
    $ hu_chose_why_after_us = False
    $ hu_chose_kingdom_abolished_magic = False
    $ hu_chose_what_your_mission = False
    $ hu_chose_why_guard_forest = False
    $ hu_chose_how_become_hunter = False
    $ hu_chose_why_cant_let_us_pass = False
    $ hu_chose_have_you_always_been_alone = False
    $ hu_chose_how_long_been_here = False
    $ hu_chose_why_didnt_chase_us_before = False
    $ hu_chose_we_went_by_mistake = False

    n "The forest's dense canopy loomed overhead as the princess and the hero cautiously moved forward, the familiar tension thickening the air. It felt as if the forest itself was holding its breath."
    n "The princess and hero could see the kingdom now, a sign that they were getting close."
    n "A twig snapped beneath the hero's foot, sending a flock of birds scattering into the sky. The sudden noise only served to heighten the tension between them."
    n "The hero tightened his grip on his sword, scanning the surroundings with a wary gaze. His instincts told him that danger was near, and he wasn't wrong."
    n "From the shadows, a figure emerged, cloaked in the dark hues of the forest."
    n "His presence was as ominous as ever, and the bow in his hand gleamed with a readiness that set both the princess and hero on edge."
    hu "You've ventured deep into the forest again. It seems you haven't learned your lesson."

    if hu_times_gotten == 1:
        pt "The Hunter again... I was hoping we wouldn't have to run into him a second time."
    
    elif hu_times_gotten == 2:
        pt "Another encounter with the hunter... Will things go differently this time?"

    else:
        pt "Let's just get this over with."

    n "The Hunter stepped closer, his movements deliberate and precise. The hero instinctively moved to place himself between the princess and The Hunter, ready to defend her with his life."
    h "Stay back, princess. We won't back down, but we don't want to fight."
    hu "How predictable. But the forest demands respect, and you are trespassing. Prepare yourselves—your choices have consequences."

    jump hu_choices_1

    # Level 1 of choice tree
    label hu_choices_1:
        # Initial branch
        menu:
            "(Act) Tell hero to brandish sword":
                jump hu_choices_2_1

            "(Act) Try to reason with The Hunter":
                jump hu_choices_2_2


            # Dialogue pool options

            "(Speak) Who are you?" if not hu_chose_who_are_you:
                $ hu_chose_who_are_you = True
                call hu_who_are_you
                jump hu_choices_1

            "(Speak) Why are you after us?" if not hu_chose_why_after_us and hu_chose_who_are_you:
                $ hu_chose_why_after_us = True
                call hu_why_after_us
                jump hu_choices_1

            "(Speak) The kingdom abolished its use of magic." if not hu_chose_kingdom_abolished_magic and hu_chose_why_after_us:
                $ hu_chose_kingdom_abolished_magic = True
                call hu_kingdom_abolished_magic
                jump hu_choices_1


            "(Speak) What is your mission?" if not hu_chose_what_your_mission:
                $ hu_chose_what_your_mission = True
                call hu_what_your_mission
                jump hu_choices_1

            "(Speak) Why do you guard this forest?" if not hu_chose_why_guard_forest and hu_chose_what_your_mission:
                $ hu_chose_why_guard_forest = True
                call hu_why_guard_forest
                jump hu_choices_1

            "(Speak) How did you become The Hunter?" if not hu_chose_how_become_hunter and hu_chose_why_guard_forest:
                $ hu_chose_how_become_hunter = True
                call hu_how_become_hunter
                jump hu_choices_1


            "(Speak) Why can't you just let us pass?" if not hu_chose_why_cant_let_us_pass:
                $ hu_chose_why_cant_let_us_pass = True
                call hu_why_cant_let_us_pass
                jump hu_choices_1

            "(Speak) Have you always been alone?" if not hu_chose_have_you_always_been_alone and hu_chose_why_cant_let_us_pass:
                $ hu_chose_have_you_always_been_alone = True
                call hu_have_you_always_been_alone
                jump hu_choices_1

            "(Speak) How long have you been here?" if not hu_chose_how_long_been_here and hu_chose_have_you_always_been_alone:
                $ hu_chose_how_long_been_here = True
                call hu_how_long_been_here
                jump hu_choices_1


            "(Speak) Why didn't you chase us before?" if not hu_chose_why_didnt_chase_us_before:
                $ hu_chose_why_didnt_chase_us_before = True
                call hu_why_didnt_chase_us_before
                jump hu_choices_1

            "(Speak) We went there by mistake. We meant no harm!" if not hu_chose_we_went_by_mistake and hu_chose_why_didnt_chase_us_before:
                $ hu_chose_we_went_by_mistake = True
                call hu_we_went_by_mistake
                jump hu_choices_1


    # Level 2 of choice tree
    label hu_choices_2_1:
        # Branching from "(Act) Tell hero to brandish sword"
        menu:
            "(Act) Charge at The Hunter":
                jump hu_choices_3_1

            "(Act) Wait for him to make a move":
                jump hu_choices_3_2

            
            # Dialogue pool options

            "(Speak) Who are you?" if not hu_chose_who_are_you:
                $ hu_chose_who_are_you = True
                call hu_who_are_you
                jump hu_choices_2_1

            "(Speak) Why are you after us?" if not hu_chose_why_after_us and hu_chose_who_are_you:
                $ hu_chose_why_after_us = True
                call hu_why_after_us
                jump hu_choices_2_1

            "(Speak) The kingdom abolished its use of magic." if not hu_chose_kingdom_abolished_magic and hu_chose_why_after_us:
                $ hu_chose_kingdom_abolished_magic = True
                call hu_kingdom_abolished_magic
                jump hu_choices_2_1


            "(Speak) What is your mission?" if not hu_chose_what_your_mission:
                $ hu_chose_what_your_mission = True
                call hu_what_your_mission
                jump hu_choices_2_1

            "(Speak) Why do you guard this forest?" if not hu_chose_why_guard_forest and hu_chose_what_your_mission:
                $ hu_chose_why_guard_forest = True
                call hu_why_guard_forest
                jump hu_choices_2_1

            "(Speak) How did you become The Hunter?" if not hu_chose_how_become_hunter and hu_chose_why_guard_forest:
                $ hu_chose_how_become_hunter = True
                call hu_how_become_hunter
                jump hu_choices_2_1


            "(Speak) Why can't you just let us pass?" if not hu_chose_why_cant_let_us_pass:
                $ hu_chose_why_cant_let_us_pass = True
                call hu_why_cant_let_us_pass
                jump hu_choices_2_1

            "(Speak) Have you always been alone?" if not hu_chose_have_you_always_been_alone and hu_chose_why_cant_let_us_pass:
                $ hu_chose_have_you_always_been_alone = True
                call hu_have_you_always_been_alone
                jump hu_choices_2_1

            "(Speak) How long have you been here?" if not hu_chose_how_long_been_here and hu_chose_have_you_always_been_alone:
                $ hu_chose_how_long_been_here = True
                call hu_how_long_been_here
                jump hu_choices_2_1


            "(Speak) Why didn't you chase us before?" if not hu_chose_why_didnt_chase_us_before:
                $ hu_chose_why_didnt_chase_us_before = True
                call hu_why_didnt_chase_us_before
                jump hu_choices_2_1

            "(Speak) We went there by mistake. We meant no harm!" if not hu_chose_we_went_by_mistake and hu_chose_why_didnt_chase_us_before:
                $ hu_chose_we_went_by_mistake = True
                call hu_we_went_by_mistake
                jump hu_choices_2_1

    label hu_choices_2_2:
        # Branching from "(Act) Try to reason with The Hunter"
        menu:
            "(Act) Appeal to The Hunter's morality":
                jump hu_choices_3_3

            "(Act) Offer a bargain":
                jump hu_choices_3_4

            # Dialogue pool options

            "(Speak) Who are you?" if not hu_chose_who_are_you:
                $ hu_chose_who_are_you = True
                call hu_who_are_you
                jump hu_choices_2_2

            "(Speak) Why are you after us?" if not hu_chose_why_after_us and hu_chose_who_are_you:
                $ hu_chose_why_after_us = True
                call hu_why_after_us
                jump hu_choices_2_2

            "(Speak) The kingdom abolished its use of magic." if not hu_chose_kingdom_abolished_magic and hu_chose_why_after_us:
                $ hu_chose_kingdom_abolished_magic = True
                call hu_kingdom_abolished_magic
                jump hu_choices_2_2


            "(Speak) What is your mission?" if not hu_chose_what_your_mission:
                $ hu_chose_what_your_mission = True
                call hu_what_your_mission
                jump hu_choices_2_2

            "(Speak) Why do you guard this forest?" if not hu_chose_why_guard_forest and hu_chose_what_your_mission:
                $ hu_chose_why_guard_forest = True
                call hu_why_guard_forest
                jump hu_choices_2_2

            "(Speak) How did you become The Hunter?" if not hu_chose_how_become_hunter and hu_chose_why_guard_forest:
                $ hu_chose_how_become_hunter = True
                call hu_how_become_hunter
                jump hu_choices_2_2


            "(Speak) Why can't you just let us pass?" if not hu_chose_why_cant_let_us_pass:
                $ hu_chose_why_cant_let_us_pass = True
                call hu_why_cant_let_us_pass
                jump hu_choices_2_2

            "(Speak) Have you always been alone?" if not hu_chose_have_you_always_been_alone and hu_chose_why_cant_let_us_pass:
                $ hu_chose_have_you_always_been_alone = True
                call hu_have_you_always_been_alone
                jump hu_choices_2_2

            "(Speak) How long have you been here?" if not hu_chose_how_long_been_here and hu_chose_have_you_always_been_alone:
                $ hu_chose_how_long_been_here = True
                call hu_how_long_been_here
                jump hu_choices_2_2


            "(Speak) Why didn't you chase us before?" if not hu_chose_why_didnt_chase_us_before:
                $ hu_chose_why_didnt_chase_us_before = True
                call hu_why_didnt_chase_us_before
                jump hu_choices_2_2

            "(Speak) We went there by mistake. We meant no harm!" if not hu_chose_we_went_by_mistake and hu_chose_why_didnt_chase_us_before:
                $ hu_chose_we_went_by_mistake = True
                call hu_we_went_by_mistake
                jump hu_choices_2_2


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


    # Dialogue pool options

    label hu_who_are_you:
        p "Who are you? Why do you stalk us like this?"
        n "The Hunter's eyes narrowed, his expression unreadable as he responded."
        hu "I am the guardian of this forest, the one who ensures that its secrets remain untouched. I was once part of your kingdom, but I saw the truth behind its falsehoods. Now, I serve only the forest."

        return
    
    label hu_why_after_us:
        p "Why are you after us? We've done nothing to harm you."
        n "The Hunter's voice was cold, filled with barely restrained anger."
        hu "You carry the stench of the kingdom, a place that has abused the gifts of magic for far too long."
        hu "Whether you wield it or not, your presence here is a threat. I will not allow you to defile this forest as your kind has done before."

        return

    label hu_kingdom_abolished_magic:
        p "The kingdom no longer uses magic! They abolished it long ago. Why can't you let go of the past?"
        n "The Hunter's eyes narrowed, his expression hardening as he responded."
        hu "Abolished? Do you think that changes what your kingdom has done? The scars left by your people's greed are etched into the very bones of this forest. Magic was twisted, corrupted by those who sought power above all else."
        n "The Hunter's voice grew colder, his anger palpable."
        hu "Words and decrees mean nothing to me. You cannot erase the past with a simple law. The kingdom's sins cannot be undone, and I will never forgive those who bear its mark."
        hu "I will not allow your kind to tread where they do not belong."

        return

    label hu_what_your_mission:
        p "What is your mission?"
        n "The Hunter's gaze hardened, his words laced with a sense of duty."
        hu "My mission is simple—to protect the forest from all who would exploit it. I hunt those who threaten its balance, those who think they can take from it without consequence. You are no different."

        return

    label hu_why_guard_forest:
        p "Why do you guard this forest so fiercely? What's so special about it?"
        n "The Hunter's voice took on a reverent tone as he spoke of the forest."
        hu "This forest is sacred, a place where magic thrives in its purest form." 
        hu "Unlike your kingdom, which sought to twist and corrupt it for power, I guard it to preserve its beauty and ensure that it remains untouched by human greed."

        return

    label hu_how_become_hunter:
        p "How did you become The Hunter? Why take on this role?"
        n "The Hunter's voice was filled with conviction, as if he had made this decision long ago."
        hu "I chose this path when I saw what the kingdom was doing—abusing the magic that should have been revered. I could no longer stand by and watch as they twisted nature's gifts for their own gain." 
        hu "So, I left, vowing to protect the forest from all who would harm it. The title of 'Hunter' was not given to me; I took it upon myself to ensure that no one else would repeat the kingdom's mistakes."

        return

    label hu_why_cant_let_us_pass:
        p "Why can't you just let us pass? We're not here to harm the forest."
        n "The Hunter's expression darkened, his grip tightening on his weapon."
        hu "Let you pass? So you can return to your kingdom and bring others here, to exploit what remains pure?"
        n "No. The forest has suffered enough at the hands of your kind. I will not allow you to defile it further. Your journey ends here."

        return

    label hu_have_you_always_been_alone:
        p "Have you always been alone out here?"
        n "The Hunter's expression briefly softened, a hint of something unspoken in his gaze."
        hu "Alone? Perhaps. But solitude is a small price to pay for the peace this forest offers."
        hu "I walked away from the kingdom long ago, abandoning the lies they told. Here, I found purpose, even if it meant leaving everything behind."

        return

    label hu_how_long_been_here:
        p "How long have you been in this forest?"
        n "The Hunter seemed to ponder the question for a moment before answering."
        hu "Time... it's lost its meaning here. I have been here long enough to see the forest grow and change, long enough to witness the kingdom's rise and fall. The forest has become my life, and I will remain here until my last breath."

        return

    label hu_why_didnt_chase_us_before:
        p "Why didn't you chase us before? You could have stopped us then."
        n "The Hunter's gaze darkened, his expression unreadable as he responded."
        hu "I thought you were different, that perhaps you were not like the others. I saw something in you—a potential to walk away, to leave this forest unscathed and in peace. So I let you go, hoping you would not return."
        n "The Hunter's voice grew colder, his anger barely restrained."
        hu "But you proved me wrong. You ventured to the sacred place—a place where no outsider should tread. By doing so, you've shown your true nature, that you cannot be trusted."
        hu "I will not make the same mistake twice. You've crossed a line, and I will not allow you to leave this forest alive."

        return

    label hu_we_went_by_mistake:
        p "We didn't mean to go there! It was a mistake. We meant no harm!"
        n "The Hunter's eyes narrowed, his expression unyielding as he responded."
        hu "A mistake? Perhaps. But intent matters little now. The fact remains that you've seen the sacred place. Its power is beyond your understanding, and even a fleeting glimpse could tempt you to exploit it."
        n "The Hunter's voice hardened, filled with a deep-seated resolve."
        hu "Whether you meant harm or not, you've been exposed to something that should remain untouched by human hands. I cannot risk letting you leave, knowing what you've seen."
        hu "The magic of the forest is not yours to wield, and I cannot afford to let you live with that knowledge. I must protect the forest, even if it means ending your lives."

        return