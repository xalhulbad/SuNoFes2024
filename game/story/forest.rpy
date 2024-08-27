# Contains the code associated with portion of the game related to the "forest" scene,
# as well as the first villain encounter.

# Default variables
default forest_choices1_seen = set()
default forest_choices1_chosen = 0

# Flags for unlockable options
default forest_asked_who_are_you = False
default forest_asked_why_did_you_come = False
default forest_asked_is_it_safe = False
default forest_asked_have_we_done_this = False
default forest_asked_why_familiar = False


label forest_start:
    scene bg blackscreen with dissolve

    "{i}{color=#808080}Rap rap rap.{/i}{/color}"

    n "The sound echoed through the stone walls of the tower. The door creaked open, revealing the hero's warm smile."
    h "Princess, it's time to leave. Come with me."
    n "The princess, heart pounding, stepped forward. She took the hero's hand, feeling a comforting warmth."

    scene bg Forest1 with fade

    n "As they emerged out of the tower, sunlight bathed them. The sky was a brilliant blue, and the forest ahead was lush and green. Birds sang from the treetops, and a gentle breeze rustled the leaves."

    if routes_completed == 0: # First route
        p "It's so beautiful... I almost forgot what the world looks like."
    elif routes_completed == 1: # Second route
        pt "The same morning, the same hero, the same scene."
        pt "What's going on? It's like the story has just replayed itself."
    else: # Any route after the second
        p "Ah, the forest. It really is beautiful."
        pt "But with beauty comes pains. The pain of being trapped."
        pt "When will this end?"

    h "Let's go. The world is waiting for your return!"
    n "Hand in hand, they stepped into the clearing, ready to face the forest and their journey ahead."

    $ forest_choices1_chosen = 0

    label forest_choices1:
        while forest_choices1_chosen < 2:
            $ forest_choices1_chosen += 1

            menu:
                set forest_choices1_seen
                # Tells renpy to hide choices in this set (prevents same option showing up twice)

                # Choices available from the start:
                "(Act) Who are you?":
                    call forest_who_are_you
                    $ forest_asked_who_are_you = True
                    jump forest_choices1

                "(Act) What is your quest?" if forest_asked_who_are_you:
                    call forest_what_is_your_quest
                    jump forest_choices1
                
                "(Act) Why did you come to rescue me?":
                    call forest_why_did_you_come
                    $ forest_asked_why_did_you_come = True
                    jump forest_choices1

                "(Act) How long have I been trapped?" if forest_asked_why_did_you_come:
                    call forest_how_long_trapped
                    jump forest_choices1

                "(Act) Is it safe outside the tower?":
                    call forest_is_it_safe
                    $ forest_asked_is_it_safe = True
                    jump forest_choices1

                "(Act) Where are we headed now?" if forest_asked_is_it_safe:
                    call forest_where_are_we_headed
                    jump forest_choices1

                "(Act) Proceed into the forest": # Progresses the game
                    $ forest_choices1_seen.remove("(Act) Proceed into the forest") 
                    # renpy automatically adds this to seen set which we don't want here

                    jump forest_proceed_into_forest

                
                # Choices available after first route completed:
                "​​(Act) Have we done this before?" if routes_completed > 0:
                    call forest_have_we_done_this
                    $ forest_asked_have_we_done_this = True
                    jump forest_choices1

                "(Act) Why does this feel familiar?" if routes_completed > 0 and forest_asked_have_we_done_this:
                    call forest_why_familiar
                    $ forest_asked_why_familiar = True
                    jump forest_choices1

                "(Act) Can we change what happens next?" if routes_completed > 0 and forest_asked_why_familiar:
                    call forest_can_we_change
                    jump forest_choices1

                "(Act) Do you remember anything unusual?" if routes_completed > 0:
                    call forest_remember_unusual
                    jump forest_choices1


                # Choices available after second route completed:
                "(Act) How many times has this story replayed?" if routes_completed > 1:
                    call forest_how_many_times
                    jump forest_choices1


        # If we get here then the player did not choose "(Act) Proceed into the forest" within 2 choices

        h "We should probably get going now. If we linger here for too long, we might run into whatever had you trapped in the tower."

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
        p "It sure has. It couldn't have been that long, but my memory is failing me. Doesn't matter, I'm so glad you're here."
        return

    label forest_where_are_we_headed:
        h "I thought we could go back to the kingdom through the forest. It's beautiful and safe, I think."
        p "It's probably the better path back to the kingdom. Do you know your way?"
        h "Not really. Ha... I really should though, shouldn't I?"
        h "We can discover it together."
        return

    label forest_why_did_you_come:
        h "I couldn't bear the thought of you being alone. It felt like my heart led me here."
        p "Your heart is very brave. Do you always follow it so faithfully?"
        h "I try to. It has not led me wrong yet."
        return

    label forest_is_it_safe:
        h "I believe it is, especially if we're together. I'll do my best to keep us safe."
        p "That's comforting. Is there anything we should watch out for?"
        h "I've heard there are wild animals, but we can be careful. Let's just try not to run into whatever locked you up."
        h "One step at a time."
        return

    label forest_what_is_your_quest:
        h "My quest? To see you free and happy, I suppose."
        h "Such a simple yet noble quest. What will you do once I am free?"
        h "I haven't thought that far ahead. For now, let's just focus on getting you out of here."
        return

    label forest_proceed_into_forest:
        n "The princess and the hero stepped forward in the forest, but something was off. A bad omen. An eerie silence enveloped them."
        scene bg Forest2 with fade
        n "A tree branch cracked under the foot of the Princess. A flock of birds scattered from the canopy above at the sudden noise."
        n "The hero narrowed his eyes and scanned his surroundings. His hand drifted towards the numerous weapons he had equipped."
        n "Suddenly, a shadowy figure emerged from the darkness, cloaked in a tattered robe."
        scene bg Forest2_far_shadowy with dissolve
        n "Their face was hidden, and their voice was a muffled hiss that sent shivers down the princess's spine."
        v "So, the princess dares to leave her tower. How brave... or foolish."
        n "The pair's eyes locked on to the figure."

        if routes_completed == 0:
            pt "Who is this? Their presence feels... menacing."
            pt "Is this the one responsible for my captivity? Maybe I can get some answers."
            p "Who are you? Why are you hiding in the shadows?"
        elif routes_completed == 1:
            pt "This figure once again. Looks like this hasn't changed either."
            p "You. We meet again."
            n "The hero glanced at the princess with a concerned look."
        else:
            pt "Let's get this over with."
        
        scene bg Forest2_hero_front_facing_far_shadowy with dissolve
        n "The figure stepped closer, their movements almost ethereal. The hero instinctively placed himself between the princess and the stranger."
        h "Stay back! We mean no harm, but we will defend ourselves if necessary."
        v "How amusing. Be careful now."
        v "{b}Your choices matter.{/b}" #TODO: discuss if we should give this a special font/colour to have more significance

        jump villain_encounter # End of forest scene


    # Forest choices that are available only after first route completed:
    label forest_have_we_done_this:
        h "Um... what are you talking about? This is my first time meeting you."
        pt "The ignorance."
        p "Hm. Strange. I feel like I know you already."
        h "Maybe we were just meant to meet. Sometimes, things happen for a reason."
        return

    label forest_why_familiar:
        h "I'm not sure, but maybe it's a good thing. We can trust each other, right?"
        pt "Is this fate's cruel trick?"
        p "Yes, trust. It's something I haven't felt in a long time."
        h "Then let's build on that. We'll figure things out together."
        return

    label forest_can_we_change:
        h "I'm not too sure what you mean, but we will carve our own future. I'm here with you, whatever comes."
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
        p "No, I'm pretty sure we've met before, over and over."
        h "Maybe that's a sign. Maybe we're destined to help each other."
        return

    return

