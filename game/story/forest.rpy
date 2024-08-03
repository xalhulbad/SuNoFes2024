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
    scene bg blackscreen

    "{i}{color=#808080}Rap rap rap.{/i}{/color}"

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
                    $ forest_choices1_seen.add("(Act) Who are you?")
                    $ forest_asked_who_are_you = True
                    jump forest_choices1

                "(Act) What is your quest?" if forest_asked_who_are_you:
                    call forest_what_is_your_quest
                    $ forest_choices1_seen.add("(Act) What is your quest?")
                    jump forest_choices1
                
                "(Act) Why did you come to rescue me?":
                    call forest_why_did_you_come
                    $ forest_choices1_seen.add("(Act) Why did you come to rescue me?")
                    $ forest_asked_why_did_you_come = True
                    jump forest_choices1

                "(Act) How long have I been trapped?" if forest_asked_why_did_you_come:
                    call forest_how_long_trapped
                    $ forest_choices1_seen.add("(Act) How long have I been trapped?")
                    jump forest_choices1

                "(Act) Is it safe outside the tower?":
                    call forest_is_it_safe
                    $ forest_choices1_seen.add("(Act) Is it safe outside the tower?")
                    $ forest_asked_is_it_safe = True
                    jump forest_choices1

                "(Act) Where are we headed now?" if forest_asked_is_it_safe:
                    call forest_where_are_we_headed
                    $ forest_choices1_seen.add("(Act) Where are we headed now?")
                    jump forest_choices1

                "(Act) Proceed into the forest": # Progresses the game
                    $ forest_choices1_seen.remove("(Act) Proceed into the forest") 
                    # For some reason renpy adds this automatically which we don't want here

                    jump forest_proceed_into_forest

                
                # Choices available after first route completed:
                "​​(Act) Have we done this before?" if routes_completed > 0:
                    call forest_have_we_done_this
                    $ forest_choices1_seen.add("​​(Act) Have we done this before?")
                    $ forest_asked_have_we_done_this = True
                    jump forest_choices1

                "(Act) Why does this feel familiar?" if routes_completed > 0 and forest_asked_have_we_done_this:
                    call forest_why_familiar
                    $ forest_choices1_seen.add("(Act) Why does this feel familiar?")
                    $ forest_asked_why_familiar = True
                    jump forest_choices1

                "(Act) Can we change what happens next?" if routes_completed > 0 and forest_asked_why_familiar:
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

