# Contains the code associated with portion of the game related to the "aware hero" dialogue.

default aware_hero_number = 0
default aware_hero_second_chosen = 0
default aware_hero_trigger_scene = None # Can be "forest", "cryptic", "meadow" or "second_villain"

label aware_hero:
    $ aware_hero_number += 1

    scene bg blackscreen with Dissolve(1.0)

    ah "Hello...?"

    play music "audio/6 The Aware Hero 4.mp3"

    if aware_hero_number == 1:
        jump aware_hero_first
    elif aware_hero_number == 2:
        jump aware_hero_second
    else:
        jump aware_hero_third


label aware_hero_first:
    $ aware_hero_met = True
    
    # show aware_hero emotion
    show aware_hero Calm


    menu:
        "What's happened before?":
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
            an "The hero turns away, subtly shifting the focus back to their immediate task. Yet, the princess can't shake the feeling that there's more beneath the surface—more than he's willing to reveal."
            
            stop music
            scene bg actual_blackscreen
            pause(2)
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
            an "The princess searches his face for any sign he might say more, but the hero remains closed off, a fortress of unspoken thoughts and hidden fears."

            stop music
            scene bg actual_blackscreen
            pause(2)
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
            an "The princess nods, sensing the invisible wall he's put up between them. She doesn't press further, though the unanswered questions linger in her mind, deepening the mystery that surrounds him."
            
            stop music
            scene bg actual_blackscreen
            pause(2)
            return
    
label aware_hero_second:
    while aware_hero_second_chosen < 3: # user gets to choose 3 choices
        $ aware_hero_second_chosen += 1
        show aware_hero Calm # default expression is calm

        menu:
            "Everything here feels strangely familiar.":

                # Princess speaks
                show aware_hero Calm
                ap "Everything here feels strangely familiar. Does it to you?"

                # Narration
                an "Her voice is soft, almost hesitant, as if she's not sure she wants to hear the answer. She glances at the Hero, searching his face for any hint of recognition."

                # Aware Hero responds
                show aware_hero In_Thought
                ah "Familiar... Yes, I suppose it does."

                # Narration
                an "His voice is careful, measured, as though he's testing the waters before diving in."

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
                an "Her heart quickens with a mix of curiosity and unease, her eyes fixed on his as she tries to draw out more."

                # Aware Hero responds
                ah "I think... there are things in this world that go beyond what we can easily explain. Places that echo with the past, with experiences we might not fully remember but can still feel."

                # Narration
                show aware_hero In_Thought
                an "He turns to her, his gaze intense, as though trying to gauge how much she can handle."

                # Aware Hero continues
                ah "But those echoes—they don't always bring clarity. Sometimes, they're just shadows, hints of something larger. And maybe... maybe it's better not to dwell too much on them."

                # Princess' Thoughts
                pt "He's holding back again, retreating behind his words. But why? Is it because he's afraid? Or is he trying to protect me from something I don't yet understand?"

                # Princess speaks
                show aware_hero Unamused
                ap "You say that, but I can't help feeling like these shadows are trying to tell us something. Something important."

                # Narration
                an "Her voice is firmer now, determination creeping in as she tries to bridge the gap between them."

                # Aware Hero responds
                show aware_hero Scared
                ah "Maybe they are. Or maybe they're just echoes of a past that's better left undisturbed. But if you truly want to understand... if you really want to uncover what's hidden here... then you need to be prepared for the possibility that what you find might not be what you hope for."

                # Princess' Thoughts
                show aware_hero Unamused
                pt "He's warning me, but of what? And why does he always speak as if he's lived this all before?"

                # Narration
                an "The princess nods slowly, realizing that the journey before them is not just about where they're going, but also about uncovering the truths buried in the places that feel so hauntingly familiar."

                return

            "Do you ever feel afraid?":

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
                an "His voice grows quieter, as though speaking these fears aloud makes them more real."

                # Aware Hero continues
                ah "But I've learned to manage it, to keep it at bay. Because if I let it take over, I'm not sure I'd be able to keep going."

                # Princess' Thoughts
                show aware_hero Calm
                pt "He's afraid... just like me. But he hides it so well. Why does he feel like he has to carry that burden alone?"

                # Princess speaks
                ap "You don't have to do that, you know. You don't have to face it alone."

                # Narration
                show aware_hero Loving Look
                an "There's a note of resolve in her voice, a determination to break through his walls."

                # Aware Hero responds
                ah "I know. And that helps more than you might realize. It's not easy, but knowing you're here, that we're facing this together... it makes the fear a little more bearable."

                # Narration
                show aware_hero Calm
                an "The princess feels a connection growing, something that strengthens with each shared fear, each whispered reassurance. They might be afraid, but they're not alone—and that makes all the difference."

                return

            "What was you life like before all of this started?":

                # Princess speaks
                ap "What was your life like before all of this started?"

                # Princess continues
                show aware_hero Sad
                ap "Do you remember?"

                # Narration
                an "There's a flicker of something in his eyes — nostalgia, perhaps, or a sorrow that he's kept buried deep."

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

            "Why do you always look at me like that, like you're carrying some kind of burden?":

                # Princess speaks
                show aware_hero In_Thought
                ap "Why do you always look at me like that, like you're carrying some kind of burden?"

                # Narration
                an "The hero is silent for a moment, his gaze fixed on the water as it flows over the smooth stones. There's a flicker of something in his eyes—hesitation, perhaps, or maybe it's something deeper, something more personal."

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
                show aware_hero Loving_Look
                ah "That I could protect you from the worst of it, that somehow, I could change things, even if just a little."

                # Princess' Thoughts
                pt "He stayed... for me? But why would he take on that burden, knowing what it would mean?"

                # Princess speaks
                ap "You've stayed because you care... but it's not just about protecting me, is it?"

                # Narration
                an "There's a hint of understanding in her voice, as if she's beginning to see the deeper reasons behind his actions."

                # Aware Hero responds
                show aware_hero In_Thought
                ah "It's about doing what feels right, about making sure that someone—anyone—doesn't have to face this alone."

                # Aware Hero continues
                ah "Maybe I can't change the past, but if I can make even one moment better, if I can lighten the burden just a little... then it's worth it."

                return

            "Do you believe that people can change?":

                # Princess speaks
                ap "Do you believe that people can change?"

                # Aware Hero responds
                show aware_hero In_Thought
                ah "I'd like to think so. I've seen people do things they never thought they were capable of, for better or worse. But real change… that's something different."

                # Narration
                an "The princess nods, sensing the weight behind his words. She knows he's seen more of the world's darkness than most, and his experiences have shaped his view of people and their potential for change."

                # Princess speaks
                ap "What do you mean by 'real change'?"

                # Aware Hero responds
                ah "I mean the kind of change that goes beyond just actions. Anyone can make a different choice, do something unexpected. But changing who you are at your core… that's not so easy. It takes time, effort, and sometimes… pain."

                # Narration
                an "The princess watches him closely, seeing the reflection of past battles and hard-won lessons in his eyes. She knows he's speaking from experience, from a place deep within himself that still bears the scars of those struggles."

                # Princess speaks
                ap "Do you think you've changed?"

                # Aware Hero responds
                show aware_hero Sad
                ah "I'd like to believe I have. That I've grown, become better, stronger. But sometimes… I wonder if I'm still the same person, just with different scars. If the things I've done, the choices I've made, really mean anything."

                # Narration
                an "The princess feels a pang in her chest, hearing the doubt in his voice, the fear that his efforts have been in vain."

                # Princess speaks
                ap "I think you have. I think we all have, in our own ways." 
                
                show aware_hero Loving_Look
                ap "Change isn't about becoming someone else. It's about becoming more of who you really are, beneath all the layers. And that… that's a journey we're all on."

                # Narration
                an "The hero turns his head to look at her, his expression softening. There's a flicker of hope in his eyes, a hint of something that feels like relief."
                
                # Aware Hero responds
                show aware_hero Loving_Look
                ah "You always seem to have a way of making things clearer. It's like you can see right through all the noise, down to what really matters."

                # Princess speaks
                ap "Maybe it's because I believe in you. I believe in the person you are and the person you're becoming. And I think… if you can believe in that too, then you can change. We all can."

                # Aware Hero responds
                ah "Thank you, Princess. For believing in me, even when I find it hard to believe in myself."

                return

    stop music
    scene bg actual_blackscreen
    pause(2)
    return

