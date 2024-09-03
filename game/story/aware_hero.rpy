# Contains the code associated with portion of the game related to the "aware hero" dialogue.

default aware_hero_number = 0
image aware_hero Calm = "aware_hero_Calm.png"

label aware_hero:
    $ aware_hero_number += 1

    scene bg blackscreen with Dissolve(1.0)

    ah "Deja vu."
    play music "audio/6 The Aware Hero 4.mp3"

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
            show aware_hero Calm
            ap "It feels like we've been through something like this before... Can you tell me anything about what's happened before?"

            # Aware Hero (ah) speaks
            show aware_hero In_Thought
            ah "I... I wish I could, but it's complicated. There are things I'm not sure you're ready to hear, or maybe it's that I'm not ready to say them yet. Let's just focus on what we can do right now, okay?"

            # Princess' thoughts
            show aware_hero Unamused
            pt "Why won't he tell me? It's as if he knows something, something important. But... maybe he's trying to protect me? Or is it himself he's protecting?"

            # Narration
            n "The hero turns away, subtly shifting the focus back to their immediate task. Yet, the princess can't shake the feeling that there's more beneath the surface—more than he's willing to reveal."
            
            stop music fadeout 1.5
            return

        "Why do you seem so distant right now?":
            
            # Princess speaks
            show aware_hero Unamused
            ap "You've been quiet... Why do you seem so distant right now?"

            # Aware Hero responds
            show aware_hero Sad
            ah "I'm sorry if I seem distant. There's just a lot on my mind. I'm trying to keep us both safe, and sometimes that means holding back a bit. It's not that I don't trust you—I do. I just... need some time to sort things out."

            # Princess' thoughts
            pt "He's holding something back, I can feel it. But why? Does he think I can't handle it? Or is he afraid of what might happen if he opens up?"

            # Narration
            show aware_hero Unamused
            n "The princess searches his face for any sign he might say more, but the hero remains closed off, a fortress of unspoken thoughts and hidden fears."

            stop music fadeout 1.5
            return

        "Where are you from?":

            # Princess speaks
            show aware_hero Unamused
            ap "Where are you from?"

            # Aware Hero responds
            show aware_hero In_Thought
            ah "Where I'm from... it feels like a lifetime ago. It's hard to explain, really. Maybe someday I'll tell you more, but for now, let's just say it's not important compared to where we are now."

            # Princess' thoughts
            pt "Why won't he tell me more? There's so much I don't know about him, so much he keeps hidden. What is he afraid of?"

            # Narration
            show aware_hero Unamused
            n "The princess nods, sensing the invisible wall he's put up between them. She doesn't press further, though the unanswered questions linger in her mind, deepening the mystery that surrounds him."
            
            stop music fadeout 1.5
            return
    
