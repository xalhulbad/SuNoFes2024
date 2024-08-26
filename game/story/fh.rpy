# Contains the code associated with portion of the game related to the "fallen hero" second villain encounter.

# Default variables


# Flags for unlockable options
default fh_chose_who_are_you = False
default fh_chose_why_hold_grudge = False
default fh_chose_things_have_changed = False
default fh_chose_what_happened = False
default fh_chose_why_kingdom_turn = False
default fh_chose_really_believe_revenge = False
default fh_chose_why_hunt_us = False
default fh_chose_killing_us_satisfy = False
default fh_chose_what_would_you_do = False
default fh_chose_why_cant_pass = False
default fh_chose_change_your_mind = False
default fh_chose_not_like_those = False

label fh_start:
    # Reset dialogue pool flags
    $ fh_chose_who_are_you = False
    $ fh_chose_why_hold_grudge = False
    $ fh_chose_things_have_changed = False
    $ fh_chose_what_happened = False
    $ fh_chose_why_kingdom_turn = False
    $ fh_chose_really_believe_revenge = False
    $ fh_chose_why_hunt_us = False
    $ fh_chose_killing_us_satisfy = False
    $ fh_chose_what_would_you_do = False
    $ fh_chose_why_cant_pass = False
    $ fh_chose_change_your_mind = False
    $ fh_chose_not_like_those = False

    # Leading text
    n "The forest seemed darker than before, the shadows deeper and more menacing as the princess and hero retraced their steps."
    n "Each rustling leaf and distant creak of branches felt like the forest itself was holding its breath. The princess and hero could see the kingdom now, a sign that they were getting close."
    n "The hero's grip tightened on his sword as they ventured further, his eyes scanning every shadow for signs of movement."
    n "He could feel it-the tension in the air that signaled they were not alone. The princess's thoughts raced as they drew closer and closer to their destination."
    n "As they pressed forward, a familiar figure stepped out from the shadows. The Fallen Hero's presence was as foreboding as ever, his scarred face a mask of bitterness and fury."
    n "His sword remained sheathed, but the tension in his stance made it clear that any peace was fragile and fleeting."

    if fh_times_gotten == 1:
        pt "It's him… the warrior who lost everything. Can we find a way through this without bloodshed?"

    elif fh_times_gotten == 2:
        pt "We meet again. Maybe this time, I can reach him-if there's still a part of him left that wants peace."

    else:
        pt "No more running. Let's put an end to this cycle, one way or another."
    
    fh "So, we meet again. I've decided that you must pay for the kingdom's past sins. Did you think the forest would forget? Or perhaps you thought you could change what's already been broken?"
    n "The hero instinctively moved to shield the princess, his stance guarded but ready for battle."
    n "He knew that any misstep could lead to bloodshed, and the Fallen Hero's rage had only grown since their last encounter."
    h "We don't want to fight, but we'll defend ourselves if we have to. There's still a chance to end this without more pain."
    fh "Pain? You speak of pain as if you understand it. But you're nothing more than pawns of the kingdom that turned its back on me."
    fh "No matter what words you offer, they're all tainted by lies."
    n "The Fallen Hero's hand drifted to the hilt of his blade, his eyes locked onto the princess with a gaze that was both accusatory and conflicted."
    n "The air crackled with unspoken threats as the forest seemed to darken around them."
    fh "Enough of this. Your fate was sealed the moment you chose to serve a kingdom built on betrayal."
    fh "Now, let's see if you can back up your convictions with steel."

    jump fh_choices_1

    # Level 1 of choice tree
    label fh_choices_1:
        # Initial branch
        menu:
            "(Act) Prepare for combat":
                jump fh_choices_2_1

            "(Act) Try to reason with him":
                jump fh_choices_2_2


            # Dialogue pool options

            "(Speak) Who are you?" if not fh_chose_who_are_you:
                $ fh_chose_who_are_you = True
                call fh_who_are_you
                jump fh_choices_1

            "(Speak) Why do you hold a grudge against the kingdom?" if not fh_chose_why_hold_grudge and fh_chose_who_are_you:
                $ fh_chose_why_hold_grudge = True
                call fh_why_hold_grudge
                jump fh_choices_1

            "(Speak) The kingdom betrayed you, but things have changed." if not fh_chose_things_have_changed and fh_chose_why_hold_grudge:
                $ fh_chose_things_have_changed = True
                call fh_things_have_changed
                jump fh_choices_1

            "(Speak) What happened to you?" if not fh_chose_what_happened:
                $ fh_chose_what_happened = True
                call fh_what_happened
                jump fh_choices_1

            "(Speak) Why did the kingdom turn against you?" if not fh_chose_why_kingdom_turn and fh_chose_what_happened:
                $ fh_chose_why_kingdom_turn = True
                call fh_why_kingdom_turn
                jump fh_choices_1

            "(Speak) Do you really believe revenge will change anything?" if not fh_chose_really_believe_revenge and fh_chose_why_kingdom_turn:
                $ fh_chose_really_believe_revenge = True
                call fh_really_believe_revenge
                jump fh_choices_1

            "(Speak) Why do you hunt us?" if not fh_chose_why_hunt_us:
                $ fh_chose_why_hunt_us = True
                call fh_why_hunt_us
                jump fh_choices_1

            "(Speak) Do you think killing us will satisfy your revenge?" if not fh_chose_killing_us_satisfy and fh_chose_why_hunt_us:
                $ fh_chose_killing_us_satisfy = True
                call fh_killing_us_satisfy
                jump fh_choices_1

            "(Speak) What would you do if you got your revenge?" if not fh_chose_what_would_you_do and fh_chose_killing_us_satisfy:
                $ fh_chose_what_would_you_do = True
                call fh_what_would_you_do
                jump fh_choices_1

            "(Speak) Why can’t you just let us pass?" if not fh_chose_why_cant_pass:
                $ fh_chose_why_cant_pass = True
                call fh_why_cant_pass
                jump fh_choices_1

            "(Speak) Is there anything that could change your mind?" if not fh_chose_change_your_mind and fh_chose_why_cant_pass:
                $ fh_chose_change_your_mind = True
                call fh_change_your_mind
                jump fh_choices_1

            "(Speak) We’re not like those who wronged you." if not fh_chose_not_like_those and fh_chose_change_your_mind:
                $ fh_chose_not_like_those = True
                call fh_not_like_those
                jump fh_choices_1


    # Level 2 of choice tree
    label fh_choices_2_1:
        # Branching from "(Act) Prepare for combat"
        menu:
            "(Act) Attack first":
                jump fh_choices_3_1
            "(Act) Defend and counter":
                jump fh_choices_3_2


            # Dialogue pool options

            "(Speak) Who are you?" if not fh_chose_who_are_you:
                $ fh_chose_who_are_you = True
                call fh_who_are_you
                jump fh_choices_2_1

            "(Speak) Why do you hold a grudge against the kingdom?" if not fh_chose_why_hold_grudge and fh_chose_who_are_you:
                $ fh_chose_why_hold_grudge = True
                call fh_why_hold_grudge
                jump fh_choices_2_1

            "(Speak) The kingdom betrayed you, but things have changed." if not fh_chose_things_have_changed and fh_chose_why_hold_grudge:
                $ fh_chose_things_have_changed = True
                call fh_things_have_changed
                jump fh_choices_2_1

            "(Speak) What happened to you?" if not fh_chose_what_happened:
                $ fh_chose_what_happened = True
                call fh_what_happened
                jump fh_choices_2_1

            "(Speak) Why did the kingdom turn against you?" if not fh_chose_why_kingdom_turn and fh_chose_what_happened:
                $ fh_chose_why_kingdom_turn = True
                call fh_why_kingdom_turn
                jump fh_choices_2_1

            "(Speak) Do you really believe revenge will change anything?" if not fh_chose_really_believe_revenge and fh_chose_why_kingdom_turn:
                $ fh_chose_really_believe_revenge = True
                call fh_really_believe_revenge
                jump fh_choices_2_1

            "(Speak) Why do you hunt us?" if not fh_chose_why_hunt_us:
                $ fh_chose_why_hunt_us = True
                call fh_why_hunt_us
                jump fh_choices_2_1

            "(Speak) Do you think killing us will satisfy your revenge?" if not fh_chose_killing_us_satisfy and fh_chose_why_hunt_us:
                $ fh_chose_killing_us_satisfy = True
                call fh_killing_us_satisfy
                jump fh_choices_2_1

            "(Speak) What would you do if you got your revenge?" if not fh_chose_what_would_you_do and fh_chose_killing_us_satisfy:
                $ fh_chose_what_would_you_do = True
                call fh_what_would_you_do
                jump fh_choices_2_1

            "(Speak) Why can’t you just let us pass?" if not fh_chose_why_cant_pass:
                $ fh_chose_why_cant_pass = True
                call fh_why_cant_pass
                jump fh_choices_2_1

            "(Speak) Is there anything that could change your mind?" if not fh_chose_change_your_mind and fh_chose_why_cant_pass:
                $ fh_chose_change_your_mind = True
                call fh_change_your_mind
                jump fh_choices_2_1

            "(Speak) We’re not like those who wronged you." if not fh_chose_not_like_those and fh_chose_change_your_mind:
                $ fh_chose_not_like_those = True
                call fh_not_like_those
                jump fh_choices_2_1

    label fh_choices_2_2:
        # Branching from "(Act) Try to reason with him"
        menu:
            "(Act) Appeal to his sense of justice":
                jump fh_choices_3_3
            "(Act) Offer a peaceful solution":
                jump fh_choices_3_4


            # Dialogue pool options

            "(Speak) Who are you?" if not fh_chose_who_are_you:
                $ fh_chose_who_are_you = True
                call fh_who_are_you
                jump fh_choices_2_2

            "(Speak) Why do you hold a grudge against the kingdom?" if not fh_chose_why_hold_grudge and fh_chose_who_are_you:
                $ fh_chose_why_hold_grudge = True
                call fh_why_hold_grudge
                jump fh_choices_2_2

            "(Speak) The kingdom betrayed you, but things have changed." if not fh_chose_things_have_changed and fh_chose_why_hold_grudge:
                $ fh_chose_things_have_changed = True
                call fh_things_have_changed
                jump fh_choices_2_2

            "(Speak) What happened to you?" if not fh_chose_what_happened:
                $ fh_chose_what_happened = True
                call fh_what_happened
                jump fh_choices_2_2

            "(Speak) Why did the kingdom turn against you?" if not fh_chose_why_kingdom_turn and fh_chose_what_happened:
                $ fh_chose_why_kingdom_turn = True
                call fh_why_kingdom_turn
                jump fh_choices_2_2

            "(Speak) Do you really believe revenge will change anything?" if not fh_chose_really_believe_revenge and fh_chose_why_kingdom_turn:
                $ fh_chose_really_believe_revenge = True
                call fh_really_believe_revenge
                jump fh_choices_2_2

            "(Speak) Why do you hunt us?" if not fh_chose_why_hunt_us:
                $ fh_chose_why_hunt_us = True
                call fh_why_hunt_us
                jump fh_choices_2_2

            "(Speak) Do you think killing us will satisfy your revenge?" if not fh_chose_killing_us_satisfy and fh_chose_why_hunt_us:
                $ fh_chose_killing_us_satisfy = True
                call fh_killing_us_satisfy
                jump fh_choices_2_2

            "(Speak) What would you do if you got your revenge?" if not fh_chose_what_would_you_do and fh_chose_killing_us_satisfy:
                $ fh_chose_what_would_you_do = True
                call fh_what_would_you_do
                jump fh_choices_2_2

            "(Speak) Why can’t you just let us pass?" if not fh_chose_why_cant_pass:
                $ fh_chose_why_cant_pass = True
                call fh_why_cant_pass
                jump fh_choices_2_2

            "(Speak) Is there anything that could change your mind?" if not fh_chose_change_your_mind and fh_chose_why_cant_pass:
                $ fh_chose_change_your_mind = True
                call fh_change_your_mind
                jump fh_choices_2_2

            "(Speak) We’re not like those who wronged you." if not fh_chose_not_like_those and fh_chose_change_your_mind:
                $ fh_chose_not_like_those = True
                call fh_not_like_those
                jump fh_choices_2_2


    # Level 3 of choice tree
    label fh_choices_3_1:
        # Branching from "(Act) Attack first"
        menu:
            "(Act) Aim for his weak spot":
                jump fh_choices_4_1
            "(Act) Charge with full force":
                jump fh_choices_4_2

    label fh_choices_3_2:
        # Branching from "(Act) Defend and counter"
        menu:
            "(Act) Use the hero's shield to block and counter":
                jump fh_choices_4_3
            "(Act) Lure him into a position where he is vulnerable":
                jump fh_choices_4_4

    label fh_choices_3_3:
        # Branching from "(Act) Appeal to his sense of justice"
        menu:
            "(Act) Remind him of his past as a protector":
                jump fh_choices_4_5
            "(Act) Convince him that the kingdom has changed":
                jump fh_choices_4_6

    label fh_choices_3_4:
        # Branching from "(Act) Offer a peaceful solution"
        menu:
            "(Act) Swear on your honor to clear his name" if not chose_magic:
                jump fh_choices_4_7
            "(Act) Offer to stay in the forest with him" if chose_magic:
                jump fh_choices_4_8

    
    # Level 4 of choice tree
    label fh_choices_4_1:
        # Branching from "(Act) Aim for his weak spot"
        menu:
            "(Act) Strike at his old injury" if not chose_magic:
                jump fh_choices_5_1
            "(Act) Use magic to enhance the attack" if chose_magic:
                jump fh_choices_5_2

    label fh_choices_4_2:
        # Branching from "(Act) Charge with full force"
        menu:
            "(Act) Overwhelm him with sheer strength" if not chose_magic:
                jump fh_choices_5_3
            "(Act) Use magic to disorient him during the charge" if chose_magic:
                jump fh_choices_5_4

    label fh_choices_4_3:
        # Branching from "(Act) Use the hero's shield to block and counter"
        menu:
            "(Act) Push him back and strike" if not chose_magic:
                jump fh_choices_5_5
            "(Act) Use magic to create an opening" if chose_magic:
                jump fh_choices_5_6

    label fh_choices_4_4:
        # Branching from "(Act) Lure him into a position where he is vulnerable"
        menu:
            "(Act) Distract him with a feint and attack":
                jump fh_choices_5_7
            "(Act) Use the environment to trap him":
                jump fh_choices_5_8

    label fh_choices_4_5:
        # Branching from "(Act) Remind him of his past as a protector"
        menu:
            "(Act) Bring up his past victories":
                jump fh_choices_5_9
            "(Act) Highlight the injustice he suffered" if not chose_magic:
                jump fh_choices_5_10

    label fh_choices_4_6:
        # Branching from "(Act) Convince him that the kingdom has changed"
        menu:
            "(Act) Explain how the kingdom has reformed":
                jump fh_choices_5_11
            "(Act) Offer him a chance to return as a hero":
                jump fh_choices_5_12

    label fh_choices_4_7:
        # Branching from "(Act) Swear on your honor to clear his name"
        menu:
            "(Act) Offer to bring evidence of his innocence":
                jump fh_choices_5_13
            "(Act) Offer to use your authority as princess":
                jump fh_choices_5_14

    label fh_choices_4_8:
        # Branching from "(Act) Offer to stay in the forest with him"
        menu:
            "(Act) Offer to perform a magical oath" if chose_magic:
                jump fh_choices_5_15
            "(Act) Betray him and prepare to strike":
                jump fh_choices_5_16


    # Level 5 of choice tree
    label fh_choices_5_1:
        # Branching from "(Act) Strike at his old injury"
        menu:
            "(Act) Exploit his pain to win the fight":
                jump sacrificed_hero
            "(Act) Hesitate, showing mercy":
                jump love_beyond_death

    label fh_choices_5_2:
        # Branching from "(Act) Use magic to enhance the attack"
        menu:
            "(Act) Overwhelm him with dark magic":
                jump forest_curse
            "(Act) Bind his power with a magical seal":
                jump happily_ever_after

    label fh_choices_5_3:
        # Branching from "(Act) Overwhelm him with sheer strength"
        menu:
            "(Act) Defeat him decisively":
                jump inherited_throne
            "(Act) Knock him unconscious":
                jump saved_hero

    label fh_choices_5_4:
        # Branching from "(Act) Use magic to disorient him during the charge"
        menu:
            "(Act) Seal him away with forbidden magic":
                jump corrupted_hero
            "(Act) Break his weapon with magic":
                jump forest_protectors

    label fh_choices_5_5:
        # Branching from "(Act) Push him back and strike"
        menu:
            "(Act) Go for a lethal blow":
                jump sacrificed_hero
            "(Act) Aim to disarm him":
                jump saved_hero

    label fh_choices_5_6:
        # Branching from "(Act) Use magic to create an opening"
        menu:
            "(Act) Shatter his defenses with dark energy":
                jump forest_curse
            "(Act) Restrain him with enchanted chains":
                jump happily_ever_after

    label fh_choices_5_7:
        # Branching from "(Act) Distract him with a feint and attack"
        menu:
            "(Act) Teleport away" if chose_magic:
                jump happily_ever_after
            "(Act) Let him surrender willingly":
                jump love_beyond_death

    label fh_choices_5_8:
        # Branching from "(Act) Use the environment to trap him"
        menu:
            "(Act) Use a snare trap" if not chose_magic:
                jump sacrificed_hero
            "(Act) Trap him with magic" if chose_magic:
                jump corrupted_hero

    label fh_choices_5_9:
        # Branching from "(Act) Bring up his past victories"
        menu:
            "(Act) Remind him of the lives he saved":
                jump saved_hero
            "(Act) Teleport away quickly" if chose_magic:
                jump happily_ever_after

    label fh_choices_5_10:
        # Branching from "(Act) Highlight the injustice he suffered"
        menu:
            "(Act) Urge him to reclaim his honor":
                jump saved_hero
            "(Act) Push him to let go of his hatred":
                jump sacrificed_hero

    label fh_choices_5_11:
        # Branching from "(Act) Explain how the kingdom has reformed"
        menu:
            "(Act) Betray and attack with magic" if chose_magic:
                jump corrupted_hero
            "(Act) Persuade him to embrace peace":
                jump love_beyond_death

    label fh_choices_5_12:
        # Branching from "(Act) Offer him a chance to return as a hero"
        menu:
            "(Act) Promise him redemption":
                jump inherited_throne
            "(Act) Betray and strike with magic" if chose_magic:
                jump corrupted_hero

    label fh_choices_5_13:
        # Branching from "(Act) Offer to bring evidence of his innocence"
        menu:
            "(Act) Offer to present proof to the kingdom":
                jump love_beyond_death
            "(Act) Betray and shoot a fireball" if chose_magic:
                jump forest_curse

    label fh_choices_5_14:
        # Branching from "(Act) Offer to use your authority as princess"
        menu:
            "(Act) Offer to declare his innocence publicly":
                jump inherited_throne
            "(Act) Betray and strike with magic" if chose_magic:
                jump forest_protectors

    label fh_choices_5_15:
        # Branching from "(Act) Offer to perform a magical oath"
        menu:
            "(Act) Follow through with your promise":
                jump forest_protectors
            "(Act) Betray and shoot a fireball":
                jump forest_curse

    label fh_choices_5_16:
        # Branching from "(Act) Betray him and prepare to strike"
        menu:
            "(Act) Strike with sword" if not chose_magic:
                jump inherited_throne
            "Act) Strike with magic" if chose_magic:
                jump forest_protectors
    