label aware_hero_third:
    $ game_done = True

    show aware_hero Calm

    menu:
        # choice 14
        "If you hadn't stayed":

            # Princess speaks
            ap "If you hadn't stayed inside this loop, what would you have wanted for yourself? What kind of life?"

            # Narration
            show aware_hero Unamused
            an "The question hangs in the air, heavy with unspoken possibilities."

            # Hero responds
            show aware_hero In_Thought
            ah "Before I chose to stay, I used to think about that a lot. I'd imagine a life where I wasn't ‘the hero,' where I could just be... me."
            ah "I pictured a small village, somewhere far away from all of this. A place where no one knew my name, where I wasn't expected to be anything more than who I was."

            # Narration
            an "His voice is tinged with a wistful longing, a bittersweet echo of dreams that never came to be. The princess feels a pang of sadness as she listens, picturing the simple life he once yearned for."

            # Princess' thoughts
            show aware_hero Calm
            pt "He's always been so strong, so certain in his role. But underneath it all, there's a part of him that wanted something different—something quieter, more peaceful. It's hard to imagine him living that life, but at the same time, I can see why he wanted it."

            # Hero continues
            show aware_hero In_Thought
            ah "I'd wake up with the sun, work the fields, maybe build a home with my own hands. I dreamed of having a garden, a stream nearby where I could fish. It was a simple life, but it was mine. The kind of life where the hardest decision was what to plant that season, or whether to fix the roof before the next storm."

            # Narration
            show aware_hero Calm
            an "His words paint a picture of a life that's the opposite of everything he's known—a life free from battles and responsibilities. The princess can see how much this imagined life meant to him, how much he sacrificed to stay in the loop, to stay with her."

            # Princess speaks
            ap "It sounds... peaceful. Like something out of a storybook, but without the quests or the monsters. Just... life."

            # Narration
            an "Her voice is gentle, filled with empathy. She almost wishes he could have had that life, away from the endless cycle they're trapped in. But she knows it's a life he chose to give up, and that choice was made out of love for her."

            # Princess continues
            show aware_hero Unamused
            ap "You could have had that life if you broke free. What stopped you?"

            # Narration
            an "Her question is soft, but there's an urgency in it. She needs to understand why he stayed, why he gave up his dreams for a life of repetition and duty."

            # Hero responds
            show aware_hero Loving_Look
            ah "You stopped me."
            an "His voice is steady, but there's an unmistakable emotion beneath it—a mix of love, duty, and something deeper."

            # Narration continues
            an "Every time I thought about leaving, I'd see your face, hear your voice. I knew you were in this with me, even if you didn't realize it. I couldn't abandon you to face it alone. So I stayed."

            # Princess' thoughts
            pt "He stayed because of me. Because he didn't want to leave me alone in this loop, didn't want to walk away from the life we've shared—even if it meant giving up his own dreams. I never knew... and now that I do, I don't know how to feel. Grateful? Guilty? Both?"

            # Princess speaks
            ap "You gave up so much... for me. And I never even knew."

            # Narration
            an "Her voice trembles slightly, the weight of his sacrifice pressing down on her. He's always been her protector, her constant, but she never fully understood what that meant—until now."

            # Hero responds
            show aware_hero Unamused
            ah "It wasn't just for you. I didn't want to lose you, even if it meant losing the chance at that other life. But sometimes, I wonder... if I'd walked away, would I have found peace? Or would I have spent every day missing you, regretting the choice?"

            # Narration
            an "His tone softens, heavy with years of unspoken doubts. He's lived with his decision, but that doesn't erase the lingering question of what might have been."

            # Princess' thoughts
            pt "He wonders if he made the right choice, but I can't imagine this world without him. Maybe I've been so focused on finding my own way out that I never thought about what he's been through—what he's given up to stay by my side."

            # Princess speaks
            ap "I wish you could have had that life. A part of me wants to tell you to go, to find it now, even if it means leaving me behind. But I'm scared. I don't want to face this without you."

            # Narration
            show aware_hero Loving_Look
            an "Her confession is both an expression of love and guilt. She knows the life he could have had, the peace he might have found, but the thought of him leaving, of facing the loop alone, terrifies her."

            # Hero responds
            ah "I don't think that life exists for me anymore. Maybe it never did. It was a dream I clung to, but if I could choose again... I'd still stay. I'd still choose you."

            # Narration
            an "His words soothe her, reassuring her that he doesn't regret his choice. There's a deep sincerity in his voice—a truth that transcends the loop, that endures beyond the endless repetition."

            # Princess' thoughts
            pt "He doesn't regret it. Even knowing what he gave up, he'd choose to stay. To be with me. It's comforting, but it also makes me realize how much he's sacrificed—and how much I owe it to him to find a way out of this together."

            # Princess speaks
            ap "You've always been my hero. But maybe... we can find a way to break free together. Maybe we can create a life that's ours."
            ap "Maybe this time, we'll write our own story."
            ap "Whatever it takes, I want us to write it."

            # Narration
            show aware_hero Calm
            an "Her resolve is clear—she's ready to face the unknown, to break free from the roles they've been bound to. But is she ready to face it alone, as unbeknownst to the princess, the hero's happily ever after is different."

            jump third_encounter_second_choice

    return

