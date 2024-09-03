# Contains the code associated with portion of the game related to the "aware hero" dialogue.

default aware_hero_number = 0

label aware_hero:
    $ aware_hero_number += 1

    scene bg blackscreen with Dissolve(1.0)

    ah "Deja vu."
    play music "audio/6 The Aware Hero 4.mp3"
    
    ah "ITS BEEN SO LONG SINCE I LAST HAVE SEEN MY SON"

    if aware_hero_number == 1:
        jump aware_hero_first
    elif aware_hero_number == 2:
        jump aware_hero_second
    elif aware_hero_number == 3:
        jump aware_hero_third
    else:
        jump aware_hero_fourth


label aware_hero_first:
    $ aware_hero_met = True
    
    # show aware_hero emotion

    menu:
        "Can you tell me anything about what's happened before?":
            # Princess speaks
            show aware_hero calm
            ap "It feels like we've been through something like this before... Can you tell me anything about what's happened before?"

            # Aware Hero (ah) speaks
            show aware_hero in thought
            ah "I... I wish I could, but it's complicated. There are things I'm not sure you're ready to hear, or maybe it's that I'm not ready to say them yet. Let's just focus on what we can do right now, okay?"

            # Princess' thoughts
            show aware_hero unamused
            pt "Why won't he tell me? It's as if he knows something, something important. But... maybe he's trying to protect me? Or is it himself he's protecting?"

            # Narration
            n "The hero turns away, subtly shifting the focus back to their immediate task. Yet, the princess can't shake the feeling that there's more beneath the surface—more than he's willing to reveal."
            
            stop music fadeout 1.5
            return

        "Why do you seem so distant right now?":
            
            # Princess speaks
            show aware_hero unamused
            ap "You've been quiet... Why do you seem so distant right now?"

            # Aware Hero responds
            show aware_hero sad
            ah "I'm sorry if I seem distant. There's just a lot on my mind. I'm trying to keep us both safe, and sometimes that means holding back a bit. It's not that I don't trust you—I do. I just... need some time to sort things out."

            # Princess' thoughts
            pt "He's holding something back, I can feel it. But why? Does he think I can't handle it? Or is he afraid of what might happen if he opens up?"

            # Narration
            show aware_hero unamused
            n "The princess searches his face for any sign he might say more, but the hero remains closed off, a fortress of unspoken thoughts and hidden fears."

            stop music fadeout 1.5
            return

        "Where are you from?":

            # Princess speaks
            show aware_hero unamused
            ap "Where are you from?"

            # Aware Hero responds
            show aware_hero in thought
            ah "Where I'm from... it feels like a lifetime ago. It's hard to explain, really. Maybe someday I'll tell you more, but for now, let's just say it's not important compared to where we are now."

            # Princess' thoughts
            pt "Why won't he tell me more? There's so much I don't know about him, so much he keeps hidden. What is he afraid of?"

            # Narration
            show aware_hero unamused
            n "The princess nods, sensing the invisible wall he's put up between them. She doesn't press further, though the unanswered questions linger in her mind, deepening the mystery that surrounds him."
            
            stop music fadeout 1.5
            return
    

label aware_hero_second:


    stop music fadeout 1.5
    return

label aware_hero_third:
    $ game_done = True
    stop music fadeout 1.5
    return

label aware_hero_route:
    
    # Tower
    call tower_start


    # Forest (and first villain encounter)
    call forest_start

    if renpy.random.randint(1, 10) <= 2: # 2/10 chance to trigger aware hero
        call aware_hero
        return
    

    # Cryptic Stonehenge
    call cryptic_start

    if renpy.random.randint(1, 10) <= 4: # 4/10 chance to trigger aware hero
        call aware_hero
        return


    # Meadow
    call meadow_start

    if renpy.random.randint(1, 10) <= 7: # 7/10 chance to trigger aware hero
        call aware_hero
        return


    # Second Villain Encounter
    call second_villain_start
    return