label fh_who_are_you:
    p "Who are you, really? Why do you hold so much hatred in your heart?"
    n "The Fallen Hero's eyes darkened, his expression hardening as old wounds surfaced."
    fh "Who am I? I was once a knight of the kingdom-a hero, they called me. But that was before the lies, the betrayal."
    fh "Now, I am nothing but a shadow, a weapon forged by the very hatred they created. You would do well to remember that."

    return

label fh_why_hold_grudge:
    p "Why do you hold such a deep grudge against the kingdom? What did they do to you?"
    n "The Fallen Hero's voice dripped with bitterness as he recalled the past."
    fh "They turned their backs on me. Falsely accused, cast out like a common criminal, all because I knew too much-because I was a threat to their corruption."
    fh "The kingdom took everything from me-my honor, my name, my life. I was left with nothing but this grudge… and a hunger for retribution."

    return

label fh_things_have_changed:
    p "The kingdom wronged you, but that was long ago. Things have changed since then."
    n "The Fallen Hero's laughter was sharp and cold, void of any mirth."
    fh "Changed? You think a few years can wash away the sins they committed? The kingdom is built on lies and betrayal."
    fh "The faces may change, but the rot remains. You're fooling yourself if you think anything has truly improved. They'll betray you just as they did me-wait and see."

    return