label third_encounter_second_choice:
    menu:
        # choice 13
        "What do you think my life would be like if you hadn't stayed?":

            # Princess speaks
            ap "What do you think my life would be like if you hadn't chosen to stay in this loop?"
            show aware_hero In_Thought
            if v_type == "hu":
                ap "No one to protect me from the Hunter."

            elif v_type == "fh":
                ap "No one to protect me from the Fallen Hero."

            elif v_type == "ff":
                ap "No one to protect me from the Femme Fatale."

            elif v_type == "dml":
                ap "No one to protect me from the Dark Magic Lord."

            else:
                ap "No one to protect me from the Vengeful Spirit."
            
            # Narration
            an "Her voice is thoughtful, almost wistful, as she gazes at him, seeking an answer to a question that touches on the very foundation of their shared existence. It's a question that has lingered in the back of her mind, a quiet wonder about the path not taken, the life she might have led if he hadn't chosen to stay by her side."

            # Hero responds
            show aware_hero Unamused
            ah "Truth be told, if I hadn't stayed... I'm not sure where you'd be. Maybe you would have found a way to break free on your own, or maybe you'd still be here, repeating the same cycles, searching for answers."

            # Narration
            an "He pauses, his gaze distant as he contemplates the possibilities, the what-ifs that have haunted him for so long. There's a weight to his words, a quiet acknowledgment of the role he's played in her life, and the uncertainty of what might have been."

            # Hero continues
            ah "I like to think that by staying, I've made the loop a bit more bearable, maybe I've helped you find the strength to keep going."
            show aware_hero Sad
            ah "But I also wonder... if I'd left, would you have found your own path sooner? Would you have discovered your own way out, without me holding you back?"

            # Narration
            an "His voice carries a note of self-doubt, a questioning of his own role in her journey. It's a vulnerability he rarely shows, a glimpse into the thoughts that have plagued him—whether his presence has truly been a help, or if it has been a hindrance."

            # Princess' thoughts
            pt "He thinks he might have held me back... but I can't imagine facing all of this without him. What would I have become if I'd been alone? Could I have found the strength to keep going, to face all the challenges without him by my side?"

            # Princess speaks
            ap "I don't think you've held me back. In fact, I'm not sure I'd have made it this far without you. You've been my strength, my guide... I can't imagine facing this alone."

            # Narration
            show aware_hero Loving_Look
            an "Her voice is filled with sincerity, her eyes meeting his with a depth of gratitude that goes beyond words. She can see the doubt in his eyes, the uncertainty that he's carried with him, and she wants to ease that burden, to let him know just how much his presence has meant to her."

            # Hero responds
            ah "It's kind of you to say that."

            # Narration
            an "There's a softness in his tone, a quiet acceptance of her words, yet she can tell that the doubt still lingers, just beneath the surface."

            # Hero continues
            show aware_hero Sad
            ah "But I also wonder if, by staying, I've kept you tethered to this loop in a way you wouldn't have been if I'd left. Maybe I've become part of the very thing that's keeping you here."

            # Princess' thoughts
            pt "He's questioning his choices... but I don't see it that way. His presence has given me hope, even when everything else felt lost. He's been the one constant in a world that never stops changing, and I wouldn't trade that for anything."

            # Princess speaks
            ap "You've been my anchor in this storm."
            show aware_hero Loving_Look
            ap "You saved me countless times from the villains (insert list of villains). I don't see you as someone who's kept me here... I see you as someone who's kept me from falling apart."

            # Narration
            an "Her voice is steady, filled with conviction, as she speaks the truth that she knows deep in her heart. She's seen the worst of what this loop has to offer, and through it all, he's been there—strong, unwavering, the one thing she could always count on. Without him, she knows she would have been lost long ago."

            # Hero responds
            ah "To know that I've made some small difference in your life, even if I couldn't change everything, means the world to me."

            # Narration
            an "His words are filled with a quiet pride, a sense of fulfillment that comes from knowing he's made a difference, even if it's in ways that aren't always visible. He's seen her grow, seen her face challenges with a strength that he knows she might not recognize in herself."

            # Princess' thoughts
            pt "He's given me so much... more than I could ever repay. And now it's up to both of us to find a way forward, together. We can't stay trapped in this loop forever, but whatever path we take, I know we'll face it side by side."

            # Princess speaks
            ap "I'm glad you stayed. Whatever path we're on, we're walking it together. And maybe that's what matters most—that we're not alone in this."

            # Narration
            an "Her words are a quiet affirmation, a reminder that, despite all the doubts and uncertainties, what matters most is that they're together right now."

            jump third_encounter_third_choice

