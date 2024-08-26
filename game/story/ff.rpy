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

    # Leading text
    n "The air was thick with tension as the princess and the hero moved cautiously through the forest, the trees closing in around them like silent sentinels. There was an unsettling calm, as if the forest itself was holding its breath."
    n "The hero scanned the surroundings with narrowed eyes, every sense on high alert. He could feel it—a presence watching them, waiting for the right moment to strike."
    n "From the shadows, a figure emerged with a graceful, almost seductive stride. Her eyes glinted with a dangerous intelligence, and a sly smile played on her lips as she sized up the pair."
    ff "Well, well, what do we have here? The princess and her brave protector, still so far from the safety of the kingdom. How... intriguing."
  
    if ff_times_gotten == 1: 
        pt "The Femme Fatale again... Her words are like poison. I need to stay focused." 
 
    elif ff_times_gotten == 2:
        pt "We’ve dealt with her before. I can’t let her get into my head again."
  
    else: 
        pt "Her games won’t work this time. I’m ready for whatever she tries."

    n "The Femme Fatale stepped closer, her movements fluid and deliberate. Every word she spoke dripped with honeyed malice, designed to unsettle and disarm."
    h "Stay back, princess. Don’t listen to her lies. We have to stay focused."
    ff "Lies? Oh, darling, I don’t need to lie. I already know everything there is to know about you. But don’t worry, I’m not here to hurt you... not yet, anyway."
    n "Her voice was smooth, almost hypnotic, as she circled them, her gaze flicking between the princess and the hero. The air around them seemed to grow colder, every word a calculated strike at their resolve."
    ff "Let’s see how far you’re willing to go, princess. Will you sacrifice everything to protect your little hero? Or will you crumble under the weight of your own choices?"

    jump ff_choices_1

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


    label ff_who_are_you:
        p "Who are you? Why do you play these games with us?"
        n "The Femme Fatale’s smile was sly, her voice dripping with honeyed malice."
        ff "Who am I? Let’s just say I’m someone who thrives on the thrill of pulling strings and watching others dance."
        ff "You could call me a connoisseur of broken dreams and shattered resolves."

        return

    label ff_why_doing_this:
        p "Why are you doing this? What’s the point of all this manipulation?"
        n "The Femme Fatale’s eyes sparkled with amusement, her tone like velvet laced with venom."
        ff "Why? Because it’s entertaining, darling. There’s nothing quite like watching someone who thinks they’re in control unravel bit by bit."
        ff "You’re all just pieces on the board, and I… well, I do love winning."

        return

    label ff_what_you_gain:
        p "What do you even gain from tormenting others? Does it really satisfy you?"
        n "The Femme Fatale’s expression turned calculating, as if weighing her words carefully."
        ff "Satisfaction? My dear, it’s not just about satisfaction. It’s about power. The power to twist minds, to reveal the ugliness beneath the surface."
        ff "You’d be surprised how much you can learn when people are at their most desperate. And that knowledge… is priceless."
        
        return

    label ff_why_enjoy_manipulating:
        p "Why do you take such pleasure in manipulating people? What do you get out of it?"
        n "The Femme Fatale’s laugh was low and smooth, like silk gliding over a razor’s edge."
        ff "Pleasure? Oh, absolutely. There’s something exquisite about seeing people unravel under the weight of their own choices."
        ff "It’s a dance, really—one where I lead, and they stumble. The thrill is in knowing I’m always two steps ahead."

        return

    label ff_isnt_there_more:
        p "Isn’t there more to life than this? Games and deceit can’t be all you care about."
        n "The Femme Fatale’s smile softened into something almost wistful, though her eyes remained sharp."
        ff "More to life? Perhaps. But where’s the fun in sincerity when lies are so much more… intriguing? Life is a game, my dear."
        ff "The difference is, I’ve chosen to play it well. Others merely lose without even realizing it."

        return

    label ff_do_you_not:
        p "Don’t you care about the harm you cause? You ruin lives with your schemes."
        n "The Femme Fatale’s gaze grew cold, her smile fading into a hard edge."
        ff "Care? You mistake me for someone who feels guilt. People are fragile, easily led astray by their own weaknesses. All I do is expose what’s already there."
        ff "If they crumble, it’s because they were weak to begin with. I simply give them a nudge."

        return

    label ff_how_did_you:
        p "How did you become like this? Were you always this cruel?"
        n "The Femme Fatale’s eyes darkened, her voice laced with an undercurrent of bitterness."
        ff "How did I become like this? Let’s just say that trust is a currency I no longer trade in. I learned that the only way to survive is to be the one holding all the cards."
        ff "Once you’ve been betrayed enough times, it’s easy to see the world for what it really is—a game of deceit where the sharpest mind wins."

        return

    label ff_was_there_ever:
        p "Was there ever a time when you cared about anyone? When you weren’t like this?"
        n "The Femme Fatale’s smile turned icy, her voice carrying a note of distant sorrow."
        ff "Once, perhaps. But caring is a liability, a weakness that others will use against you. I learned that the hard way."
        ff "Love, loyalty—those are illusions people cling to before they’re inevitably betrayed. I chose to shed those illusions and embrace what truly matters: control."
                
        return
    
    label ff_do_you_think:
        p "Do you think you can ever change? Or is this who you are now, forever?"
        n "The Femme Fatale’s expression shifted, her eyes narrowing as if she found the question distasteful."
        ff "Change? Why would I want to? To become soft, vulnerable? No, darling. People don’t change—they just become better at hiding what they truly are."
        ff "I’ve found my path, and I’ll walk it until the very end, unburdened by sentiment or regret."

        return

    label ff_what_do_you:
        p "What do you really want from us? What’s the point of all this?"
        n "The Femme Fatale’s gaze was sharp, a smirk playing at the corner of her lips."
        ff "What do I want? Oh, nothing much. Just to see how far I can push you before you break."
        ff "There’s a certain artistry in that—finding the cracks, applying just the right pressure, and watching the pieces fall apart."
        ff "It’s fascinating, really."

        return

    label ff_is_this_just:
        p "Is this all just a game to you? Do our lives mean nothing?"
        n "The Femme Fatale’s laughter was soft, mocking, with an edge that cut deep."
        ff "A game? Yes, but a game with very real stakes. Your lives, your choices—they’re merely the pieces I move around the board."
        ff "The difference is, I know how this ends… and I’m always the one who comes out on top. You, on the other hand? You’re just trying to keep up."

        return

    label ff_when_will_it:
        p "When will this end? What are you really trying to achieve?"
        n "The Femme Fatale’s smile turned almost pitying, as if she found the question naïve."
        ff "When will it end? When I’ve taken everything I can from you—your hope, your resolve, your trust. I’m not after riches or power; I’m after the satisfaction of knowing I’ve stripped away every illusion you cling to."
        ff "When there’s nothing left but the truth—when you see the world as I do—then, perhaps, I’ll be satisfied. But until then? The game continues."

        return