label fh_what_happened:
    p "What happened to you? How did you become like this?"
    n "The Fallen Hero's eyes were filled with a mixture of pain and fury as he responded."
    fh "What happened? I was betrayed. They accused me of treachery-stripped me of everything I was, all because I dared to question those in power."
    fh "They turned me into this-this monster that hunts in the shadows. But make no mistake, I'm still the same knight I once was… only now, I serve no one but my hatred."

    return

label fh_why_kingdom_turn:
    p "Why did the kingdom turn against you? What did you do to deserve that?"
    n "The Fallen Hero's grip on his sword tightened, his eyes burning with rage."
    fh "Deserve? I dared to expose the rot festering within the walls of that kingdom. I knew secrets they wanted buried, truths that threatened their power."
    fh "Rather than face justice, they pinned false charges on me and banished me like a criminal. It wasn't justice-it was self-preservation at my expense."

    return

label fh_really_believe_revenge:
    p "Even if you get your revenge, do you really think it will change anything?"
    n "The Fallen Hero's gaze wavered for a moment, uncertainty flickering behind his anger."
    fh "Maybe it won't change anything for them. But for me… it's all I have left. My honor was stolen, my name tarnished, and there's no undoing that."
    fh "But I can still make them pay-make them feel the pain they've caused. What else is there for someone like me?"

    return