$ aware_hero_second_chosen = 0
label aware_hero_second:
    while aware_hero_second_chosen < 3: # user gets to choose 3 choices
        $ aware_hero_second_chosen += 1

        menu:
            "Everything here feels strangely familiar. Does it to you?":

                # Princess speaks
                show aware_hero Calm
                ap "Everything here feels strangely familiar. Does it to you?"

                # Narration
                n "Her voice is soft, almost hesitant, as if she's not sure she wants to hear the answer. She glances at the Hero, searching his face for any hint of recognition."

                # Aware Hero responds
                show aware_hero In_Thought
                ah "Familiar... Yes, I suppose it does."

                # Narration
                n "His voice is careful, measured, as though he's testing the waters before diving in."

                # Aware Hero continues
                show aware_hero Angry_Confused
                ah "It's strange, isn't it? How certain places can stir something deep inside, like a memory just out of reach."

                # Aware Hero continues
                show aware_hero In_Thought
                ah "Or perhaps it's more than that... perhaps it's something we've lived before, in another time, another life."

                # Princess' Thoughts
                show aware_hero Calm
                pt "There it is again—that sense that he knows more than he's saying. But why does he keep holding back? What is it that he's not telling me?"

                # Princess speaks
                ap "Do you think it's possible? That we've been here before?"

                # Narration
                n "Her heart quickens with a mix of curiosity and unease, her eyes fixed on his as she tries to draw out more."

                # Aware Hero responds
                ah "I think... there are things in this world that go beyond what we can easily explain. Places that echo with the past, with experiences we might not fully remember but can still feel."

                # Narration
                show aware_hero In_Thought
                n "He turns to her, his gaze intense, as though trying to gauge how much she can handle."

                # Aware Hero continues
                ah "But those echoes—they don't always bring clarity. Sometimes, they're just shadows, hints of something larger. And maybe... maybe it's better not to dwell too much on them."

                # Princess' Thoughts
                pt "He's holding back again, retreating behind his words. But why? Is it because he's afraid? Or is he trying to protect me from something I don't yet understand?"

                # Princess speaks
                show aware_hero Unamused
                ap "You say that, but I can't help feeling like these shadows are trying to tell us something. Something important."

                # Narration
                n "Her voice is firmer now, determination creeping in as she tries to bridge the gap between them."

                # Aware Hero responds
                show aware_hero Scared
                ah "Maybe they are. Or maybe they're just echoes of a past that's better left undisturbed. But if you truly want to understand... if you really want to uncover what's hidden here... then you need to be prepared for the possibility that what you find might not be what you hope for."

                # Princess' Thoughts
                show aware_hero Unamused
                pt "He's warning me, but of what? And why does he always speak as if he's lived this all before?"

                # Narration
                n "The princess nods slowly, realizing that the journey before them is not just about where they're going, but also about uncovering the truths buried in the places that feel so hauntingly familiar."

                return

            "You always seem so composed... Do you ever feel afraid?":

                # Princess speaks
                show aware_hero Calm
                ap "You always seem so composed… Do you ever feel afraid?"

                # Aware Hero responds
                show aware_hero Smirk
                ah "Composed, huh? I suppose it's easier to look calm when you've been through the same things over and over again."

                # Aware Hero continues
                show aware_hero In_Thought
                ah "But yes, I do feel afraid. More often than you might think."

                # Aware Hero continues
                ah "Fear isn't something you can just... brush off. It's always there, lurking in the shadows, reminding you of what you stand to lose."

                # Narration
                n "His voice grows quieter, as though speaking these fears aloud makes them more real."

                # Aware Hero continues
                ah "But I've learned to manage it, to keep it at bay. Because if I let it take over, I'm not sure I'd be able to keep going."

                # Princess' Thoughts
                show aware_hero Calm
                pt "He's afraid... just like me. But he hides it so well. Why does he feel like he has to carry that burden alone?"

                # Princess speaks
                ap "You don't have to do that, you know. You don't have to face it alone."

                # Narration
                show aware_hero Loving Look
                n "There's a note of resolve in her voice, a determination to break through his walls."

                # Aware Hero responds
                ah "I know. And that helps more than you might realize. It's not easy, but knowing you're here, that we're facing this together... it makes the fear a little more bearable."

                # Narration
                show aware_hero Calm
                n "The princess feels a connection growing, something that strengthens with each shared fear, each whispered reassurance. They might be afraid, but they're not alone—and that makes all the difference."

                return

            "What was you life like before all of this started? Do you remember?":

                # Princess speaks
                ap "What was your life like before all of this started?"

                # Princess continues
                ap "Do you remember?"

                # Narration
                n "There's a flicker of something in his eyes—nostalgia, perhaps, or a sorrow that he's kept buried deep."

                # Aware Hero responds
                ah "I remember... bits and pieces."

                # Aware Hero continues
                ah "Before all of this—before the loops, the endless repetition—things were different. The world was different."

                # Aware Hero continues
                ah "I was a knight, sworn to protect the kingdom. Back then, the land was vibrant, full of life and promise. The fields were green, the villages bustling with people. I had a loving family back home. It was... simpler, I suppose."

                # Princess' Thoughts
                pt "The world he describes... It sounds so different from the one we know now. What happened to change it so much?"

                # Princess speaks
                ap "What happened? How did things become... this?"

                # Aware Hero responds
                ah "There were rumors at first—whispers of strange occurrences. Then people realized it was magic."

                # Aware Hero continues
                ah "I didn't understand it at first. None of us did. People hate what they don't understand."

                # Aware Hero continues
                ah "The kingdom fell into disarray, as if the very fabric of reality was unraveling."

                # Princess' Thoughts
                pt "So this is how it all began... A world unraveling, a kingdom falling apart. But who or what could have caused such a thing?"

                return

            # "Sometimes, I wonder if we're really in control of our own fate. What do u think?"

            "Why do you always look at me like that, like you're carrying some kind of burden?":

                # Princess speaks
                ap "Why do you always look at me like that, like you're carrying some kind of burden?"

                # Narration
                n "The hero is silent for a moment, his gaze fixed on the water as it flows over the smooth stones. There's a flicker of something in his eyes—hesitation, perhaps, or maybe it's something deeper, something more personal."

                # Aware Hero responds
                ah "This loop we're in... it's taken a lot from both of us. It's made us face things over and over again, things that most people only ever experience once, if at all."

                # Aware Hero continues
                ah "That's why I look at you like that. Because I know what you've been through, and I know what it's cost you. And maybe... maybe I feel like I could have done more to spare you from it."

                # Princess' Thoughts
                pt "He's seen it all—every struggle, every loss. But why does he bear it so heavily? What is it that he's not telling me?"

                # Princess speaks
                ap "But it's not your fault. You've done everything you could... Haven't you?"

                # Aware Hero responds
                ah "I stayed behind, in this loop, because I thought I could make a difference."

                # Aware Hero continues
                ah "That I could protect you from the worst of it, that somehow, I could change things, even if just a little."

                # Princess' Thoughts
                pt "He stayed... for me? But why would he take on that burden, knowing what it would mean?"

                # Princess speaks
                ap "You've stayed because you care... but it's not just about protecting me, is it?"

                # Narration
                n "There's a hint of understanding in her voice, as if she's beginning to see the deeper reasons behind his actions."

                # Aware Hero responds
                ah "It's about doing what feels right, about making sure that someone—anyone—doesn't have to face this alone."

                # Aware Hero continues
                ah "Maybe I can't change the past, but if I can make even one moment better, if I can lighten the burden just a little... then it's worth it."

                return

            "Do you believe that people can change?":

                # Princess speaks
                ap "Do you believe that people can change?"

                # Aware Hero responds
                ah "I'd like to think so. I've seen people do things they never thought they were capable of, for better or worse. But real change… that's something different."

                # Narration
                n "The princess nods, sensing the weight behind his words. She knows he's seen more of the world's darkness than most, and his experiences have shaped his view of people and their potential for change."

                # Princess speaks
                ap "What do you mean by 'real change'?"

                # Aware Hero responds
                ah "I mean the kind of change that goes beyond just actions. Anyone can make a different choice, do something unexpected. But changing who you are at your core… that's not so easy. It takes time, effort, and sometimes… pain."

                # Narration
                n "The princess watches him closely, seeing the reflection of past battles and hard-won lessons in his eyes. She knows he's speaking from experience, from a place deep within himself that still bears the scars of those struggles."

                # Princess speaks
                ap "Do you think you've changed?"

                # Aware Hero responds
                ah "I'd like to believe I have. That I've grown, become better, stronger. But sometimes… I wonder if I'm still the same person, just with different scars. If the things I've done, the choices I've made, really mean anything."

                # Narration
                n "The princess feels a pang in her chest, hearing the doubt in his voice, the fear that his efforts have been in vain."

                # Princess speaks
                ap "I think you have. I think we all have, in our own ways. Change isn't about becoming someone else. It's about becoming more of who you really are, beneath all the layers. And that… that's a journey we're all on."

                # Aware Hero responds
                ah "You always seem to have a way of making things clearer. It's like you can see right through all the noise, down to what really matters."

                # Princess speaks
                ap "Maybe it's because I believe in you. I believe in the person you are and the person you're becoming. And I think… if you can believe in that too, then you can change. We all can."

                # Aware Hero responds
                ah "Thank you, Princess. For believing in me, even when I find it hard to believe in myself."

                return

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