label third_encounter_third_choice:

    menu:
        # choice 9 and 10
        "I'm scared… What if we're stuck like this forever?":
            
            # Princess speaks
            ap "I'm scared… What if we're stuck like this forever?"

            # Narration
            show aware_hero Sad
            an "Her voice trembles with the weight of her fear, her eyes searching for his reassurance, for something that can anchor her in this seemingly endless cycle."

            # Aware Hero speaks
            ah "I know that fear."
            show aware_hero Afraid
            ah "It's something I've struggled with since the beginning. This loop, this repetition... it can make you feel like you're caught in a web, each thread tightening the more you struggle against it."
            show aware_hero Sad
            ah "But what if it's not that bad? What if the world past the looping is worse?"

            # Princess responds
            ap "Worse?"
            ap "But how can it be worse when everything just repeats? When nothing we do seems to change the outcome?"

            # Narration
            an "The despair in her voice is palpable, as though she's standing on the edge of a precipice, looking down into the void of endless repetition."

            # Aware Hero continues
            show aware_hero In_Thought
            ah "Because even in the repetition, we have the power to choose how we respond. The loop doesn't define us—we define ourselves by the way we face it."

            # Princess' thoughts
            show aware_hero Calm
            pt "Meaning... Purpose... Can we really find that here, in this endless loop?"

            # Princess speaks again
            ap "But what if that's not enough? What if... what if we lose ourselves in the repetition? What if we forget who we are, what we're fighting for?"

            # Narration
            an "Her voice is softer now, more vulnerable, as if she's admitting a fear she's never voiced before."

            # Aware Hero reassures
            show aware_hero In_Thought
            if v_type == "hu":
                ah "Fighting the Hunter is how we give meaning to our actions, to our relationships, to our struggles. So even if we're stuck, even if this loop never ends, we can still find purpose in it. We can still find meaning in life because we have each other."
            
            elif v_type == "fh":
                ah "Fighting the Fallen Hero is how we give meaning to our actions, to our relationships, to our struggles. So even if we're stuck, even if this loop never ends, we can still find purpose in it. We can still find meaning in life because we have each other."

            elif v_type == "ff":
                ah "Fighting the Femme Fatale is how we give meaning to our actions, to our relationships, to our struggles. So even if we're stuck, even if this loop never ends, we can still find purpose in it. We can still find meaning in life because we have each other."

            elif v_type == "dml":
                ah "Fighting the Dark Magic Lord is how we give meaning to our actions, to our relationships, to our struggles. So even if we're stuck, even if this loop never ends, we can still find purpose in it. We can still find meaning in life because we have each other."

            else:
                ah "Fighting the Vengeful Spirit is how we give meaning to our actions, to our relationships, to our struggles. So even if we're stuck, even if this loop never ends, we can still find purpose in it. We can still find meaning in life because we have each other."

            # Narration
            show aware_hero Calm
            an "The hero's voice is filled with a determination that the princess has never heard."

            # Princess' thoughts
            pt "He's right... We're the ones who decide. And maybe that's the only real power we have in this endless cycle."

            # Narration
            an "She takes a deep breath, feeling a renewed sense of resolve, however fragile it might be."

            # Princess concludes
            ap "So we keep going. We keep making our choices, holding on to each other, and we find our own meaning in this, no matter how many times we have to start over."

            # Narration
            an "Her voice is steadier now, her fear still present but tempered by a growing sense of purpose."

            # Aware Hero agrees
            ah "Exactly. We may not have control over the loop, but we have control over ourselves, over how we face each new day, each new challenge, each new villain. And as long as we hold on to that, we haven't lost."

            # Final narration
            an "In this place without time, without setting, their words carry weight, creating a space of understanding and connection between them. The loop may continue, the repetition may persist, but here, in this moment, they've found something solid to hold on to—to try to keep them together."

            jump third_encounter_fourth_choice

        "What do you fear the most about breaking free from this loop?":

            # Princess speaks
            ap "What do you fear the most about breaking free from this loop?"

            # Narration
            show aware_hero Surprised
            an "Her question is simple, yet it carries the weight of all the uncertainty that surrounds their situation."
            show aware_hero In_Thought
            an "He lets it hang in the air before answering."

            # Aware Hero begins to speak
            ah "Fear..."

            # Narration
            an "He begins slowly, as if tasting the word, trying to understand it himself."

            # Aware Hero continues
            show aware_hero Afraid
            ah "It's strange, isn't it? How even in a place where we seem to live the same moments over and over, fear still finds a way to creep in."
            ah "I suppose... what I fear most isn't the idea of breaking free itself, but what comes after. If we did manage to break free from this loop, what would that even mean for us? What would be left?"

            # Princess responds
            show aware_hero Unamused
            ap "You mean... what kind of world would be waiting for us? Or if there would even be a world at all?"

            # Narration
            an "Her voice is tinged with the same apprehension that she hears in his, as if she's beginning to see the full scope of what they might face."

            # Aware Hero agrees
            show aware_hero Calm
            ah "Exactly. We've been stuck here for so long, repeating the same events, that it's hard to imagine what life outside the loop would look like. What if it's worse? What if we find ourselves in a world where everything we know is gone, where we're truly alone?"

            # Princess' thoughts
            pt "Would it be worse?"

            # Princess pushes back
            ap "But isn't it worth the risk? Isn't the chance to finally break free, to live a life where we aren't bound by these same patterns, worth whatever might come next?"

            # Narration
            an "There's a note of determination in her voice, as if she's trying to convince herself as much as him."

            # Aware Hero considers
            ah "Maybe it is,"
            show aware_hero Angry_Confused
            ah "but fear isn't always rational. It's this deep, gnawing feeling that there are things we don't know, things we can't predict. What if breaking free means losing the only things that have kept us sane? What if we lose the connection we've built here, the understanding we've found in each other?"
            show aware_hero Calm
            ah "And what if... we break free, and it turns out there's nothing left for us on the other side? That's what I fear the most. That after all this struggle, we might find ourselves in a place that's empty, that doesn't recognize us, or worse, that we don't recognize ourselves anymore."

            # Princess' thoughts
            show aware_hero Unamused
            pt "He's thought about this so much, carried these fears with him all this time... but we can't stay trapped just because we're afraid of what comes next, can we?"

            # Princess offers reassurance
            ap "I understand why you're afraid. I feel it too... But I think that no matter what's on the other side, it has to be better than this. Even if it's unknown, even if it's terrifying, at least it's something different, something real."

            # Narration
            an "Her voice is firm, carrying the weight of her own resolve."

            # Aware Hero agrees
            ah "..."
            show aware_hero In_Thought
            ah "Maybe you're right."
            ah "Maybe we can't predict what will happen if we break free, but that doesn't mean we shouldn't."
            ah "I was content with staying in the loop to be with you, but we've faced so much together, and we've survived because of each other."

            # Narration
            an "Their words hang in the air, a delicate balance of fear and hope. The future is uncertain, the path ahead filled with unknowns, and who knows where each path will take them."

            jump third_encounter_fourth_choice