label fh_why_hunt_us:
    p "Why are you after us? What do we have to do with your grudge?"
    n "The Fallen Hero's voice was low and dangerous, filled with menace."
    fh "You carry the kingdom's blood-its stench is on you. Whether you realize it or not, you're its agents."
    fh "Killing you would send a message, show them that their sins will not go unpunished. Besides, you were foolish enough to enter this forest. That alone is reason enough for me to hunt you down."

    return

label fh_killing_us_satisfy:
    p "Will killing us really satisfy that thirst for revenge? Is that what you want?"
    n "The Fallen Hero's eyes narrowed, a hint of doubt creeping into his gaze."
    fh "Satisfy? It's not about satisfaction-it's about making things right. The kingdom took everything from me, so I'll take everything from them."
    fh "If ending you serves that purpose, then so be it. But deep down, I know… no bloodshed will ever truly balance the scales."

    return

label fh_what_would_you_do:
    p "What happens if you succeed? What will you do after you get your revenge?"
    n "The Fallen Hero fell silent, as if the question itself was one he had avoided for a long time."
    fh "What would I do…? I've asked myself that many times. Perhaps there is nothing left after that-no life beyond the hatred."
    fh "But if there's nothing more, then at least I'll go down knowing I took them with me. Peace is a lie, princess… the only end for someone like me is a blade in the dark."

    return

label fh_why_cant_pass:
    p "Why can't you just let us pass? We're not here to fight you."
    n "The Fallen Hero's expression hardened, his grip on his weapon firm."
    fh "Let you pass? And what, let you return to your kingdom, where you'll be praised as heroes while my name is spat on? No. I won't let that happen."
    fh "I've given too much for this fight to end with you simply walking away. If you came into this forest, then you're prepared to face the consequences."

    return

label fh_change_your_mind:
    p "Is there anything we can say or do that would make you change your mind?"
    n "The Fallen Hero's eyes narrowed, suspicion written in every line of his face."
    fh "Change my mind? You're grasping at straws, princess. There's no deal, no promise, no plea that can erase what's been done."
    fh "I've walked this path too far to turn back now. If you're looking for mercy, you're wasting your time."

    return

label fh_not_like_those:
    p "We're not like those who betrayed you. We're here to help."
    n "The Fallen Hero's laughter was cold and bitter, devoid of any warmth."
    fh "Help? From you? I've heard those words before-promises from those who smiled while twisting the knife in my back."
    fh "You may think you're different, but I see through the lies. The kingdom's poison runs deep, and you're tainted by it just like the rest. I won't fall for it again."

    return

