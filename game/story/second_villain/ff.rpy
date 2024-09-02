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

    $ ff_times_gotten += 1

    # Leading text
    scene bg Villain with fade
    n "The air was thick with tension as the princess and the hero moved cautiously through the forest, the trees closing in around them like silent sentinels. There was an unsettling calm, as if the forest itself was holding its breath."
    n "The hero scanned the surroundings with narrowed eyes, every sense on high alert. He could feel it—a presence watching them, waiting for the right moment to strike."
    play music "audio/5 Second Villian 3.mp3" loop volume 1.0 fadein 0.5
    scene bg villain_far_ff with dissolve
    n "From the shadows, a figure emerged with a graceful, almost seductive stride. Her eyes glinted with a dangerous intelligence, and a sly smile played on her lips as she sized up the pair."
    ff "Well, well, what do we have here? The princess and her brave protector, still so far from the safety of the kingdom. How... intriguing."
  
    if ff_times_gotten == 1: 
        pt "The Femme Fatale again... Her words are like poison. I need to stay focused." 
 
    elif ff_times_gotten == 2:
        pt "We've dealt with her before. I can't let her get into my head again."
  
    else: 
        pt "Her games won't work this time. I'm ready for whatever she tries."

    n "The Femme Fatale stepped closer, her movements fluid and deliberate. Every word she spoke dripped with honeyed malice, designed to unsettle and disarm."
    h "Stay back, princess. Don't listen to her lies. We have to stay focused."
    ff "Lies? Oh, darling, I don't need to lie. I already know everything there is to know about you. But don't worry, I'm not here to hurt you... not yet, anyway."
    n "Her voice was smooth, almost hypnotic, as she circled them, her gaze flicking between the princess and the hero. The air around them seemed to grow colder, every word a calculated strike at their resolve."
    ff "Let's see how far you're willing to go, princess. Will you sacrifice everything to protect your little hero? Or will you crumble under the weight of your own choices?"

    jump ff_choices_1

    # Level 1 of choice tree
    label ff_choices_1:
        # Initial branch
        menu:
            "(Act) Play her game":
                n "The princess observed the Femme Fatale, noting the sly smile that never left her face. She knew this wasn't an opponent she could simply overpower."
                p "You seem to be enjoying this little game. Why don't we see who's really the better player?"
                n "The Femme Fatale's eyes gleamed with amusement, her lips curling into a smirk."
                ff "Oh, darling, I do love it when my opponents think they can outwit me. Let's see if you're as clever as you think."
                n "The hero shot a concerned glance at the princess, unsure of her approach, but he tightened his grip on his sword, ready for anything."
                h "Careful, princess. This is what she wants."

                jump ff_choices_2_1

            "(Act) Engage her directly":
                n "The princess's expression hardened as she faced the Femme Fatale, cutting straight through her manipulative charm."
                p "I see through your lies and games. Let's get to the truth—why are you doing this?"
                n "The Femme Fatale laughed, the sound light and sweet like poisoned honey."
                ff "How boring. Always trying to peel back the layers, to find some grand reason behind it all. Maybe I just enjoy the thrill, darling. Have you considered that?"
                n "The hero stepped forward, ready to charge at a moment's notice. His eyes flicked to the princess, waiting for her command."
                h "I'm ready when you are, princess. Just say the word."

                jump ff_choices_2_2


            # Dialogue pool options

            "(Inquire) Who are you?" if not ff_chose_who_are_you:
                $ ff_chose_who_are_you = True
                call ff_who_are_you
                jump ff_choices_1

            "(Inquire) Why are you doing this?" if not ff_chose_why_doing_this and ff_chose_who_are_you:
                $ ff_chose_why_doing_this = True
                call ff_why_doing_this
                jump ff_choices_1

            "(Inquire) What do you gain from tormenting others?" if not ff_chose_what_you_gain and ff_chose_why_doing_this:
                $ ff_chose_what_you_gain = True
                call ff_what_you_gain
                jump ff_choices_1

            "(Inquire) Why do you enjoy manipulating people?" if not ff_chose_why_enjoy_manipulating:
                $ ff_chose_why_enjoy_manipulating = True
                call ff_why_enjoy_manipulating
                jump ff_choices_1

            "(Inquire) Isn't there more to life than games and deceit?" if not ff_chose_isnt_there_more and ff_chose_why_enjoy_manipulating:
                $ ff_chose_isnt_there_more = True
                call ff_isnt_there_more
                jump ff_choices_1

            "(Inquire) Do you not care about the harm you cause?" if not ff_chose_do_you_not and ff_chose_isnt_there_more:
                $ ff_chose_do_you_not = True
                call ff_do_you_not
                jump ff_choices_1
            
            "(Inquire) How did you become like this?" if not ff_chose_how_did_you:
                $ ff_chose_how_did_you = True
                call ff_how_did_you
                jump ff_choices_1

            "(Inquire) Was there ever a time when you cared about anyone?" if not ff_chose_was_there_ever and ff_chose_how_did_you:
                $ ff_chose_was_there_ever = True
                call ff_was_there_ever
                jump ff_choices_1

            "(Inquire) Do you think you can ever change?" if not ff_chose_do_you_think and ff_chose_was_there_ever:
                $ ff_chose_do_you_think = True
                call ff_do_you_think
                jump ff_choices_1

            "(Inquire) What do you really want from us?" if not ff_chose_what_do_you:
                $ ff_chose_what_do_you = True
                call ff_what_do_you
                jump ff_choices_1

            "(Inquire) Is this just a game to you?" if not ff_chose_is_this_just and ff_chose_what_do_you:
                $ ff_chose_is_this_just = True
                call ff_is_this_just
                jump ff_choices_1

            "(Inquire) When will it end?" if not ff_chose_when_will_it and ff_chose_is_this_just:
                $ ff_chose_when_will_it = True
                call ff_when_will_it
                jump ff_choices_1


    # Level 2 of choice tree
    label ff_choices_2_1:
        # Branching from "(Act) Play her game"
        menu:
            "(Act) Flatter her and pretend to be impressed":
                n "The princess adopted a softer tone, leaning into the Femme Fatale's vanity."
                p "You're incredible... It's no wonder you've outwitted so many. I can see why people fear you—you have such a sharp mind and grace."
                n "The Femme Fatale's smile grew wider, clearly savoring the praise. Her eyes gleamed with satisfaction."
                ff "Well, I'm glad someone here appreciates true talent. It's rare to find anyone who can recognize brilliance when they see it."
                n "The princess exchanged a subtle look with the hero, who gave a slight nod. They were both aware this was all part of her ploy, but it was a necessary step in gaining the upper hand."

                jump ff_choices_3_1
            "(Act) Feign weakness and vulnerability":
                n "The princess took a different approach, letting her voice waver as she pretended to be overwhelmed."
                p "Please... We're not here to fight. We just want to get through this. You're clearly in control—what chance do we even have against someone like you?"
                n "The Femme Fatale's eyes narrowed, assessing the princess's words. There was a hint of suspicion in her gaze, but her posture relaxed slightly."
                ff "Giving up so easily? How disappointing. I expected more of a challenge. Still, it's only natural to submit when you know you're outmatched."
                n "The princess kept her expression subdued, knowing that showing any sign of defiance too early would ruin the ruse. Meanwhile, the hero watched, ready to spring into action if things went south."

                jump ff_choices_3_2

            
            # Dialogue pool options

            "(Inquire) Who are you?" if not ff_chose_who_are_you:
                $ ff_chose_who_are_you = True
                call ff_who_are_you
                jump ff_choices_2_1

            "(Inquire) Why are you doing this?" if not ff_chose_why_doing_this and ff_chose_who_are_you:
                $ ff_chose_why_doing_this = True
                call ff_why_doing_this
                jump ff_choices_2_1

            "(Inquire) What do you gain from tormenting others?" if not ff_chose_what_you_gain and ff_chose_why_doing_this:
                $ ff_chose_what_you_gain = True
                call ff_what_you_gain
                jump ff_choices_2_1

            "(Inquire) Why do you enjoy manipulating people?" if not ff_chose_why_enjoy_manipulating:
                $ ff_chose_why_enjoy_manipulating = True
                call ff_why_enjoy_manipulating
                jump ff_choices_2_1

            "(Inquire) Isn't there more to life than games and deceit?" if not ff_chose_isnt_there_more and ff_chose_why_enjoy_manipulating:
                $ ff_chose_isnt_there_more = True
                call ff_isnt_there_more
                jump ff_choices_2_1

            "(Inquire) Do you not care about the harm you cause?" if not ff_chose_do_you_not and ff_chose_isnt_there_more:
                $ ff_chose_do_you_not = True
                call ff_do_you_not
                jump ff_choices_2_1
            
            "(Inquire) How did you become like this?" if not ff_chose_how_did_you:
                $ ff_chose_how_did_you = True
                call ff_how_did_you
                jump ff_choices_2_1

            "(Inquire) Was there ever a time when you cared about anyone?" if not ff_chose_was_there_ever and ff_chose_how_did_you:
                $ ff_chose_was_there_ever = True
                call ff_was_there_ever
                jump ff_choices_2_1

            "(Inquire) Do you think you can ever change?" if not ff_chose_do_you_think and ff_chose_was_there_ever:
                $ ff_chose_do_you_think = True
                call ff_do_you_think
                jump ff_choices_2_1

            "(Inquire) What do you really want from us?" if not ff_chose_what_do_you:
                $ ff_chose_what_do_you = True
                call ff_what_do_you
                jump ff_choices_2_1

            "(Inquire) Is this just a game to you?" if not ff_chose_is_this_just and ff_chose_what_do_you:
                $ ff_chose_is_this_just = True
                call ff_is_this_just
                jump ff_choices_2_1

            "(Inquire) When will it end?" if not ff_chose_when_will_it and ff_chose_is_this_just:
                $ ff_chose_when_will_it = True
                call ff_when_will_it
                jump ff_choices_2_1

    label ff_choices_2_2:
        # Branching from "(Act) Engage her directly"
        menu:
            "(Act) Have the hero charge with his sword":
                n "The princess gave a sharp nod to the hero, who gripped his sword tightly before charging forward, his expression fierce."
                p "Now, while she's distracted!"
                n "The Femme Fatale's eyes widened in surprise as the hero rushed at her with startling speed, his blade arcing toward her."
                scene bg villain_hero_charging_far_ff with dissolve
                ff "Oh, how crude. But effective, I suppose!"
                n "At the last moment, she twirled out of the way with elegant precision, her daggers flashing as she countered with a swift strike."
                scene bg villain_far_ff with dissolve
                h "She's quick—much faster than she looks!"
                n "The hero barely managed to parry the attack, the clash of steel ringing out as the Femme Fatale's smirk returned."
                ff "I expected nothing less from a brute like you."

                jump ff_choices_3_3
            "(Act) Confront her about her deception":
                n "The princess's voice cut through the Femme Fatale's amusement, sharp and unwavering."
                p "You can drop the act. You're hiding something—something that goes beyond your games and lies. Why don't you tell us the real reason you're here?"
                n "The Femme Fatale's eyes narrowed dangerously, but her smile never wavered."
                ff "Oh, you think you've figured it out? How adorable. But darling, if I'm hiding something, it's only because it's none of your concern."
                n "The princess held her ground, refusing to be swayed by the Femme Fatale's dismissive tone. The hero stepped closer, ready for whatever came next."
                h "She's definitely hiding something, princess. We just need to push her a bit further."

                jump ff_choices_3_4


            # Dialogue pool options

            "(Inquire) Who are you?" if not ff_chose_who_are_you:
                $ ff_chose_who_are_you = True
                call ff_who_are_you
                jump ff_choices_2_2

            "(Inquire) Why are you doing this?" if not ff_chose_why_doing_this and ff_chose_who_are_you:
                $ ff_chose_why_doing_this = True
                call ff_why_doing_this
                jump ff_choices_2_2

            "(Inquire) What do you gain from tormenting others?" if not ff_chose_what_you_gain and ff_chose_why_doing_this:
                $ ff_chose_what_you_gain = True
                call ff_what_you_gain
                jump ff_choices_2_2

            "(Inquire) Why do you enjoy manipulating people?" if not ff_chose_why_enjoy_manipulating:
                $ ff_chose_why_enjoy_manipulating = True
                call ff_why_enjoy_manipulating
                jump ff_choices_2_2

            "(Inquire) Isn't there more to life than games and deceit?" if not ff_chose_isnt_there_more and ff_chose_why_enjoy_manipulating:
                $ ff_chose_isnt_there_more = True
                call ff_isnt_there_more
                jump ff_choices_2_2

            "(Inquire) Do you not care about the harm you cause?" if not ff_chose_do_you_not and ff_chose_isnt_there_more:
                $ ff_chose_do_you_not = True
                call ff_do_you_not
                jump ff_choices_2_2
            
            "(Inquire) How did you become like this?" if not ff_chose_how_did_you:
                $ ff_chose_how_did_you = True
                call ff_how_did_you
                jump ff_choices_2_2

            "(Inquire) Was there ever a time when you cared about anyone?" if not ff_chose_was_there_ever and ff_chose_how_did_you:
                $ ff_chose_was_there_ever = True
                call ff_was_there_ever
                jump ff_choices_2_2

            "(Inquire) Do you think you can ever change?" if not ff_chose_do_you_think and ff_chose_was_there_ever:
                $ ff_chose_do_you_think = True
                call ff_do_you_think
                jump ff_choices_2_2

            "(Inquire) What do you really want from us?" if not ff_chose_what_do_you:
                $ ff_chose_what_do_you = True
                call ff_what_do_you
                jump ff_choices_2_2

            "(Inquire) Is this just a game to you?" if not ff_chose_is_this_just and ff_chose_what_do_you:
                $ ff_chose_is_this_just = True
                call ff_is_this_just
                jump ff_choices_2_2

            "(Inquire) When will it end?" if not ff_chose_when_will_it and ff_chose_is_this_just:
                $ ff_chose_when_will_it = True
                call ff_when_will_it
                jump ff_choices_2_2


    # Level 3 of choice tree
    label ff_choices_3_1:
        # Branching from "(Act) Flatter her and pretend to be impressed"
        menu:
            "(Act) Compliment her cunning":
                n "The princess kept her tone sweet and admiring, knowing this was the best way to keep the Femme Fatale talking."
                p "It's amazing how effortlessly you play these games. You always seem to be ten steps ahead—how do you do it? I wish I had your insight."
                n "The Femme Fatale chuckled softly, her eyes gleaming with satisfaction."
                ff "Flattery will get you everywhere, darling. But it's more than just insight—it's about knowing how to twist every situation to your advantage. Most people are so predictable—like pieces on a chessboard."
                n "The princess nodded thoughtfully, hiding her true intentions behind a mask of admiration. She exchanged a brief glance with the hero, signaling that they were getting closer to what they needed."

                jump ff_choices_4_1
            "(Act) Question her motives subtly" if chose_magic:
                n "The princess's tone grew more curious, as if she were genuinely intrigued by the Femme Fatale's reasons for her actions."
                p "You must have your reasons for all this—clearly, it's not just for fun. What drives someone as brilliant as you? Surely you're aiming for something greater than just playing with people's lives."
                n "The Femme Fatale's expression tightened slightly, but she quickly masked it with another smile."
                ff "Ah, the inevitable question of ‘why.' It's always the same, isn't it? Everyone wants to know the grand plan, the deeper purpose. But let me tell you a secret—sometimes, the game itself is the goal."
                n "The princess noticed the flicker of something more behind her words—a hint of bitterness, perhaps? The hero caught the shift as well, his stance tensing as they prepared for what might come next."

                jump ff_choices_4_2

    label ff_choices_3_2:
        # Branching from "(Act) Feign weakness and vulnerability"
        menu:
            "(Act) Appear desperate for her help":
                n "The princess's voice grew softer, tinged with desperation."
                p "Please... I don't know what else to do. You're clearly more capable than us. If we're going to survive this, we need someone like you to guide us."
                n "The Femme Fatale raised an eyebrow, intrigued by the princess's sudden display of helplessness."
                ff "How amusing. You think I'd waste my time helping the likes of you? Still, I do enjoy watching people grovel—it's so... satisfying."
                n "The princess swallowed her pride, lowering her gaze as if in defeat. Meanwhile, the hero watched silently, ready to act if the charade failed."

                jump ff_choices_4_3
            "(Act) Ask for guidance in using magic" if chose_magic:
                n "The princess's tone shifted, becoming eager and deferential as she leaned into the Femme Fatale's expertise."
                p "I know you have such a command over magic—it's incredible. I can barely control my own power. If you taught me, maybe I could at least be useful to you."
                n "The Femme Fatale's eyes glinted with interest, clearly intrigued by the princess's offer."
                ff "You wish to learn from me? How flattering. I suppose I could show you a thing or two—if only to prove how outclassed you really are."
                n "The princess nodded eagerly, masking her true intentions. The hero exchanged a wary glance with her, unsure of where this was heading."

                jump ff_choices_4_4

    label ff_choices_3_3:
        # Branching from "(Act) Have the hero charge with his sword"
        menu:
            "(Act) Aim for her weak spots" if not chose_magic:
                n "The princess's eyes narrowed, noticing the gaps in the Femme Fatale's defense—small but exploitable."
                p "Her left side! Go for it!"
                n "The hero adjusted his stance, zeroing in on the weak spot as he launched his next strike."
                scene bg villain_hero_charging_far_ff with dissolve
                h "I've got it!"
                n "But the Femme Fatale anticipated the move, twisting away with fluid grace. Her daggers lashed out in response, forcing the hero to retreat."
                scene bg villain_far_ff with dissolve
                ff "Did you really think you could take advantage of me? You'll have to be quicker than that."
                n "The princess bit her lip in frustration, realizing that she would have to come up with a better plan."

                jump ff_choices_4_5
            "(Act) Distract her and strike when she lunges":
                n "The princess signaled to the hero with a quick glance, silently communicating her plan."
                p "Get ready—let her think she has the upper hand, then counter when she overextends!"
                n "The hero nodded, feigning an opening as he waited for the Femme Fatale to strike."
                scene bg villain_hero_sword_facing_far_ff with dissolve
                h "Come on, then. Let's see what you've got."
                n "The Femme Fatale smirked, her eyes gleaming with malicious delight as she lunged forward, aiming straight for the hero's exposed side."
                ff "So predictable—"
                n "But the hero's trap snapped shut as he sidestepped her lunge, spinning to land a counterstrike that forced her back."
                scene bg villain_far_ff with dissolve
                h "Got you that time!"
                n "The Femme Fatale hissed in irritation, her smirk momentarily replaced with a scowl."

                jump ff_choices_4_6

    label ff_choices_3_4:
        # Branching from "(Act) Confront her about her deception"
        menu:
            "(Act) Accuse her of hiding something":
                n "The princess's voice grew colder, cutting through the Femme Fatale's facade."
                p "You're not just playing games for fun—there's something else going on here. What are you really after?"
                n "The Femme Fatale's smile didn't waver, but her eyes darkened with a hint of menace."
                ff "Curiosity killed the cat, darling. But you're right—there's always more than meets the eye. Unfortunately for you, some secrets are best left buried."
                n "The princess held her ground, refusing to back down. The hero gripped his sword, ready to strike if the conversation took a dangerous turn."
                h "She's definitely hiding something. We just need to push a little harder."
                
                jump ff_choices_4_7
            "(Act) Challenge her to prove her superiority":
                n "The princess's tone turned mocking, daring the Femme Fatale to show her true strength."
                p "You talk a big game, but is that all you've got? If you're really as superior as you claim, why not prove it instead of hiding behind all these tricks?"
                n "The Femme Fatale's eyes flashed with anger, her smug expression shifting into something more predatory."
                ff "You dare question me? Very well—I'll show you exactly why you should fear me."
                n "The hero tensed, readying himself for the inevitable clash. The Femme Fatale's grip tightened on her daggers as she prepared to make her move."
                h "Careful, princess. She's dangerous when provoked."

                jump ff_choices_4_8

    
    # Level 4 of choice tree
    label ff_choices_4_1:
        # Branching from "(Act) Compliment her cunning"
        menu:
            "(Act) Offer to join forces with her" if chose_magic:
                n "The princess let a hint of admiration color her tone as she made her next move."
                p "You're right—most people are predictable and weak. But what if you didn't have to play this game alone? Together, we could achieve more than anyone could stand against."
                n "The Femme Fatale's eyes sparkled with interest, her smile curling into something more genuine."
                ff "Ah, an alliance? How delightfully ambitious of you. But tell me, darling, are you truly capable of matching my level of finesse? Or would I just be dragging dead weight along with me?"
                n "The princess maintained her poised expression, knowing that this was her moment to convince the Femme Fatale—or trick her. The hero glanced at the princess, wary of where this conversation might lead."
                h "This could be a trap, princess. Be careful how you answer."

                jump ff_choices_5_1
            "(Act) Lure her into overconfidence and trap her":
                n "The princess kept up her admiring tone, pushing the Femme Fatale to let her guard down even further."
                p "With all your skill and brilliance, it must be exhausting to deal with opponents who can't even keep up with you. It's almost unfair—like watching someone play with toys."
                n "The Femme Fatale's smile widened as she soaked in the praise, clearly pleased with herself."
                ff "Oh, you do know how to stroke a girl's ego, don't you? But you're absolutely right—these little games become dull when there's no challenge involved. But, I suppose it's still fun toying with those who think they're clever."
                n "The princess exchanged a quick glance with the hero, who subtly positioned himself for an ambush. They both knew they had to exploit this moment when the Femme Fatale's arrogance reached its peak."
                h "She's getting overconfident, princess. Now's our chance."

                jump ff_choices_5_2

    label ff_choices_4_2:
        # Branching from "(Act) Question her motives subtly"
        menu:
            "(Act) Pretend to agree with her goals":
                n "The princess's voice took on a conspiratorial tone, as if she were finally beginning to see things from the Femme Fatale's perspective."
                p "You know, you're right—most people don't see the bigger picture. They're so limited in their thinking. I can see why you've taken matters into your own hands."
                n "The Femme Fatale's expression shifted slightly, her gaze sharpening as she considered the princess's words."
                ff "Oh? So you're beginning to understand, are you? It's refreshing to meet someone with a bit of vision, someone who can see beyond the petty rules and moral constraints that bind most fools."
                n "The princess nodded slowly, pretending to be drawn in by the Femme Fatale's twisted logic. The hero watched cautiously, knowing that any slip in their act could be dangerous."
                h "Princess, don't let her drag you in too deep. Remember what's at stake."

                jump ff_choices_5_3
            "(Act) Provoke her to reveal her true intentions":
                n "The princess's voice turned more direct, challenging the Femme Fatale with a subtle edge."
                p "You talk about having a higher purpose, but I wonder—do you even know what you're really after? Or are you just hiding behind all this manipulation because you're afraid to confront the truth yourself?"
                n "The Femme Fatale's eyes flashed with irritation, the playful lilt in her voice momentarily dropping."
                ff "Afraid? How cute that you think you've hit a nerve. But perhaps I do have intentions that go beyond your understanding. You're far too naive to grasp the complexities at play here."
                n "The princess held her ground, refusing to let the Femme Fatale regain control of the conversation. Meanwhile, the hero tensed, ready for the confrontation to escalate."
                h "She's losing patience, princess. Keep pushing—we might be able to get her to slip up."

                jump ff_choices_5_4

    label ff_choices_4_3:
        # Branching from "(Act) Appear desperate for her help"
        menu:
            "(Act) Beg her for protection":
                n "The princess lowered her voice, making herself seem as pitiful as possible."
                p "You're so much stronger than us. I don't know how we can possibly survive without your help. If you protect us, we'll do whatever you ask."
                n "The Femme Fatale's smile grew wicked as she leaned in, clearly savoring the princess's submission."
                ff "Begging for mercy already? How utterly delicious. But I must say, there's something appealing about having someone as desperate as you under my control. You might just be useful after all."
                n "The princess kept her expression one of fearful compliance, but her mind was racing for a way to turn the situation in their favor. The hero's grip tightened on his sword, prepared to act if things took a darker turn."
                h "I don't like this, princess. She's enjoying this far too much."

                jump ff_choices_5_5
            "(Act) Pretend to surrender":
                n "The princess took a deep breath, letting her shoulders sag in mock defeat."
                p "You win. We don't stand a chance against someone like you. If you're going to take us, let's at least make it quick."
                n "The Femme Fatale's eyes gleamed with triumph as she moved closer, clearly confident that she'd won."
                ff "Such a wise decision, darling. Submission suits you far better than defiance. Now, be a good girl and accept your fate."
                n "But the moment she let her guard down, the princess's demeanor changed in an instant. The hero's eyes met hers, ready to act the second she struck."

                jump ff_choices_5_6

    label ff_choices_4_4:
        # Branching from "(Act) Ask for guidance in using magic"
        menu:
            "(Act) Learn her techniques and betray her":
                n "The princess leaned in, adopting a tone of eager curiosity."
                p "Teach me. I want to understand how you wield your magic so flawlessly. If I'm going to survive in this world, I need to learn from the best."
                n "The Femme Fatale's smirk returned, clearly delighted by the princess's apparent willingness to learn."
                ff "Flattery and ambition—two traits I can respect. Very well, I'll teach you a few tricks, though I doubt you'll ever fully grasp my methods."
                n "The princess listened intently, feigning awe as the Femme Fatale began to explain her techniques, weaving dark magic through the air with practiced grace. The hero watched from the sidelines, concern etched into his expression."
                h "Be careful, princess. The more you learn, the more dangerous this becomes."
                n "But the princess knew exactly what she was doing. As the Femme Fatale grew absorbed in her own power, the princess prepared for the perfect moment to turn the tables."

                jump ff_choices_5_7
            "(Act) Use her own spells against her":
                n "The princess pretended to be in awe, following the Femme Fatale's instructions with exaggerated enthusiasm."
                p "You make it look so easy... Maybe if I practice enough, I can at least come close to your level."
                n "The Femme Fatale chuckled, a mixture of condescension and amusement lacing her voice."
                ff "Oh, darling, you could spend a lifetime practicing and still never reach my level. But I'll admit, it's amusing to watch you try."
                n "As the Femme Fatale demonstrated a spell, the princess carefully mimicked her movements, secretly altering the spell's structure. The hero's eyes narrowed as he realized what the princess was attempting."
                h "She's giving away her secrets, princess. Turn them against her before she notices what you're doing."
                n "The Femme Fatale remained oblivious, too absorbed in her own performance to notice the trap being laid for her."

                jump ff_choices_5_8

    label ff_choices_4_5:
        # Branching from "(Act) Aim for her weak spots"
        menu:
            "(Act) Strike at her unarmored side":
                n "The princess's gaze locked onto the vulnerable spot, a gap in the Femme Fatale's armor that was barely visible."
                p "There—her side! It's exposed!"
                n "The hero moved swiftly, driving his blade toward the unarmored spot with precision. The Femme Fatale's eyes widened as she realized her mistake."
                scene bg villain_hero_charging_far_ff with dissolve
                ff "You think you've found an opening? How quaint."
                n "But the hero's strike was relentless, and the blade found its mark. The Femme Fatale hissed in pain, staggering back as blood stained her elegant dress. Her smile wavered, but the malice in her eyes burned even brighter."
                scene bg villain_far_ff with dissolve
                ff "Congratulations, darling. You've managed to draw blood. But you'll regret making me bleed."
                n "The princess tensed, knowing that an injured Femme Fatale was far more dangerous, her rage fueling every move. The hero prepared for another attack, ready to exploit the opening he'd created."
                jump ff_choices_5_9

            "(Act) Go for a quick, decisive blow":
                n "The princess's voice was sharp, urging the hero to finish the fight before the Femme Fatale could recover."
                p "Now! Don't give her a chance to retaliate—end this!"
                n "The hero surged forward, his sword aimed directly at the Femme Fatale's heart. Her eyes widened in surprise at the sudden speed of the attack."
                scene bg villain_hero_charging_far_ff with dissolve
                ff "You're faster than I gave you credit for... but not fast enough."
                n "At the last moment, the Femme Fatale twisted away, the blade narrowly missing her vital point. But the hero's momentum carried him forward, and with a quick adjustment, he slashed across her midsection, leaving a deep wound."
                scene bg villain_far_ff with dissolve
                h "You're finished!"
                n "The Femme Fatale staggered back, clutching her wound. Her smile faded, replaced by a look of cold fury. But even in her weakened state, the venom in her gaze was as sharp as ever."
                ff "Impressive, but you've made a fatal mistake if you think I'm done yet."

                jump ff_choices_5_10

    label ff_choices_4_6:
        # Branching from "(Act) Distract her and strike when she lunges"
        menu:
            "(Act) Let her tire herself out before countering":
                n "The princess gave a subtle signal to the hero, instructing him to bait the Femme Fatale into attacking recklessly."
                p "Make her chase you—wear her down until she's vulnerable."
                n "The hero nodded, adjusting his stance as he prepared to dodge and evade rather than strike. The Femme Fatale's eyes gleamed with irritation, realizing she was being toyed with."
                scene bg villain_hero_sword_facing_far_ff with dissolve
                ff "Running away, are we? Pathetic. But if that's how you want to play, I'll indulge you... for now."
                n "She lunged forward, her daggers flashing with deadly precision, but the hero sidestepped with practiced ease, forcing her to overextend herself."
                scene bg villain_far_ff with dissolve
                h "Come on—keep chasing me. Let's see how long you can keep up."
                n "With each failed strike, the Femme Fatale's movements grew more erratic, her frustration mounting. The princess watched closely, waiting for the perfect moment to strike back."
                p "Just a little longer—she's tiring herself out."

                jump ff_choices_5_11
            "(Act) Knock her off balance and disarm her" if not chose_magic:
                n "The princess's eyes focused on the Femme Fatale's footing, noticing a slight instability in her stance."
                p "Now! Go for her legs—throw her off balance!"
                n "The hero feinted high before dropping low, sweeping his leg in a quick motion that caught the Femme Fatale by surprise. Her graceful movements faltered as she stumbled, momentarily losing her balance."
                scene bg villain_hero_charging_far_ff with dissolve
                ff "You insolent little—"
                n "Before she could regain her footing, the hero struck again, knocking one of her daggers from her hand. It clattered to the ground, leaving her momentarily defenseless."
                scene bg villain_far_ff with dissolve
                h "Got you!"
                p "Don't let her recover—she's at her weakest now."

                jump ff_choices_5_12

    label ff_choices_4_7:
        # Branching from "(Act) Accuse her of hiding something"
        menu:
            "(Act) Challenge her to reveal her secrets" if chose_magic:
                n "The princess's voice cut through the tension, daring the Femme Fatale to drop her charade."
                p "You're hiding something—why don't you show us what you're really capable of? Or are you afraid that your little secrets aren't as impressive as you claim?"
                n "The Femme Fatale's eyes narrowed, her smile sharpening into something more dangerous."
                ff "Afraid? Darling, you're sorely mistaken. But if you insist, I'll give you a taste of what true power looks like."
                n "Her hand twitched, dark energy gathering at her fingertips. The air crackled with a sinister energy as she prepared to unleash a spell."
                ff "You wanted a show? Then watch closely. I'll make sure it's unforgettable."
                n "The princess held her breath, knowing they had pushed the Femme Fatale into revealing more of her hand. The hero gripped his sword tightly, ready to react at a moment's notice."
                h "This could be the opening we need, but we have to be quick—she's not someone to underestimate."

                jump ff_choices_5_13
            "(Act) Force her to admit her weaknesses":
                n "The princess's tone grew colder, striking directly at the Femme Fatale's pride."
                p "You put on a convincing act, but deep down, you're just as vulnerable as anyone else. You hide behind your charm because you're afraid of being exposed. Admit it—you're not as invincible as you pretend to be."
                n "The Femme Fatale's smile wavered, a flicker of doubt crossing her eyes before she masked it with her usual smirk."
                ff "How cute. Trying to dig beneath the surface, thinking you've uncovered some deep flaw. But you're wrong, darling—I've turned my weaknesses into weapons. And you've just given me another reason to use them."
                n "The hero's eyes narrowed, sensing the Femme Fatale's anger bubbling just beneath the surface."
                h "She's rattled, princess. We might have a chance if we keep pressing her."
                n "The princess nodded, knowing that exposing the Femme Fatale's vulnerabilities was their best shot at breaking her control over the situation."

                jump ff_choices_5_14

    label ff_choices_4_8:
        # Branching from "(Act) Challenge her to prove her superiority"
        menu:
            "(Act) Goad her into a one-on-one duel":
                n "The princess's voice dripped with mockery as she issued a direct challenge."
                p "All your talk of superiority, and yet you rely on tricks and schemes. Why not settle this the old-fashioned way—no magic, just skill. Unless, of course, you're worried you can't win without cheating."
                n "The Femme Fatale's eyes flashed with fury, her pride stung by the princess's taunt."
                ff "You dare challenge me? Fine—let's see if you can handle a real fight. No more games."
                n "She brandished her daggers with a flourish, her graceful demeanor giving way to a cold, lethal intent. The hero shot a concerned glance at the princess, uncertain if this was the right move."
                h "Careful, princess—she's more dangerous than she looks."
                n "But the princess knew that this was the only way to level the playing field, forcing the Femme Fatale to abandon her tricks and fight directly."

                jump ff_choices_5_15
            "(Act) Pretend to be impressed, then strike when she's distracted" if not chose_magic:
                n "The princess adopted a wide-eyed expression, feigning admiration for the Femme Fatale's prowess."
                p "You really are incredible—I've never seen anyone move like that. It's no wonder you've never lost a game. You must be unstoppable."
                n "The Femme Fatale's smile returned in full force, clearly savoring the praise. Her posture relaxed slightly, her guard lowering just enough."
                ff "Flattery will get you everywhere, darling. But do keep going—I never tire of hearing how brilliant I am."
                n "The princess exchanged a quick glance with the hero, signaling him to prepare for a surprise strike while the Femme Fatale basked in her own vanity."
                h "She's distracted—this is our chance."
                n "The princess nodded subtly, every muscle tensed as she waited for the perfect moment to shatter the Femme Fatale's illusion of control."

                jump ff_choices_5_16


    # Level 5 of choice tree
    label ff_choices_5_1:
        # Branching from "(Act) Offer to join forces with her"
        menu:
            "(Act) Betray her at the last moment":
                n "The princess pretended to be swayed by the Femme Fatale's honeyed words, letting the villain's confidence grow unchecked. Her smile widened, savoring the taste of victory that seemed inevitable."
                ff "You see? Together, we can rewrite the world as we see fit, free from the constraints of those who fear our power."
                n "The princess met the hero's eyes, her heart heavy with the choice she was about to make. They had come too far to turn back now—this was the moment everything would change."
                p "You're right... But power comes with a price."
                n "Just as the Femme Fatale began to bask in her perceived triumph, the princess's expression hardened. Dark energy crackled in her hands, ready to strike the moment the villain dropped her guard."
                ff "What are you—"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "Before she could finish, the princess unleashed a blast of magic, aimed directly at the Femme Fatale's chest. The spell struck true, sending the villain reeling in shock."
                n "The Femme Fatale's laughter turned to a scream of fury as she realized she had been betrayed. Her body crumpled to the ground, lifeless, a victim of her own hubris."
                n "But the cost of victory was high. As the last echoes of the battle faded, the hero rushed to the princess's side—only to find her lifeless on the forest floor, her body drained by the spell's backlash."
                n "Desperate and unwilling to accept her death, the hero did the unthinkable—he used forbidden magic to bring her back. The princess's eyes fluttered open, filled with gratitude and confusion as she realized what he had done."
                n "But their reunion was short-lived. The kingdom, upon learning of the hero's taboo act, branded him a danger and exiled him for defying nature's laws."
                n "The princess, alive but forever marked by tragedy, was forced to carry on alone, haunted by the love that could never be fulfilled."
                n "And the princess lived happily ever—"

                jump unfulfilled_love
            "(Act) Teleport away once she's distracted":
                n "The princess nodded along as the Femme Fatale boasted, allowing her arrogance to grow unchecked. The villain's eyes gleamed with the certainty of her impending triumph."
                ff "You see, darling? You've made the right choice. Together, we could be unstoppable—free to shape the world as we wish."
                n "But as the Femme Fatale reveled in her imagined victory, the princess whispered a spell under her breath, preparing for the perfect moment to escape."
                p "You're right... but there's one thing you forgot."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "Before the Femme Fatale could react, the princess activated her teleportation spell. A burst of light enveloped her and the hero, whisking them away in an instant, far from the clutches of the villain."
                n "The Femme Fatale's laughter faded into silence as she realized she had been outmaneuvered. Left alone in the empty clearing, her dreams of power crumbled to dust."
                n "The princess and hero reappeared in a peaceful meadow, far from the dangers of the forest. They had not only escaped the Femme Fatale's schemes but also freed themselves from the burdens of the kingdom's expectations."
                n "Choosing a life guided by their own desires, they set out on a journey beyond the confines of their former roles, determined to live life on their own terms."
                n "And the princess and hero lived happily ever—"

                jump happily_ever_after

    label ff_choices_5_2:
        # Branching from "(Act) Lure her into overconfidence and trap her"
        menu:
            "(Act) Use a snare trap" if not chose_magic:
                n "The princess's eyes caught sight of an old snare trap hidden beneath the undergrowth. With a subtle gesture, she signaled to the hero, who immediately understood her intent."
                p "Draw her toward the trap—we'll catch her when she least expects it."
                n "The hero maneuvered carefully, baiting the Femme Fatale into the narrow path where the trap was set. The villain's smirk grew wider as she believed she had them cornered, her confidence blinding her to the danger."
                ff "You really think you can outsmart me with such a simple trick?"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The snare snapped shut around the Femme Fatale's ankle, throwing her off balance. She cursed under her breath, realizing too late what had happened."
                n "But as the Femme Fatale struggled to free herself, she lashed out with one final, desperate strike—her poisoned dagger flashing toward the princess with deadly intent."
                n "The hero, seeing the danger, didn't hesitate. He threw himself in front of the blade, taking the strike meant for the princess."
                n "The hero staggered, the poison from the dagger spreading rapidly through his veins. The Femme Fatale, weakened and bound by the trap, fell lifeless to the ground, but her final act of malice had already sealed the hero's fate."
                n "The princess rushed to the hero's side, tears streaming down her face as she held him close. His breathing was shallow, his life slipping away with every moment."
                n "Though the villain was defeated, the price was paid in the hero's sacrifice. His final act had been to protect the one he loved most, even at the cost of his own life."
                n "The princess would return to the kingdom alone, forever marked by the memory of the hero's loyalty and courage. Though her heart ached with grief, she knew she had to carry on, for his sacrifice would not be in vain."
                n "And the princess lived happily ever—"

                jump sacrificed_hero
            "(Act) Trap her with her own poison":
                n "The princess noticed the small vial of poison hanging from the Femme Fatale's belt—an irony that couldn't be ignored. Quickly, she signaled to the hero, who prepared to engage the villain while she set the trap."
                p "We'll use her own tricks against her. Distract her, and I'll handle the rest."
                n "The hero nodded and lunged forward, drawing the Femme Fatale's full attention. She blocked his strikes effortlessly, her eyes gleaming with cruel satisfaction."
                scene bg villain_hero_charging_far_ff with dissolve
                ff "Is this really all you've got? You're hardly worth my time."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But the hero refused to back down, even as the Femme Fatale's daggers flashed in the dim light. With each swipe, she drew closer to delivering a lethal blow. Finally, one of her strikes landed—a deep cut across the hero's arm that made him stumble back in pain."
                n "The villain's smirk widened as she closed in for the kill, savoring her victory. The hero, bleeding and cornered, struggled to hold his ground as she raised her blade for the final strike."         
                n "But just as she prepared to deliver the fatal blow, the princess made her move. With precise timing, she struck the vial of poison hanging from the villain's belt, shattering it and releasing a toxic cloud that caught the Femme Fatale completely off guard."
                n "The venomous fumes spread quickly, and the villain recoiled in shock, realizing too late that she had fallen into her own trap. Her eyes widened as the poison seeped into her skin, weakening her with every passing second."
                n "The Femme Fatale gasped for breath, her strength sapped by the very poison she had relied on so many times before. As the life drained from her eyes, the villain's reign of terror finally came to an end."
                n "With the danger gone, the princess immediately turned her attention to the hero's wounds. Kneeling beside him, she carefully dressed the deep cut on his arm, her heart pounding with relief."
                n "The hero winced as she bandaged him, but his eyes held a quiet gratitude. He knew that without her quick thinking and bravery, he wouldn't have survived."
                n "The forest, once heavy with tension, seemed to exhale in peace as the villain's dark influence faded. The princess and hero, battered but victorious, took a moment to catch their breath."
                n "They had faced death together and emerged stronger than ever. With the villain defeated, they would return to the kingdom as partners, knowing that their bond had been tested and proven unbreakable."
                n "And the princess and hero lived happily ever—"

                jump saved_hero

    label ff_choices_5_3:
        # Branching from "(Act) Pretend to agree with her goals"
        menu:
            "(Act) Reverse the magic she's using":
                n "The princess's eyes narrowed as she watched the Femme Fatale manipulate the surrounding magic for her own twisted purposes. But the princess knew something that the villain didn't—how to reverse the flow and turn it against her."
                p "You're not the only one who knows how to twist magic to your advantage."
                n "With a focused incantation, the princess began to unravel the Femme Fatale's spell. The magic warped, shifting from dark energy to a calming force that began to heal the forest instead of corrupting it."
                ff "What... what are you doing?!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The villain's voice cracked in panic as she felt the power slip from her control. Her attempt to seize back the energy failed, leaving her powerless as the forest itself turned against her."
                n "The Femme Fatale's strength drained away as the very magic she had tried to exploit now bound her in place. The forest, sensing her malevolence, tightened its grip, ensuring she could never harm it again."
                n "As the forest restored its balance, the princess and hero felt a deep sense of peace wash over them. They had not only protected the land but found their purpose in doing so."
                n "Choosing to stay, they would dedicate themselves to preserving the harmony they had fought to restore, becoming guardians of the enchanted woods."
                n "The forest would thrive under their stewardship, a testament to their bond and shared mission."
                n "And the princess and hero lived happily ever—"

                jump forest_protectors
            "(Act) Escape with a sudden teleport":
                n "The princess knew that engaging the Femme Fatale any further would only lead to more danger. Instead, she decided it was time to escape and leave the kingdom behind."
                p "We've played her game long enough—it's time we vanish from this story."
                n "With a flick of her wrist, the princess summoned a teleportation spell, the magic swirling around them as she prepared to whisk them away from the villain's grasp."
                ff "Running away? How predictable."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But the Femme Fatale's taunts fell on deaf ears as the spell took hold, wrapping the princess and hero in a veil of light. The villain reached out to stop them, but she was too late."
                n "In an instant, the princess and hero were gone, leaving behind the kingdom and all its expectations. The Femme Fatale's schemes crumbled into irrelevance, her victory snatched away as they vanished into a new life of freedom."
                n "Far from the prying eyes of the kingdom, they found peace in a simpler existence, where they could live by their own rules."
                n "No longer bound by the weight of tradition or duty, the princess and hero forged a new path, guided only by their love and shared dreams."
                n "And the princess and hero lived happily ever—"

                jump happily_ever_after

    label ff_choices_5_4:
        # Branching from "(Act) Provoke her to reveal her true intentions"
        menu:
            "(Act) Turn her ambition against her":
                n "The princess's gaze sharpened as she subtly probed the Femme Fatale's ambitions, knowing that arrogance was often a villain's greatest weakness."
                p "You're driven by more than just games. What are you really after—power, control, or something more?"
                n "The Femme Fatale's eyes glittered with malice as she leaned in closer, finally letting her mask slip just enough to reveal her true desires."
                ff "Power, control, the thrill of bending others to my will... it's all part of the game, darling."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But in that moment, the princess saw something deeper—a hunger that could be exploited. With quick thinking, she turned the conversation, subtly goading the villain into overreaching."
                n "Blinded by her ambition, the Femme Fatale pushed too far, letting her desire for dominance lead her into a fatal mistake. Sensing her vulnerability, the princess used magic to reverse the situation."
                n "But the spell backfired, causing a catastrophic surge of dark energy. The princess was mortally wounded, collapsing as the magic tore through her. In desperation, the hero broke the kingdom's most sacred law—he used forbidden magic to bring her back."
                n "The kingdom's response was swift and merciless. The hero was banished, condemned for defying nature itself. Though resurrected, the princess was left to face the kingdom alone, burdened by the memory of their lost love."
                n "And the princess lived happily ever—"

                jump unfulfilled_love
            "(Act) Shoot a fireball while she's distracted":
                n "The princess's eyes narrowed as she spotted a momentary lapse in the Femme Fatale's focus. Now was the time to strike—decisively and without hesitation."
                p "Enough games—this ends now!"
                n "Gathering the arcane energy within her, the princess unleashed a roaring fireball straight at the villain. The flames streaked through the air, too fast for the Femme Fatale to react."
                ff "Wha—"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The fireball struck with devastating force, sending the Femme Fatale crashing to the ground. Her smug grin twisted into shock as the fire consumed her."
                n "The Femme Fatale's final scream was drowned out by the roar of flames that quickly spread from the impact. The fire surged out of control, devouring the forest around them. In an instant, victory turned into disaster."
                n "The once-vibrant woods were reduced to a scorched wasteland, and the magic that had once thrived there twisted into a dark curse. Realizing the catastrophic consequences of her spell, the princess's heart sank."
                n "To atone for what they had unleashed, the princess and hero vowed to stay within the cursed forest, dedicating their lives to restoring the land they had so carelessly ruined."
                n "Though the curse would never fully lift, they found solace in their shared mission, protecting what little remained and guarding against future threats."
                n "Together, they became the eternal stewards of the forest, bound by duty and regret, yet finding purpose in their penance."
                n "And the princess and hero lived happily ever—"

                jump forest_curse

    label ff_choices_5_5:
        # Branching from "(Act) Beg her for protection"
        menu:
            "(Act) Pretend to serve her, then backstab her":
                n "The princess knelt before the Femme Fatale, her voice trembling with false humility."
                p "We... we'll serve you. Spare us, and we will follow your every command."
                n "The Femme Fatale's eyes gleamed with satisfaction, her lips curling into a smile as she savored her apparent victory."
                ff "How delightful! Watching you grovel almost makes this worthwhile. Very well, you may serve me, and I may reconsider sparing you."
                n "The princess bowed her head, masking her intentions. She exchanged a brief glance with the hero, who was poised, ready to act."
                p "Thank you... for your mercy."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "Just as the Femme Fatale turned her attention away, the princess sprang to her feet, a hidden dagger glinting in her hand. She lunged at the villain, aiming for a quick, decisive blow."
                n "The blade found its mark, sinking into the Femme Fatale's side. She gasped, her eyes wide with shock."
                n "With a snarl, the Femme Fatale swiped her poisoned dagger in a desperate counter, her aim wild. As the villain staggered back, her eyes locked onto the hero, intent on taking him down with her."
                n "Seeing the threat, the princess didn't hesitate. She threw herself in front of the hero, taking the dagger's strike directly into her chest."
                n "The princess's body collapsed, the poison working quickly through her veins. The hero caught her, his face a mask of horror and grief as he held her close."
                n "The Femme Fatale's smirk faded into a final grimace as her strength failed, and she crumpled to the ground, defeated."
                n "The hero cradled the princess in his arms, his heart breaking as her life slipped away. Her sacrifice had saved him, but at the cost of her own."
                n "The kingdom would hear of her bravery, but the hero would return alone, forever haunted by the memory of her selfless act."
                n "And the hero lived happily ever—"

                jump sacrificed_princess
            "(Act) Strike her with a fireball while she's distracted":
                n "The princess knew that pleading wouldn't get them far, but she needed to buy time. She pretended to cower, her voice trembling with false fear."
                p "We'll do anything you ask... just spare us, please."
                n "The Femme Fatale's eyes sparkled with cruel delight, believing she had won."
                ff "Begging suits you, princess. Very well, serve me, and perhaps I'll consider sparing your miserable lives."
                n "But the princess wasn't about to let her guard down. With a subtle glance to the hero, she prepared her next move."
                p "Thank you... but I have a better idea."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "As the Femme Fatale basked in her victory, the princess summoned a fireball, her hands glowing with arcane power. She hurled the fiery orb directly at the villain, aiming to catch her off guard."
                n "The fireball struck the Femme Fatale, engulfing her in flames. She screamed in pain and fury, but the attack had unintended consequences."
                n "The fire spread quickly, consuming the surrounding forest. The ancient magic within the woods reacted violently to the blaze, twisting into a dark and vengeful curse."
                n "The once-protective forest became a hostile wasteland, filled with shadows and twisted branches that reached for the sky like skeletal hands. The curse bound the princess and hero to the forest, trapping them within its borders forever."
                n "Realizing their mistake, the princess and hero vowed to protect the forest from further harm, becoming its eternal guardians. Bound by their shared penance, they sought redemption for their reckless actions."
                n "Though the curse would never fully lift, they found purpose in their duty, guarding the forest against any who dared enter."
                n "And the princess and hero lived happily ever—"

                jump forest_curse

    label ff_choices_5_6:
        # Branching from "(Act) Pretend to surrender"
        menu:
            "(Act) Feign weakness and strike back" if not chose_magic:
                n "The princess stumbled back, her body trembling as if in defeat, her arms hanging limply at her sides."
                p "Please... we can't fight anymore. You've won."
                n "The Femme Fatale's smile widened, her confidence growing with the sight of the princess seemingly broken."
                ff "How delightful. Watching you squirm and beg is almost better than finishing you off."
                n "The hero, tense and ready, glanced at the princess, searching her eyes for a plan. She gave a subtle nod toward a heavy branch lying nearby."
                n "As the Femme Fatale closed in, the princess suddenly lunged, grabbing the branch and swinging it with all her might. The strike connected with the villain's arm, knocking her back."
                ff "You think a branch can defeat me?"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The Femme Fatale, recovering from the blow, turned her attention to the hero, seeing him as the greater threat. Her dagger gleamed as she aimed for his heart."
                n "But just as she lunged, the princess leapt forward, positioning herself between the hero and the Femme Fatale. The dagger pierced her chest instead."
                n "The princess collapsed to the ground, the life quickly draining from her as the hero caught her in his arms. The Femme Fatale, weakened from the struggle, fell as well, her last breath escaping in a sigh of defeat."
                n "The hero held the princess close, his tears falling as he watched her life slip away. Her final, selfless act saved him, but the cost was her life."
                n "The Femme Fatale's death meant victory, but the hero would always remember the sacrifice that defined their journey, the love that endured beyond death."
                n "And the hero lived happily ever—"

                jump sacrificed_princess
            "(Act) Lure her into a vulnerable position":
                n "The princess dropped her hands to her sides, her posture slumping in defeat."
                p "You've won... please, just let us go."
                n "The Femme Fatale laughed, her eyes gleaming with triumph."
                ff "Oh, princess, how naive. I don't show mercy."
                n "The hero glanced at the princess, uncertainty in his eyes. She gave him a subtle signal, directing his attention to a narrow ledge behind the Femme Fatale."
                n "As the villain moved closer, taunting her captives, the princess pretended to trip, drawing the Femme Fatale forward."
                p "Please... just spare him."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "Seeing her moment, the princess darted to the side, grabbing a loose stone and hurling it at the villain's feet. The Femme Fatale stumbled, momentarily off-balance."
                n "The hero seized the opportunity, moving to push her off balance further. But as he did, the Femme Fatale slashed out with her dagger, grazing his arm."
                n "The hero gasped, clutching his arm as the venom began to spread. The princess's eyes widened with horror as she saw the wound begin to darken."
                n "Realizing the hero had been poisoned and that he wouldn't survive, the princess made a desperate choice. She grabbed the dagger from the ground and plunged it into her own heart, choosing to follow him in death."
                n "The hero's eyes filled with tears as he fell beside her, their hands clasped together in their final moments."
                n "The Femme Fatale, seeing her victory tainted by their tragic choice, lay dying as well, the poison that had grazed her seeping into her veins."
                n "In their last moments, the princess and hero shared a final, silent vow, their souls forever united in the afterlife."
                n "And the princess and hero died happily ever—"

                jump love_beyond_death

    label ff_choices_5_7:
        # Branching from "(Act) Learn her techniques and betray her"
        menu:
            "(Act) Use what you've learned to outmaneuver her":
                n "The princess carefully watched every movement the Femme Fatale made, her keen eyes memorizing the intricate gestures and incantations of the villain's spells."
                p "I've seen enough... It's time to end this."
                n "Drawing upon what she had learned, the princess began to chant a counter-incantation, her voice steady and filled with purpose. The Femme Fatale's expression shifted from smug confidence to surprise as she realized her spells were unraveling."
                ff "How...? You think you can match me?"
                n "The princess continued, her magic expertly weaving through the dark energy that filled the air. She reversed the flow, turning the destructive power back into the earth, where it could do no harm."
                ff "You—impossible!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The ground beneath them trembled as the forest responded to the princess's call. The trees bent toward her, their branches reaching to protect her and the hero from the villain's final, desperate strikes."
                n "The Femme Fatale, realizing she had been outmaneuvered, tried to retreat, but it was too late. The forest closed in around her, sensing her malevolence, binding her with roots that grew and twisted around her body, holding her fast."
                n "As the forest sealed away its threat, the princess and hero felt a deep connection to the land, a calling they couldn't ignore. They knew their place was here, as guardians of the enchanted woods."
                n "Together, they vowed to protect the forest from any who sought to harm it, dedicating their lives to ensuring its magic would always thrive."
                n "And the princess and hero lived happily ever—"

                jump forest_protectors
            "(Act) Exploit her hubris and escape":
                n "The princess feigned hesitation, allowing the Femme Fatale's confidence to swell with each passing second. The villain's smirk widened, utterly convinced of her superiority."
                ff "Do you see now, darling? You were never a match for me."
                n "The princess nodded subtly to the hero, their plan set in motion. As the Femme Fatale gloated, the princess reached for a nearby branch, her hand trembling with feigned fear."
                p "I suppose you're right... but maybe there's still a way to win."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But as she lunged to strike, the Femme Fatale, anticipating her move, deftly sidestepped and plunged a hidden dagger into the princess's side. The sharp pain stole her breath away as she collapsed to the ground."
                n "The hero rushed to the princess's side, his eyes wide with horror as he watched her life ebb away. Desperation clawed at his heart, and without a second thought, he called upon forbidden magic to resurrect her."
                n "As the princess's eyes fluttered open, life returning to her pallid cheeks, she realized the cost of her salvation. The hero's hand trembled with the dark power that flowed through him—a power the kingdom had long forbidden."
                n "Though the princess was saved, the hero had committed an unforgivable act. Upon their return, the kingdom learned of his transgression. The hero was exiled, forever cast out for defying the laws of life and death."
                n "The princess, alive but forever changed, was left to face the consequences of their choices alone, haunted by the love that could never truly be fulfilled."
                n "And the princess lived happily ever—"

                jump unfulfilled_love

    label ff_choices_5_8:
        # Branching from "(Act) Use her own spells against her"
        menu:
            "(Act) Reflect her spell back at her":
                n "The princess watched as the Femme Fatale conjured a spell, dark energy crackling at her fingertips. The princess knew she had only one chance to turn the tide."
                p "If you want to play with magic, then let's see how well you handle your own spells!"
                n "With a quick incantation, the princess focused her energy, creating a mirror of magic that caught the Femme Fatale's spell mid-flight and hurled it back at her."
                ff "No! How dare you—"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The spell struck the Femme Fatale with a violent force, throwing her to the ground. But the impact triggered a chain reaction—the surrounding forest erupted into flames, ignited by the raw, uncontrolled power of their magic clash."
                n "The fire spread quickly, consuming everything in its path. The forest, once full of life, was reduced to ash, the magic within twisted into a dark curse that spread through the land. Realizing the irreversible damage caused, the princess's heart filled with dread."
                n "To atone for their actions, the princess and the hero swore to remain within the cursed forest, dedicating their lives to healing the land they had scarred."
                n "Bound by their regret and responsibility, they vowed to protect the remnants of the once-thriving forest and prevent any further harm from coming to it."
                n "Together, they became the forest's eternal guardians, finding a new purpose in their shared penance, but forever marked by their mistake."
                n "And the princess and hero lived happily ever—"

                jump forest_curse
            "(Act) Shatter her control with a counterspell":
                n "The princess could feel the oppressive weight of the Femme Fatale's magic twisting the very air around them. She knew she had to act fast."
                p "Your spells might be strong, but they are nothing compared to the power of a counterspell."
                n "Focusing her energy, the princess began chanting an incantation, her voice steady and clear. The air around them shifted as her magic clashed with the Femme Fatale's dark spells."
                ff "What... what are you doing?!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The Femme Fatale's eyes widened as she felt her control slipping away. The princess's counterspell shattered the dark energy in a brilliant explosion of light."
                n "The burst of magic left the Femme Fatale powerless, her once confident smirk replaced by shock and fear. She stumbled back, defeated, her reign of terror finally over."
                n "With the villain vanquished, the forest breathed a sigh of relief, the natural balance restored. The princess and hero, victorious, took a moment to catch their breath, knowing they had made the right choice."
                n "Though they had won the battle, they knew returning to the kingdom was not an option. The magic they had wielded, though just, would never be accepted by those who feared its power."
                n "Together, they chose a new path—one free from the constraints of the kingdom's laws and expectations. Far from those who would judge them, they sought a life where they could use their magic for good, on their own terms."
                n "Freed from the weight of the past, they set their sights on a future guided by their own choices, far away from the shadows of the kingdom."
                n "And the princess and hero lived happily ever—"

                jump happily_ever_after

    label ff_choices_5_9:
        # Branching from "(Act) Strike at her unarmored side"
        menu:
            "(Act) Exploit her pain to secure a win":
                n "The princess spotted the momentary wince on the Femme Fatale's face—a sign of pain from an earlier wound. She knew this was their only opportunity to strike."
                p "Now! Aim for her weakness!"
                n "The hero moved swiftly, his sword flashing in the dim light as he targeted the vulnerable spot. But as the blade drew close, the Femme Fatale twisted in a final act of desperation, her dagger aimed at the hero's heart."
                ff "I'll take you down with me!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "Seeing the threat, the princess acted on instinct. She grabbed a fallen branch from the ground and lunged forward, placing herself between the Femme Fatale and the hero. The dagger pierced her side, and she gasped in pain."
                n "The princess fell to the ground, her vision blurring as the pain spread. The hero, struck by grief, held her close, his heart shattering with every shallow breath she took."
                n "The Femme Fatale, weakened by her injuries, fell beside them, her life slipping away as the hero's sword delivered a final blow."
                n "The hero cradled the princess in his arms as her life ebbed away, her sacrifice sealing the victory but at a great cost. The forest grew silent, the weight of her selfless act heavy in the air."
                n "Though they had won, the hero's heart was forever scarred by the loss of the one he loved most. He would return to the kingdom alone, carrying the memory of her sacrifice with him always."
                n "And the hero lived happily ever—"

                jump sacrificed_princess
            "(Act) Hesitate, showing mercy":
                n "The hero's sword hovered over the Femme Fatale, ready to strike the final blow. But the princess hesitated, a flicker of doubt crossing her face."
                p "Wait... maybe we don't have to end it this way."
                n "The Femme Fatale, sensing the hesitation, saw her chance. With a swift, desperate motion, she lashed out with her poisoned dagger, grazing the hero's arm."
                ff "A moment's hesitation, and now you both pay the price!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero staggered back, clutching his arm as the venom spread quickly through his veins. The princess's eyes filled with horror, realizing what had happened."
                n "As the poison began to take hold, the hero's strength ebbed away. The princess, heartbroken and desperate, saw the inevitable end approaching. Unable to imagine a life without him, she made a fateful decision."
                n "Taking the villain's dagger, she plunged it into her own heart, choosing to follow the hero into the afterlife rather than face a world without him."
                n "The hero, his vision blurring, reached out to her, their fingers entwined in their final moments. The Femme Fatale, realizing her victory came at a bitter cost, succumbed to the darkness of her own wounds."
                n "Their souls, united in death, vowed to remain together in the realm beyond, forever bound by love that transcended life itself."
                n "And the princess and hero died happily ever—"

                jump love_beyond_death

    label ff_choices_5_10:
        # Branching from "(Act) Go for a quick, decisive blow"
        menu:
            "(Act) Strike her down immediately":
                n "The princess gave the hero a quick nod, signaling him to act without hesitation. There was no time to waste; the Femme Fatale was vulnerable, and this was their chance."
                p "Now, hero! Finish this!"
                n "The hero, his expression fierce and determined, surged forward. His sword gleamed in the dim light as he aimed directly for the Femme Fatale's heart."
                scene bg villain_hero_charging_far_ff with dissolve
                n "But as he moved in for the final blow, the Femme Fatale, with one last desperate act, lashed out with a hidden dagger, catching the hero's arm."
                ff "I won't go down... alone!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero's strike landed true, and the Femme Fatale crumpled to the ground, her life fading away. But her parting strike had grazed the hero with a poisoned blade."
                n "The hero staggered, his breath growing ragged as the poison spread through his veins. The princess's heart sank as she realized what had happened."
                n "Seeing that the hero had been poisoned and knowing he wouldn't survive, the princess made a fateful decision. Tears streaming down her face, she seized the Femme Fatale's fallen dagger and turned it upon herself."
                n "The hero's eyes widened with shock as the princess plunged the dagger into her own heart, choosing to join him in death rather than live without him."
                n "The Femme Fatale's last breath was drawn with a bitter smile as the darkness consumed them all. In their final moments, the princess and hero found solace in each other's arms, their souls entwined forever."
                n "And the princess and hero died happily ever—"

                jump love_beyond_death
            "(Act) Overwhelm her and retreat":
                n "The princess saw the opening and signaled to the hero to press the advantage. They had to overwhelm the Femme Fatale before she could regain her footing."
                p "Keep pushing, don't let her recover!"
                n "The hero charged forward with a series of powerful strikes, each one driving the Femme Fatale back. Her smirk faltered as she struggled to keep up, clearly unprepared for the hero's relentless assault."
                scene villain_hero_charging_far_ff with dissolve
                ff "You... you think you can overpower me?!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But as the hero moved in for a decisive blow, the Femme Fatale's eyes flashed with sudden resolve. With a desperate lunge, she aimed her dagger straight at the princess, determined to take her down with her."
                n "Seeing the imminent danger, the hero acted on instinct. He dove in front of the princess, taking the fatal blow meant for her."
                n "The hero crumpled to the ground, the poisoned dagger buried deep in his side. His breath came in shallow gasps as he lay dying in the princess's arms."
                n "The Femme Fatale, weakened from the battle, staggered back and collapsed, defeated at last. But the victory was hollow, as the hero's life slipped away."
                n "The princess wept over his lifeless body, her heart shattered by his sacrifice. He had given everything to protect her, leaving her to carry on without him."
                n "Though she had survived, the price of their triumph was etched into her soul—a reminder of the love and loyalty that had defined their journey together."
                n "She would return to the kingdom alone, bearing the weight of his loss, but knowing his memory would forever guide her."
                n "And the princess lived happily ever—"

                jump sacrificed_hero

    label ff_choices_5_11:
        # Branching from "(Act) Let her tire herself out before countering"
        menu:
            "(Act) Strike her with magic" if chose_magic:
                n "The princess watched as the Femme Fatale launched attack after attack, her movements growing increasingly frantic and sloppy with each swing. It was clear she was tiring, and soon she would leave herself wide open."
                p "Hold on... just a little longer. She's wearing herself out."
                n "The hero nodded, maintaining a defensive stance as the Femme Fatale's strikes grew weaker. Finally, seeing her stumble, the princess knew it was time."
                scene villain_hero_sword_facing_far_ff with dissolve
                p "Now! Use your magic!"
                n "The hero nodded and summoned his remaining strength, channeling his magic into a powerful blast aimed directly at the Femme Fatale. The force of the spell caught her off guard, throwing her back."
                ff "What... no!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The magic struck her with a blinding light, wrapping around her like vines as it drained the last of her strength. The Femme Fatale collapsed, unable to fight any longer."
                n "As the magic bound the Femme Fatale, the forest around them seemed to breathe a sigh of relief. The darkness that had hung over the woods began to lift, replaced by a serene calm."
                n "The princess and hero, seeing the change, knew that their decision to harness magic for good had paid off. The forest, once cursed, now thrived under their protection."
                n "They chose to stay within the woods, dedicating themselves to preserving its newfound peace. As guardians of the forest, they found a deeper purpose, their bond stronger than ever."
                n "Together, they would protect the land they had saved, ensuring that no one would ever harm it again."
                n "And the princess and hero lived happily ever—"

                jump forest_protectors
            "(Act) Deflect her attack and disarm her" if not chose_magic:
                n "The princess waited for the perfect moment, knowing the Femme Fatale's frenzied attacks would eventually leave her exposed. The hero, too, remained patient, his eyes locked on the villain's every move."
                p "Stay ready... when she overextends, that's when we strike."
                scene bg villain_hero_sword_facing_far_ff with dissolve
                n "As the Femme Fatale swung wildly with her dagger, the hero saw his opportunity. He deflected her attack with a quick parry, knocking the weapon from her hand."
                n "For a moment, it seemed like victory was within their grasp. But as the Femme Fatale stumbled back, she lashed out one last time with a hidden blade, aiming for the princess."
                ff "I won't lose... not like this!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero saw the danger and acted without hesitation. He moved in front of the princess, taking the blade meant for her."
                n "The hero crumpled to the ground, the blade buried deep in his side. His eyes met the princess's for a final, fleeting moment before closing forever."
                n "The Femme Fatale, disarmed and now defenseless, fell to her knees, her defeat complete. But the cost of victory was steep. The hero's sacrifice weighed heavily on the princess's heart as she knelt beside him, tears streaming down her face."
                n "She held him close, whispering her gratitude and sorrow, knowing he had given his life to save hers. She vowed to carry on in his memory, her heart forever marked by his bravery."
                n "Though she would return to the kingdom alone, she would never forget the hero who had stood by her side, sacrificing everything for her."
                n "And the princess lived happily ever—"

                jump sacrificed_hero

    label ff_choices_5_12:
        # Branching from "(Act) Knock her off balance and disarm her"
        menu:
            "(Act) Strike while she's vulnerable":
                n "The hero moved swiftly, knocking the Femme Fatale off balance with a powerful strike. She stumbled, her footing unsure, but quickly regained her composure."
                scene bg villain_hero_charging_far_ff with dissolve
                ff "Is that all you've got? Pathetic."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "Before the hero could respond, the Femme Fatale lunged, her dagger slashing through the air. She knocked the hero to the ground, her blade poised to strike a fatal blow."
                n "The Femme Fatale's smirk widened, savoring her moment of victory as she prepared to end the hero's life."
                n "But the princess didn't hesitate. She spotted a heavy branch on the forest floor and seized it. With a burst of strength, she swung it with all her might, striking the Femme Fatale across the back of her head."
                n "The villain stumbled forward, her eyes wide with shock as she realized she had been caught off guard. She dropped her dagger, which clattered uselessly to the ground."
                n "The hero quickly rolled away from the Femme Fatale, narrowly avoiding her flailing grasp as she fell."
                n "The Femme Fatale crumpled to the ground, unconscious from the blow. The princess immediately dropped to her knees beside the hero, her hands shaking as she checked him for injuries."
                n "A deep cut ran along his arm, but it was nothing the princess couldn't handle. She tore a strip of cloth from her dress and wrapped it around his wound, her movements quick and practiced."
                n "The hero winced but gave her a reassuring smile, grateful for her quick thinking and bravery."
                n "With the Femme Fatale defeated and the immediate danger passed, the princess and hero took a moment to breathe, leaning on each other for support."
                n "They had faced death together and emerged stronger, their bond tested and proven unbreakable. The princess's decisive action had not only saved the hero's life but also reaffirmed their commitment to each other."
                n "Once the hero had recovered, they would return to the kingdom, their love and partnership stronger than ever."
                n "And the princess and hero lived happily ever—"

                jump saved_hero
            "(Act) Give her a chance to surrender":
                n "The princess saw the Femme Fatale's moment of weakness and knew she had the upper hand. But instead of striking, she hesitated, compassion flickering in her eyes."
                p "It doesn't have to end like this. Surrender now, and we'll spare you. There's no need for more bloodshed."
                n "The Femme Fatale's eyes narrowed, her expression a mix of fear and defiance. For a moment, it seemed like she might consider the offer."
                ff "You think I would grovel for mercy? Never."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But as the hero stepped forward, ready to back the princess's offer, the Femme Fatale lashed out with a final, desperate move. Her dagger, hidden in her sleeve, slashed across the hero's arm, leaving a thin but deep cut."
                n "The hero staggered back, his hand clutching his wound. The venom from the Femme Fatale's blade began to spread almost immediately, darkening the veins around the wound."
                n "Seeing the hero's fate sealed by the poison, the princess made a heart-wrenching decision. She couldn't bear the thought of life without him."
                n "Grabbing the fallen dagger, she turned it on herself, plunging it into her chest. She would rather join him in death than live without him."
                n "As the venom took hold, the princess fell beside the hero, their hands finding each other in their final moments."
                n "The Femme Fatale, already weakened, watched in shock as the couple chose death over defeat. Her own strength fading, she collapsed, her ambitions dying with her."
                n "Together, the princess and hero died with the knowledge that their love was stronger than any curse or blade."
                n "And the princess and hero died happily ever—"

                jump love_beyond_death

    label ff_choices_5_13:
        # Branching from "(Act) Challenge her to reveal her secrets"
        menu:
            "(Act) Shoot a fireball at her":
                n "The princess's eyes narrowed as she saw the Femme Fatale's lips curl into a secretive smile, still withholding the truths she guarded so fiercely."
                p "Enough of your games! If you won't reveal your secrets, I'll end this now!"
                n "Summoning her magic, the princess quickly formed a blazing fireball in her hands, the flames crackling with fierce intensity. She hurled it straight at the Femme Fatale."
                ff "Do you really think—"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The fireball struck before the Femme Fatale could finish her taunt. Flames engulfed her, and a horrified scream tore through the air as she was consumed by the inferno."
                n "But the fire did not stop there. The flames spread rapidly, fueled by the dry forest underbrush. In an instant, the blaze grew uncontrollable, devouring everything in its path."
                n "Realizing the disaster she had unleashed, the princess's heart filled with regret. The once-vibrant forest was now a sea of fire, and the magic that once thrived here twisted into a dark, malevolent force."
                n "Overwhelmed by guilt and determination to make amends, the princess and hero vowed to stay in the cursed forest. They dedicated their lives to restoring the land they had carelessly ruined."
                n "Though the curse would never fully lift, they found solace in their shared mission. Together, they became eternal stewards of the forest, bound by duty and regret, yet finding purpose in their penance."
                n "And the princess and hero lived happily ever—"

                jump forest_curse
            "(Act) Teleport away":
                n "The princess saw an opportunity as the Femme Fatale continued to boast, her arrogance leaving her distracted."
                ff "You have no idea of the secrets I hold, the power I could share... if only you were worthy."
                n "The princess gave the hero a subtle nod, signaling her intent. Whispering a spell under her breath, she prepared to make their escape."
                p "Perhaps we aren't worthy... but we won't be your pawns, either."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "In an instant, the princess activated her teleportation spell. A burst of light enveloped her and the hero, whisking them away from the Femme Fatale's grasp."
                n "The Femme Fatale's triumphant grin vanished as she realized she had been outsmarted. Alone in the clearing, her schemes fell apart in the face of their escape."
                n "The princess and hero reappeared in a quiet meadow, far from the reach of the villain and the dangers of the forest. They had not only escaped the Femme Fatale's machinations but also freed themselves from the expectations of the kingdom."
                n "Aware that their use of magic was forbidden by the kingdom's laws, they chose not to return. Instead, they sought a new life beyond the constraints of their past."
                n "Together, they set off on a journey guided by their own desires, determined to build a future where they could live freely and fully."
                n "And the princess and hero lived happily ever—"

                jump happily_ever_after

    label ff_choices_5_14:
        # Branching from "(Act) Force her to admit her weaknesses"
        menu:
            "(Act) Manipulate her into a reckless move":
                n "The princess watched carefully, sensing a crack in the Femme Fatale's composure. She decided to press further, pushing her toward a reckless decision."
                p "You hide behind your games because you're afraid—afraid of failing, afraid of being seen as weak. Prove me wrong."
                n "The Femme Fatale's eyes blazed with fury at the princess's words. Her grip on her daggers tightened, her pride wounded."
                ff "Afraid? I'll show you what fear really looks like!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "Driven by rage, the Femme Fatale lunged forward, her movements wild and uncontrolled. The princess's plan was working—the villain was losing her carefully maintained balance."
                n "As the Femme Fatale overextended, the princess seized the moment, drawing on her magic to turn the tide against her."
                n "A powerful surge of energy ripped through the clearing, engulfing the Femme Fatale. She let out a scream as she was thrown back, her body collapsing lifelessly to the ground."
                n "But the cost of this victory was immense. As the dust settled, the princess fell to the ground, her body lifeless from the magical onslaught."
                n "The hero, realizing she was slipping away, made a desperate choice. Breaking the kingdom's most sacred rule, he used forbidden magic to bring her back."
                n "When the princess awoke, her relief was overshadowed by the consequences of his actions. The kingdom, upon learning of the hero's transgression, branded him a danger and exiled him for defying nature's laws."
                n "The princess, alive but forever marked by tragedy, was forced to carry on alone, haunted by the love that could never be fulfilled."
                n "And the princess lived happily ever—"

                jump unfulfilled_love
            "(Act) Use her moment of doubt to strike":
                n "The princess saw a flicker of doubt in the Femme Fatale's eyes, a hesitation that opened a narrow window of opportunity."
                p "Now, hero—she's vulnerable!"
                n "The hero lunged forward, but the Femme Fatale recovered quickly, striking him across the face with the hilt of her dagger. The blow sent the hero crashing to the ground, dazed and vulnerable."
                scene bg villain_hero_charging_far_ff with dissolve
                n "With the hero down, the Femme Fatale stood over him, a cruel smile on her lips as she raised her dagger for the final blow."
                scene bg villain_far_ff with dissolve
                ff "Pathetic... is this all the kingdom's champion has to offer?"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The princess's heart pounded. Without a second thought, she grabbed a sturdy branch from the forest floor and charged forward, striking the Femme Fatale across the back."
                n "The villain stumbled, her dagger slipping from her hand as she turned in shock. The princess didn't let up, swinging again with all her strength."
                n "The final blow from the branch hit the Femme Fatale squarely in the temple, and she collapsed to the ground, unconscious."
                n "With the villain defeated, the princess immediately knelt beside the hero, her hands trembling as she checked his wounds. He was breathing, but badly hurt."
                n "Tearing a strip from her dress, she bandaged his injuries, her heart racing as she worked to save him."
                n "As the hero's eyes fluttered open, he managed a weak smile, grateful for her quick thinking and bravery."
                n "They had faced death together and emerged stronger for it. With the Femme Fatale's threat ended, they could return to the kingdom, their bond deeper than ever."
                n "And the princess and hero lived happily ever—"

                jump saved_hero

    label ff_choices_5_15:
        # Branching from "(Act) Goad her into a one-on-one duel"
        menu:
            "(Act) Strike her with magic" if chose_magic:
                n "As the duel began, the Femme Fatale danced around the princess and hero, her daggers flashing with deadly intent."
                ff "Is this all you have, little princess? Your kingdom has sent you to die."
                n "The princess's eyes narrowed, drawing on her inner strength. She whispered an incantation under her breath, her hands beginning to glow with a soft light."
                p "I don't need a sword to stop you. Magic will be enough."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The Femme Fatale lunged forward, but the princess thrust her hands out, releasing a wave of magic that enveloped the villain. The forest seemed to respond, the air thickening with energy."
                n "The magic surged around the Femme Fatale, vines erupting from the ground and wrapping around her limbs. She struggled, but the forest tightened its grip, binding her in place."
                n "The Femme Fatale's eyes widened in horror as the very magic she had sought to control now restrained her. The forest, sensing her dark intent, refused to let her go."
                n "The princess and hero, seeing the villain subdued, felt a profound sense of duty to the enchanted woods. They decided to stay and protect the forest from future threats, becoming its new guardians."
                n "As they took their place among the ancient trees, a sense of peace settled over them. They had found a purpose greater than themselves, and a bond that could withstand any trial."
                n "And the princess and hero lived happily ever—"

                jump forest_protectors
            "(Act) Use her own poison against her" if not chose_magic:
                n "The princess watched the Femme Fatale closely, noting the subtle way she wielded her poisoned daggers. With every movement, the princess could see a pattern—a chance to use the villain's own weapons against her."
                p "Hero, distract her! We need to turn her own tools back on her."
                n "The hero nodded, launching into a series of feints and strikes, drawing the Femme Fatale's attention entirely onto him."
                scene villain_hero_charging_far_ff with dissolve
                ff "You're predictable! Do you think you can defeat me with such basic tactics?"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The princess moved swiftly behind the Femme Fatale, her eyes locked on the vial of poison hanging at the villain's waist."
                n "In a moment of daring, she grabbed the vial and tossed it to the hero, who caught it with a deft hand. The Femme Fatale, realizing too late what was happening, spun around in shock."
                n "The hero smashed the vial against the ground, releasing a cloud of toxic fumes. The Femme Fatale recoiled, covering her mouth, but the damage was already done. The poison began to take hold, slowing her movements."
                n "But as the poison cloud spread, the Femme Fatale, with a final desperate lunge, threw one of her daggers toward the princess, aiming for a fatal strike."
                n "The hero, seeing the danger, acted on pure instinct. He jumped in front of the princess, taking the dagger square in his chest."
                n "The hero staggered, the poison-laced blade lodged deep in his body. The Femme Fatale fell lifeless to the ground, but her final act of malice had claimed one last victim."
                n "The princess rushed to the hero's side, tears streaming down her face as she held him close. His breath came in ragged gasps, his life slipping away."
                n "Though they had won the battle, the victory felt hollow. The hero's sacrifice weighed heavily on the princess's heart as she realized the price of their triumph."
                n "She would return to the kingdom alone, forever marked by the memory of the hero's loyalty and courage. Though her heart ached with grief, she knew she had to carry on, for his sacrifice would not be in vain."
                n "And the princess lived happily ever—"

                jump sacrificed_hero

    label ff_choices_5_16:
        # Branching from "(Act) Pretend to be impressed, then strike when she's distracted"
        menu:
            "(Act) Use the hero's sword to land a fatal blow":
                n "The princess feigned awe, her eyes wide as she watched the Femme Fatale twirl her daggers with a sinister grace."
                p "You're incredible... truly, I've never seen such skill."
                n "The Femme Fatale smirked, clearly reveling in the praise, her confidence growing with every word."
                ff "Flattery, darling, will get you nowhere. But I must admit, it is delightful to hear."
                n "The hero, seeing the opportunity, tightened his grip on his sword, ready to strike. The princess gave him a subtle nod, signaling the moment had come."
                p "Hero, now!"
                n "As the Femme Fatale's attention was entirely on the princess, the hero moved with swift precision, raising his sword to strike. But as he lunged, the villain turned at the last second, her reflexes sharp."
                scene bg villain_hero_charging_far_ff with dissolve
                n "She parried his attack and with a swift movement, kicked his feet out from under him, knocking him to the ground. She stood over him, ready to deliver a fatal strike."
                scene bg villain_far_ff with dissolve
                ff "Nice try, but you'll have to do better than that!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The princess, acting quickly, spotted a large branch on the ground. With no time to waste, she grabbed it and struck the Femme Fatale from behind, catching her off guard."
                n "The villain stumbled, dropping one of her daggers. The hero seized the chance and thrust his sword upward, piercing the Femme Fatale's side. She gasped, shock flashing in her eyes."
                n "The Femme Fatale crumpled to the ground, her reign of terror brought to a sudden end by the combined efforts of the princess and hero."
                n "With the danger passed, the princess quickly knelt beside the hero, her hands trembling as she checked him for injuries. The hero's breath was ragged, but he managed a weak smile, grateful for her quick thinking."
                n "The princess tended to his wounds, her relief palpable as she realized he would survive. Their bond, tested by the fires of battle, had only grown stronger."
                n "Once the hero regained his strength, they would return to the kingdom, ready to face whatever challenges awaited them, united in purpose and heart."
                n "And the princess and hero lived happily ever—"

                jump saved_hero
            "(Act) Escape while she's distracted":
                n "The princess's eyes darted around the clearing, her mind racing as she weighed their chances. She knew they couldn't win by sheer force alone."
                p "Hero... when I give the signal, we need to run."
                n "The hero nodded, his expression grim as he prepared to follow her lead. The Femme Fatale, still basking in her perceived superiority, failed to notice the silent exchange."
                ff "Oh, princess, you look like a deer caught in the headlights. Are you that afraid of me?"
                n "The princess feigned fear, stepping back as if retreating. The Femme Fatale laughed, her confidence blinding her to the danger."
                p "Hero, now!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "They turned to flee, but the Femme Fatale's eyes flashed with fury at their attempt to escape. She hurled a dagger, aimed directly at the hero's back."
                n "Seeing the blade hurtling toward him, the princess acted without hesitation. She threw herself in front of the hero, the dagger sinking into her chest with a sickening thud."
                n "The hero caught the princess as she fell, her lifeblood spilling out onto the forest floor. Desperation filled his heart as he realized the depth of her sacrifice."
                n "He quickly turned, his sword flashing in the dim light as he struck down the Femme Fatale in a single, decisive blow, ending her reign of terror."
                n "The hero cradled the princess in his arms, tears streaming down his face as her life ebbed away. Her last breath was a whisper of love, a silent farewell that shattered his heart."
                n "Though the villain was defeated, the cost was far too high. The hero, now alone, would carry the weight of her loss with him for the rest of his days, her selfless act forever etched into his soul."
                n "And the hero lived happily ever—"

                jump sacrificed_princess


    label ff_who_are_you:
        p "Who are you? Why do you play these games with us?"
        n "The Femme Fatale's smile was sly, her voice dripping with honeyed malice."
        ff "Who am I? Let's just say I'm someone who thrives on the thrill of pulling strings and watching others dance."
        ff "You could call me a connoisseur of broken dreams and shattered resolves."

        return

    label ff_why_doing_this:
        p "Why are you doing this? What's the point of all this manipulation?"
        n "The Femme Fatale's eyes sparkled with amusement, her tone like velvet laced with venom."
        ff "Why? Because it's entertaining, darling. There's nothing quite like watching someone who thinks they're in control unravel bit by bit."
        ff "You're all just pieces on the board, and I... well, I do love winning."

        return

    label ff_what_you_gain:
        p "What do you even gain from tormenting others? Does it really satisfy you?"
        n "The Femme Fatale's expression turned calculating, as if weighing her words carefully."
        ff "Satisfaction? My dear, it's not just about satisfaction. It's about power. The power to twist minds, to reveal the ugliness beneath the surface."
        ff "You'd be surprised how much you can learn when people are at their most desperate. And that knowledge... is priceless."
        
        return

    label ff_why_enjoy_manipulating:
        p "Why do you take such pleasure in manipulating people? What do you get out of it?"
        n "The Femme Fatale's laugh was low and smooth, like silk gliding over a razor's edge."
        ff "Pleasure? Oh, absolutely. There's something exquisite about seeing people unravel under the weight of their own choices."
        ff "It's a dance, really—one where I lead, and they stumble. The thrill is in knowing I'm always two steps ahead."

        return

    label ff_isnt_there_more:
        p "Isn't there more to life than this? Games and deceit can't be all you care about."
        n "The Femme Fatale's smile softened into something almost wistful, though her eyes remained sharp."
        ff "More to life? Perhaps. But where's the fun in sincerity when lies are so much more... intriguing? Life is a game, my dear."
        ff "The difference is, I've chosen to play it well. Others merely lose without even realizing it."

        return

    label ff_do_you_not:
        p "Don't you care about the harm you cause? You ruin lives with your schemes."
        n "The Femme Fatale's gaze grew cold, her smile fading into a hard edge."
        ff "Care? You mistake me for someone who feels guilt. People are fragile, easily led astray by their own weaknesses. All I do is expose what's already there."
        ff "If they crumble, it's because they were weak to begin with. I simply give them a nudge."

        return

    label ff_how_did_you:
        p "How did you become like this? Were you always this cruel?"
        n "The Femme Fatale's eyes darkened, her voice laced with an undercurrent of bitterness."
        ff "How did I become like this? Let's just say that trust is a currency I no longer trade in. I learned that the only way to survive is to be the one holding all the cards."
        ff "Once you've been betrayed enough times, it's easy to see the world for what it really is—a game of deceit where the sharpest mind wins."

        return

    label ff_was_there_ever:
        p "Was there ever a time when you cared about anyone? When you weren't like this?"
        n "The Femme Fatale's smile turned icy, her voice carrying a note of distant sorrow."
        ff "Once, perhaps. But caring is a liability, a weakness that others will use against you. I learned that the hard way."
        ff "Love, loyalty—those are illusions people cling to before they're inevitably betrayed. I chose to shed those illusions and embrace what truly matters: control."
                
        return
    
    label ff_do_you_think:
        p "Do you think you can ever change? Or is this who you are now, forever?"
        n "The Femme Fatale's expression shifted, her eyes narrowing as if she found the question distasteful."
        ff "Change? Why would I want to? To become soft, vulnerable? No, darling. People don't change—they just become better at hiding what they truly are."
        ff "I've found my path, and I'll walk it until the very end, unburdened by sentiment or regret."

        return

    label ff_what_do_you:
        p "What do you really want from us? What's the point of all this?"
        n "The Femme Fatale's gaze was sharp, a smirk playing at the corner of her lips."
        ff "What do I want? Oh, nothing much. Just to see how far I can push you before you break."
        ff "There's a certain artistry in that—finding the cracks, applying just the right pressure, and watching the pieces fall apart."
        ff "It's fascinating, really."

        return

    label ff_is_this_just:
        p "Is this all just a game to you? Do our lives mean nothing?"
        n "The Femme Fatale's laughter was soft, mocking, with an edge that cut deep."
        ff "A game? Yes, but a game with very real stakes. Your lives, your choices—they're merely the pieces I move around the board."
        ff "The difference is, I know how this ends... and I'm always the one who comes out on top. You, on the other hand? You're just trying to keep up."

        return

    label ff_when_will_it:
        p "When will this end? What are you really trying to achieve?"
        n "The Femme Fatale's smile turned almost pitying, as if she found the question naïve."
        ff "When will it end? When I've taken everything I can from you—your hope, your resolve, your trust. I'm not after riches or power; I'm after the satisfaction of knowing I've stripped away every illusion you cling to."
        ff "When there's nothing left but the truth—when you see the world as I do—then, perhaps, I'll be satisfied. But until then? The game continues."

        return