label villain_encounter:

    # level 1 of villain enounter
    menu:
        "(Act) Hide":
            n "The princess and the hero found a shadowy corner, crouching low and holding their breath as the figure approached, shrouded in darkness."
            scene bg blackscreen with dissolve
            p "Stay quiet. Let's see what we're dealing with."
            h "Agreed. Keep an eye on them."
            n "As the figure prowled closer, the princess and hero remained hidden, the tension thickening with each passing moment."
            jump villain1
        
        "(Act) Tell hero to brandish sword":
            n "The princess signaled the hero, who drew his sword with steely determination. The blade caught the light, gleaming ominously."
            scene bg Forest2_hero_sword_facing_far_shadowy with dissolve
            p "Be ready for anything. We don't know what they're capable of."
            h "Understood. I'll protect you."
            jump villain2

        "(Act) Tell hero to draw his bow with poisonous arrows":
            n "With a nod from the princess, the hero pulled an arrow tipped with a deadly poison from his quiver, drawing his bowstring back."
            scene bg Forest2_hero_bow_aiming_far_shadowy with dissolve
            p "With this distance, this might be our best chance. Prepare to shoot."
            jump villain3

        "(Act) Try to reason with the figure":
            n "The princess spoke in a gesture of peace, her voice calm but firm."
            p "Wait! We don't have to fight. Let's talk this through."
            h "Careful, princess. They may not be willing to listen."
            n "The figure eerily stood there. Intentions unclear. Gaze stern and unfazed."
            jump villain4


    # level 2 of villain encounter
    label villain1:
        menu:
            "(Act) Remain hidden and observe":
                n "The pair huddled deeper into the shadows, watching the figure's every move with keen eyes."
                p "Let's see what they're up to. We need to gather more information."
                h "Right. Stay quiet and alert."
                n "The figure paced back and forth, muttering incoherently. Occasionally, they glanced around but didn't seem to notice the pair hidden nearby."
                n "Were they insane? Frustrated? Angry?"
                jump villain1_1

            "(Act) Step out and confront the figure":
                n "The princess and hero stepped out from their hiding spot, determination etched on her face as she confronted the figure."
                scene bg Forest2_far_shadowy
                p "Face us! Who are you?"
                h "Careful now."
                n "The figure's eye flicked towards the princess, a sinister smile spreading across their shadowed face as they stepped closer, clearly unfazed."
                jump villain1_2

    label villain2:
        menu:
            "(Act) Charge at the figure":
                n "The princess and hero saw an opportunity to take on the shadowy figure head-on. The hero gripped his sword tightly, nerves meeting adrenaline."
                scene bg Forest2_hero_charging_far_shadowy
                n "The hero charged, sword pointed sternly ahead, poised to overcome anything that stands in the way. Princess trailing tightly behind."
                n "But to their dismay, the figure was far more nimble than anticipated, Swiftly dodging the hero's attack, and knocking the sword out of his hand."
                n "Stumbled, the hero was left defenceless. He quickly retreated back to the princess."
                scene bg Forest2_hero_facing_far_shadowy
                jump villain2_1

            "(Act) Demand the figure for answers":
                p "We won't move until you tell us what you're doing here!"
                n "The figure sneered, seeming to enjoy the tension. But they remained silent, eyes filled with malice."
                jump villain4_2

            "(Act) Retreat to a safer distance":
                n "The princess and hero retreated to a safer distance, slowly backing up, sword poised and prepared for any sudden movements."
                scene bg Forest2_very_far_shadowy
                n "Holding their new position, they assessed their situation, the distance somewhat calming their nerves."
                jump villain2_3

    label villain3:
        menu:
            "(Act) Shoot an arrow to wound the figure":
                n "The hero released the arrow, watching as it narrowly missed the figure's arm."
                h "These arrows should slow them down."
                scene bg Forest2_hero_facing_far_shadowy
                jump villain3_1

            "(Act) Keep the bow drawn and demand answers":
                n "The hero kept his bow drawn, eyes locked on the figure as the tension thickened."
                h "We need answers. Why are you following us?"
                h "We will not hesitate to shoot. You will regret it."
                n "The figure remained silent. Unfazed. Was it not afraid?"
                jump villain3_2

    label villain4:
        menu:
            "(Act) Appeal to what the figure wants":
                n "The princess relaxes her demeanor, her voice steady and calm."
                p "What do you want from us? There's no need for violence."
                n "The figure paused, considering her words, but their eyes remained wary and distrustful."
                jump villain4_1

            "(Act) Demand the figure for answers":
                n "The princess firmly stood her ground, her demeanor changing at the figure's unwillingness to cooperate."
                n "Her voice ringed out with authority as she confronted the figure directly."
                p "Who are you and why are you watching us? We. Deserve. Answers."
                n "The figure shifted in his spot, agitation building. Perhaps this was not the right decision, but the princess, determined, pushed aside any doubts."
                n "The tension in the air was discomforting."
                jump villain4_2

    # level 3 of villain encounter

    label villain1_1:
        menu:
            "(Act) Step out and confront the figure":
                scene bg Forest2_far_shadowy
                n "After observing for a moment, the princess stepped out of hiding, confronting the figure with courage."
                p "Enough hiding. Who are you, and what do you want?"
                n "The figure turned abruptly, eyes narrowing as they sized up the princess and hero. The tension in the air grew palpable."
                jump villain1_1_1

            "(Act) Make a surprise attack":
                n "The princess and hero exchanged a determined glance, their minds made up. With a nod, the hero drew his sword, and princess readied herself."
                p "Now! Let's catch them off guard."
                n "They leaped from their hiding spot, charging towards the figure with the elements of surprise on their side. But as they closed in, the figure's demeanor changed, a sly smile spreading across their face."
                scene bg Forest2_hero_charging_close_shadowy
                s "How predictable."
                n "In a fluid motion, the figure sidestepped the hero's strike, their movements almost too fast to follow. The hero stumbled, unbalanced by the sudden miss."
                h "What...?"
                scene bg Forest2_hero_facing_close_ff
                ff "Did you really think you could outmaneuver me? I've been watching you from the moment you entered the forest."
                n "The hero and princess regrouped, but their confidence wavered, the realization of the Femme Fatale's superiority sinking in."
                p "How...? We were so careful."
                ff "Your every move, your every whisper - it was all so transparent. You cannot hide your intentions from someone like me."
                n "The Femme Fatale's voice dripped with condescension, her presence overwhelming. She seemed to revel in their despair, the thrill of mental warfare evident in her eyes."
                ff "Your little surprise attack was amusing, but ultimately futile. Now, what will you do? Continue this charade, or flee like the cowards you are?"
                n "The hero's grip tightened on his sword, but the princess laid a hand on his arm, shaking her head." 
                p "We can't win this. Not like this."
                n "with their morale crushed and their resolve shaken, the princess and hero turned and fled into the depths of the forest, the Femme Fatale's laughter echoing behind them."
                scene bg Forest1
                ff "Run along now. But remember, the shadows of this forest are mine, and I will always be watching."
                n "As they ran, the weight of their failiure bore down on them. The encounter with the Femme Fatale had left a deep mark, her words a haunting reminder of their vulnerability."
                h "We need to regroup. Find a way to counter her."
                p "Yes, but for now, we must survive. We must be ready for the next time."
                n "The princess and hero pressed on, the path ahead fraught with danger and uncertainty, but their resolve to overcome grew ever stronger."
                $ v_type = "ff"
                return

            "(Act) Set a trap":
                n "The princess and hero silently nodded to each other, deciding to set a trap. The hero quickly rigged a snare, hiding it under a pile of leaves."
                p "This should catch them off guard. Let's see what happens."
                n "They retreated to their hiding spot, waiting with bated breath. The figure continued to mutter, oblivious to the trap set in his path."
                n "Suddenly, the figure stepped into the snare. The trap sprang, lifting him off his feet. But instead of panic, the figure's laughter echoed through the forest."
                s "You think this will stop me?"
                n "With a flick of his hand, dark energy surged, breaking the trap effortlessly. He landed gracefully, his eyes glowing with power."
                scene bg Forest2_close_dml
                p "Who are you?"
                n "The figure turned, revealing his true form. Cloaked in shadows, he radiated an aura of corrupt magic."
                dml "I am the Dark Magic Lord, the true ruler of this forest. Your pathetic trap is nothing compared to my power."
                n "The hero stepped forward, sword drawn."
                h "Your magic is destroying this forest. We won't let you continue."
                dml "Destroying? No, I am transforming it, making it a reflection of my greatness. You simpletons cannot comprehend my vision."
                n "The forest around them seemed to wither, the life drained by the dark magic emanating from the figure. The princess's heart ached at the sight."
                p "You're killing everything with your delusions!"
                dml "Silence! I am the hero this world needs, even if it cannot see it yet."
                n "With a wave of his hand, he summoned a surge of dark energy. The hero and princess barely managed to dodge the attack, the ground where they stood moments ago now charred and lifeless."
                scene bg Forest2_far_dml
                h "We need to retreat and find another way to stop him."
                n "As they fled deeper into the forest, the Dark Magic Lord's laughter echoed behind them, a haunting reminder of the power they faced."
                scene bg Forest1
                dml "Run, little mice. You cannot escape my domain."
                n "The princess and hero knew their journey had only just begun. They had seen the true face of their enemy, and the fight to save the forest would be more challenging than they had ever imagined."
                $ v_type = "dml"
                return

            "(Act) Remain hidden until the right moment":
                n "The princess and hero remained in their hiding spot, refusing to make the first move. The figure continued to pace, his muttering barely audible."
                h "Do you think he's alone?"
                p "I don't know, but we can't risk exposing ourselves yet."
                n "The forest grew eerily quiet, the only sounds being the figure's footsteps and occasional muttering. The pair strained their ears, trying to pick up any hint of another presence."
                n "They were so focused on the distant sounds that they failed to notice the silent figure moving closer."
                n "Suddenly, the faint twang of a bowstring behind them broke the silence. Instinctively, the hero raised his shield just in time to deflect an arrow aimed straight at his chest."
                h "Who was that?"
                n "They both turned, eyes wide with shock, realizing the figure had been much closer than they had thought. His presence, almost ghostly, had eluded them completely."
                scene bg Forest2_close_charging_hu
                n "The Hunter, silent and dealy, stepped into the faint light, his eyes cold and calculating. He held another arrow, ready to be notched."
                hu "You should have stayed hidden."
                n "The princess and hero exchanged a glance, realizing they were outclassed. The Hunter's senses were far beyond their own, his movements almost inhuman."
                p "We don't want to fight you."
                hu "It's not about what you want."
                n "Without another word, the Hunter released his arrow. The hero barely had time to raise his shield again, the impact driving him back a step."
                scene bg Forest2_hero_sword_facing_close_hu
                h "We need to move, now!"
                n "They scrambled to their feet, the Hunter's relentless pursuit keeping them on edge. His arrows flew with deadly precision."
                n "The hero and princess ducked behind a large tree, panting heavily. The Hunter's cold gaze never wavered, his presence like a looming shadow."
                n "Just as they thought they might have lost him, another arrow whizzed past, embedding itself in a tree inches from the princess."
                hu "You children have some fight in you. I respect that. I will let you go this time. But should we meet again, it will not be the same."
                n "With a final, stern look, the Hunter disappeared into the shadows, his voice echoing through the forest."
                hu "Remember, I will be watching. Trespassers in my forest shall receive no considerations."
                scene bg Forest1
                n "As the princess and hero fled, the weight of the Hunter's presence hung over them. They had survived the encounter, but the knowledge of his silent, deadly techniques would haunt them every step of their journey."
                $ v_type = "hu"
                return

    label villain1_2:
        menu:
            "(Act) Prepare for a fight":
                n "Anticipating a battle, the princess and hero braced themselves."
                p "Get ready. This might have been a mistake."
                n "The hero, silently nervous himself, steadies himself. A certain hear was present in his eyes, but it wasn't for him."
                n "The figure's expression darkened, the tension in the air reaching a climax."
                jump villain1_2_1

            "(Act) Try to negotiate":
                n "The princess took a deep breath, her voice steady as she tried to diffuse the tension."
                p "We got off on the wrong foot. Let's talk this out."
                n "The figure's smile widened, a flicker of recognition in his eyes. He stepped into the light, revealing weathered face scarred by betrayal and rage."
                scene bg Forest2_far_fh
                fh "Talk? With those who serve the kingdom that betrayed me? How amusing."
                n "The hero tightened his grip on his sword, sensing the danger in the figure's tone."
                h "We're not your enemies. Let's find a way to resolve this without bloodshed."
                n "The Fallen Hero's eyes flashed with anger, his hand gripping the hild of his blade."
                fh "Resolve? There is no resolution for the scars they left on me. You represent the kingdom that cast me aside, and for that, you will pay."
                n "The Fallen Hero drew his sword, the blade catching the light with a deadly gleam. The air grew thick with tension as he squared off against the hero."
                fh "Enough talk. Let's see if your blade can back up your words."
                n "With a swift, practiced motion, the Fallen Hero lunged at the hero, their swords clashing with a resounding clang. The hero parried the blow, their faces mere inches apart, locked in a deadly dance."
                scene bg Forest2_hero_close_charging_fh
                n "The princess watched in horror as the battle unfolded, the forest echoing with the sounds of their struggle."
                n "Despite the hero's skill, it was clear the Fallen Hero's experience and hatred gave him a fierce edge. He has practiced to perfection the technique of the kingdom knights."
                n "The hero fought valiantly, but the Fallen Hero's relentless attacks began to overwhelm him. With a powerful strike, the hero was knocked off balance, stumbling to the ground."
                n "The princess's heart pounded as she rushed to the hero's side, helping him to his feet. The Fallen Hero stood over them, eyes blazing with triumph."
                fh "This is your end."
                n "Gathering all their courage, the princess and hero made a desperate dash into the dense forest, branches and undergrowth tearing at their clothes as they fled."
                scene bg Forest1
                n "The Fallen Hero did not pursue, his bitter laugh echoing through the trees."
                fh "Run, cowards. But remember, the shadows of this forest will always be mine."
                n "As the princess and hero disappeared into the darkness, the sense of foreboding lingered, They had escaped, but the encounter with the Fallen Hero left a lasting mark on their souls, a reminder of the kingdom's dark past and the enemies it had created."
                $ v_type = "fh"
                return

    label villain2_1:
        menu:
            "(Act) Try to retrieve the sword":
                p "Get the sword! I'll cover you!"
                n "The hero dashed to retrieve his sword. A strike from the figure narrowly missed the hero thanks to the princess, distracting the figure with a fake strike."
                n "The hero picked up the sword, jumped back next to the princess, and tightened his grip, steeling himself for what was to come."
                scene bg Forest2_hero_sword_facing_far_shadowy
                jump villain2_1_1

            "(Act) Use the environment":
                p "Quick! To the trees!"
                n "The figure lunged for a strike at the defenceless hero, but just in time, the two ducked behind a nearby tree, using it as cover as they planned their next move."
                scene bg blackscreen
                n "The figure let out a frustrated grunt, and with building anger, slowly approached the tree."
                h "Shoot. What now?"
                jump villain2_1_2

    label villain2_3:
        menu:
            "(Act) Try to reason with the figure":
                p "We can talk from here. What do you want?"
                n "The figure's posture relaxed slightly, but their eyes remained suspicious and wary. Their confidence still filled the air."
                jump villain4

            "(Act) Look for an escape route":
                n "While keeping an eye on the figure, the princess and hero scanned their surroundings for an escape route. They consciously whispered to each other to not reveal their intentions."
                p "We need a way out of here. Look around."
                h "I see a path. We need to be ready to evacuate when we get a chance."
                n "They identified a narrow path through the trees that might lead to safety, but it would be a risky dash."
                jump villain2_3_2

    label villain3_1:
        menu:
            "(Act) Nock another arrow":
                n "The hero quickly nocked another arrow, eyes narrowing as he aimed. The figure staggered slightly but stood their ground, a growl escaping their lips."
                scene bg Forest2_hero_bow_aiming_far_shadowy
                p "Keep the pressure on. Don't give them a chance to recover."
                jump villain3_1_1

            "(Act) Switch to a different weapon":
                n "The hero slung his bow over his shoulder and drew his sword, stepping forward with determined eyes. The figure watched him warily, sensing the change in tactics."
                scene bg Forest2_hero_sword_facing_far_shadowy
                h "Time to finish this up close."
                jump villain3_1_2

    label villain3_2:
        menu:
            "(Act) Threaten to shoot":
                p "We have you in our sights. One more step and we'll release."
                n "The hero kept his bow steady, the arrow trained on the figure's heart. The figure sneered but hesitated, their confidence shaken slightly."
                h "Your move. Speak now or face the consequences."
                jump villain3_2_1

            "(Act) Let the arrow fly":
                n "The hero released the arrow."
                n "The projectile whipped through the air, making a sharp zipping sound, as it sliced through the air."
                n "{i}Thump.{/i}"
                n "It narrowly missed the figure, but it was clear that they were more cautious now."
                h "That should slow them down."
                jump villain3_1

    label villain4_1:
        menu:
            "(Act) Soothe them":
                n "The princess stepped closer, her tone soft and heartfelt."
                scene bg Forest2_close_shadowy
                p "Please, I can see the pain in your eyes. We're not here to hurt you. We all have our struggles. Let's find a way to understand each other."
                n "The figure's stance loosened slightly, the tension in their shoulders easing. They seemed torn, conflicted between aggression and the princess's calming presence."
                p "We're listening. Just tell us what you need."
                n "The figures hesitated, a flicker of vulnerability showing in their eyes as they considered the princess's sincere plea."
                n "They lower their weapon, opening themselves to hear the princess' words."
                jump villain4_1_1

            "(Act) Offer information":
                n "The princess spoke earnestly, hoping to build trust."
                p "We know things that could help you. Let us share what we know, and maybe we can assist each other."
                h "It's valuable knowledge. Hear us out."
                n "Unexpectedly, the figure's smirk widened, revealing a calculating gleam in their eyes. The posture relaxed, but it was a deceptive ease, like a predator toying with its prey."
                n "The figure stepped into the light, shifting the hood of the cloak to reveal an elegant woman donning an array of corrupt accessories."
                scene bg Forest2_far_ff
                ff "Information, you say? How delightful. But you see, I already know more about you than you realize. Your fears, your desires, your weaknesses. They are all laid bare before me."
                n "The figures's voice dripped with honeyed malice, each word a carefully crafted weapon aimed at their resolve. The air grew colder as shadows seemed to deepen around them."
                p "What... what do you mean?"
                n "The figure stepped closer, their presence overwhelming, as if they were enveloping the very light around them."
                scene bg Forest2_close_ff
                ff "You, dear princess, are an open book. Your thoughts, your heart - so easy to read. And you, brave hero, so predictable in your gallant efforts. You think you can bargain with me? How quaint."
                n "The princess and hero stood their ground, but the unease in their eyes betrayed their growing uncertainty. The figure's words cut deep, eroding their confidence."
                ff "But fear not. I have no interest in trinkets or knowledge you might offer. No, I revel in the game, the dance of shadows and secrets. And for now, I am satisfied with what I have seen."
                n "With a final, piercing gaze, the figure began to slink back into the darkness, their form dissolving into the inky blackness of the forest."
                scene bg Forest2
                s "Until we meet again, my dear pawns. Remember, the game has only just begun."
                n "As the figure vanished, the oppressive weight lifted, leaving the princess and hero standing in the eerie silence of the forest. The encounter had ended, but the unease lingered, a haunting reminder of the shadowy figure's words."
                h "What just happened? Who was that?"
                p "I don't know, but I have a feeling this isn't the last we've seen of them."
                n "With a shared look of resolve, the princess and hero knew their journey was far from over. The path ahead was fraught with danger and mystery, and the figure's ominous presence would be a constant shadow on their quest."
                $ v_type = "ff"
                return

    label villain4_2:
        menu:
            "(Act) Threaten the figure":
                n "The hero stepped forward, the blade in his hand gleaming menacingly. The figure's eyes narrowed, a low growl escaping their lips."
                scene bg Forest2_hero_sword_facing_far_shadowy
                h "Tell us who you are, or face the consequences."
                n "The figure sneered, unfazed by the threat, their eyes glinting with dark amusement."
                n "To their dismay, the figure's stance sharply shifted, readying for an imminent clash, their smirk widening as they accepted the challenge."
                jump villain4_2_1

            "(Act) Pressure the figure and look for a weakness":
                n "The princess and hero scanned the figure, searching for an opening. The figure's eyes sharpened, sensing their intent."
                h "Look for an opening. We cannot go down here."
                n "The figure stared cautiously at the princess and hero, unsure of what was to come."
                jump villain4_2_2

            "(Act) Bluff strength":
                n "The princess's voice was firm, projecting confidence. The figure's expression darkened, but a flicker of doubt crossed their eyes."
                p "We're stronger than you think. It's not worth the risk."
                n "The figure took a small step back. They seemed to have switched to taking a defensive approach to the situation."
                scene bg Forest2_very_far_shadowy
                jump villain4_2_3

    label villain1_1_1:
        menu:
            "(Act) Demand answers":
                n "The princess's voice rang out with authority as she demanded answers."
                p "Who are you? What do you want from us?"
                n "The air around them grew colder, an unsettling chill creeping into their bones. The figure's form began to shimmer and distort, revealing a ghostly, ethereal figure with eyes that burned with an unearthly fire."
                scene bg Forest2_far_vs
                vs "I am the reckoning for those who disturb the balance. You, who come from the kingdom of corruption, shall face my wrath."
                n "The spirit's voice echoed through the forest, each word dripping with ancient malice and vengeance. The hero stepped forward, trying to reason with the apparition."
                h "We're not your enemies. We can make amends. We seek to restore balance, not destroy it."
                n "The spirit's hollowlaugh resonated through the trees, a sound devoid of any warmth or forgiveness."
                vs "There are no amends for the dead. Only revenge. The forest has taken its toll on the wicked, and you will pay for the sins of your kingdom."
                n "The spirit's form flickered, the surrounding trees seeming to bend towards it, feeding off its dark energy. The princess's heart pounded, realizing the gravity of the situation."
                p "We seek to heal the forest, to undo the wrongs of the past. Let us help."
                n "The spirit's eyes flared brighter, its voice a whisper of rage and sorrow."
                vs "Help? You are but puppets of a corrupted kingdom. There is no help for the damned. Only the sweet release of vengeance."
                n "The ground beneath them began to tremble roots and vines twisting and writhing as they responded to the spirit's anger. The hero tightened his grip on his sword, readying himself for the inevitable."
                h "We need to move, princess. Theis spirit won't be reasoned with."
                n "As they took a step back, the spirit surged forward, its form growing larger and more menacing, shadows swirling around it."
                scene bg Forest2_close_charging_vs
                vs "Run if you must, but know this: the forest sees all, and it will have its revenge."
                n "With a final, haunting wail, the spirit vanished, leaving the forest in an eerie, oppressive silence. THe princess and hero exchanged a glance, their resolve hardening."
                scene bg Forest2
                h "This isn't over. We need to find a way to counter this spirit's power."
                p "Agreed. But we must be careful. The forest is more dangerous than we ever imagined."
                n "With the weight of the encounter heavy on their minds, the princess and hero pressed on, the path ahead fraught with uncertainty and danger, but their determination to restore balance and defeat the Vengeful Spirit never wavering."
                $ v_type = "vs"
                return

            "(Act) Challenge them to a duel":
                n "The princess's voice rang out with a clear challenge."
                p "Face us honorably, if you dare!"
                n "The figure's eyes narrowed further as he stepped into the light, revealing a scarred face filled with rage and sorrow. His hand moved to the hilt of his sword, his expression a mixture of bitterness and determination."
                scene bg Forest2_far_fh
                fh "Honor? From the likes of you? But very well, I accept your challenge."
                n "The hero stepped forward, drawing his sword and matching the figure's determined stance."
                h "We'll fight, but I won't let you harm her. I've heard the stories about you."
                n "The Fallen Hero's grip tightened on his blade, his eye flashing with old grudges and new resolve."
                fh "Then let the past be avenged with steel."
                n "With a swift, practiced motion, the Fallen Hero lunged at the hero, their swords clashing with a resounding clang. The hero parried the blow, their faces mere inches apart, locked in a deadly dance of blades." 
                scene bg Forest2_hero_sword_close_charging_fh
                n "The princess watched in horror as the battle unfolded, the forest echoing with the sounds of their struggle. Despite the hero's skill, it was clear the Fallen Hero's experience and hatred gave him a fierce edge." 
                n "The hero fought valiantly, but the Fallen Hero's relentless attacks began to overwhelm him. With a powerful strike, the hero was knocked off balance, stumbling to the ground." 
                scene bg Forest2_close_fh
                p "No! We have to find another way!" 
                n "The princess's heart pounded as she rushed to the hero's side, helping him to his feet. The Fallen Hero stood over them, eyes blazing with triumph and deep-seated anger." 
                fh "This is your end. You will pay for the kingdom's betrayal." 
                n "Gathering all their courage, the princess and hero made a desperate dash into the dense forest, branches and undergrowth tearing at their clothes as they fled. The Fallen Hero did not pursue, his bitter laugh echoing through the trees." 
                scene bg Forest1
                fh "Run, cowards. But remember, the shadows of this forest will always be mine." 
                n "As the princess and hero disappeared into the darkness, the sense of foreboding lingered. They had escaped, but the encounter with the Fallen Hero left a lasting mark on their souls, a reminder of the kingdom's dark past and the enemies it had created." 
                h "We need to regroup and find a way to counter him. This fight isn't over." 
                p "Agreed. But for now, we must survive. We must be ready for the next time." 
                n "With heavy hearts and newfound determination, the princess and hero pressed on, knowing that the road ahead would be filled with peril and the lingering presence of the Fallen Hero."
                $ v_type = "fh"
                return
    
    label villain1_2_1:
        menu:
            "(Act) Strike first":
                n "The hero made the first move, charging forward with his sword raised high. The princess followed closely behind, determination etched on her face." 
                scene bg Forest2_hero_charging_far_shadowy
                h "Now! We strike first!" 
                n "The figure's eyes gleamed with malevolent delight as the hero closed the distance. With a flick of his wrist, a dark, crackling energy began to form around his hands." 
                scene bg Forest2_hero_charging_far_dml
                dml "Fools. You dare to challenge me?" 
                n "The hero swung his sword, aiming for the figure's midsection, but the Dark Magic Lord moved with unnatural speed, deflecting the blow with a shield of dark magic." 
                scene bg Forest2_far_dml
                dml "You are nothing against my power. Witness the true ruler of this forest!" 
                n "The Dark Magic Lord turned his gaze to the princess, his eyes glowing with an eerie light." 
                dml "You cannot stop me. I am the hero this world needs, even if it cannot see it yet." 
                n "The forest around them seemed to wither, the life drained by the dark magic emanating from the figure. The princess's heart ached at the sight." 
                p "You're killing everything with your delusions!" 
                dml "Silence! I am the savior this world needs, even if it cannot see it yet." 
                n "With a wave of his hand, he summoned a surge of dark energy. The hero and princess barely managed to dodge the attack, the ground where they stood moments ago now charred and lifeless." 
                h "We need to retreat and find another way to stop him."
                scene bg Forest1
                n "As they fled deeper into the forest, the Dark Magic Lord's laughter echoed behind them, a haunting reminder of the power they faced." 
                dml "Run, little mice. You cannot escape my domain." 
                n "The princess and hero knew their journey had only just begun. They had seen the true face of their enemy, and the fight to save the forest would be more challenging than they had ever imagined."
                $ v_type = "dml"
                return

            "(Act) Defend and counter":
                n "The hero held his sword in a defensive stance, waiting for the figure to make the first move."
                scene bg Forest2_hero_sword_facing_far_shadowy 
                h "Stay behind me. We need to defend and counter." 
                n "The figure's eyes gleamed with a predatory light as he drew his weapon, a finely crafted bow. The Hunter emerged from the shadows, his movements silent and precise." 
                scene bg Forest2_hero_sword_facing_far_hu
                hu "Interesting. You choose to defend rather than attack. A wise choice, but will it save you?" 
                n "The Hunter notched an arrow with fluid grace, his eyes never leaving the hero. The forest seemed to hold its breath, the tension palpable." 
                p "We don't want to fight you. Just let us pass." 
                n "The Hunter's lips curled into a cold smile, but he did not lower his weapon." 
                hu "It's not about what you want. It's about the hunt."
                n "Without warning, the Hunter released the arrow. The hero's reflexes kicked in, and he raised his shield just in time, the arrow deflecting with a sharp clang." 
                h "Stay close, princess. We need to counter his moves."
                n "The princess, without a weapon of her own, borrowed the hero's dagger, holding it ready. The Hunter moved with inhuman speed, dodging her attempt to strike effortlessly. He returned fire, his arrows coming in quick succession." 
                n "The hero's shield deflected most of the arrows, but one grazed his arm, drawing a thin line of blood. He gritted his teeth, maintaining his focus." 
                hu "Impressive. But how long can you keep this up?" 
                n "The hero and the Hunter circled each other, their eyes locked in a deadly dance. The princess moved to the side, trying to find a better angle to support the hero." 
                p "We don't want this fight. Please, let us go." 
                hu "You cannot escape the hunt. But... you have earned my respect." 
                n "The Hunter lowered his bow slightly, his gaze calculating." 
                hu "I will let you go this time. But remember, the forest is my domain. Next time, you may not be so lucky." 
                n "With a final, stern look, the Hunter disappeared into the shadows, his voice echoing through the forest." 
                scene bg Forest2
                hu "Remember, I will be watching. Trespassers in my forest shall receive no consideration." 
                n "As the princess and hero fled, the weight of the Hunter's presence hung over them. They had survived the encounter, but the knowledge of his silent, deadly techniques would haunt them every step of their journey." 
                h "We need to regroup and plan our next move. This isn't over." 
                p "Agreed. We have to be ready for anything." 
                n "With determination in their hearts, the princess and hero pressed on, knowing that the forest held many more dangers and the Hunter would always be a shadow in their path."
                $ v_type = "hu"
                return

    label villain2_1_1:
        menu:
            "(Act) Distract the figure":
                n "The princess and hero exchanged a quick glance, knowing they needed to distract the figure to buy time." 
                p "We need to outsmart them. I'll create a diversion." 
                n "The princess moved to the side, drawing the figure's attention with a series of taunts." 
                p "Over here! You want me, right?" 
                n "The figure's eyes followed her, a wicked smile spreading across their face. The hero took the opportunity to reposition, his movements stealthy and precise." 
                scene bg Forest2_far_shadowy
                h "Stay focused. We need to be ready for anything." 
                n "The figure's demeanor changed, becoming more calculated and less aggressive. The Femme Fatale revealed herself, her presence exuding confidence and malice."
                scene bg Forest2_far_ff
                ff "Clever little princess, thinking you can outwit me. But I see through your every move."
                n "The princess felt a chill run down her spine as the Femme Fatale's eyes locked onto hers, filled with a predatory gleam." 
                p "Who are you?" 
                ff "I am the one who knows all your secrets, who reads your fears and desires like an open book. You thought you could distract me, but you're merely a pawn in my game." 
                n "The hero tightened his grip on his sword, feeling the weight of the Femme Fatale's words." 
                h "We're not here to play games. Let us pass." 
                ff "Oh, but where would the fun be in that? I relish in this dance of shadows and deceit." 
                n "The Femme Fatale's voice dripped with honeyed malice, each word a carefully crafted weapon aimed at their resolve. The air grew colder, the forest seeming to close in around them." 
                p "We're not afraid of you." 
                ff "Oh, but you should be. Your bravado is charming, but ultimately futile. I can see into your very souls, and I will break you from within." 
                n "With a graceful yet menacing movement, the Femme Fatale circled them, her eyes never leaving theirs." 
                ff "Run along now, little mice. But remember, the shadows are my domain, and I will always be watching." 
                n "With their morale crushed and their resolve shaken, the princess and hero turned and fled into the depths of the forest, the Femme Fatale's laughter echoing behind them." 
                scene bg Forest1
                ff "Until we meet again, my dear pawns. The game has only just begun." 
                n "As they ran, the weight of their failure bore down on them. The encounter with the Femme Fatale had left a deep mark, her words a haunting reminder of their vulnerability." 
                h "We need to regroup. Find a way to counter her." 
                p "Yes, but for now, we must survive. We must be ready for the next time." 
                n "The princess and hero pressed on, the path ahead fraught with danger and uncertainty, but their resolve to overcome grew ever stronger."
                $ v_type = "ff"
                return

            "(Act) Lure them into a trap":
                n "The princess and hero exchanged a quick glance, formulating a plan to lure the figure into a trap."
                p "We need to be smart about this. Let's draw them in."
                n "The hero nodded, moving to a strategic position while the princess readied herself."
                h "Follow my lead. We'll trap them together."
                n "The figure, unaware of their plan, advanced with a dark, menacing aura. The Dark Magic Lord reveled in his perceived superiority."
                scene bg Forest2_close_dml
                dml "Foolish children. Do you think your tricks can outmatch my power?"
                n "The hero feigned a retreat, drawing the Dark Magic Lord closer to the trap they had set earlier. The princess remained hidden, ready to spring the snare."
                p "Now!"
                n "As the figure stepped into the snare, the trap sprang to life, binding his legs with enchanted ropes. The Dark Magic Lord's laughter echoed through the forest, unfazed by the trap."
                scene bg blackscreen
                dml "You think this will hold me?"
                n "With a flick of his hand, dark energy surged, breaking the trap effortlessly. He landed gracefully, his eyes glowing with malevolent power."
                scene bg Forest2_close_dml
                p "Who are you?"
                dml "I am the Dark Magic Lord, the true ruler of this forest. Your pathetic trap is nothing compared to my power."
                n "The hero stepped forward, sword drawn."
                h "Your magic is destroying this forest. We won't let you continue."
                dml "Destroying? No, I am transforming it, making it a reflection of my greatness. You simpletons cannot comprehend my vision."
                p "You're killing everything with your delusions!"
                dml "Silence! I am the hero this world needs, even if it cannot see it yet."
                n "With a wave of his hand, he summoned a surge of dark energy. The hero and princess barely managed to dodge the attack, the ground where they stood moments ago now charred and lifeless."
                h "We need to retreat and find another way to stop him."
                n "As they fled deeper into the forest, the Dark Magic Lord's laughter echoed behind them, a haunting reminder of the power they faced."
                scene bg Forest1
                dml "Run, little mice. You cannot escape my domain."
                n "The princess and hero knew their journey had only just begun. They had seen the true face of their enemy, and the fight to save the forest would be more challenging than they had ever imagined."
                $ v_type = "dml"
                return

    label villain2_1_2:
        menu:
            "(Act) Ambush from above":
                n "The hero and princess silently climbed the trees, positioning themselves for an ambush. The figure, unaware, moved closer, searching for them."
                p "We'll strike from above. Be ready."
                n "The hero nodded, gripping his sword tightly. The Hunter, drawn by their tactical approach, watched with keen interest from a distance."
                hu "Clever. But not clever enough."
                n "The hero and princess launched their ambush, leaping down from the branches. The figure looked up just in time to see them descending upon him."
                h "Now!"
                n "Their attack was swift and coordinated, but the Hunter moved faster. In a blur, he intercepted their strike, parrying with his bow and knocking them off balance."
                hu "A worthy effort, but the forest is my domain."
                n "The princess and hero scrambled to their feet, their eyes widening as the Hunter revealed himself, his presence commanding and lethal."
                scene bg Forest2_hero_sword_facing_close_hu
                p "Who are you?"
                hu "I am the Hunter. You trespass in my forest, and now you will face the consequences."
                n "The Hunter's voice was cold, devoid of any mercy. He notched an arrow with fluid precision, aiming at the hero."
                h "We don't want to fight you. Let us go, and we'll leave your forest."
                hu "It is not that simple. The hunt must be completed."
                n "Without warning, the Hunter released the arrow. The hero raised his shield just in time, the impact driving him back a step. The Hunter notched another arrow, ready to continue the assault."
                p "We need to move. Now!"
                n "The hero and princess took off, weaving through the trees as the Hunter's arrows flew with deadly accuracy. Their hearts pounded as they evaded his relentless pursuit."
                scene bg Forest1
                n "As the princess and hero fled, the weight of the Hunter's presence hung over them. They had survived the encounter, but the knowledge of his silent, deadly techniques would haunt them every step of their journey."
                h "We need to regroup and plan our next move. This isn't over."
                p "Agreed. We have to be ready for anything."
                n "With determination in their hearts, the princess and hero pressed on, knowing that the forest held many more dangers and the Hunter would always be a shadow in their path."
                $ v_type = "hu"
                return
            "(Act) Use surroundings to escape":
                n "The princess and hero moved stealthily through the underbrush, using the dense foliage to mask their escape."
                p "We need to lose them in the forest. Keep moving."
                n "The hero nodded, staying close behind as they navigated the twisting paths and thick vegetation. The air grew colder, a sense of dread creeping into their hearts."
                n "Suddenly, the forest around them seemed to come alive, the trees twisting and turning, their branches reaching out like skeletal fingers."
                scene bg Forest2_far_vs
                vs "You think you can escape me?"
                n "The voice echoed through the trees, cold and haunting. The princess and hero looked around, their eyes wide with fear."
                h "What is this?"
                n "The ground beneath their feet began to shift, roots and vines writhing as if possessed. The Vengeful Spirit materialized before them, its form shimmering with dark energy."
                vs "The forest will not let you go. You will pay for the sins of your kingdom."
                p "We didn't mean to harm the forest. We're trying to help!"
                n "The spirit's eyes burned with unearthly fire, its anger palpable."
                vs "Help? Your kind only knows how to destroy. You cannot fool me."
                n "The princess and hero tried to move, but the roots and vines tightened around their ankles, holding them in place."
                h "We need to break free!"
                n "The hero swung his sword at the vines, but they were resilient, resisting his efforts. The spirit's form flickered, the forest responding to its rage."
                vs "You will not leave this place. The forest demands retribution."
                n "The princess's heart raced as she desperately looked for a way out. Her eyes fell on a small opening between the trees."
                p "There! We have to get through there!"
                n "With a renewed sense of urgency, the hero hacked at the vines, finally breaking them free. They sprinted towards the opening, the spirit's wail of fury echoing behind them."
                n "As they squeezed through the narrow gap, the forest seemed to close in around them, the spirit's presence looming like a dark cloud."
                vs "Run, but know this: you cannot escape the forest's wrath."
                scene bg Forest1
                n "They emerged on the other side, panting and shaken. The oppressive atmosphere lifted slightly, but the fear of the Vengeful Spirit lingered."
                h "We can't keep running. We need to find a way to stop that spirit."
                p "Agreed. But we need a plan. We need to understand what we're dealing with."
                n "With a shared look of determination, the princess and hero pressed on, their minds racing with the encounter's implications. The forest held many secrets, and the Vengeful Spirit was a formidable foe they would have to confront sooner or later."
                $ v_type = "vs"
                return

    label villain2_3_2:
        menu:
            "(Act) Run for the escape route":
                n "The princess and hero nodded at each other, steeling their resolve for a desperate dash towards the escape route."
                p "On three... one, two, three, go!"
                n "They sprinted towards the narrow path, the forest around them seeming to shift and twist in response. Just as they thought they were free, the ground beneath them erupted, roots and vines shooting up to block their path."
                vs "You cannot escape."
                n "The voice was cold and filled with malice. The Vengeful Spirit materialized before them, its ghostly form shimmering with dark energy."
                scene bg Forest2_far_vs
                vs "The forest demands retribution for your kingdom's sins."
                h "We didn't mean to harm the forest! We're trying to help!"
                n "The spirit's eyes burned with an unearthly fire, its presence oppressive and suffocating."
                vs "Your kind only knows destruction. You cannot fool me with your lies."
                n "The princess and hero tried to push through the barrier of roots and vines, but they were ensnared, the forest itself turning against them."
                p "We need to break free!"
                n "The hero swung his sword desperately, hacking at the vines, but they seemed to regenerate faster than he could cut them."
                vs "You will not leave this place. The forest will have its vengeance."
                n "The spirit surged forward, its ghostly hands reaching out. The hero and princess struggled, their movements becoming more frantic."
                scene bg Forest2_close_charging_vs
                p "We have to find another way!"
                n "With a final, desperate effort, the hero hacked at the vines once more, creating a small opening."
                h "Through here, quickly!"
                n "They squeezed through the gap, their hearts pounding. The spirit's wail of fury echoed behind them as they tumbled into a clearing, breathless and shaken."
                vs "Run, but know this: you cannot escape the forest's wrath."
                scene bg Forest1
                n "The oppressive atmosphere lifted slightly, but the fear of the Vengeful Spirit lingered."
                h "We can't keep running. We need to find a way to stop that spirit."
                p "Agreed. But we need a plan. We need to understand what we're dealing with."
                n "With a shared look of determination, the princess and hero pressed on, their minds racing with the encounter's implications. The forest held many secrets, and the Vengeful Spirit was a formidable foe they would have to confront sooner or later."
                $ v_type = "vs"
                return

            "(Act) Find hidden path":
                n "The princess and hero cautiously moved towards the hidden path, hoping to escape the looming threat."
                p "Stay low and follow me. I think there's a way through here."
                n "They moved stealthily, trying to make as little noise as possible. The forest seemed to watch them, every rustle of leaves amplifying their fear."
                n "Suddenly, an arrow embedded itself in the tree beside them, and the Hunter emerged from the shadows, his eyes sharp and calculating."
                scene bg Forest2_far_hu
                hu "You think you can hide from me in my own forest?"
                h "We're not here to cause trouble. We just want to leave."
                n "The Hunter's expression remained unreadable, his bow still drawn, an arrow aimed at the hero."
                hu "The forest has eyes everywhere. You cannot escape its gaze."
                n "The princess stepped forward, trying to defuse the situation."
                p "Please, we mean no harm. Let us go, and we won't come back."
                hu "Words are cheap. Prove your worth."
                n "The hero lowered his sword slightly, trying to show they were not a threat."
                h "We respect your territory. We just need safe passage."
                n "The Hunter studied them for a moment, then slowly lowered his bow."
                hu "Very well. But remember, the forest is my domain. Should you break your word, there will be no mercy next time."
                n "With a swift, almost imperceptible movement, the Hunter disappeared back into the shadows, his presence lingering like a dark omen."
                p "Let's move, quickly."
                n "The princess and hero continued their journey, the weight of the Hunter's gaze still heavy upon them. They knew they had been given a chance, but the forest held many more dangers, and the Hunter would always be watching."
                scene bg Forest1
                h "We need to be careful. The forest is full of unexpected allies and enemies."
                p "Agreed. Let's keep moving and stay vigilant."
                n "As they pressed on, the encounter with the Hunter stayed in their minds, a reminder that their path was fraught with peril and that they must tread carefully to survive."
                $ v_type = "hu"
                return
    
    label villain3_1_1:
        menu:
            "(Act) Aim for a disabling shot":
                n "The hero steadied his aim, focusing on a disabling shot to ensure the figure could not retaliate."
                p "Aim carefully. We need to disable them, not just wound."
                n "The hero's breath steadied, his focus sharp as he released the arrow with pinpoint precision. It struck the figure's leg, causing them to stagger."
                h "That should keep them from chasing us."
                n "The air grew still, the sound of the arrow hitting its mark echoing through the forest. The Hunter emerged from the shadows, his eyes gleaming with approval."
                scene bg Forest2_far_hu
                hu "Impressive. Your skill with the bow is commendable."
                n "The hero and princess turned to see the Hunter, his presence commanding and lethal."
                p "Who are you?"
                hu "I am the Hunter. This forest is my domain, and you have caught my interest with your precision."
                n "The Hunter approached, his bow at the ready, but his demeanor less hostile than before."
                hu "You have shown skill, but do you have the resolve to match it?"
                h "We don't want to fight you. We only want to stop them."
                hu "The forest has seen many intruders, but few with your skill. I will allow you to pass, but know this: the forest watches, and so do I."
                n "The Hunter's gaze was intense, his words carrying a weight that pressed upon their shoulders."
                p "Thank you. We will respect your territory."
                hu "See that you do. The next time we meet, I will not be so forgiving."
                n "With a final, piercing look, the Hunter disappeared back into the shadows, his presence lingering like a dark omen."
                scene bg Forest2
                h "Let's move, quickly."
                n "The princess and hero continued their journey, the weight of the Hunter's gaze still heavy upon them. They knew they had been given a chance, but the forest held many more dangers, and the Hunter would always be watching."
                p "We need to be careful. The forest is full of unexpected allies and enemies."
                h "Agreed. Let's keep moving and stay vigilant."
                n "As they pressed on, the encounter with the Hunter stayed in their minds, a reminder that their path was fraught with peril and that they must tread carefully to survive."
                $ v_type = "hu"
                return

            "(Act) Shoot to kill":
                n "The hero's eyes hardened with determination as he aimed for a lethal shot, hoping to end the threat once and for all."
                p "Finish this. We can't let them keep attacking us."
                n "The hero released the arrow, aiming for the figure's heart. The projectile flew true, but as it neared its target, the air around the figure shimmered with dark energy."
                scene bg Forest2_far_dml
                dml "You dare attempt to kill me?"
                n "The arrow stopped inches from the figure's chest, suspended in midair by an unseen force. The Dark Magic Lord raised a hand, and the arrow disintegrated into dust."
                dml "Your pitiful attempts are futile."
                n "The forest around them seemed to darken as the Dark Magic Lord's power surged. Shadows writhed and twisted, responding to his anger."
                h "We need to retreat. Now!"
                n "The hero grabbed the princess's hand, pulling her away as the Dark Magic Lord advanced, his eyes glowing with malevolent energy."
                dml "Run, little mice. Your struggle only makes your demise more entertaining."
                n "They ran away, the Dark Magic Lord's voice following them."
                dml "Remember, you cannot hide from me. My power is absolute."
                n "As they stumbled into a clearing, gasping for breath, the oppressive darkness lifted slightly, but the fear of the Dark Magic Lord lingered."
                scene bg Forest1
                h "We need to find a way to stop him. He's too powerful."
                p "Agreed. But we need a plan. We can't face him head-on like that again."
                n "With a shared look of determination, the princess and hero pressed on, knowing that their journey had become even more perilous. The Dark Magic Lord was a formidable enemy, and the fight to save the forest would be more challenging than they had ever imagined."
                $ v_type = "dml"
                return

    label villain3_1_2:
        menu:
            "(Act) Brandish sword":
                n "The hero brandished his sword, stepping forward with a determined gaze. The figure's eyes narrowed, recognizing the stance."
                scene bg Forest2_hero_sword_facing_far_shadowy
                h "This ends now. We won't let you harm anyone else."
                n "The figure's demeanor changed, their eyes flickering with a mix of recognition and anger."
                fh "So, the kingdom sends another pawn to face me. Very well, let us see if your blade is worthy."
                n "The Fallen Hero stepped into the light, revealing a scarred face etched with years of bitterness and rage. He drew his sword with practiced ease, the blade glinting menacingly."
                scene bg Forest2_hero_sword_facing_far_fh
                fh "I've been waiting for this. Let's see if you can match the skills of a true knight."
                n "The hero tightened his grip, readying himself for the duel. The princess watched anxiously, her heart pounding."
                p "Be careful. He's dangerous."
                h "I know. Stay back."
                n "The Fallen Hero lunged, their swords clashing with a resounding clang. The hero parried, their faces inches apart, locked in a deadly dance of blades."
                n "The forest echoed with the sounds of their struggle, each strike and counterstrike a testament to their skill and determination. Despite the hero's efforts, it was clear the Fallen Hero's experience and hatred gave him a fierce edge."
                n "With a powerful strike, the Fallen Hero knocked the hero off balance, sending him stumbling to the ground."
                fh "You are no match for me. The kingdom's betrayal runs too deep."
                n "The princess's heart raced as she rushed to the hero's side, helping him to his feet. The Fallen Hero stood over them, eyes blazing with triumph and deep-seated anger."
                fh "This is your end. You will pay for the kingdom's sins."
                n "Gathering all their courage, the princess and hero made a desperate dash into the dense forest, branches and undergrowth tearing at their clothes as they fled. The Fallen Hero did not pursue, his bitter laugh echoing through the trees."
                scene bg Forest1
                fh "Run, cowards. But remember, the shadows of this forest will always be mine."
                n "As the princess and hero disappeared into the darkness, the sense of foreboding lingered. They had escaped, but the encounter with the Fallen Hero left a lasting mark on their souls, a reminder of the kingdom's dark past and the enemies it had created."
                h "We need to regroup and find a way to counter him. This fight isn't over."
                p "Agreed. But for now, we must survive. We must be ready for the next time."
                n "With heavy hearts and newfound determination, the princess and hero pressed on, knowing that the road ahead would be filled with peril and the lingering presence of the Fallen Hero."
                $ v_type = "fh"
                return

            "(Act) Tackle the figure":
                n "The hero, seeing an opportunity, decided to close the distance with a bold move."
                h "Stay back. I'm going to take them down."
                n "The princess watched as the hero lunged forward, intending to tackle the figure to the ground. But as he made contact, the air around them grew icy, and the figure's form flickered like a dying flame."
                scene bg Forest2_hero_charging_close_shadowy
                vs "Foolish mortal. You dare challenge the very essence of the forest's wrath?"
                n "The hero's arms passed through the figure's now-translucent body, and he stumbled, falling to the ground. The Vengeful Spirit materialized fully, its ghostly form shimmering with dark energy."
                scene bg Forest2_far_vs
                vs "The forest remembers the sins of your kingdom. You will pay for the destruction you have wrought."
                p "What... what are you?"
                n "The spirit's eyes burned with an unearthly fire, its presence suffocating and oppressive."
                vs "I am the vengeance of the forest, the embodiment of its rage. Your kind will suffer for their greed."
                n "The hero scrambled to his feet, but the ground beneath him shifted, roots and vines wrapping around his ankles, holding him in place."
                h "We need to get out of here!"
                n "The princess rushed to the hero's side, desperately trying to free him from the entangling roots. The spirit advanced, its form growing more solid and menacing with each step."
                p "We didn't mean to harm the forest! We're trying to help!"
                vs "Lies! Your kind only knows how to take and destroy. The forest demands retribution."
                n "With a final, desperate effort, the hero broke free from the roots, pulling the princess along as they fled deeper into the forest. The spirit's wail of fury echoed behind them, a haunting reminder of its relentless pursuit."
                vs "Run, but know this: you cannot escape the forest's wrath. It will find you, and you will pay."
                n "They stumbled into a clearing, gasping for breath, the oppressive atmosphere lifting slightly but the fear of the Vengeful Spirit lingering."
                scene bg Forest1
                h "We need to find a way to stop that spirit. It's too powerful to face head-on."
                p "Agreed. But we need a plan. We need to understand what we're dealing with."
                n "With a shared look of determination, the princess and hero pressed on, knowing that the forest held many more dangers and that the Vengeful Spirit was a formidable foe they would have to confront sooner or later."
                $ v_type = "vs"
                return
    
    label villain3_2_1:
        menu:
            "(Act) Demand surrender":
                n "The hero's voice rang out with authority, demanding the figure's surrender."
                h "Drop your weapon and surrender now!"
                n "The air grew thick with tension as the figure's expression darkened, a malevolent smile spreading across his face."
                dml "You dare challenge me? The forest itself bends to my will."
                n "The Dark Magic Lord raised his hand, dark energy swirling around him as he summoned his power."
                scene bg Forest2_hero_charging_far_dml
                dml "You are nothing but pawns in my grand design. I am the true ruler of this forest."
                n "The hero kept his bow drawn, but the oppressive energy emanating from the Dark Magic Lord made it difficult to focus."
                p "We won't let you continue your tyranny. Surrender now, or face our wrath!"
                n "The Dark Magic Lord's laughter echoed through the forest, chilling them to the bone."
                dml "Foolish mortals. You think you can stand against me? I will show you the true power of darkness."
                n "With a wave of his hand, the Dark Magic Lord unleashed a surge of dark energy. The hero released his arrow, but it was deflected by the magical barrier surrounding the figure."
                n "The ground trembled as the dark energy spread, roots and vines writhing and twisting as they reached out to ensnare the princess and hero."
                h "We need to get out of here!"
                n "The hero grabbed the princess's hand, pulling her away as the Dark Magic Lord advanced, his eyes glowing with malevolent energy."
                dml "You cannot escape my wrath. The forest bends to my will."
                n "The hero swung his sword desperately, trying to cut through the roots. The Dark Magic Lord watched, his expression one of twisted amusement."
                dml "Run, little mice. Your struggle only makes your demise more entertaining."
                n "With a final, desperate effort, the hero hacked through the roots, creating a narrow gap. They squeezed through, the Dark Magic Lord's voice following them."
                dml "Remember, you cannot hide from me. My power is absolute."
                scene bg Forest1
                n "As they stumbled into a clearing, gasping for breath, the oppressive darkness lifted slightly, but the fear of the Dark Magic Lord lingered."
                h "We need to find a way to stop him. He's too powerful."
                p "Agreed. But we need a plan. We can't face him head-on like that again."
                n "With a shared look of determination, the princess and hero pressed on, knowing that their journey had become even more perilous. The Dark Magic Lord was a formidable enemy, and the fight to save the forest would be more challenging than they had ever imagined."
                $ v_type = "dml"
                return

            "(Act) Fire warning shot":
                n "The hero's hands were steady as he aimed his bow slightly off target and released an arrow, which flew past the figure's head and embedded itself in a tree behind."
                h "That was just a warning. Next one won't miss."
                n "The figure's eyes flickered with surprise, but they remained silent. From the shadows, a new presence made itself known, the Hunter emerging with a bow of his own."
                scene bg Forest2_far_hu
                hu "Interesting. You show restraint and skill."
                n "The Hunter moved with an almost ethereal grace, his eyes sharp and assessing."
                hu "Many would have aimed to kill. But you chose to assert dominance without bloodshed."
                p "We're not here to fight. We're trying to stop them."
                n "The Hunter's gaze flicked to the figure and then back to the hero, a nod of approval barely perceptible."
                hu "You have caught my interest. I respect those who value precision and control."
                n "The tension in the air shifted as the Hunter lowered his bow, his expression still stern but less hostile."
                h "We just want to pass through safely. Can you help us?"
                hu "I will let you pass, but know this: the forest is my domain. Should you betray its balance, you will answer to me."
                n "The princess and hero exchanged a glance, relief mingling with the weight of the Hunter's words."
                p "Thank you. We will respect your territory."
                hu "See that you do. And remember, I will be watching."
                n "With a final, piercing look, the Hunter disappeared back into the shadows, his presence lingering like a silent sentinel."
                scene bg Forest2
                h "Let's move, quickly."
                n "The princess and hero continued their journey, the weight of the Hunter's gaze still heavy upon them. They knew they had been given a chance, but the forest held many more dangers, and the Hunter would always be watching."
                p "We need to be careful. The forest is full of unexpected allies and enemies."
                h "Agreed. Let's keep moving and stay vigilant."
                n "As they pressed on, the encounter with the Hunter stayed in their minds, a reminder that their path was fraught with peril and that they must tread carefully to survive."
                $ v_type = "hu"
                return

    label villain4_1_1:
        menu:
            "(Act) Appeal to their past":
                n "The princess's voice was gentle, filled with empathy and understanding."
                p "I know you've been hurt, betrayed by those you once trusted. But not everyone is like them. We can help each other."
                n "The figure's eyes flickered with a mix of pain and nostalgia, their grip on their weapon loosening slightly."
                fh "You speak of things you do not understand. My past is filled with pain and betrayal, and trust is a luxury I can no longer afford."
                n "The hero stepped forward, his voice steady and respectful."
                scene bg Forest2_far_fh
                h "We've heard the stories about you. A knight betrayed by his own kingdom. We're not your enemies. We want to make things right."
                n "The Fallen Hero's expression softened for a moment, the weight of his past evident in his eyes."
                fh "Words are easy. Proving them is another matter."
                p "Let us prove it. We can start by listening, by understanding your story."
                n "The Fallen Hero hesitated, the conflict within him apparent. Finally, he lowered his sword, though his stance remained guarded."
                fh "Very well. But know this, trust is not given lightly, and betrayal is never forgotten."
                n "The tension in the air eased slightly as the princess and hero nodded, understanding the gravity of his words."
                p "We will earn your trust. One step at a time."
                n "With a final, wary glance, the Fallen Hero turned and disappeared into the forest, leaving the princess and hero to reflect on the encounter."
                scene bg Forest2
                h "We need to be careful. He may give us a chance, but his trust is fragile."
                p "Agreed. But it's a start. Let's move forward with caution and respect."
                n "As they continued their journey, the encounter with the Fallen Hero stayed with them, a reminder of the delicate balance of trust and the shadows of the past that still lingered."
                $ v_type = "fh"
                return
            
            "(Act) Appeal to their pride":
                n "The princess's voice was sincere, filled with a mix of respect and curiosity."
                p "You possess great power, power that can shape the very fabric of this forest. Surely, someone as remarkable as you has a greater purpose than this."
                n "The figure's eyes gleamed with pride, their stance shifting as they considered her words."
                dml "You recognize true greatness when you see it. Indeed, I am no ordinary being. I am the Dark Magic Lord, master of the arcane and ruler of this forest."
                scene bg Forest2_far_dml
                n "The hero stepped forward, his voice steady but cautious."
                h "We've heard of your abilities. Such power must have a profound purpose. What drives you to wield it?"
                n "The Dark Magic Lord's expression softened, a hint of vanity in his eyes as he relished the attention."
                dml "My purpose is to transform this forest into a realm of unmatched power and beauty, a testament to my greatness. The weak and unworthy will be purged, and only the strong will remain."
                p "But wouldn't true greatness come from protecting and nurturing the forest, rather than destroying it?"
                n "The Dark Magic Lord's eyes narrowed, a flicker of doubt crossing his face before his arrogance returned."
                dml "You speak of balance and harmony, concepts for the weak. True power lies in domination and control."
                h "Power without purpose can lead to ruin. We can work together to find a way to use your strength for the greater good."
                n "The Dark Magic Lord hesitated, the conflicting emotions evident in his eyes. For a moment, the forest seemed to hold its breath, awaiting his decision."
                dml "Perhaps there is some wisdom in your words. But know this: I will not be swayed easily. Prove your worth, and perhaps we can find common ground."
                n "The tension eased slightly as the princess and hero nodded, understanding the challenge ahead."
                p "We will prove ourselves. Together, we can create something truly remarkable."
                n "With a final, wary glance, the Dark Magic Lord turned and disappeared into the shadows, leaving the princess and hero to reflect on the encounter."
                scene bg Forest2
                h "We need to tread carefully. His power is immense, and his ego is fragile."
                p "Agreed. But if we can earn his trust, we might just find a way to save this forest."
                n "As they continued their journey, the encounter with the Dark Magic Lord stayed with them, a reminder of the delicate balance of power and the potential for redemption that lay within even the darkest of hearts."
                $ v_type = "dml"
                return

    label villain4_2_1:
        menu:
            "(Act) Intimidate with strength":
                n "The hero's voice was firm, his presence radiating strength and determination."
                h "This is your last chance. Tell us who you are, or face the consequences."
                n "The figure's eyes flickered with a mix of fear and defiance. Just as they were about to speak, an arrow whizzed through the air, embedding itself in the ground between them."
                hu "Enough."
                n "The Hunter stepped from the shadows, his bow drawn and another arrow ready. His eyes were cold and calculating."
                scene bg Forest2_far_hu
                hu "Strength and resolve are admirable, but intimidation has its limits. I am the Hunter, and this forest is under my protection."
                n "Without warning, the Hunter released the arrow. The hero raised his shield just in time, the impact driving him back a step. The Hunter notched another arrow, ready to continue the assault."
                p "We need to move. Now!"
                n "The hero and princess took off, weaving through the trees as the Hunter's arrows flew with deadly accuracy. Their hearts pounded as they evaded his relentless pursuit."
                scene bg Forest1
                n "As the princess and hero fled, the weight of the Hunter's presence hung over them. They had survived the encounter, but the knowledge of his silent, deadly techniques would haunt them every step of their journey."
                h "We need to regroup and plan our next move. This isn't over."
                p "Agreed. We have to be ready for anything."
                n "With determination in their hearts, the princess and hero pressed on, knowing that the forest held many more dangers and the Hunter would always be a shadow in their path."
                $ v_type = "hu"
                return

            "(Act) Bluff greater power":
                n "The hero's eyes glinted with a feigned confidence as he bluffed about their supposed power."
                h "You don't know who you're dealing with. We have forces beyond your understanding. Surrender, or face our true power."
                n "The figure's eyes widened momentarily, but they quickly masked their reaction with a sneer. From the shadows, a soft, mocking laugh echoed, and the Femme Fatale emerged, her movements fluid and graceful."
                scene bg Forest2_far_ff
                ff "Oh, how delightful. You think you can deceive me with your little bluff?"
                n "The air grew colder as the Femme Fatale approached, her presence commanding and unsettling."
                ff "You must understand, darling, I can see right through you. Your fears, your doubts—they are all so transparent."
                p "Who are you?"
                n "The Femme Fatale's smile widened, her eyes gleaming with malicious delight."
                ff "I am the Femme Fatale, the mistress of shadows and whispers. And you, my dear, are nothing more than pawns in my little game."
                n "The hero tightened his grip on his sword, but the princess laid a hand on his arm, sensing the danger of provoking her further."
                h "We won't fall for your tricks."
                ff "Tricks? Oh, sweetheart, this is merely the beginning. Your bravado is charming, but ultimately futile."
                n "The forest seemed to close in around them, the shadows growing longer and darker as the Femme Fatale's influence spread."
                p "What do you want from us?"
                ff "I want to see how far you'll go, how much you'll break before you realize the truth. This forest is mine, and you are merely passing through my web."
                n "The hero and princess exchanged a glance, their resolve tested but unbroken."
                h "We're not afraid of you."
                ff "Brave words, but we'll see how long they last."
                n "With a final, chilling laugh, the Femme Fatale melted back into the shadows, her presence lingering like a dark cloud."
                scene bg Forest2
                ff "Remember, I'll always be watching. And when you least expect it, I'll be there."
                n "The princess and hero stood in the eerie silence, the weight of the encounter pressing heavily on their shoulders."
                p "We need to stay strong. She feeds on our fear."
                h "Agreed. Let's keep moving and not let her get to us."
                n "As they pressed on, the encounter with the Femme Fatale stayed with them, a constant reminder of the psychological battles they would face in their journey through the forest. They knew they had to be vigilant and resilient to withstand her manipulations."
                $ v_type = "ff"
                return

    label villain4_2_2:
        menu:
            "(Act) Exploit their hesitation":
                n "The hero saw a moment of hesitation in the figure's eyes and took the chance to strike."
                h "Now, while they're off balance!"
                n "The hero lunged forward, aiming to exploit the figure's hesitation. But as his sword swung through the air, the figure's form wavered and flickered, revealing its true nature."
                vs "You dare to attack the embodiment of vengeance?"
                n "The air grew cold and heavy as the Vengeful Spirit fully materialized, its ghostly form radiating anger and malice."
                scene bg Forest2_far_vs
                p "What... what are you?"
                vs "I am the forest's fury, the amalgamation of its wrath against those who have wronged it. Your kingdom's sins have not been forgotten."
                n "The spirit's eyes burned with an unearthly light, its presence suffocating and oppressive. The hero's sword passed through its ethereal form, leaving him vulnerable."
                h "We need to get out of here!"
                n "The princess pulled the hero back, her heart racing as they faced the spirit's relentless anger."
                p "We didn't mean to harm the forest! We're trying to make things right!"
                vs "Words of repentance will not save you. The forest demands retribution."
                n "The ground trembled as roots and vines erupted, reaching out to ensnare the princess and hero. The spirit's fury was palpable, its form growing more menacing with each step."
                h "We can't fight this thing. We need to retreat!"
                n "The hero and princess turned to flee, but the spirit's vengeful wail echoed through the forest, shaking the very air around them."
                scene bg Forest1
                vs "Run, mortals! But know this: the forest's wrath is eternal. You will never escape its judgment."
                n "They stumbled through the dense undergrowth, the spirit's presence lingering like a dark cloud over their path."
                p "We need to find a way to appease the forest. This spirit won't stop until it has its vengeance."
                h "Agreed. But first, we need to regroup and figure out how to deal with it."
                n "As they fled deeper into the forest, the encounter with the Vengeful Spirit haunted them, a chilling reminder of the forest's fury and the dangers that lay ahead. They knew they had to find a way to calm the spirit's rage, or their journey would end in disaster."
                $ v_type = "vs"
                return
            
            "(Act) Use surroundings to gain advantage":
                n "The hero and princess quickly scanned their surroundings, searching for anything that could give them an advantage."
                p "Use the trees! We need to outmaneuver them!"
                n "The hero nodded, ducking behind a large tree as the princess darted in the opposite direction, attempting to confuse the figure. The figure's eyes glinted with amusement at their efforts."
                dml "Clever, but futile. You cannot hide from me."
                scene bg Forest2_far_dml
                n "The Dark Magic Lord raised his hands, dark energy crackling around him as he summoned his power. The forest seemed to shiver in response, the trees groaning as they were infused with dark magic."
                dml "I control the very essence of this forest. Your tricks are meaningless."
                n "The hero and princess continued to use the trees for cover, but the Dark Magic Lord's power was overwhelming. Shadows lengthened and twisted, reaching out like grasping hands."
                h "We need to find a way to break his concentration!"
                p "I'll distract him. You find an opening!"
                n "The princess stepped out from behind a tree, her voice ringing out with defiance."
                p "Is this all you can do? Show us your true power!"
                n "The Dark Magic Lord's eyes narrowed, his pride pricked by her challenge."
                dml "Very well. Witness the full extent of my might."
                n "As he focused his energy, the hero saw his chance. With a swift, silent movement, he closed the distance and struck at the Dark Magic Lord's exposed side."
                dml "Argh!"
                n "The attack disrupted the flow of dark energy, causing the shadows to waver. The hero and princess pressed their advantage, driving the Dark Magic Lord back."
                p "Keep pushing! We can do this!"
                n "But the Dark Magic Lord quickly recovered, his eyes burning with fury. He raised his hands once more, and a surge of dark energy erupted from the ground, forcing the hero and princess to retreat."
                dml "You are formidable, but you will not defeat me. This forest bends to my will, and you are merely insects in my grand design."
                scene bg Forest1
                n "The hero and princess regrouped, panting and worn, but their resolve unbroken."
                h "We need a new plan. He's too powerful to face directly."
                p "Agreed. We need to find a way to disrupt his control over the forest, but for now, we aren't prepared to take him on."
                n "As they ran, they heard a final, mocking laugh. The Dark Magic Lord disappeared into the shadows, his presence lingering like a dark cloud over their path."
                dml "Run, little mice. The forest is mine, and you will never escape my grasp."
                n "As they fled deeper into the forest, the encounter with the Dark Magic Lord haunted them, a chilling reminder of the power they faced and the dangers that lay ahead. They knew they had to find a way to break his hold over the forest, or their journey would end in disaster."
                $ v_type = "dml"
                return

    label villain4_2_3:
        menu:
            "(Act) Pretend you know how to use magic":
                n "The princess held out her hand, pretending to summon a powerful spell, her voice steady and commanding."
                p "We possess magic that can rival even the greatest sorcerers. Stand down, or face our wrath."
                n "The figure's eyes widened momentarily, but their expression quickly hardened with curiosity and skepticism. The air grew heavy with anticipation."
                dml "Magic, you say? Let us see this power you claim to wield."
                n "The Dark Magic Lord stepped forward, his presence radiating an aura of dark energy. His eyes gleamed with a mix of arrogance and intrigue."
                scene bg Forest2_dml
                dml "Show me your magic, and perhaps I will consider sparing you."
                n "The hero, sensing the bluff's potential danger, stepped closer to the princess, ready to protect her."
                h "Be careful. We can't underestimate him."
                p "Trust me. We have to keep up the act."
                n "The princess concentrated, her eyes locked with the Dark Magic Lord's. She willed herself to appear confident, her hand glowing faintly as she mimicked the gestures of casting a spell."
                dml "Interesting. But mere illusions will not suffice."
                n "The Dark Magic Lord raised his hand, and a swirl of dark energy formed in his palm. The forest around them seemed to wither, the air growing colder."
                dml "Allow me to demonstrate true power."
                n "With a flick of his wrist, the Dark Magic Lord unleashed a wave of dark energy. The princess and hero barely managed to dodge, the ground where they stood moments ago now charred and lifeless."
                p "Magic... it's real?"
                h "How is this possible? Magic is forbidden!"
                n "The Dark Magic Lord's eyes gleamed with amusement at their shock."
                dml "You fools. You thought you could bluff your way through? I am the master of this forbidden art. Your ignorance is laughable."
                n "The realization of their bluff's failure and the true danger they faced hit them hard. The hero's voice was filled with urgency."
                h "We need to retreat and find another way to stop him!"
                p "Agreed. We can't face him head-on like this."
                scene bg Forest1
                n "As they fled deeper into the forest, the Dark Magic Lord's laughter echoed behind them, a haunting reminder of the power they faced."
                dml "Run, little mice. You cannot escape my domain."
                n "The princess and hero knew their journey had only just begun. They had seen the true face of their enemy, and the fight to save the forest would be more challenging than they had ever imagined."
                h "We need a plan. Something that can counter his magic."
                p "We'll find a way. We have to."
                n "With determination in their hearts and the Dark Magic Lord's presence looming over them, the princess and hero pressed on, knowing that the road ahead would be fraught with peril."
                $ v_type = "dml"
                return

            "(Act) Pretend to have reinforcements":
                n "The princess straightened, her voice strong and unwavering."
                p "You think you can handle the two of us alone? Our reinforcements are just beyond the trees. Call off your threats, or you'll be overwhelmed."
                n "The figure's eyes narrowed, but a flicker of uncertainty crossed their face. The forest around them grew eerily quiet, the tension palpable. Suddenly, an arrow whizzed through the air, embedding itself in a nearby tree."
                hu "Enough deception. I see through your lies."
                n "The Hunter emerged from the shadows, his bow drawn and another arrow ready. His presence was commanding, his eyes cold and calculating."
                scene bg Forest2_far_hu
                hu "You thought you could fool me? The forest is my domain, and I know every movement within it."
                p "We're not here to fight. We're just trying to understand what's happening in this forest."
                n "The Hunter's gaze was unyielding, his focus entirely on the pair before him."
                hu "The forest does not forgive trespassers. You are lucky to still be breathing."
                h "We don't want any trouble. Just let us pass."
                n "The Hunter's expression remained stern, his grip on the bow unwavering."
                hu "I have no interest in your intentions. My mission is clear, and you are in my way."
                n "The hero and princess exchanged a tense glance, realizing the gravity of their situation."
                h "We need to move, now!"
                p "Agreed. Let's go!"
                n "As they turned to flee, the Hunter's voice followed them, chilling and relentless."
                hu "Run all you want. My arrows will find you."
                n "They stumbled through the dense foliage, hearts pounding, as the Hunter's relentless pursuit kept them on edge. His arrows flew with deadly precision, each one narrowly missing its mark."
                n "Finally, they managed to outrun the Hunter, reaching a small clearing."
                scene bg Forest1
                p "We should be safe here for now."
                h "We need to figure out a way to counter him. He's too powerful in his element."
                n "The encounter with the Hunter left them shaken but resolute. They knew they had to find a way to outsmart him if they were to survive the forest's many dangers."
                p "We'll find a way. Together."
                n "With determination in their hearts and the Hunter's presence looming over them, the princess and hero prepared for the next steps of their perilous journey."
                $ v_type = "hu"
                return