label villain_encounter:

    # level 1 of villain enounter
    menu:
        "(Act) Hide":
            n "The princess and the hero found a shadowy corner, crouching low and holding their breath as the figure approached, shrouded in darkness."
            p "Stay quiet. Let's see what we're dealing with."
            h "Agreed. Keep an eye on them."
            n "As the figure prowled closer, the princess and hero remained hidden, the tension thickening with each passing moment."
            jump villain1
        
        "(Act) Tell hero to brandish sword":
            n "The princess signaled the hero, who drew his sword with steely determination. The blade caught the light, gleaming ominously."
            p "Be ready for anything. We don't know what they're capable of."
            h "Understood. I'll protect you."
            jump villain2

        "(Act) Tell hero to draw his bow with poisonous arrows":
            n "With a nod from the princess, the hero pulled an arrow tipped with a deadly poison from his quiver, drawing his bowstring back."
            p "With this distance, this might be our best chance. Prepare to shoot."
            jump villain3

        "(Act) Try to reason with the figure":
            n "Stepping forward cautiously, the princess raises a hand in a gesture of peace, her voice calm but firm."
            p "Wait! We don't have to fight. Let's talk this through."
            h "Careful, princess. They may not be willing to listen."
            n "The figure eerily stands there. Intentions unclear. Gaze stern and unfazed."
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
                n "The princess stepped out from their hiding spot, determination etched on her face as she confronted the figure."
                p "Face us! Who are you?"
                h "Careful now."
                n "The figure's eye flicked towards the princess, a sinister smile spreading across their shadowed face as they stepped closer, clearly unfazed."
                jump villain1_2

    label villain2:
        menu:
            "(Act) Charge at the figure":
                n "The pair see an opportunity to take on the shadowy figure head-on. The hero grips his sword tightly, nerves meeting adrenaline."
                n "The hero charges, sword pointed sternly ahead, poised to overcome anything that stands in the way. Princess trailing tightly behind."
                n "But to their dismay, the figure was far more nimble than anticipated. Swiftly dodging the hero's attack, and knocking the sword out of his hand."
                n "Stumbled, the hero was left defenceless."
                jump villain2_1

            "(Act) Demand the figure for answers":
                p "We won't move until you tell us what you're doing here!"
                n "The figure sneered, seeming to enjoy the tension. But they remained silent, eyes filled with malice."
                jump villain4_2

            "(Act) Retreat to a safer distance":
                n "The princess and hero retreat to a safer distance, slowly backing up, sword poised and prepared for any sudden movements."
                n "Holding their new position, they assessed their situation, the distance somewhat calming their nerves."
                jump villain2_3

    label villain3:
        menu:
            "(Act) Shoot an arrow to wound the figure":
                n "The hero released the arrow, watching as it found its mark on the figure's arm. The figure hissed in pain, clutching the wound."
                h "That should slow them down."
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
                n "After observing for a moment, the princess stepped out of hiding, confronting the figure with courage."
                p "Enough hiding. Who are you, and what do you want?"
                n "The figure turned abruptly, eyes narrowing as they sized up the princess and hero. The tension in the air grew palpable."
                jump villain1_1_1

            "(Act) Make a surprise attack - Femme Fatale":
                n "The princess and hero exchanged a determined glance, their minds made up. With a nod, the hero drew his sword, and princess readied herself."
                p "Now! Let's catch them off guard."
                n "They leaped from their hiding spot, charging towards the figure with the elements of surprise on their side. But as they closed in, the figure's demeanor changed, a sly smile spreading across their face."
                s "How predictable."
                n "In a fluid motion, the figure sidestepped the hero's strike, their movements almost too fast to follow. The hero stumbled, unbalanced by the sudden miss."
                h "What...?"
                n "The Femme Fatale's eyes gleamed with a knowing light as she effortlessly parried the princess's sttempt to strike."
                ff "Did you really think you could outmaneuver me? I've been watching you from the moment you entered the forest."
                n "The hero and princess regrouped, but their confidence wavered, the realization of the Femme Fatale's superiority sinking in."
                p "How...? We were so careful."
                ff "Your every move, your every whisper - it was all so transparent. You cannot hide your intentions from someone like me."
                n "The Femme Fatale's voice dripped with condescension, her presence overwhelming. She seemed to revel in their despair, the thrill of mental warfare evident in her eyes."
                ff "Your little surprise attack was amusing, but ultimately futile. Now, what will you do? Continue this charade, or flee like the cowards you are?"
                n "The hero's grip tightened on his sword, but the princess laid a hand on his arm, shaking her head." 
                p "We can't win this. Not like this."
                n "with their morale crushed and their resolve shaken, the princess and hero turned and fled into the depths of the forest, the Femme Fatale's laughter echoing behind them."
                ff "Run along now. But remember, the shadows of this forest are mine, and I will always be watching."
                n "As they ran, the weight of their failiure bore down on them. The encounter with the Femme Fatale had left a deep mark, her words a haunting reminder of their vulnerability."
                h "We need to regroup. Find a way to counter her."
                p "Yes, but for now, we must survive. We must be ready for the next time."
                n "The princess and hero pressed on, the path ahead fraught with danger and uncertainty, but their resolve to overcome grew ever stronger."
                jump villain1_1_2

            "(Act) Set a trap - Dark Magic Lord":
                n "The princess and hero silently nodded to each other, deciding to set a trap. The hero quickly rigged a snare, hiding it under a pile of leaves."
                p "This should catch them off guard. Let's see what happens."
                n "They retreated to their hiding spot, waiting with bated breath. The figure continued to mutter, oblivious to the trap set in his path."
                n "Suddenly, the figure stepped into the snare. The trap sprang, lifting him off his feet. But instead of panic, the figure's laughter echoed through the forest."
                s "You think this will stop me?"
                n "With a flick of his hand, dark energy surged, breaking the trap effortlessly. He landed gracefully, his eyes glowing with power."
                p "Who are you?"
                n "The figure turned, revealing his tru form. Cloaked in shadows, he radiated an aura of corrupt magic."
                dml "I am the Dark Magic Lord, the true ruler of this forest. Your pathetic trap is nothing compared to my power."
                n "The hero stepped forward, sword drawn."
                h "Your magic is destroying this forest. We won't let you continue."
                dml "Destroying? No, I am transforming it, making it a reflection of my greatness. You simpletons cannot comprehend my vision."
                n "The forest around them seemed to wither, the life drained by the dark magic emanating from the figure. The princess's heart ached at the sight."
                p "You're killing everything with your delusions!"
                dml "Silence! I am the hero this world needs, even if it cannot see it yet."
                n "With a wave of his hand, he summoned a surge of dark energy. The hero and princess barely managed to dodge the attack, the ground where they stood moments ago now charred and lifeless."
                h "We need to retreat and find another way to stop him."
                n "As they fled deeper into the forest, the Dark Magic Lord's laughter echoed behind them, a haunting reminder of the power they faced."
                dml "Run, little mice. You cannot escape my domain."
                n "The princess and hero knew their journey had only just begun. They had seen the true face of their enemy, and the fight to save the forest would be more challenging than they had ever imagined."
                jump villain1_1_3

            "(Act) Keep hiding. You refuse to make the first move - Hunter":
                n "The princess and hero remained in their hiding spot, refusing to make the first move. The figure continued to pace, his muttering barely audible."
                h "Do you think he's alone?"
                p "I don't know, but we can't risk exposing ourselves yet."
                n "The forest grew eerily quiet, the only sounds being the figure's footsteps and occasional muttering. The pair strained their ears, trying to pick up any hint of another presence."
                n "They were so focused on the distant sounds that they failed to notice the silent figure moving closer."
                n "Suddenly, the faint twang of a bowstring behind them broke the silence. Instinctively, the hero raised his shield just in time to deflect an arrow aimed straight at his chest."
                h "Who was that?"
                n "They both turned, eyes wide with shock, realizing the figure had been much closer than they had thought. His presence, almost ghostly, had eluded them completely."
                n "The Hunter, silent and dealy, stepped into the faint light, his eyes cold and calculating. He held another arrow, ready to be notched."
                hu "You should have stayed hidden."
                n "The princess and hero exchanged a glance, realizing they were outclassed. The Hunter's senses were far beyond their own, his movements almost inhuman."
                p "We don't want to fight you."
                hu "It's not about what you want."
                n "Without another word, the Hunter released his arrow. The hero barely had time to raise his shield again, the impact driving him back a step."
                h "We need to move, now!"
                n "They scrambled to their feet, the Hunter's relentless pursuit keeping them on edge. His arrows flew with deadly precision."
                n "The hero and princess ducked behind a large tree, panting heavily. The Hunter's cold gaze never wavered, his presence like a looming shadow."
                n "Just as they thought they might have lost him, another arrow whizzed past, embedding itself in a tree inches from the princess."
                hu "You children have some fight in you. I respect that. I will let you go this time. But should we meet again, it will not be the same."
                n "With a final, stern look, the Hunter disappeared into the shadows, his voice echoing through the forest."
                hu "Remember, I will be watching. Trespassers in my forest shall receive no considerations."
                n "As the princess and hero fled, the weight of the Hunter's presence hung over them. They had survived the encounter, but the knowledge of his silent, deadly techniques would haunt them every step of their journey."
                jump villain1_1_4

    label villain1_2:
        menu:
            "(Act) Prepare for a fight":
                n "Anticipating a battle, the princess and hero braced themselves, weapons at the ready."
                p "Get ready. This might have been a mistake."
                n "The hero, silently nervous himself, steadies himself. A certain hear was present in his eyes, but it wasn't for him."
                n "The figure's expression darkened as they pulled out a weapon of their own, the tension in the air reaching a climax."
                jump villain1_2_1

            "(Act) Try to negotiate - Fallen Hero":
                n "The princess took a deep breath, her voice steady as she tried to diffuse the tension."
                p "We got off on the wrong foot. Let's talk this out."
                n "The figure's smile widened, a flicker of recognition in his eyes. He stepped into the light, revealing weathered face scarred by betrayal and rage."
                fh "Talk? With those who serve the kingdom that betrayed me? How amusing."
                n "The hero tightened his grip on his sword, sensing the danger in the figure's tone."
                h "We're not your enemies. Let's find a way to resolve this without bloodshed."
                n "The Fallen Hero's eyes flashed with anger, his hand gripping the hild of his blade."
                fh "Resolve? There is no resolution for the scars they left on me. You represent the kingdom that cast me aside, and for that, you will pay."
                n "The Fallen Hero drew his sword, the blade catching the light with a deadly gleam. The air grew thick with tension as he squared off against the hero."
                fh "Enough talk. Let's see if your blade can back up your words."
                n "With a swift, practiced motion, the Fallen Hero lunged at the hero, their swords clashing with a resounding clang. The hero parried the blow, their faces mere inches apart, locked in a deadly dance."
                n "The princess watched in horror as the battle unfolded, the forest echoing with the sounds of their struggle."
                n "Despite the hero's skil, it was clear the Fallen Hero's experience and hatred gave him a fierce edge. He has practiced to perfection the technique of the kingdom knights."
                n "The hero fought valiantly, but the Fallen Hero's relentless attacks began to overwhelm him. With a powerful strike, the hero was knocked off balance, stumbling to the ground."
                n "The princess's heart pounded as she rushed to the hero's side, helping him to his feet. The Fallen Hero stood over them, eyes blazing with triumph."
                fh "This is your end."
                n "Gathering all their courage, the princess and hero made a desperate dash into the dense forest, branches and undergrowth tearing at their clothes as they fled."
                n "The Fallen Hero did not pursue, his bitter laugh echoing through the trees."
                fh "Run, cowards. But remember, the shadows of this forest will always be mine."
                n "As the princess and hero disappeared into the darkness, the sense of foreboding lingered, They had escaped, but the encounter with the Fallen Hero left a lasting mark on their souls, a reminder of the kingdom's dark past and the enemies it had created."
                jump villain1_2_2

    label villain2_1:
        menu:
            "(Act) Try to retrieve the sword":
                p "Get the sword! I'll cover you!"
                n "The hero dashed to retrieve his sword. A strike from the figure narrowly misses the hero thanks to the princess, distracting the figure with a fake strike."
                n "The hero picks up the sword, jumps back next to the princess, and tightens his grip, steeling himself for what's to come."
                jump villain2_1_1

            "(Act) Use the environment":
                p "Quick! To the trees!"
                n "The figure lunged for a strike at the defenceless hero, but just in time, the two ducked behind a nearby tree, using it as cover as they planned their next move."
                n "The figure let out a frustrated grunt, and with building anger, slowly approached the tree."
                h "Shit. What now?"
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
                p "Keep the pressure on. Don't give them a chance to recover."

            "(Act) Switch to a different weapon":
                n "The hero slung his bow over his shoulder and drew his sword, stepping forward with determined eyes. The figure watched him warily, sensing the change in tactics."
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
                n "It found its mark on the figure's arm. THe figure hissed in pain, clutching the wound. They shot a sharp look at you, almost shocked that you had the prowess to back your claims."
                h "That should slow them down."
                jump villain3_1

    label villain4_1:
        menu:
            "(Act) Soothe them":
                n "The princess stepped closer, her tone soft and heartfelt."
                p "Please, I can see the pain in your eyes. We're not here to hurt you. We all have our struggles. Let's find a way to understand each other."
                n "The figure's stance loosened slightly, the tension in their shoulders easing. They seemed torn, conflicted between aggression and the princess's calming presence."
                p "We're listening. Just tell us what you need."
                n "The figures hesitated, a flicker of vulnerability showing in their eyes as they considered the princess's sincere plea."
                n "They lower their weapon, opening themselves to hear the princess' words."
                jump villain4_1_1

            "(Act) Offer information - Femme Fatale":
                n "The princess spoke earnestly, hoping to build trust."
                p "We know things that could help you. Let us share what we know, and maybe we can assist each other."
                h "It's a valuable knowledge. Hear us out."
                n "Unexpectedly, the figure's smirk widened, revealing a calculating gleam in their eyes. The posture relaxed, but it was a deceptive ease, like a predator toying with its prey."
                n "The figure steps into the light, shifting the hood of the cloak to reveal an elegant woman donning an array of corrupt accessories."
                ff "Information, you say? How delightful. But you see, I already know more about you than you realize. Your fears, your desires, your weaknesses. They are all laid bare before me."
                n "The figures's voice dripped with honeyed malice, each word a carefully crafted weapon aimed at their resolve. The air grew colder as shadows seemed to deepen around them."
                p "What... what do you mean?"
                n "The figure stepped closer, their presence overwhelming, as if they were enveloping the very light around them."
                ff "You, dear princess, are an open book. Your thoughts, your heart - so easy to read. And you, brave hero, so predictable in your gallant efforts. You think you can bargain with me? How quaint."
                n "The princess and hero stood their ground, but the unease in their eyes betrayed their growing uncertainty. The figure's words cut deep, eroding their confidence."
                ff "But fear not. I have no interest in trinkets or knowledge you might offer. No, I revel in the game, the dance of shadows and secrets. And for now, I am satisfied with what I have seen."
                n "With a final, piercing gaze, the figure began to slink back into the darkness, their form dissolving into the inky blackness of the forest."
                s "Until we meet again, my dear pawns. Remember, the game has only just begun."
                n "As the figure vanished, the oppressive weight lifted, leaving the princess and hero standing in the eerie silence of the forest. The encounter had ended, but the unease lingered, a haunting reminder of the shadowy figure's words."
                h "What just happened? Who was that?"
                p "I don't know, but I have a feeling this isn't the last we've seen of them."
                n "With a shared look of resolve, the princess and hero knew their journey was far from over. The path ahead was fraught with danger and mystery, and the figure's ominous presence would be a constant shadow on their quest."
                jump villain4_1_2

    label villain4_2:
        menu:
            "(Act) Threaten the figure":
                n "The hero stepped forward, the blade in his hand gleaming menacingly. The figure's eyes narrowed, a low growl escaping their lips."
                h "Tell us who you are, or face the consequences."
                n "The figure sneered, unfazed by the threat, their eyes glinting with dark amusement."
                n "To their dismay, the figure's stance sharply shifted, readying for an imminent clash, their smirk widening as they accepted the challenge."
                jump villain4_2_1

            "(Act) Pressure the figure and look for a weakness":
                n "The princess and hero circled the figure, searching for an opening. The figure's eyes sharpened, sensing their intent."
                h "Look for an opening. We cannot go down here."
                n "Like a trapped feral animal, the figure violently lurched outwards."
                n "Like a flash of lightning, the figure was midair, lunging an attack towards the princess."
                jump villain4_2_2

            "(Act) Bluff strength":
                n "The princess's voice was firm, projecting confidence. The figure's expression darkened, but a flicker of doubt crossed their eyes."
                p "We're stronger than you think. It's not worth the risk."
                n "The figure takes a small step back. It seems they have switched to taking a defensive approach to the situation."
                jump villain4_2_3

    label villain1_1_1:
        menu:
            "(Act) Demand answers - Vengeful Spirit":
                n "The princess's voice rang out with authority as she demanded answers."
                p "Who are you? What do you want from us?"
                n "The air around them grew colder, an unsettling chill creeping into their bones. The figure's form began to shimmer and distort, revealing a ghostly, ethereal figure with eyes that burned with an unearthly fire."
                vs "I am the reckoning for those who disturb the balance. You, who come from the kingdom of corruption, shall face my wrath."
                n "The spirit's voice echoed through the forest, each word dripping with ancient malice and vengeance. The hero stepped forward, trying to reason with the apparition."