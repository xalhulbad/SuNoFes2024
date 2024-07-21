# Contains the code associated with portion of the game related to the "forest" scene,
# as well as the first villain encounter.

# Default variables
default forest_choices1_seen = set()

label forest_start:
    scene bg blackscreen

    n "The sound echoed through the stone walls of the tower. The door creaked open, revealing the hero's warm smile."
    h "Princess, it's time to leave. Come with me."
    n "The princess, heart pounding, stepped forward. She took the hero's hand, feeling a comforting warmth."

    scene bg forest with fade

    n "As they emerged out of the tower, sunlight bathed them. The sky was a brilliant blue, and the forest ahead was lush and green. Birds sang from the treetops, and a gentle breeze rustled the leaves."

    if routes_completed == 0: # First route
        p "It's so beautiful... I almost forgot what the world looks like."
    elif routes_completed == 1: # Second route
        pt "The same morning, the same hero, the same scene."
        pt "What’s going on? It’s like the story has just replayed itself."
    else: # Any route after the second
        p "Ah, the forest. It really is beautiful."
        pt "But with beauty comes pains. The pain of being trapped."
        pt "When will this end?"

    h "Let's go. The world is waiting for your return!"
    n "Hand in hand, they stepped into the clearing, ready to face the forest and their journey ahead."

    label forest_choices1:
        while len(forest_choices1_seen) < 2:
            menu:
                set tower_choices1_seen
                # Tells renpy to hide choices in this set (prevents same option showing up twice)

                # Choices available from the start:
                "(Act) Who are you?":
                    call forest_who_are_you
                    $ forest_choices1_seen.add("(Act) Who are you?")
                    jump forest_choices1

                "(Act) How long have I been trapped?":
                    call forest_how_long_trapped
                    $ forest_choices1_seen.add("(Act) How long have I been trapped?")
                    jump forest_choices1

                "(Act) Where are we headed now?":
                    call forest_where_are_we_headed
                    $ forest_choices1_seen.add("(Act) Where are we headed now?")
                    jump forest_choices1

                "(Act) Why did you come to rescue me?":
                    call forest_why_did_you_come
                    $ forest_choices1_seen.add("(Act) Why did you come to rescue me?")
                    jump forest_choices1

                "(Act) Is it safe outside the tower?":
                    call forest_is_it_safe
                    $ forest_choices1_seen.add("(Act) Is it safe outside the tower?")
                    jump forest_choices1

                "(Act) What is your quest?":
                    call forest_what_is_your_quest
                    $ forest_choices1_seen.add("(Act) What is your quest?")
                    jump forest_choices1

                "(Act) Proceed into the forest": # Progresses the game
                    $ forest_choices1_seen.clear() # Reset seen choices for later
                    jump forest_proceed_into_forest

                
                # Choices available after first route completed:
                "​​(Act) Have we done this before?" if routes_completed > 0:
                    call forest_have_we_done_this
                    $ forest_choices1_seen.add("​​(Act) Have we done this before?")
                    jump forest_choices1

                "(Act) Why does this feel familiar?" if routes_completed > 0:
                    call forest_why_familiar
                    $ forest_choices1_seen.add("(Act) Why does this feel familiar?")
                    jump forest_choices1

                "(Act) Can we change what happens next?" if routes_completed > 0:
                    call forest_can_we_change
                    $ forest_choices1_seen.add("(Act) Can we change what happens next?")
                    jump forest_choices1

                "(Act) Do you remember anything unusual?" if routes_completed > 0:
                    call forest_remember_unusual
                    $ forest_choices1_seen.add("(Act) Do you remember anything unusual?")
                    jump forest_choices1


                # Choices available after second route completed:
                "(Act) How many times has this story replayed?" if routes_completed > 1:
                    call forest_how_many_times
                    $ forest_choices1_seen.add("(Act) How many times has this story replayed?")
                    jump forest_choices1


        # If we get here then the player did not choose "(Act) Proceed into the forest" within 2 choices

        $ tower_choices1_seen.clear() # Reset seen choices for later

        # Force player to choose "(Act) Proceed into the forest"
        menu:
            "(Act) Proceed into the forest": # Progresses the game
                    jump forest_proceed_into_forest # No call because we don't want to return


    # Forest choices that are available from the start:
    label forest_who_are_you:
        h "I'm just a humble hero, it is my commission to help you."
        pt "Cute."
        p "How did you come to be my rescuer?"
        h "I heard stories of your plight and couldn't bear the thought of you being alone. I had to help. That tower does not look fun."
        p "You're right about that."
        return

    label forest_how_long_trapped:
        h "I... don't really know, but it must have felt like forever."
        p "It sure has. It couldn’t have been that long, but my memory is failing me. Doesn’t matter, I’m so glad you’re here."
        return

    label forest_where_are_we_headed:
        h "I thought we could go back to the kingdom through the forest. It's beautiful and safe, I think."
        p "It’s probably the better path back to the kingdom. Do you know your way?"
        h "Not really. Ha... I really should though, shouldn’t I?"
        h "We can discover it together."
        return

    label forest_why_did_you_come:
        h "I couldn't bear the thought of you being alone. It felt like my heart led me here."
        p "Your heart is very brave. Do you always follow it so faithfully?"
        h "I try to. It has not led me wrong yet."
        return

    label forest_is_it_safe:
        h "I believe it is, especially if we're together. I'll do my best to keep us safe."
        p "That’s comforting. Is there anything we should watch out for?"
        h "I've heard there are wild animals, but we can be careful. Let’s just try not to run into whatever locked you up."
        h "One step at a time."
        return

    label forest_what_is_your_quest:
        h "My quest? To see you free and happy, I suppose."
        h "Such a simple yet noble quest. What will you do once I am free?"
        h "I haven't thought that far ahead. For now, let's just focus on getting you out of here."
        return

    label forest_proceed_into_forest:
        n "The princess and the hero stepped forward in the forest, but something was off. A bad omen. An eerie silence enveloped them."
        n "A tree branch cracked under the foot of the Princess. A flock of birds scattered from the canopy above at the sudden noise."
        n "The hero narrowed his eyes and scanned his surroundings. His hand drifted towards the numerous weapons he had equipped."
        n "Suddenly, a shadowy figure emerged from the darkness, cloaked in a tattered robe. Their face was hidden, and their voice was a muffled hiss that sent shivers down the princess’s spine."
        v "So, the princess dares to leave her tower. How brave... or foolish."
        n "The pair’s eyes locked on to the figure."

        if routes_completed == 0:
            pt "Who is this? Their presence feels... menacing."
            pt "Is this the one responsible for my captivity? Maybe I can get some answers."
            p "Who are you? Why are you hiding in the shadows?"
        elif routes_completed == 1:
            pt "This figure once again. Looks like this hasn’t changed either."
            p "You. We meet again."
            n "The hero glanced at the princess with a concerned look."
        else:
            pt "Let's get this over with."
        
        n "The figure stepped closer, their movements almost ethereal. The hero instinctively placed himself between the princess and the stranger."
        h "Stay back! We mean no harm, but we will defend ourselves if necessary."
        v "How amusing. Be careful now."
        v "Your choices matter." #TODO: discuss if we should give this a special font/colour to have more significance

        return # End of forest scene


    # Forest choices that are available only after first route completed:
    label forest_have_we_done_this:
        h "Um... what are you talking about? This is my first time meeting you."
        pt "The ignorance."
        p "Hm. Strange. I feel like I know you already."
        h "Maybe we were just meant to meet. Sometimes, things happen for a reason."
        return

    label forest_why_familiar:
        h "I'm not sure, but maybe it's a good thing. We can trust each other, right?"
        pt "Is this fate’s cruel trick?"
        p "Yes, trust. It's something I haven't felt in a long time."
        h "Then let's build on that. We'll figure things out together."
        return

    label forest_can_we_change:
        h "I’m not too sure what you mean, but we will carve our own future. I'm here with you, whatever comes."
        pt "The story has been replayed. What is happening?"
        p "We'll face whatever comes. We must."
        return

    label forest_remember_unusual:
        h "Not really. Just my mission to save you."
        pt "The same obliviousness."
        p "It's like a dream I can't wake up from. Do you ever feel that way?"
        h "Sometimes. But maybe dreams can change."
        return


    # Forest choices that are available only after second route completed:
    label forest_how_many_times:
        h "I don't understand. This is the first time I've come for you."
        pt "If only you knew the truth."
        p "No, I’m pretty sure we've met before, over and over."
        h "Maybe that's a sign. Maybe we're destined to help each other."
        return

    return