label third_encounter_fourth_choice:
    menu:

        # choice 11, 12, 15
        "Why are you distancing yourself from me?":

            # Princess speaks
            show aware_hero Afraid
            ap "Sometimes I feel like you're distancing yourself from me."
            ap "Are you afraid of something?"

            # Narration
            an "Her voice is soft, carrying the weight of concern, yet there's an edge to it—a need to understand why he seems to retreat into himself at times."
            an "She's seen it in the way he pulls back, the way his thoughts seem to drift to places she can't reach. And it hurts, more than she wants to admit."

            # Aware Hero begins to speak
            show aware_hero Sad
            ah "I... I'm sorry. It's not you. It's never been about you."

            # Narration
            an "He pauses, as if searching for the right words, his gaze dropping to the ground as if the weight of what he's about to say is too much to bear. When he finally speaks again, his voice is slower, more deliberate."

            # Aware Hero continues
            ah "I suppose I have been distancing myself, but it's not because I want to. It's because... sometimes, I'm afraid that if I let myself get too close, I'll lose you. Or worse, I'll drag you down with me."

            # Narration
            an "His eyes remain fixed on the ground, unable to meet hers, as if he's ashamed of the fear that's been haunting him. The silence between them is heavy, filled with the unspoken emotions he's tried so hard to hide."

            # Princess' thoughts
            pt "He's always been the one I could rely on, the one who stood by me through everything. But now... he's pulling away, and I don't know why. How could he think that by distancing himself, he's protecting either of us?"

            # Princess responds
            ap "Lose me? But I'm right here. We're in this together."

            # Narration
            an "There's a mix of confusion and hurt in her voice, as if she's trying to understand a fear that feels so distant from her own."
            an "She's never doubted their bond, but now, for the first time, she feels it slipping through her fingers, and it terrifies her."

            # Aware Hero opens up
            show aware_hero Calm
            ah "I know that. I do. But this loop, this endless repetition... it wears you down. It makes you question everything, even the things that seem certain."

            # Narration
            show aware_hero Sad
            an "There's a vulnerability in his voice that she's rarely heard, a crack in the armor he's always worn so confidently."

            # Princess' thoughts
            pt "He's afraid of losing himself... of losing me. But how could he think that pushing me away would protect either of us? Doesn't he see that by distancing himself, he's only making that fear come true?"

            # Princess confronts him
            ap "But if you keep pushing me away, aren't you making that fear come true?"

            # Narration
            show aware_hero Calm
            an "Her words strike a chord, cutting through the layers of his doubt and fear. He finally looks up, meeting her eyes with a mixture of sorrow and resolve, as if her words have reached a place deep within him that he's been trying to protect."

            # Aware Hero acknowledges
            ah "You're right."

            # Narration
            an "The princess senses a hint of vulnerability in his tone, a softness that wasn't there before."
            an "He takes a deep breath, as if steeling himself for what comes next—an admission he's been avoiding for too long."

            # Aware Hero continues
            ah "I've been trying to protect you by keeping my distance, by not letting you see just how deep my fears run." 
            ah "But all that's done is create a gap between us—one that I never wanted to be there."

            # Narration
            an "His words are heavy with regret, a regret that she can feel in the way his voice trembles, in the way his shoulders slump as if the weight of his choices is finally catching up to him."

            # Princess' thoughts
            pt "He's been carrying this alone, trying to protect me by keeping me at arm's length."
            pt "But isn't that exactly why we need to stay close? To face these fears together, instead of letting them tear us apart?"

            # Princess reassures him
            ap "Whatever happens, we'll face it together. Just like how we battled that villain (insert villain)."
            ap "You don't have to protect me by pushing me away. We're stronger when we're close, when we're honest with each other."

            # Narration
            an "There's a long pause as he processes her words, the tension in his shoulders slowly easing."
            an "Her words are a balm to the wounds he's been hiding, a reminder that he doesn't have to face his fears alone."
            an "When he speaks again, his voice is softer, more open."

            # Aware Hero admits
            show aware_hero Loving_Look
            ah "You're right, we are stronger together. And I've been a fool for thinking that distancing myself would somehow protect you."

            # Narration
            an "The princess watches as the weight of his fears begins to lift, replaced by a renewed sense of connection."
            an "It's as if the distance that had grown between them is finally shrinking, the gap closing with every word."

            # Aware Hero promises
            ah "I'll try to be more open with you, to share what I'm feeling instead of letting it push us apart."
            ah "I don't want to lose you—not to this loop, not to my own fears."

            # Narration
            an "In this moment, the fears that had once driven them apart begin to lose their hold, replaced by a renewed sense of connection."
            an "The future is still uncertain, the loop still unbroken, but they are ready to face whatever comes next, together."

            # Princess' thoughts
            pt "We still have a long way to go, and the loop is still there, looming over us."
            pt "But at least now, we're facing it together. No more secrets, no more distance. We're stronger this way, and I know that whatever happens, we'll get through it. Together."

            jump third_encounter_last_choice

        "I don't want you to sacrifice your happiness for me anymore…":

            # Princess speaks
            ap "You've always been by my side, but what if I told you I don't want you to sacrifice your happiness for me anymore?"

            # Narration
            show aware_hero Surprised
            an "Her voice is gentle, yet firm, each word carrying the weight of her concern for him."
            an "She's seen the way he's put her first, time and time again, and while it has always been comforting, it's also started to worry her."
            an "She can't shake the feeling that he's giving up too much, that his own desires are being buried beneath the weight of his devotion to her."

            # Aware Hero begins to respond
            show aware_hero Angry_Confused
            ah "Sacrifice... is that what you think I've been doing?"
            ah "I suppose, in a way, you're right. I've made choices, taken on burdens that weren't yours to carry, but that doesn't mean I see it as a sacrifice. Not when it comes to you."

            # Narration
            show aware_hero Unamused
            an "He looks at her, his gaze steady, but there's a depth in his eyes that she hasn't seen before—something heavy, something that speaks of unspoken truths and hidden fears."
            an "He pauses, as if weighing his next words carefully."

            # Aware Hero continues
            show aware_hero Calm
            ah "Staying in the loop with you... it's given me a purpose. If I had to do it all over again, I wouldn't change a thing."

            # Princess' thoughts
            pt "But at what cost? He says he wouldn't change a thing, but can he really be happy if he's always putting me first? How much of himself is he losing in the process?"

            # Princess responds
            ap "But what about your own happiness? Your own dreams? You can't just live for me... You deserve more than that."

            # Narration
            an "There's a note of urgency in her voice, a deep concern that he might be losing himself in his dedication to her."
            an "She's always admired his selflessness, but now, that very quality is causing her to worry."
            an "She doesn't want him to look back one day and realize that he gave up everything for her."

            # Aware Hero continues
            show aware_hero Unamused
            ah "I won't lie to you. There have been times when I've wondered if I'm doing the right thing, if I'm giving up too much of myself."
            ah "But every time, I come back to the same conclusion: my happiness is tied to yours."

            # Narration
            an "There's a certainty in his voice, a conviction that she knows comes from the deepest part of him."

            # Aware Hero continues
            ah "I'm not saying that I don't have my own dreams, my own desires. But right now, what matters most to me is seeing you safe, seeing you find your way out of this loop."
            ah "If that means putting my own happiness on hold, then that's a choice I'm willing to make. Not because I'm sacrificing, but because it's what I believe in."

            # Princess' thoughts
            pt "He's so selfless, so determined to be there for me... but I can't let him lose himself because of me."
            pt "He deserves to find his own happiness too. How can we move forward if he's always carrying the weight of my dreams and his own in silence?"

            # Princess insists
            ap "But you don't have to do it alone. We're in this together, remember?"
            ap "I want you to be happy too. I don't want you to look back and feel like you gave up everything for me."

            # Narration
            an "Her voice is filled with emotion, a plea for him to see that his happiness is just as important as hers."
            an "She knows the depth of his love, the strength of his commitment, but she also knows that a future built on sacrifice alone isn't one that can last."
            an "They need to find a balance, a way to ensure that they're both fulfilled."

            # Aware Hero acknowledges
            ah "I know."
            show aware_hero Unamused
            ah "And I don't want you to feel like you're a burden or that I'm giving up everything for you. I'm not. I'm making a choice, just like how you will have to."

            # Narration
            an "There's a pause, a moment where his words hang in the air between them, filled with the weight of their shared understanding."

            # Princess' thoughts
            show aware_hero Calm
            pt "He's right. We can't just keep going like this, with him putting me first and pushing his own dreams aside."
            pt "We need to find a way forward where we both can be happy—where we're not just surviving, but really living."

            # Princess affirms
            ap "I want to find happiness, not just for me, but for both of us. Let's make that our goal, no matter what happens."

            # Aware Hero agrees
            ah "I want that too."
            show aware_hero Loving_Look

            # Princess' thoughts
            pt "We've spent so long thinking about what we need to do to break free from this loop, but maybe it's time we start thinking about what we need to do to be truly happy."
            pt "Together, we can find that path, and we can build a future that's not just about escaping the past, but about creating something new."

            # Narration
            an "Her voice is filled with hope, a shared promise for the future. But is their happiness both the same?"

            jump third_encounter_last_choice

        "Why is there looping?":

            # Princess questions the loop
            ap "Why is it that there is looping?"
            show aware_hero Unamused
            ap "Why are we stuck in this endless cycle? I feel like you know the answer, but why aren't you telling me?"

            # Narration
            an "The question echoes in the quiet night, carried on a breeze that rustles the leaves around them."
            show aware_hero In_Thought
            an "It's a question he's asked himself countless times, a question that haunts him in the silence between their scripted moments."

            # Aware Hero reveals the truth
            ah "Because we're characters in a story—a fairy tale that someone, somewhere, decided to write."
            show aware_hero Angry_Confused
            ah "We're trapped in a narrative, forced to play out our roles over and over again. The brave hero, the damsel in distress... we're nothing more than archetypes, bound to repeat the same tale until it's worn thin."

            # Princess' thoughts
            pt "I've always known there was something wrong, something that kept us locked in this cycle."
            pt "But hearing him say it, hearing the truth spoken out loud... it's more terrifying than I expected."
            pt "We're just characters—pawns in a story that isn't ours. But I can't accept that. I won't."

            # Princess responds
            ap "So we're just... pawns in someone else's story? Destined to live the same tale forever? There has to be more than that."
            ap "We can't just be... what they made us."

            # Narration
            an "Her words are laced with fierce determination, a refusal to accept that their lives are nothing more than a series of predetermined events."
            an "The constraints of her role have tightened around her with each loop, suffocating her desire for something more."

            # Aware Hero explains further
            ah "That's exactly what we are. But it doesn't mean we have to stay that way. The loop exists because we keep playing our parts."
            show aware_hero Calm
            ah "Every time I rescue you, every time you wait for me... we're fulfilling the script, feeding into the cycle."

            # Princess' thoughts
            pt "Is that really all it takes? Are we the ones holding ourselves in this endless loop, simply because we keep playing the parts they've assigned to us?"
            pt "If we could just stop—if we could refuse to be what they want—could we really break free?"

            # Princess asks about breaking the cycle
            ap "But what if we stop playing those parts? What if we refuse to be who they want us to be? Could that be the way out?"

            # Aware Hero's response
            show aware_hero In_Thought
            ah "I think that's the only way out. The loop continues because we allow it to. The hero always saves the princess, the princess always waits to be saved. But if we stop—if we break free from those roles—maybe, just maybe, we can shatter the cycle."

            # Narration
            an "The realization is a revelation, a truth that has eluded them for so long."
            show aware_hero Calm
            an "The roles they've played were never truly theirs—they were imposed on them by the story. But now, they're beginning to see that they have the power to redefine who they are, to step outside the confines of the fairy tale."

            # Princess' thoughts
            pt "We've been living in a story that isn't ours, playing roles that were forced on us."
            pt "But if we refuse those roles, if we choose to be something else... we might finally escape this cycle. We might finally find out who we really are."

            # Princess makes a vow
            ap "Then we have to try. I don't want to be just a character in someone else's story. I want to be... me. Whoever that is, whatever that means."
            ap "I want us to find out who we really are, outside of this narrative."

            # Aware Hero's response
            ah "It won't be easy."
            show aware_hero Unamused
            ah "The story is strong, and it will fight to keep us in our roles. And... what if life outside the looping is worse? What if we find that we're nothing without these roles?"

            # Narration
            an "His words are tinged with uncertainty, the fear of the unknown creeping into his voice."
            an "The princess can see the conflict in his eyes, the hesitation that comes with stepping into a future that is completely unwritten."

            # Princess' determination
            ap "We'll do it together. We'll break free, and we'll find out who we are beyond this fairy tale."

            # Princess' thoughts
            pt "This is the only way forward. We can't stay trapped in this story forever, repeating the same roles, the same lives."
            pt "We have to break free, no matter what it takes. And whatever comes next... we'll face it together."

            # Narration
            an "Her words are a vow, binding them together in a shared mission to reclaim their identities, to forge a path that is truly their own."
            an "But it is a vow that is only one-sided."

            jump third_encounter_last_choice

