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
    scene bg Villain
    n "The forest seemed darker than before, the shadows deeper and more menacing as the princess and hero retraced their steps."
    n "Each rustling leaf and distant creak of branches felt like the forest itself was holding its breath. The princess and hero could see the kingdom now, a sign that they were getting close."
    n "The hero's grip tightened on his sword as they ventured further, his eyes scanning every shadow for signs of movement."
    n "He could feel it-the tension in the air that signaled they were not alone. The princess's thoughts raced as they drew closer and closer to their destination."
    play music "audio/5 Second Villian 3.mp3" loop volume 1.0 fadein 0.5
    scene bg Villain_far_fh
    n "As they pressed forward, a familiar figure stepped out from the shadows. The Fallen Hero's presence was as foreboding as ever, his scarred face a mask of bitterness and fury."
    n "His sword remained sheathed, but the tension in his stance made it clear that any peace was fragile and fleeting."

    if fh_times_gotten == 1:
        pt "It's him... the warrior who lost everything. Can we find a way through this without bloodshed?"

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
                n "The princess signaled to the hero, who drew his sword with a fluid motion. The air grew tense as the Fallen Hero stepped forward, his eyes burning with an old bitterness."
                scene bg Villain_hero_sword_facing_far_fh
                p "We can't hold back against him. He's not just another opponent."
                h "I know. He carries the weight of a past we don't fully understand. But I'll follow your lead."

                jump fh_choices_2_1

            "(Act) Try to reason with him":
                n "The princess took a deep breath and stepped forward, extending her hand in a gesture of peace."
                n "The forest held its breath as the Fallen Hero's gaze bore into her, hard and unyielding."
                p "You were once the kingdom's greatest champion. We don't need to fight like this. We can find another way."
                h "Careful, princess. His hatred for the kingdom runs deep."
                n "The Fallen Hero's grip on his sword tightened, his expression shadowed by years of betrayal. Yet, beneath the rage, there was a flicker of something-a memory, perhaps."
                fh "Another way? That's a fantasy for those who haven't tasted the kingdom's lies."

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

            "(Speak) Why can't you just let us pass?" if not fh_chose_why_cant_pass:
                $ fh_chose_why_cant_pass = True
                call fh_why_cant_pass
                jump fh_choices_1

            "(Speak) Is there anything that could change your mind?" if not fh_chose_change_your_mind and fh_chose_why_cant_pass:
                $ fh_chose_change_your_mind = True
                call fh_change_your_mind
                jump fh_choices_1

            "(Speak) We're not like those who wronged you." if not fh_chose_not_like_those and fh_chose_change_your_mind:
                $ fh_chose_not_like_those = True
                call fh_not_like_those
                jump fh_choices_1


    # Level 2 of choice tree
    label fh_choices_2_1:
        # Branching from "(Act) Prepare for combat"
        menu:
            "(Act) Attack first":
                n "The hero adjusted his stance, muscles tensing as he prepared to strike. The princess gave a quick nod, signaling the attack."
                p "Go, now! We have to catch him off-guard!"
                n "With a powerful swing, the hero launched himself at the Fallen Hero, his blade slicing through the air. But the Fallen Hero's experience showed in his fluid dodge, sidestepping the blow with practiced ease."
                scene bg Villain_hero_charging_far_fh
                fh "Is this all the kingdom can muster? A pale imitation of what I once was."
                n "The Fallen Hero retaliated swiftly, his counterstrike leaving the hero barely time to block."
                scene bg Villain_hero_sword_facing_far_fh
                n "The force of the clash echoed through the clearing as the princess desperately scanned for a way to shift the balance."

                jump fh_choices_3_1
            "(Act) Defend and counter":
                n "The princess signaled for the hero to hold his ground. The two stood firm, waiting for the Fallen Hero's move."
                n "The tension between them crackled like a storm ready to break."
                h "He's watching, waiting for us to slip. Stay ready."
                n "The Fallen Hero's gaze was cold, calculating. In a flash, he lunged, sword sweeping in a deadly arc."
                n "The hero raised his shield just in time, deflecting the blow and pushing back with all his strength."
                fh "You think defense will save you? You've already lost if you're on the back foot."
                n "Despite his harsh words, there was a hint of respect in the Fallen Hero's voice."
                n "The princess could sense that he was testing them, probing their resolve."

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

            "(Speak) Why can't you just let us pass?" if not fh_chose_why_cant_pass:
                $ fh_chose_why_cant_pass = True
                call fh_why_cant_pass
                jump fh_choices_2_1

            "(Speak) Is there anything that could change your mind?" if not fh_chose_change_your_mind and fh_chose_why_cant_pass:
                $ fh_chose_change_your_mind = True
                call fh_change_your_mind
                jump fh_choices_2_1

            "(Speak) We're not like those who wronged you." if not fh_chose_not_like_those and fh_chose_change_your_mind:
                $ fh_chose_not_like_those = True
                call fh_not_like_those
                jump fh_choices_2_1

    label fh_choices_2_2:
        # Branching from "(Act) Try to reason with him"
        menu:
            "(Act) Appeal to his sense of justice":
                n "The princess spoke with conviction, her voice cutting through the silence of the forest."
                p "You fought for justice once. I know that part of you still exists. The kingdom betrayed you, but that doesn't mean you have to betray who you are."
                h "Keep talking, princess. He might still listen if he remembers what he once stood for."
                n "The Fallen Hero's expression hardened, though his eyes betrayed a fleeting uncertainty. His grip on the sword wavered for just a moment."
                fh "Justice? That word lost its meaning the day I was cast out. I no longer fight for ideals-I fight for survival."
                n "The princess held her breath. The hint of hesitation showed that her words had struck something deep within him, though whether it was enough remained uncertain."

                jump fh_choices_3_3
            "(Act) Offer a peaceful solution":
                n "The princess's voice softened, adopting a tone both calm and sincere."
                p "You don't have to be alone out here, driven by anger. There's another path. I could clear your name, restore your honor... or even join you if you'd rather stay away from it all."
                h "Are you sure about this, princess? We're offering him a way out, but it's still risky."
                n "The Fallen Hero's eyes narrowed, suspicion lacing his every movement."
                n "Yet beneath the mistrust, there was a flicker of something more-hope, perhaps, or longing for a life he'd thought forever lost."
                fh "You'd risk everything for a man the kingdom threw away? Your offer is tempting... but I've learned that trust is a luxury I can't afford."
                n "Though his tone was guarded, the princess sensed an opening."
                n "This might be the chance to sway him, if she could find the right words-or take the right action."

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

            "(Speak) Why can't you just let us pass?" if not fh_chose_why_cant_pass:
                $ fh_chose_why_cant_pass = True
                call fh_why_cant_pass
                jump fh_choices_2_2

            "(Speak) Is there anything that could change your mind?" if not fh_chose_change_your_mind and fh_chose_why_cant_pass:
                $ fh_chose_change_your_mind = True
                call fh_change_your_mind
                jump fh_choices_2_2

            "(Speak) We're not like those who wronged you." if not fh_chose_not_like_those and fh_chose_change_your_mind:
                $ fh_chose_not_like_those = True
                call fh_not_like_those
                jump fh_choices_2_2


    # Level 3 of choice tree
    label fh_choices_3_1:
        # Branching from "(Act) Attack first"
        menu:
            "(Act) Aim for his weak spot":
                n "The princess noticed a brief hesitation in the Fallen Hero's movements, a subtle limp that hinted at an old injury."
                p "Focus on his left side! It's our best shot!"
                n "The hero nodded, eyes sharp as he aimed for the weak spot."
                scene bg Villain_hero_charging_far_fh
                n "But as his sword swung toward the target, the Fallen Hero's reflexes kicked in. He deflected the strike with practiced ease, a grim smile tugging at his lips."
                fh "You think I haven't learned to live with my pain? Weakness is only for those who let it consume them."
                n "The counterattack came swiftly, the hero barely managing to block the incoming blow."
                scene bg Villain_hero_sword_facing_far_fh
                n "The princess could see the frustration in the hero's eyes-they were facing someone who had turned every scar into a weapon."

                jump fh_choices_4_1
            "(Act) Charge with full force":
                n "The princess steeled herself, knowing that they had to overwhelm him with raw power."
                p "No hesitation-go all out!"
                n "The hero gripped his sword with both hands, charging with every ounce of strength he had."
                scene bg Villain_hero_charging_far_fh
                n "The Fallen Hero's eyes narrowed, and for a moment, his guard dropped, as if daring them to strike."
                n "But just as the hero's blade descended, the Fallen Hero twisted away, the attack grazing him without connecting fully."
                fh "Strength alone is a blunt weapon. You'll need more than that to bring me down."
                n "The air crackled with tension as the Fallen Hero retaliated with a brutal strike that sent the hero reeling."
                scene bg Villain_hero_sword_facing_far_fh
                n "The princess's heart raced-she knew they couldn't afford many more failed attacks."

                jump fh_choices_4_2

    label fh_choices_3_2:
        # Branching from "(Act) Defend and counter"
        menu:
            "(Act) Use the hero's shield to block and counter":
                n "The princess kept her eyes locked on the Fallen Hero's stance, noticing the subtle shifts in his posture."
                p "Keep your shield up! Wait for the right moment to strike back!"
                n "The hero braced himself, shield raised as the Fallen Hero lunged forward with a powerful swing."
                n "The clash was deafening as metal met metal, the hero holding firm before pushing back with all his might."
                n "The counterattack was swift, but the Fallen Hero sidestepped with almost inhuman grace."
                fh "Your defense is strong, but it's only delaying the inevitable. How long do you think you can last before it crumbles?"
                n "The princess could see the strain on the hero's face, but there was determination there too."
                n "They needed to find a way to break the Fallen Hero's rhythm if they wanted to stand a chance."

                jump fh_choices_4_3
            "(Act) Lure him into a position where he is vulnerable":
                n "The princess's eyes darted across the clearing, analyzing every possible angle. An idea sparked in her mind."
                p "Draw him to the left! If we can funnel him into that narrow spot, he'll be trapped!"
                n "The hero nodded and began maneuvering carefully, baiting the Fallen Hero to follow."
                scene bg Villain_far_fh
                n "The plan seemed to work-until the Fallen Hero caught on."
                n "With a swift, calculated move, he shifted his weight and took a step back, avoiding the trap entirely."
                fh "You think you can outmaneuver me in my own battlefield? You're sorely mistaken."
                n "The failed strategy left the hero off-balance, and the Fallen Hero seized the opportunity, striking with ruthless precision."
                n "The princess's heart sank-this was going to take more than clever tricks."

                jump fh_choices_4_4

    label fh_choices_3_3:
        # Branching from "(Act) Appeal to his sense of justice"
        menu:
            "(Act) Remind him of his past as a protector":
                n "The princess's voice softened, appealing to the memory of the man he once was."
                p "You were the kingdom's greatest hero, a beacon of hope. That part of you is still in there, buried beneath the anger."
                h "He was a legend-a symbol of everything good. Maybe that part of him can still be reached."
                n "The Fallen Hero's eyes flickered, the anger momentarily giving way to something else-regret, or perhaps longing."
                n "But the hardness quickly returned."
                fh "The kingdom's 'hero'? That man was a fool, blind to the rot beneath the crown. I protect nothing now but myself."
                n "His words were laced with bitterness, but the princess sensed a faint crack in his resolve."
                n "She could tell her words had stirred something within him, even if he refused to acknowledge it."

                jump fh_choices_4_5
            "(Act) Convince him that the kingdom has changed":
                n "The princess took a step closer, determination clear in her voice."
                p "The kingdom isn't what it was when you were betrayed. It's changed-people have changed. You don't have to keep carrying this burden."
                h "If anyone knows how much a place can change, it's him. He deserves to know the truth."
                n "The Fallen Hero's grip on his sword tightened, his expression conflicted."
                n "The years of bitterness warred against the faint hope that things might be different."
                fh "Change? Promises of change are just illusions. The moment I let my guard down, history will repeat itself."
                n "Despite his harsh words, the hesitation in his stance was telling."
                n "The princess realized she might be close to reaching him if she pressed further."

                jump fh_choices_4_6

    label fh_choices_3_4:
        # Branching from "(Act) Offer a peaceful solution"
        menu:
            "(Act) Swear on your honor to clear his name" if not chose_magic:
                n "The princess's voice was solemn, her tone carrying the weight of a royal promise."
                p "I swear on my honor as princess-I'll clear your name. I'll bring your truth to light and see justice done."
                h "That's a dangerous promise, princess, but it might be the only way to reach him."
                n "The Fallen Hero's expression darkened, but there was a flicker of curiosity in his eyes."
                n "His years of bitterness clashed with a faint yearning for redemption."
                fh "You think words and titles can erase years of exile? Honor means nothing when it's stained by betrayal."
                n "Though he remained guarded, the princess sensed that her offer had at least given him pause."
                n "He wasn't ready to trust her, but she had his attention."

                jump fh_choices_4_7
            "(Act) Offer to stay in the forest with him" if chose_magic:
                n "The princess's voice softened, her offer more personal, almost intimate."
                p "You don't have to be alone in this forest anymore. If you can't trust the kingdom, then trust me. I'll stay with you, away from all the lies and betrayals."
                h "Princess, that's-"
                n "The hero's words were cut short by the Fallen Hero's cold stare. A long silence hung in the air as the offer lingered."
                fh "Stay... here, in exile? You'd sacrifice everything for that? For someone who could turn against you at any moment?"
                n "There was disbelief in his voice, but also a spark of something deeper-longing, perhaps."
                n "The princess could tell her words had shaken something within him, but whether it was enough to reach him remained to be seen."

                jump fh_choices_4_8

    
    # Level 4 of choice tree
    label fh_choices_4_1:
        # Branching from "(Act) Aim for his weak spot"
        menu:
            "(Act) Strike at his old injury" if not chose_magic:
                n "The hero tightened his grip on the sword, eyes fixed on the Fallen Hero's weakened side. The princess knew this was their best chance, but one wrong move could end it all."
                p "Go for it! This is our opening!"
                n "The hero lunged forward, aiming for the injury, but the Fallen Hero's instincts flared to life. Despite the pain, he twisted away, evading the strike with a snarl."
                scene bg Villain_hero_charging_far_fh
                v "You think I'm not used to fighting with pain? You're just another naïve fool."
                scene bg Villain_hero_sword_facing_far_fh
                n "The counterattack was brutal-a backhanded slash that nearly knocked the hero off his feet. The princess could see the strain in the hero's movements. They were running out of chances."

                jump fh_choices_5_1
            "(Act) Use magic to enhance the attack" if chose_magic:
                n "The princess's eyes glowed with determination as she channeled her energy into the hero's blade. The sword hummed with newfound power, crackling with magic."
                p "This time, we'll end it! Strike with all your strength!"
                n "The hero surged forward, the blade cutting through the air with a trail of shimmering light. The Fallen Hero's eyes widened as he recognized the surge of magic, but it was too late-this strike was far more precise than before."
                scene bg Villain_hero_charging_far_fh
                v "So you resort to magic... Fine, let's see how far it takes you!"
                n "The attack connected, forcing the Fallen Hero to stumble back. But his anger only deepened, and a dangerous light filled his eyes."
                scene bg Villain_far_fh
                n "They had wounded him, but the fight was not over."

                jump fh_choices_5_2

    label fh_choices_4_2:
        # Branching from "(Act) Charge with full force"
        menu:
            "(Act) Overwhelm him with sheer strength" if not chose_magic:
                n "The hero gritted his teeth, summoning all his strength for one decisive attack. The princess knew this was a battle of wills as much as skill."
                p "Don't hold back! Everything you have-now!"
                n "With a fierce battle cry, the hero rushed forward, swinging his sword with raw power. The Fallen Hero met the attack head-on, his expression shifting into one of grim determination."
                scene bg Villain_hero_charging_far_fh
                n "Steel clashed against steel, the force of the impact sending shockwaves through the clearing."
                v "Is this what you call strength? You're nothing but an echo of the warrior I once was."
                n "Though the hero's attack was mighty, the Fallen Hero's experience and hardened resolve allowed him to stand firm."
                scene bg Villain_hero_sword_facing_far_fh
                n "The clash pushed both combatants to their limits, leaving the princess with a crucial choice to make before their strength ran out."

                jump fh_choices_5_3
            "(Act) Use magic to disorient him during the charge" if chose_magic:
                n "The princess whispered an incantation, her voice barely audible as she called forth an enchantment that shimmered around the hero."
                p "The moment he moves, I'll create an opening. Be ready to strike!"
                n "As the hero charged forward, the air crackled with energy. The Fallen Hero's eyes narrowed, sensing the distortion in the space around him."
                scene bg Villain_hero_charging_far_fh
                n "Suddenly, the princess unleashed a burst of light, disorienting him just long enough for the hero's blade to find its mark."
                v "Magic tricks? So this is the extent of your courage."
                n "The attack landed, but the Fallen Hero's resolve remained unbroken. Though visibly shaken, he quickly recovered, eyes blazing with renewed fury."
                scene bg Villain_hero_sword_facing_far_fh
                n "The princess could feel the tension rising-this battle was only growing more dangerous."

                jump fh_choices_5_4

    label fh_choices_4_3:
        # Branching from "(Act) Use the hero's shield to block and counter"
        menu:
            "(Act) Push him back and strike" if not chose_magic:
                n "The hero braced himself, raising his shield high as the Fallen Hero's blade came crashing down. The impact was fierce, but the hero held firm, muscles straining against the force."
                p "Now! Push him back and counter!"
                n "With a grunt of effort, the hero deflected the blow, shoving the Fallen Hero off-balance before launching a swift counterattack."
                scene bg Villain_hero_sword_facing_close_fh
                n "For a split second, the Fallen Hero's guard dropped, and the hero's strike connected."
                v "Not bad, but don't think that will be enough."
                n "Despite the hit, the Fallen Hero's eyes gleamed with an unsettling calm. He barely flinched, as if the wound only fueled his rage."
                scene bg Villain_far_fh
                n "The princess realized that while they were making progress, this battle would not end easily."

                jump fh_choices_5_5
            "(Act) Use magic to create an opening" if chose_magic:
                n "The princess's eyes flashed as she focused her energy into a single spell. Time was running out, and they needed every advantage they could muster."
                p "I'll hold him down-strike when you see the chance!"
                n "Magic swirled around the Fallen Hero, binding his movements for a brief moment. The hero seized the opportunity, driving his blade toward the Fallen Hero's exposed side."
                scene bg Villain_hero_charging_far_fh
                v "You rely on tricks because you lack true strength!"
                scene bg Villain_hero_sword_facing_far_fh
                n "The spell worked, and the hero's attack hit its mark. But the Fallen Hero's endurance was unyielding, his eyes locked onto the princess with seething rage."
                n "She could feel the tension mounting-he wouldn't fall for the same trick twice."

                jump fh_choices_5_6

    label fh_choices_4_4:
        # Branching from "(Act) Lure him into a position where he is vulnerable"
        menu:
            "(Act) Distract him with a feint and attack":
                n "The princess's gaze sharpened as she observed the Fallen Hero's stance, noting the small gaps in his defense."
                p "Feint left, then strike from the right! He won't see it coming!"
                n "The hero moved swiftly, executing the feint as instructed. For a moment, the Fallen Hero shifted his attention, only to realize too late that the true attack was coming from the other side."
                scene bg Villain_hero_charging_far_fh
                n "The hero's blade found its target, landing a solid hit."
                v "Clever. But cleverness only gets you so far."
                n "The Fallen Hero grimaced as the blow connected, but his retaliation was swift. He adjusted instantly, turning the tables in the blink of an eye."
                scene bg Villain_far_fh
                n "The princess could sense his growing frustration-this battle was quickly escalating into a dangerous dance of wit and skill."

                jump fh_choices_5_7
            "(Act) Use the environment to trap him":
                n "The princess's eyes darted to the surrounding trees and undergrowth, formulating a plan. She signaled the hero, subtly directing him toward a narrow thicket."
                p "Lead him into that tight space-he'll be stuck!"
                n "The hero nodded, shifting his movements to draw the Fallen Hero into the trap. It was working-bit by bit, the Fallen Hero was funneled into the confined area."
                scene bg blackscreen
                n "But just as the trap was about to spring, he caught on, shifting his stance and using the trees to his advantage."
                v "You think I haven't learned every inch of this forest? You underestimate me."
                n "The trap failed, and the Fallen Hero lashed out, using the terrain to his advantage."
                scene bg Villain_far_fh
                n "The situation grew more perilous as he cornered the hero. The princess realized they were running out of time-the next move had to be decisive."

                jump fh_choices_5_8

    label fh_choices_4_5:
        # Branching from "(Act) Remind him of his past as a protector"
        menu:
            "(Act) Bring up his past victories":
                n "The princess's voice softened as she reached out to the part of him that still held onto the honor he once had."
                p "Remember who you were-the victories you achieved, the lives you saved. That man is still inside you, buried beneath all this hatred."
                h "You were a legend-people still talk about your deeds. You don't have to be this way."
                n "The Fallen Hero's eyes flickered, a storm of conflicting emotions swirling within. For a moment, he seemed lost in memory, the bitterness in his expression giving way to something softer."
                v "You speak of the past as if it matters now. Those victories are ashes-meaningless in a world that cast me aside."
                n "Though he tried to harden his heart, the princess could see the conflict raging within him. The memories were still there, and they tugged at his resolve."
                n "This might be their chance-if she could press just a bit more."

                jump fh_choices_5_9
            "(Act) Highlight the injustice he suffered" if not chose_magic:
                n "The princess's voice was laced with empathy, acknowledging the wrongs that had been done to him."
                p "They wronged you-they betrayed someone who only wanted to protect them. But there's still a way to find justice, to reclaim what you lost."
                h "It wasn't right, what happened to you. But that doesn't mean you have to keep hurting others because of it."
                n "The Fallen Hero's expression darkened, his grip tightening on his sword. Beneath the anger, there was something deeper-pain, loss, and a sense of betrayal that ran deeper than any wound."
                v "Justice? Don't speak to me of justice. It's a lie-like everything else they promised me."
                n "Though his voice was laced with bitterness, the princess could see that her words had struck a chord. He wasn't unmoved-there was still a spark of the man he once was, buried beneath the scars."

                jump fh_choices_5_10

    label fh_choices_4_6:
        # Branching from "(Act) Convince him that the kingdom has changed"
        menu:
            "(Act) Explain how the kingdom has reformed":
                n "The princess's voice was firm, determined to show him that time had changed more than just the people."
                p "The kingdom isn't what it used to be. The corruption, the lies-they've been exposed and torn down. You don't have to keep fighting a war that's already ended."
                h "He deserves to know that the kingdom isn't the place that betrayed him. It's different now-it's better."
                n "The Fallen Hero's eyes narrowed in suspicion, though there was a flicker of curiosity beneath the mistrust."
                n "The princess could sense his doubt, the walls he'd built around himself beginning to crack."
                v "I've heard promises before, and they always turned to dust. What makes you think this time is any different?"
                n "Though his words were laced with skepticism, the princess knew that the idea had taken root. If she could show him that change was real, there might still be hope."

                jump fh_choices_5_11
            "(Act) Offer him a chance to return as a hero":
                n "The princess took a step closer, her voice gentle but filled with conviction."
                p "You could be the hero you once were-people would follow you, trust you. You don't have to live like this, bound by old wounds."
                h "You were a symbol of hope once. That can be true again."
                n "The Fallen Hero's gaze wavered, the weight of her words pressing against the bitterness he clung to."
                n "For a moment, something like hope sparked in his eyes, but it was quickly drowned by years of anger and distrust."
                v "Return as a hero? To a kingdom that turned its back on me? You're asking for the impossible."
                n "Despite his refusal, the princess could see that her words had shaken him. There was a part of him that longed for that life again, even if he refused to admit it."
                n "This moment could be the turning point, if she found the right way to guide him."

                jump fh_choices_5_12

    label fh_choices_4_7:
        # Branching from "(Act) Swear on your honor to clear his name"
        menu:
            "(Act) Offer to bring evidence of his innocence":
                n "The princess's voice took on a steely resolve as she stepped forward, her eyes unwavering."
                p "I'll do more than just speak on your behalf. I'll gather proof-the evidence they ignored-and I'll make sure they hear it, no matter what it takes."
                h "That's a dangerous promise, but if anyone can dig up the truth, it's her."
                n "The Fallen Hero's expression darkened, suspicion still heavy in his eyes. But there was a flicker-an old hope, buried deep beneath years of bitterness."
                v "Proof? Do you think they'll care about facts when their lies hold more power? You're offering an impossible fight."
                n "His words dripped with cynicism, but the princess sensed the crack in his resolve. The chance to reclaim the honor he lost still tugged at him, no matter how much he tried to deny it."
                n "This was a battle against the doubt in his own heart, and she could see that a part of him wanted to believe her."

                jump fh_choices_5_13
            "(Act) Offer to use your authority as princess":
                n "The princess straightened, letting her royal presence carry in her voice. Her words were backed by more than just determination-they were backed by her birthright."
                p "As princess, I can see to it that your case is heard, fairly this time. I'll stand by you, and they'll have to listen. I can promise you that."
                h "This isn't like before. She's different from the ones who wronged you."
                n "The Fallen Hero's gaze narrowed, weighing the offer against the scars of betrayal he still carried."
                n "For a moment, his hardened expression softened, doubt creeping into his eyes."
                v "A princess's word? You think your title can rewrite history? I've seen how easily royalty can turn against their own when it suits them."
                n "Though skepticism clung to his voice, the princess could tell that her authority held weight. The years had stripped him of his faith in the kingdom, but this was an opportunity to restore what he'd lost."
                n "If she could earn his trust, it might be enough to sway him."

                jump fh_choices_5_14

    label fh_choices_4_8:
        # Branching from "(Act) Offer to stay in the forest with him"
        menu:
            "(Act) Offer to perform a magical oath" if chose_magic:
                n "The princess's voice softened, her tone more sincere than ever. She stepped closer to the Fallen Hero, magic sparking faintly at her fingertips as she made her offer."
                p "If it's trust you need, I'm willing to offer a magical oath. I'll bind myself to my promise-to stay, to help you find peace. I won't leave until it's done."
                h "Princess... that's a serious offer. Are you really ready to make such a vow?"
                n "The Fallen Hero's eyes widened in surprise, the bitterness in his gaze momentarily giving way to something softer-curiosity, even disbelief."
                n "He had expected more empty words, but this was something he hadn't anticipated."
                v "A magical oath? You would make such a binding promise for someone like me? Do you even understand the weight of what you're offering?"
                n "The princess held his gaze, unwavering. She could tell he was taken aback-years of isolation and betrayal had taught him that trust was a fool's game, and yet here she was, offering something that could change everything."
                n "The moment hung heavy in the air, as if the world itself waited to see what he would say next."

                jump fh_choices_5_15
            "(Act) Betray him and prepare to strike":
                n "The princess's expression darkened as she glanced at the hero. She had considered every option, but in the end, the risk of trusting the Fallen Hero seemed too great."
                n "She leaned in close to the hero, her voice low and decisive."
                p "I've made my decision. We can't let him walk away from this. We strike when the time is right."
                h "I'm with you. He's dangerous-this might be our only shot to end it."
                n "The princess's heart pounded as she and the hero exchanged a look of grim determination. There was no turning back now-they had made their choice."
                n "They would play along for as long as needed, but when the opportunity came, they would end this on their terms."
                n "The plan was set, and the air crackled with tension as they prepared for the confrontation to come."

                jump fh_choices_5_16


    # Level 5 of choice tree
    label fh_choices_5_1:
        # Branching from "(Act) Strike at his old injury"
        menu:
            "(Act) Exploit his pain to win the fight":
                n "The hero's eyes locked onto the Fallen Hero's old wound, the only visible weakness in his otherwise ironclad defense. The princess, torn between compassion and survival, steeled herself and gave the signal."
                p "Do it! Strike now!"
                scene bg blackscreen
                n "The hero lunged, driving his blade toward the weakened spot. The Fallen Hero, gritting his teeth against the searing pain, staggered back, realizing too late that the hero had found his vulnerable point."
                n "Desperation flashed in his eyes as he turned his focus away from the hero and toward the princess, his intent clear."
                n "The Fallen Hero charged toward the princess, his sword aimed directly at her heart. But before the blade could reach her, the hero pushed her aside, taking the strike himself."
                n "The blade sank deep into his chest, and he collapsed, blood pooling beneath him."
                n "The princess cried out in horror as the hero crumpled at her feet, his breath shallow and fading fast."
                n "With his final moments, he managed a pained smile, knowing that he had fulfilled his duty by protecting the one he loved."
                n "The princess held him close as the life drained from him, her tears mingling with the blood on his armor."
                n "Though the Fallen Hero was defeated, the princess was left to mourn the loss of the one who had stood by her side through every trial."
                n "Her grief was deep, but she knew that she must carry on, returning to the kingdom with a heavy heart and the memory of the hero's sacrifice forever etched in her soul."
                n "And the princess lived happily ever-"

                jump sacrificed_hero
            "(Act) Hesitate, showing mercy":
                n "The hero's blade hovered above the Fallen Hero's weakened side, but the princess's voice rang out, pleading for mercy."
                p "Wait-don't do it! We've fought enough. There's been enough death."
                scene bg blackscreen
                n "The hero hesitated, lowering his sword as the princess stepped forward, offering her hand to the Fallen Hero in an act of compassion."
                n "For a fleeting moment, it seemed that the years of bitterness might give way to something softer, a chance for peace."
                n "The Fallen Hero's expression twisted in fury at the offered mercy, and in a final act of defiance, he drove his blade into the hero's side."
                n "Blood poured from the wound as the hero collapsed into the princess's arms. Despair filled her eyes as she realized that there was no saving him-he was bleeding out too fast."
                n "Faced with the loss of the one she loved, the princess made a desperate decision."
                n "She took up the hero's sword and ended her own life, choosing to follow him into death rather than face a world without him."
                n "As they lay side by side, their souls departed this world together, finding peace in the afterlife where no more battles awaited them."
                n "And the princess and hero died happily ever-"

                jump love_beyond_death

    label fh_choices_5_2:
        # Branching from "(Act) Use magic to enhance the attack"
        menu:
            "(Act) Overwhelm him with dark magic":
                n "The princess's eyes glowed with determination as she channeled dark energy into the hero's blade. The air crackled with power, the magic humming with a sinister force that made the very ground tremble beneath them."
                p "This is our only chance-pour everything into this strike!"
                scene bg blackscreen
                n "The hero nodded, charging forward with the blade infused with dark magic. The Fallen Hero's eyes widened in shock as the corrupted energy surged toward him."
                n "His defenses crumbled under its overwhelming force."
                n "The dark magic struck the Fallen Hero, consuming him in a blaze of destructive power."
                n "But the victory was hollow-the corrupted energy did not dissipate."
                n "Instead, it spread, corrupting the very forest around them. The trees twisted into grotesque shapes, their branches reaching out like claws."
                n "The ground cracked open, spewing darkness that tainted the land."
                n "The princess and hero realized their terrible mistake as the cursed forest bound them to its soil."
                n "Their souls became tied to the land they had ruined, forced to remain as eternal guardians of the very darkness they had unleashed."
                n "In time, they accepted their fate, choosing to spend eternity atoning for the destruction they had caused by protecting what little life remained in the cursed forest."
                n "And the princess and hero lived happily ever-"

                jump forest_curse
            "(Act) Bind his power with a magical seal":
                n "The princess's magic flowed through her fingers as she began to weave a complex spell, summoning enchanted chains of light that coiled around the Fallen Hero."
                n "The magic pulsed with an unbreakable force, fueled by her determination to end the battle without further bloodshed."
                p "I'll bind his power-this ends here!"
                scene bg blackscreen
                n "The hero stood by, ready to defend her as the magic closed in around the Fallen Hero, locking him in place."
                n "He struggled against the spell, his anger boiling over as the chains tightened, stripping him of the power that had driven his relentless rage."
                n "The sealing spell completed, encasing the Fallen Hero in an enchanted prison from which there was no escape."
                n "As his strength faded, the darkness that had plagued the forest began to recede, and the land was slowly restored to its former tranquility."
                n "With the threat vanquished and the forest saved, the princess and hero chose to leave the kingdom behind, seeking a life where they could live free from the responsibilities that had once burdened them."
                n "Knowing that the kingdom would never accept their use of magic, they decided to carve out a peaceful existence far away, where they could live on their own terms, exploring the world and forging their own path."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after

    label fh_choices_5_3:
        # Branching from "(Act) Overwhelm him with sheer strength"
        menu:
            "(Act) Defeat him decisively":
                n "The hero tightened his grip on his sword, every ounce of his strength channeled into one final, decisive strike. The princess's eyes blazed with determination as she gave the order."
                p "Now-end this once and for all!"
                scene bg blackscreen
                n "With a roar, the hero swung his blade, the force of his attack shattering the Fallen Hero's defenses. The blow struck true, cutting through armor and leaving the Fallen Hero staggering."
                n "His eyes widened in disbelief as his strength gave out, the years of bitterness finally catching up to him."
                n "The Fallen Hero fell, his life slipping away as his final attempt at vengeance crumbled into dust. With the battle won, the princess and hero returned to the kingdom as triumphant protectors."
                n "The kingdom, now free from the shadow of the Fallen Hero's wrath, looked to the princess as a symbol of hope."
                n "In time, she took her place as queen, with the hero by her side as her most trusted companion."
                n "Together, they ruled with wisdom and compassion, ensuring that the darkness that once threatened the land would never return."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne
            "(Act) Knock him unconscious":
                n "The hero's focus was sharp, his blade poised for a precise strike. But as he lunged, the Fallen Hero moved with blinding speed, disarming him in a single motion."
                n "The hero stumbled, unarmed, as the Fallen Hero pinned him to the ground, ready to deliver a fatal blow."
                p "No! I won't let you hurt him!"
                scene bg blackscreen
                n "The princess's heart raced as she sprang into action. Grabbing a nearby branch, she rushed forward, striking the Fallen Hero across the head with all her strength."
                n "The force of the blow stunned him, causing him to release the hero and stagger backward."
                n "The princess's quick thinking saved the hero's life as the Fallen Hero collapsed, knocked unconscious by her strike. With the immediate danger passed, the princess rushed to the hero's side, her hands trembling as she tended to his wounds."
                n "The hero's breathing was ragged, but he managed a weak smile, grateful for her courage in the moment that mattered most."
                n "The princess stayed by his side as he recovered, ensuring that his injuries were treated before they dared leave the forest."
                n "Though exhausted and battered, they both knew that this ordeal had strengthened their bond."
                n "The princess's decisive action had not only saved the hero's life but proved that she could stand as his equal in the face of danger."
                n "Once the hero was strong enough, they would return to the kingdom together, carrying the lessons they had learned and the memories of the battle they had won."
                n "And the princess and hero lived happily ever-"

                jump saved_hero

    label fh_choices_5_4:
        # Branching from "(Act) Use magic to disorient him during the charge"
        menu:
            "(Act) Seal him away with forbidden magic":
                n "The princess's voice trembled as she began to chant the forbidden spell, her hands glowing with a dangerous, pulsating energy. The hero's eyes filled with concern, but he knew there was no other way."
                p "We can't let him keep fighting-this is our last option!"
                h "Be careful, princess-this magic comes with a cost!"
                scene bg blackscreen
                n "Ignoring the hero's warning, the princess unleashed the spell. Dark tendrils of magic shot out, wrapping around the Fallen Hero and dragging him to the ground."
                n "He struggled, but the magic was too powerful, forcing him into submission as the darkness closed in. But something went wrong-the spell lashed out in all directions, its chaotic energy striking the hero as well."
                n "The forbidden magic did its job, sealing away the Fallen Hero and stripping him of his power. But the cost was far greater than the princess had anticipated."
                n "The hero, caught in the spell's backlash, began to change-his body twisted, his eyes filled with pain as he fought to maintain control."
                n "The darkness clawed at him, threatening to turn him into something monstrous."
                n "Realizing what was happening, the hero made a final, desperate choice-he drove his own sword through his heart, ending his life before the corruption could fully take hold."
                n "The princess was left alone, her victory hollow as she cradled the hero's lifeless body. Though the Fallen Hero was gone, the price of victory was one she would carry for the rest of her days."
                n "Even as she returned to the kingdom, her heart would remain scarred by the loss of the one she loved most."
                n "And the princess lived happily ever-"

                jump corrupted_hero
            "(Act) Break his weapon with magic":
                n "The princess's hands crackled with energy as she focused her magic on the Fallen Hero's sword. She knew that without his weapon, he would be left vulnerable, giving them a chance to end this fight without further bloodshed."
                p "We have to stop him-destroy his blade, and he won't be able to continue."
                scene bg blackscreen
                n "The hero leapt forward to cover her as she unleashed a burst of magic. The energy surged toward the Fallen Hero's weapon, shattering it into pieces before he could react."
                n "The blade broke apart in his hands, leaving him defenseless and at their mercy."
                n "With his weapon destroyed, the Fallen Hero could no longer continue the fight. Defeated and stripped of his power, he fled deeper into the forest, vanishing from sight."
                n "As the echoes of battle faded, the forest itself seemed to breathe a sigh of relief, its ancient magic stirring in approval of the princess and hero's victory."
                n "The princess and hero, sensing the forest's contentment, chose to remain behind, dedicating their lives to protecting the land from future threats."
                n "Together, they became the forest's guardians, using their magic to maintain balance and ensure that the peace they had fought for would endure."
                n "The forest, satisfied with their presence, offered them a home where they could live in harmony with nature, free from the expectations of the outside world."
                n "And the princess and hero lived happily ever-"

                jump forest_protectors

    label fh_choices_5_5:
        # Branching from "(Act) Push him back and strike"
        menu:
            "(Act) Go for a lethal blow":
                n "The hero gritted his teeth as he pushed the Fallen Hero back, the weight of the battle pressing down on him. The princess saw the desperation in his eyes as he prepared for a final, decisive strike."
                p "Do it-end this!"
                scene bg blackscreen
                n "With a fierce battle cry, the hero lunged forward, aiming for a lethal blow. But as his blade descended, the Fallen Hero's eyes glinted with one last burst of defiance."
                n "In a flash, he sidestepped and turned his sword toward the princess, his intent clear."
                n "The princess barely had time to react before the Fallen Hero's blade cut through the air, aimed straight at her heart."
                n "But in that critical moment, the hero moved without hesitation, shielding her from the fatal strike."
                n "The sword plunged into his chest, and he collapsed, mortally wounded."
                n "The princess's world shattered as she cradled the hero in her arms, watching the light in his eyes fade."
                n "The Fallen Hero, now defeated, staggered back, his life force spent. As he fell, the princess realized that victory had come at too great a cost."
                n "She would return to the kingdom, but her heart would remain with the hero who sacrificed everything to save her."
                n "Though her grief was deep, she knew she would carry on, honoring his memory as she took on the responsibilities ahead."
                n "And the princess lived happily ever-"

                jump sacrificed_hero
            "(Act) Aim to disarm him":
                n "The princess signaled to the hero, urging him to go for the Fallen Hero's weapon rather than a killing blow. She knew that taking away his ability to fight was their best chance of ending this without more bloodshed."
                p "Don't go for the kill-just disarm him!"
                scene bg blackscreen
                n "The hero adjusted his stance, waiting for the right moment. As the Fallen Hero lunged forward, the hero deflected the attack and swiftly struck at his wrist, sending the sword flying from his hand."
                n "But instead of backing down, the Fallen Hero lunged at the hero, determined to end him with his bare hands."
                n "The Fallen Hero's wild charge caught the hero off guard, and he was driven to the ground, the breath knocked out of him."
                n "But just as the Fallen Hero raised his hand for a final strike, the princess acted. With quick reflexes, she grabbed the fallen sword and slashed at the Fallen Hero, forcing him back and saving the hero from certain death."
                n "The battle was over-the princess's quick thinking had turned the tide."
                n "The princess knelt beside the hero, tending to his wounds as he caught his breath. The bond between them had only grown stronger, each knowing they would always protect the other."
                n "Though their journey wasn't over, they would face whatever lay ahead together, returning to the kingdom with newfound confidence in each other's strength."
                n "And the princess and hero lived happily ever-"

                jump saved_hero

    label fh_choices_5_6:
        # Branching from "(Act) Use magic to create an opening"
        menu:
            "(Act) Shatter his defenses with dark energy":
                n "The princess's voice was steady as she whispered an incantation, channeling dark energy into her hands. The magic crackled ominously, carrying a power that could not be easily controlled."
                p "I'll break his defenses-be ready to strike!"
                scene bg blackscreen
                n "The hero nodded, preparing himself as the princess unleashed a surge of dark magic toward the Fallen Hero. The energy tore through the air like a storm, slamming into him with overwhelming force and shattering his defenses."
                n "The dark magic worked too well, tearing through the Fallen Hero's defenses and leaving him broken."
                n "But the victory came at a terrible price-the corrupted energy spread outward, seeping into the forest itself."
                n "Trees withered, the ground cracked open, and a foul mist began to rise, signaling the awakening of an ancient curse."
                n "The princess and hero realized too late what they had unleashed. The forest's wrath chained them to the cursed land, binding them as eternal stewards."
                n "Determined to atone, they chose to stay behind, dedicating their lives to healing the damage they had caused."
                n "The forest, now twisted by dark magic, would forever be their burden, but they found purpose in protecting what remained."
                n "And the princess and hero lived happily ever-"

                jump forest_curse
            "(Act) Restrain him with enchanted chains":
                n "The princess's voice rang out as she began to cast a binding spell, summoning chains of light that snaked through the air toward the Fallen Hero."
                p "I'll hold him down-strike when he's bound!"
                scene bg blackscreen
                n "The hero braced himself as the magical chains wrapped around the Fallen Hero, pulling him to the ground and locking him in place."
                n "The more he struggled, the tighter the chains grew, draining his strength."
                n "The enchanted chains did their job, sealing the Fallen Hero's power and leaving him helpless. With his threat neutralized, the battle was over."
                n "The princess and hero knew that returning to the kingdom would only bring more complications, given the kingdom's disdain for magic."
                n "Instead, they chose to leave that world behind and embrace a life free from the constraints of royal duties and societal expectations."
                n "Together, they ventured into the unknown, eager to build a life where they could be truly free."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after

    label fh_choices_5_7:
        # Branching from "(Act) Distract him with a feint and attack"
        menu:
            "(Act) Teleport away" if chose_magic:
                n "The princess whispered the incantation under her breath, focusing on the magic that would allow them to escape. The Fallen Hero's eyes were locked on her, unaware of her true intentions."
                p "Trust me-we're getting out of here."
                scene bg blackscreen
                n "The hero nodded, grabbing her hand as she completed the spell. In an instant, the magic swirled around them, transporting them away from the battlefield in a flash of light."
                n "The teleportation spell carried the princess and hero far from the dangers of the forest, depositing them in a peaceful glade where the air was filled with the scent of flowers and the sun shone brightly overhead."
                n "Free from the pursuit of the Fallen Hero, they decided not to return to the kingdom, knowing that their use of magic would only lead to further conflict there."
                n "Instead, they chose to explore the world together, embracing the freedom that came with leaving the past behind."
                n "They would build a new life, one defined by the choices they made for themselves, far from the shadows of duty and obligation."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after
            "(Act) Let him surrender willingly":
                n "The hero held back, waiting for the princess's signal. But instead of giving the order to strike, she took a step forward, her voice filled with empathy."
                p "You don't have to keep fighting-there's still a way out for both of us."
                scene bg blackscreen
                n "The Fallen Hero's eyes flickered with hesitation as he considered her offer. For the first time, the rage that had fueled him seemed to waver, as if he was tired of the endless cycle of pain and anger."
                n "The Fallen Hero's grip on his weapon loosened as he made the decision to lower his blade. But just as it seemed that peace was possible, his body stiffened, and he collapsed."
                n "Mortally wounded from the battle, he had pushed himself beyond his limit. As he fell, his sword slipped from his grasp, but in a final moment of defiance, he lashed out at the hero, stabbing him in a wild, desperate strike."
                n "The hero staggered, blood pouring from the wound, knowing it was fatal."
                n "The princess, consumed by grief, realized that she could not go on without him. Choosing love over life, she took up the hero's sword and joined him in death, preferring to spend eternity together rather than live in a world without him."
                n "In the afterlife, they found the happiness that eluded them in life, their love unburdened by pain or fear."
                n "And the princess and hero died happily ever-"

                jump love_beyond_death

    label fh_choices_5_8:
        # Branching from "(Act) Use the environment to trap him"
        menu:
            "(Act) Use a snare trap" if not chose_magic:
                n "The princess's eyes darted across the forest floor, spotting the remnants of an old snare trap. Quickly, she signaled to the hero, who nodded in understanding."
                p "Lead him toward the trap-we'll use it to catch him off guard!"
                scene bg blackscreen
                n "The hero maneuvered carefully, baiting the Fallen Hero into the narrow path. But as they sprung the trap, the Fallen Hero reacted with unnatural speed, turning his attention to the princess."
                n "The snare trap snapped shut, catching the Fallen Hero's leg, but it wasn't enough to stop him. Fueled by desperation, he broke free and charged at the princess with his sword raised."
                n "The hero, realizing the danger, threw himself in front of the strike. The blade pierced his chest, leaving the princess screaming as she watched the hero collapse in a pool of blood."
                n "Though the Fallen Hero was ultimately defeated, the price of victory was paid in the hero's life. The princess cradled him as he took his final breath, her tears falling freely as he whispered his last words of love and loyalty."
                n "The battle was won, but the cost was too high. The princess would return to the kingdom alone, forever marked by the sacrifice of the one who had given everything to protect her."
                n "Yet, in time, she would find a way to carry on, knowing that his memory would always be with her."
                n "And the princess lived happily ever-"

                jump sacrificed_hero
            "(Act) Trap him with magic" if chose_magic:
                n "The princess's fingers crackled with energy as she began to weave a magical snare. The air hummed with power as she focused on binding the Fallen Hero where he stood."
                p "I'll trap him-get ready to strike once he's caught!"
                n "The hero nodded, his grip tightening on his sword as he prepared for the opening. The Fallen Hero advanced, unaware of the snare forming beneath his feet."
                n "With a sudden burst of light, the magical trap snapped shut, ensnaring him in a tangle of glowing chains."
                scene bg blackscreen
                n "The magic held fast, rendering the Fallen Hero immobile. But the power required to maintain the trap was immense, and the dark energy began to spiral out of control."
                n "The spell's backlash surged through the clearing, lashing out toward the hero. The magic corrupted him in an instant, twisting his body and mind as he fought desperately against the transformation."
                n "The hero's eyes filled with fear as he realized what was happening-he was becoming something monstrous, no longer in control of himself."
                n "With the last of his humanity, he took his own life to protect the princess from the creature he was becoming."
                n "The princess, devastated and alone, was left to mourn the hero who had saved her one final time. Though she returned to the kingdom, the burden of loss would forever weigh on her heart."
                n "And the princess lived happily ever-"

                jump corrupted_hero

    label fh_choices_5_9:
        # Branching from "(Act) Bring up his past victories"
        menu:
            "(Act) Remind him of the lives he saved":
                n "The princess's voice was gentle yet firm as she reminded the Fallen Hero of the person he once was."
                p "You saved so many lives. You were a hero-a protector. That man is still in you, isn't he?"
                scene bg blackscreen
                n "The Fallen Hero's eyes flickered, his grip on his weapon loosening as old memories resurfaced. The hero cautiously stepped forward, hoping to capitalize on the moment of doubt."
                n "But the Fallen Hero's bitterness flared back up, and in a desperate rage, he charged at the hero, aiming to strike him down."
                n "The Fallen Hero's attack was fast, too fast for the hero to block. With a savage blow, the hero was knocked to the ground, his weapon flying from his hand."
                n "The Fallen Hero loomed over him, poised to deliver the final strike. But the princess, acting on pure instinct, seized the opportunity."
                n "She grabbed a nearby stone and struck the Fallen Hero from behind, knocking him off balance and giving the hero a chance to recover."
                n "The princess rushed to the hero's side, helping him to his feet. Though wounded and weakened, he managed a grateful smile as she tended to his injuries."
                n "The battle was over-the Fallen Hero, now defeated, lay unconscious at their feet."
                n "The princess and hero knew they had narrowly escaped a tragic end, and as they prepared to return to the kingdom, they felt their bond strengthened by the trials they had faced."
                n "And the princess and hero lived happily ever-"

                jump saved_hero
            "(Act) Teleport away quickly" if chose_magic:
                n "The princess's voice was barely a whisper as she began the incantation, her eyes focused on the space around them. The Fallen Hero advanced, unaware of the spell being woven beneath his feet."
                p "Hold on tight-this will get us out of here."
                scene bg blackscreen
                n "The hero took her hand, trusting her completely as she unleashed the magic. With a flash of light, they vanished from the battlefield, leaving the Fallen Hero standing alone, his chance at revenge lost."
                n "The teleportation spell whisked the princess and hero far away, depositing them in a serene meadow bathed in sunlight."
                n "The tension of the battle melted away as they realized they were finally free from the Fallen Hero's grasp."
                n "Knowing that the kingdom would never accept their use of magic, they made the decision to leave their old lives behind."
                n "Together, they set out to explore the world, embracing the freedom that came with escaping the expectations and burdens of royalty."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after

    label fh_choices_5_10:
        # Branching from "(Act) Highlight the injustice he suffered"
        menu:
            "(Act) Urge him to reclaim his honor":
                n "The princess's voice was filled with conviction as she appealed to the part of the Fallen Hero that still longed for justice."
                p "You were wronged, and I can't change that. But you can still reclaim your honor-prove to them that they were wrong about you."
                scene bg blackscreen
                n "The Fallen Hero's eyes narrowed, his thoughts clearly torn between revenge and the desire to clear his name."
                n "But instead of backing down, he renewed his assault on the hero, determined to end the fight once and for all."
                n "The Fallen Hero's ferocity caught the hero off guard, and with a vicious strike, he disarmed him, sending his sword clattering to the ground."
                n "The hero fell back, defenseless as the Fallen Hero raised his blade for a killing blow. But in that critical moment, the princess stepped forward, raising her voice in a desperate plea."
                p "Stop! This isn't who you are-don't let them take everything from you!"
                n "Her words struck a chord deep within him, causing him to hesitate. The hero, seizing the moment, grabbed his sword and countered, finally disarming the Fallen Hero."
                n "The battle was over, and the princess's intervention had saved the hero from certain death."
                n "As the princess knelt beside the hero to tend to his wounds, they both knew that they had faced their greatest challenge yet and emerged stronger together."
                n "And the princess and hero lived happily ever-"

                jump saved_hero
            "(Act) Push him to let go of his hatred":
                n "The princess's voice softened as she took a step forward, her eyes full of compassion."
                p "Holding onto this hatred is tearing you apart. You don't have to keep suffering like this-let go, and find peace."
                scene bg blackscreen
                n "The Fallen Hero's eyes wavered as the bitterness in his expression flickered. For a moment, it seemed that her words might reach him."
                n "But the years of anger and betrayal were too deeply ingrained, and in a final burst of rage, he lashed out at the hero with all his strength."
                n "The Fallen Hero's wild attack caught the hero off guard, knocking him to the ground. His sword was torn from his grasp as the Fallen Hero, consumed by fury, turned his blade toward the princess."
                n "The hero, refusing to let her be harmed, threw himself in front of her, taking the fatal strike meant for her. The sword plunged into his chest, and he collapsed, blood pouring from the wound."
                n "The princess's scream echoed through the forest as she held the hero close, watching the life drain from his eyes. The Fallen Hero, now spent, fell to his knees as his rage finally burned out."
                n "But the victory was hollow-the hero's sacrifice had come too late to save him."
                n "The princess returned to the kingdom, forever marked by the loss of the one who had given everything for her."
                n "Though she carried the weight of his death, she vowed to live a life worthy of his sacrifice, finding a way to move forward despite the grief that would never fully fade."
                n "And the princess lived happily ever-"

                jump sacrificed_hero

    label fh_choices_5_11:
        # Branching from "(Act) Explain how the kingdom has reformed"
        menu:
            "(Act) Betray and attack with magic" if chose_magic:
                n "The princess's expression shifted, her voice hardening as she prepared to act."
                p "The kingdom has changed-and so have we. But you'll never get the chance to see it."
                scene bg blackscreen
                n "The Fallen Hero's eyes narrowed, sensing the trap just as the princess unleashed a surge of dark magic. The energy crackled with malevolent power as it shot toward him, striking with overwhelming force."
                n "The dark magic tore through the Fallen Hero, shattering his defenses and leaving him crumpled on the ground. But the spell was wild and uncontrollable-its backlash surged outward, striking the hero as well."
                n "As the corrupted energy took hold, the hero's body twisted in agony, his form warping as he fought against the transformation. Realizing he was losing control, the hero made a desperate choice-he drove his own sword into his heart, ending his life before the darkness could fully consume him."
                n "The princess was left alone, her victory tainted by the price she had paid. Though the kingdom was safe from the Fallen Hero, the loss of the hero was a wound that would never heal."
                n "She returned to the kingdom, haunted by the knowledge that her actions had led to the very tragedy she had tried to prevent."
                n "And the princess lived happily ever-"

                jump corrupted_hero
            "(Act) Persuade him to embrace peace":
                n "The princess's voice softened as she reached out, hoping to guide the Fallen Hero away from his path of anger and destruction."
                p "It doesn't have to be this way. You've suffered enough-there's still time to find peace, for all of us."
                scene bg blackscreen
                n "The Fallen Hero's gaze wavered as her words began to reach him. The tension in his posture slowly eased, and for the first time, he seemed open to the possibility of laying down his sword."
                n "But just as the Fallen Hero was about to surrender, his strength gave out. Mortally wounded from the battle, he collapsed, his final breath escaping as his hatred faded away."
                n "As he fell, his sword struck out in a wild arc, catching the hero off guard and delivering a deep wound to his side. The hero staggered, blood pouring from the wound, knowing that he had only moments left to live."
                n "The princess, her heart breaking, could not imagine a life without him. Choosing love over life, she took the hero's hand and ended her own life, joining him in death."
                n "In the afterlife, they found the peace that had eluded them in life, their love finally free from the pain and suffering that had once torn them apart."
                n "And the princess and hero died happily ever-"

                jump love_beyond_death

    label fh_choices_5_12:
        # Branching from "(Act) Offer him a chance to return as a hero"
        menu:
            "(Act) Promise him redemption":
                n "The princess's voice was filled with sincerity as she extended a hand toward the Fallen Hero."
                p "You were a hero once, and you can be one again. Help us rebuild the kingdom-you don't have to be alone anymore."
                scene bg blackscreen
                n "The Fallen Hero's gaze faltered, the weight of his past clashing with the hope in the princess's words. He took a hesitant step forward, considering the offer."
                n "But the years of bitterness still gnawed at him, and in a final act of defiance, he raised his sword, prepared to strike."
                n "The hero moved quickly, intercepting the attack and knocking the Fallen Hero's blade aside. In a swift, decisive motion, he struck back, disarming the Fallen Hero and bringing him to his knees."
                n "The princess's offer of redemption was genuine, but the Fallen Hero could not let go of his pain, and in the end, his stubbornness led to his defeat."
                n "With the threat ended, the princess and hero returned to the kingdom, where the princess took her rightful place as queen."
                n "The Fallen Hero's story became a cautionary tale-a reminder of the dangers of letting grief and anger consume one's soul."
                n "As queen, the princess would rule with the wisdom gained from her journey, with the hero as her steadfast partner by her side."
                n "Together, they would lead the kingdom into a new era, one where hope and justice prevailed."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne
            "(Act) Betray and strike with magic" if chose_magic:
                n "The princess's eyes hardened as she made her decision. The time for words was over-she knew there was only one way to end this."
                p "Redemption? For someone like you? You'll never deserve it."
                scene bg blackscreen
                n "The Fallen Hero's eyes flashed with realization just as the princess unleashed a surge of dark magic. The energy crackled with malevolent force, tearing through the air as it raced toward him."
                n "The hero, too late to react, could only watch as the spell's power tore through the Fallen Hero's defenses."
                n "The dark magic overwhelmed the Fallen Hero, driving him to his knees as his strength gave out. But as the spell reached its peak, its energy spiraled out of control, lashing back toward the hero."
                n "The hero's body convulsed as the corrupted magic twisted him into something monstrous, stripping away his humanity."
                n "In his final moments of clarity, the hero chose to end his own life rather than become the very thing he fought against."
                n "The princess was left alone, her victory hollow and stained by the loss of the one who had stood by her side. Though the kingdom was safe, the darkness that had claimed the hero left an indelible mark on her heart."
                n "She returned to her duties, but the memory of what she had done-and what she had lost-would haunt her forever."
                n "And the princess lived happily ever-"

                jump corrupted_hero

    label fh_choices_5_13:
        # Branching from "(Act) Offer to bring evidence of his innocence"
        menu:
            "(Act) Offer to present proof to the kingdom":
                n "The princess's voice was calm and determined as she made her final offer."
                p "I'll gather the proof myself-I'll clear your name and restore your honor. You'll finally have the justice you deserve."
                scene bg blackscreen
                n "The Fallen Hero's eyes softened, the bitterness in his expression giving way to a glimmer of hope. He nodded slowly, lowering his weapon as he considered the possibility of redemption."
                n "But the wounds of the past ran deep, and as he took a step toward the princess, his strength gave out."
                n "Mortally wounded from the battle, the Fallen Hero collapsed, his life slipping away before the promise of justice could be fulfilled. But in his final moments, he lashed out in desperation, driving his blade into the hero's side."
                n "The hero staggered, knowing the wound was fatal. The princess, unable to bear the thought of living without him, made a choice."
                n "She took the hero's hand and ended her own life, preferring to be with him in death rather than face a world without him."
                n "In the afterlife, the princess and hero found peace together, their love no longer burdened by the pain and tragedy that had marked their journey."
                n "Free from the conflicts of the mortal world, they could finally share the happiness that had always eluded them in life."
                n "And the princess and hero died happily ever-"

                jump love_beyond_death
            "(Act) Betray and shoot a fireball" if chose_magic:
                n "The princess's eyes narrowed as she made her decision. The time for compassion had passed-now, she would use her magic to end this fight once and for all."
                p "You'll never get your redemption, and you'll never escape this forest."
                scene bg blackscreen
                n "The Fallen Hero's eyes widened as he realized what was coming, but it was too late. The princess summoned a blazing fireball, the dark flames crackling with destructive energy."
                n "With a single motion, she hurled it at him, determined to burn him down."
                n "The fireball exploded on impact, engulfing the Fallen Hero in flames. But the spell did more than destroy its target-it unleashed a wave of dark energy that spread throughout the forest, corrupting everything it touched."
                n "The trees withered, and the land turned barren as an ancient curse awoke, binding the princess and hero to the ruined forest."
                n "Realizing that they had caused irreparable harm, the princess and hero chose to remain in the cursed land, dedicating their lives to healing the damage they had wrought."
                n "Though the curse would never fully lift, they found solace in their shared mission, protecting what little remained of the once-vibrant forest."
                n "They became eternal stewards of the land, finding a new kind of peace in their never-ending task."
                n "And the princess and hero lived happily ever-"

                jump forest_curse

    label fh_choices_5_14:
        # Branching from "(Act) Offer to use your authority as princess"
        menu:
            "(Act) Offer to declare his innocence publicly":
                n "The princess's voice was resolute as she made her promise."
                p "As princess, I have the power to clear your name and restore your honor. I'll stand by you in front of the entire kingdom-I'll make sure they hear the truth."
                scene bg blackscreen
                n "The Fallen Hero's gaze wavered, the years of anger and distrust slowly giving way to a sliver of hope. But the memories of betrayal still burned in his heart, and he raised his sword one final time, refusing to trust in words alone."
                n "The hero moved quickly, intercepting the Fallen Hero's strike and disarming him in one swift motion. With his weapon gone, the Fallen Hero finally fell to his knees, his strength spent."
                n "The princess's offer had been genuine, but his own bitterness had led to his downfall. With the conflict resolved, the princess and hero returned to the kingdom, where the princess took her place as queen."
                n "The Fallen Hero's story was remembered as a tragedy, but one that shaped a better future for the kingdom."
                n "The princess and hero ruled together, bringing justice and peace to a land that had once been torn by darkness."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne
            "(Act) Betray and strike with magic" if chose_magic:
                n "The princess's expression hardened as she decided on a course of action. The Fallen Hero could not be allowed to walk away from this fight-his time was up."
                p "Your story ends here-this forest deserves better than to be tainted by your darkness."
                scene bg blackscreen
                n "The Fallen Hero's eyes flashed with realization as the princess gathered her magic. With a determined shout, she unleashed a burst of energy that struck him with unrelenting force."
                n "The hero moved quickly to support her, blocking the Fallen Hero's desperate counterattack as the spell took hold."
                n "The magic shattered the Fallen Hero's defenses, leaving him powerless and broken. As he fell, the forest's ancient magic stirred, recognizing the princess and hero as protectors of the land."
                n "The forest, now free from the threat of the Fallen Hero's corruption, welcomed them as its new guardians."
                n "The princess and hero chose to remain behind, embracing their role as stewards of the forest. Together, they watched over the land, ensuring that it remained safe from any future threats."
                n "The forest flourished under their care, and they found happiness in their shared purpose."
                n "And the princess and hero lived happily ever-"

                jump forest_protectors

    label fh_choices_5_15:
        # Branching from "(Act) Offer to perform a magical oath"
        menu:
            "(Act) Follow through with your promise":
                n "The princess's voice was calm as she extended her hand, magic crackling around her fingertips."
                p "I swear on this magic-we'll stay here and find peace, together. I won't leave until the forest is healed."
                scene bg blackscreen
                n "The Fallen Hero's eyes softened with surprise, but he quickly turned away, unable to accept the possibility of redemption."
                n "But the princess was true to her word. She and the hero remained in the forest, fulfilling their oath to protect the land."
                n "The forest, recognizing the sincerity in the princess's vow, accepted her magic and granted her and the hero a place among its protectors."
                n "The Fallen Hero, no longer a threat, faded into the depths of the forest, leaving the princess and hero to tend to the land."
                n "Together, they nurtured the forest back to life, restoring what had been lost."
                n "Though they could have returned to the kingdom, they chose to stay, finding fulfillment in the quiet peace of their new home."
                n "They vowed to remain in the forest as its guardians, protecting it from any future threats to come."
                n "And the princess and hero lived happily ever-"

                jump forest_protectors
            "(Act) Betray and shoot a fireball":
                n "The princess's eyes narrowed as she made her decision. There was no more room for kindness-she would end this with a single, decisive strike."
                p "You'll never find peace-you'll only find ashes."
                scene bg blackscreen
                n "The Fallen Hero's eyes widened as the princess summoned a fireball, its flames laced with dark magic."
                n "With a swift motion, she hurled it toward him, determined to burn him and everything he stood for to the ground."
                n "The fireball exploded on impact, engulfing the Fallen Hero in flames. But the spell unleashed more than just destruction-it awakened a curse that spread through the forest like wildfire."
                n "The trees twisted into monstrous shapes, and the ground cracked open, releasing a dark mist that bound the princess and hero to the corrupted land."
                n "Realizing their mistake, they chose to remain in the cursed forest, devoting themselves to undoing the damage they had caused."
                n "They would become eternal guardians, seeking redemption through their efforts to heal what had been lost."
                n "And the princess and hero lived happily ever-"

                jump forest_curse

    label fh_choices_5_16:
        # Branching from "(Act) Betray him and prepare to strike"
        menu:
            "(Act) Strike with sword" if not chose_magic:
                n "The princess's eyes met the hero's, and without a word, they both knew what had to be done. They had played along long enough, and now it was time to end it."
                p "Let's finish this-together."
                scene bg blackscreen
                n "The hero nodded, his grip tightening on his sword as they prepared for the decisive strike. With one swift motion, they launched their coordinated attack, the hero's blade gleaming as it arced toward the Fallen Hero."
                n "The hero's strike was swift and true, cutting through the Fallen Hero's defenses. His sword pierced the armor, and the Fallen Hero's eyes widened in shock as his strength left him."
                n "He staggered, finally defeated, as the weight of his past caught up with him."
                n "With the battle won, the princess and hero returned to the kingdom, where the princess took her place as queen."
                n "The hero stood proudly by her side as they ruled with the wisdom and strength forged through their trials."
                n "Together, they would surely bring prosperity to a kingdom that had once been torn by conflict, ensuring that peace would reign for generations to come."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne
            "Act) Strike with magic" if chose_magic:
                n "The princess's voice was resolute as she prepared to unleash her magic. There would be no more pretending-this battle was about to end on her terms."
                p "We'll use our magic to protect this forest and drive him out for good."
                scene bg blackscreen
                n "The hero nodded in agreement, raising his shield as the princess's hands glowed with arcane energy."
                n "With a powerful chant, she unleashed a burst of light, the magic searing through the air toward the Fallen Hero."
                n "The energy coiled around him, binding him in place as the hero moved in for the final blow."
                n "The magic struck true, overwhelming the Fallen Hero and forcing him to retreat deep into the forest, where he could no longer threaten the land."
                n "As he vanished from sight, the forest itself seemed to sigh in relief, its ancient spirits acknowledging the princess and hero as its new guardians."
                n "The princess and hero chose to stay behind, dedicating themselves to protecting the forest from any future threats."
                n "Together, they would watch over the land, ensuring that peace and balance were maintained."
                n "The forest would thrive under their care, and they would find a sense of purpose and fulfillment in their shared role as protectors of the natural world."
                n "And the princess and hero lived happily ever-"

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
    fh "The kingdom took everything from me-my honor, my name, my life. I was left with nothing but this grudge... and a hunger for retribution."

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
    fh "They turned me into this-this monster that hunts in the shadows. But make no mistake, I'm still the same knight I once was... only now, I serve no one but my hatred."

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
    fh "Maybe it won't change anything for them. But for me... it's all I have left. My honor was stolen, my name tarnished, and there's no undoing that."
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
    fh "If ending you serves that purpose, then so be it. But deep down, I know... no bloodshed will ever truly balance the scales."

    return

label fh_what_would_you_do:
    p "What happens if you succeed? What will you do after you get your revenge?"
    n "The Fallen Hero fell silent, as if the question itself was one he had avoided for a long time."
    fh "What would I do...? I've asked myself that many times. Perhaps there is nothing left after that-no life beyond the hatred."
    fh "But if there's nothing more, then at least I'll go down knowing I took them with me. Peace is a lie, princess... the only end for someone like me is a blade in the dark."

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