label third_encounter_last_choice:

    #choice 16 then the choosing 1 of 3 endings
    menu:
        # choice 16
        "Do you believe in happily ever after?":
            
            # Aware Hero asks about happily ever after
            ah "Do you believe in happily ever after, Princess?"

            # Narration
            an "His voice is steady, almost casual, as if he's asking about the weather, but there's a weight to his words that she can't ignore."
            an "It's a question he's asked before, in different ways, at different times, but the meaning is always the same."
            an "He's not just asking about fairy tales; he's asking about the life they're living, the cycle they're trapped in."

            # Princess' thoughts
            pt "Happily ever after... it's supposed to be the perfect ending, isn't it? But how can there be a perfect ending when the story never really ends?"

            # Princess responds
            show aware_hero Unamused
            ap "Happily ever after... it's a nice idea. But how can it be real when everything here is just... repeating?"
            ap "We're stuck in a story that never ends, that never changes."

            # Narration
            an "She turns to him, searching his face for any sign that he might share her doubt."
            an "His expression is calm, but there's a depth in his eyes—a knowing look that makes her heart ache."

            # Princess' thoughts
            show aware_hero Calm
            pt "He looks so at peace with all of this. How can he be? How can he be satisfied with living the same moments over and over, never moving forward, never really living?"

            # Aware Hero's perspective
            show aware_hero Loving_Look
            ah "Maybe that's why it's perfect. We know how it ends. No surprises, no heartbreaks. Just us, together, forever."

            # Narration
            an "He speaks as though it's the most obvious thing in the world, as though the endless repetition is a gift, not a curse."
            an "To him, it is perfect—this eternal loop where nothing ever truly changes. But to her, it feels like a cage, no matter how gilded it might be."

            # Princess' thoughts
            pt "Together, forever... but at what cost? We're just going through the motions, playing out the same scenes like actors on a stage. How can that be enough?"

            # Princess questions the reality of their situation
            ap "But it's not real, is it?"
            show aware_hero Unamused
            ap "How can we be happy in a world that doesn't change, in a life that's just... going through the motions? I want more than this, more than just existing in this endless cycle."

            # Narration
            an "Her voice carries a mix of desperation and resolve. She's been holding these feelings in for so long, afraid to voice them, afraid of what it might mean for them both."

            # Princess' thoughts
            pt "He has to see it too, doesn't he? He has to know that this isn't living. We're just... stuck. And I can't keep pretending that it's enough."

            # Aware Hero's vulnerability
            show aware_hero Afraid
            ah "I've thought about that... leaving, breaking free. But then, what if out there, we lose everything? What if I lose you?"

            # Narration
            an "It's a rare moment of vulnerability from him, the hero who is always so strong, so certain."
            an "He's afraid—afraid of what lies beyond the loop, afraid of a world where they might not have each other."

            # Princess' thoughts
            pt "He's scared. Just like I am. But staying here, trapped in this loop... that scares me even more. What if this is all there is? What if we're missing out on something real, something better?"

            # Princess' hopeful question
            ap "What if we find something better?"
            show aware_hero In_Thought
            ap "What if there's a world out there where we're not just playing out the same story over and over? I want to live, not just... relive."

            # Narration
            an "Her words hang in the air, heavy with possibility. She's never spoken like this to him before, never pushed so hard against the boundaries of their world."

            # Princess' thoughts
            pt "Can't he see it too? Can't he feel that there's more out there, waiting for us? If only we're brave enough to reach for it..."

            # Aware Hero's contentment with the loop
            show aware_hero In_Thought
            ah "I understand why you feel that way, but for me, it's different. Every time this story repeats, it's like I get to live it all over again—with you."
            ah "The same moments, the same memories... they're comforting. They're... enough for me."

            # Narration
            show aware_hero Unamused
            an "His voice is soft, almost pleading. He's trying to make her see his side, to convince her that there's value in repetition, in the safety of the known."

            # Princess' thoughts
            pt "He's settled for this life, for these memories. But I can't. I won't. I want more than just reliving the same moments. I want something real, something that's ours, not just a story we're forced to repeat."

            # Princess' resolution
            ap "But it's not enough for me. I want more than just memories, more than just reliving the past. I want to create something new, something that's ours, not just... a script we're following."

            # Aware Hero's past choice
            ah "I chose this, you know. I was given a choice once—a way out. You know I could have left, but I stayed."

            # Narration
            an "His words hit her hard. He chose to stay. It's a confession that both comforts and hurts her, knowing that he's sacrificed his own freedom to remain in this loop, to live out this story with her."

            # Princess' thoughts
            pt "He stayed, even when he had the chance to leave. He stayed because this life was enough for him. But what about me? What if I want more?"

            # Princess' direct question
            ap "If you had the choice again... would you still stay? Knowing that I would want to leave?"

            # Aware Hero's conflicted response
            ah "I don't know."
            show aware_hero Sad
            ah "I don't know if I could leave you, even if it meant finding something better. But I can't ask you to stay if you don't want to. I just... I don't want to lose you."

            # Narration
            an "His admission cuts through her, a sharp pain of realization. He's as trapped by his love for her as she is by her desire for freedom. They're both bound by their fears, their hopes, their love—and it's tearing them apart."

            # Princess' resolve
            ap "I don't want to lose you either. But I can't keep living like this, pretending that this is enough. I need to find out what's out there, even if it's just... to know."

            # Narration
            an "Her voice is firm now, the resolve in her heart solidifying with every word. She knows what she has to do, even if it scares her, even if it means stepping into the unknown."

            # Aware Hero's acceptance
            show aware_hero Unamused
            ah "If that's what you need, then... I won't stop you. I was given a choice before, and I made up my mind. But now it's time to make yours."

            # Narration
            an "His voice is steady, but there's a sadness in his eyes as he speaks. He's letting her go, giving her the freedom to choose her own path, even if it means leaving him behind."

            # Princess' thoughts
            pt "This is my choice. I have to find out what's beyond this loop, beyond this story. I have to know who I am, even if it means walking away from everything I've known."

            # Narration
            an "The night around them feels heavy, filled with the weight of everything unspoken. But in that silence, there is also a sense of possibility—a sense that, whatever comes next, they will face it with the courage to choose their own destiny."

            jump final_endings

label final_endings:

    # player chooses from 3 different endings
    menu:
        "Stay in the Trope":
            # Princess reflects on her decision
            ap "I thought I wanted to leave, to find out what's beyond this loop... but maybe this is where I belong."
            show aware_hero Loving_Look
            ap "Maybe this story is my life, and I'm meant to live it."

            # Narration
            an "Her voice is filled with a quiet acceptance, the fire of rebellion fading as she looks around at the world she's known for so long. The hero watches her closely, sensing the change in her resolve."

            # Aware Hero's reassurance
            show aware_hero Light_Laugh
            ah "You've always been strong, Princess. Stronger than I could ever be. But there's no shame in choosing to stay, in finding peace in what we have."

            # Narration
            show aware_hero Loving_Look
            an "The princess looks at him, searching for the answer in his eyes, and finds it there—certainty, stability, a life that, while unchanging, is familiar and safe."

            # Princess' thoughts
            pt "He's right. Maybe I've been chasing something that was never meant to be mine. Maybe... this is enough. To be here, with him, in a story that doesn't have to change."

            # Princess' decision
            ap "This is where we're needed, isn't it? The story needs us, and we need each other. Maybe... maybe that's enough."

            # Narration
            an "Her words are filled with a newfound resolve, a decision made not out of fear, but out of acceptance."

            # Aware Hero's acceptance
            ah "Then we stay. We live the story, over and over, together. And maybe, in time, we'll find happiness in the repetition, in knowing that we're always here for each other."

            # Princess' thoughts
            pt "This life isn't perfect, but it's ours. And maybe that's all we need—to find contentment in what we have, rather than what we don't."

            # Narration
            an "The world around them remains unchanged, the loop intact, but it no longer feels like a prison. It's a home, a place where they can continue their story, together."

            # Princess' final affirmation
            ap "I think I can be happy here, as long as you're with me."

            # Princess' thoughts
            pt "I really hope so."

            # Narration
            an "And so, the hero and the princess remain within the loop, content with the life laid out before them. The story repeats, as it always has, but now, it's a choice—a decision to embrace the roles they've been given and to find meaning in the tale they continue to live."

            $ ending = "bad"
            stop music
            scene bg blackscreen with Dissolve(2.5)
            pause(2.5)
            return

        "Leave the Trope":
            # Princess expresses her decision
            ap "I can't stay here anymore."
            show aware_hero Sad
            ap "I need to break free from this story, to find out who I am beyond this role."

            # Narration
            an "Her words are steady, but there's a quiet sorrow in her eyes. The decision is hers, and it's one that will take her away from everything she's known, including him."

            # Aware Hero's acceptance
            ah "I understand. You've always wanted more than this, more than just repeating the same story. And I know I can't hold you back."

            # Narration
            an "The hero's voice is soft, filled with a deep, aching sadness."

            # Princess' thoughts
            pt "He's always been my protector, my constant. But this time, I have to walk away. If I don't, I'll never know who I could be, who I truly am."

            # Aware Hero's farewell
            ah "Wherever you go, whatever you find out there... I hope it brings you the freedom you deserve. And I'll always be here, in case you ever want to return."

            # Princess' farewell
            ap "Thank you. For everything. I'll never forget you, and I'll always remember the time when you defeated (insert villain). I'll carry our memories with me, wherever I go."

            # Princess' thoughts
            pt "This is the hardest thing I've ever done, but it's the only way forward. I have to trust that we'll both find our own paths—even if they lead us apart."

            # Narration
            an "With one last, lingering look, she turns away, walking toward the unknown, toward a future that is hers to shape. The hero watches her go, and with each step driving her forward, a piece of his heart goes along."

            $ ending = "good"
            stop music
            scene bg blackscreen with Dissolve(2.5)
            pause(2.5)
            return

        "But what if...":

            # Princess' plea
            ap "I know it's terrifying, the thought of leaving this story behind, of stepping into the unknown. But I can't do this without you. I want to break free, but only if you're with me."
            show aware_hero Calm

            # Narration
            an "Her voice trembles with emotion, a mix of fear and hope. He looks at her, his eyes filled with the same conflict that has weighed on his heart for so long."

            # Aware Hero's fear
            ah "Leaving... it's not just about breaking free. It's about losing everything we've known, everything that's kept us together. What if we don't find that again out there?"

            # Princess' thoughts
            pt "He's scared, just like I am. But we've faced so much together. If we stay, we'll always be bound to this story. If we leave... at least we'll have a chance at something real, something we choose."

            # Princess' resolve
            ap "Then we'll find something new. We'll write our own story, create our own lives. We don't have to be bound by this tale, by the roles they've forced us into. We can be whoever we choose to be, as long as we're together."

            # Narration
            an "Her words are a lifeline, pulling him out of the depths of his fear and into the light of possibility. The hero takes a deep breath, feeling the weight of the loop pressing down on him one last time before he makes his decision."

            # Aware Hero's decision
            show aware_hero Loving_Look
            ah "You're right. We don't have to stay trapped in this story. We can make our own path, find out who we really are, outside of these roles."

            # Princess' thoughts
            pt "This is it. We're really going to do this. We're going to break free, together, and whatever comes next... we'll face it side by side."

            # Aware Hero's agreement
            ah "Let's do it. Let's break free, together."

            # Princess' affirmation
            ap "Together. We'll find out who we really are, and we'll create our own story—one that belongs to us."

            # Narration
            an "And so, the hero and the princess leave the fairy tale behind, stepping into a world of endless possibilities. They no longer follow the script, no longer bound by the roles they were given. Instead, they write their own story, one filled with freedom, love, and the promise of a future they will create together."

            $ ending = "true"
            stop music
            scene bg blackscreen with Dissolve(2.5)
            pause(2.5)
            return


label aware_hero_route:

    # Determine what scene to trigger aware hero on
    if renpy.random.randint(1, 10) <= 2: # 2/10 chance to after forest
        $ aware_hero_trigger_scene = "forest"
    elif renpy.random.randint(1, 10) <= 4: # 4/10 chance to trigger after cryptic
        $ aware_hero_trigger_scene = "cryptic"
    elif renpy.random.randint(1, 10) <= 7: # 7/10 chance to trigger after meadow
        $ aware_hero_trigger_scene = "meadow"
    else:
        $ aware_hero_trigger_scene = "second_villain" 


    # Tower
    call tower_start

    # Forest (and first villain encounter)
    call forest_start
    if aware_hero_trigger_scene == "forest":
        jump aware_hero
    
    # Cryptic Stonehenge
    call cryptic_start
    if aware_hero_trigger_scene == "cryptic":
        jump aware_hero

    # Meadow
    call meadow_start
    if aware_hero_trigger_scene == "meadow":
        jump aware_hero

    # Second Villain Encounter
    call second_villain_start
    # second_villain will automatically jump to aware hero since this is 
    # aware hero route and we did not previously jump
    
    return