# Contains the code associated with portion of the game related to the "dark magic lord" second villain encounter.

# Default Variables


# Flags for unlockable options

default dml_chose_who_are_you = False
default dml_chose_why_do_you = False
default dml_chose_what_do_you = False
default dml_chose_how_did_you = False
default dml_chose_what_drives_your = False
default dml_chose_do_you_not = False
default dml_chose_what_is_your = False
default dml_chose_do_you_really = False
default dml_chose_how_do_you = False
default dml_chose_why_cant_you = False
default dml_chose_is_there_nothing = False
default dml_chose_what_would_happen = False

label dml_start:
    $ dml_chose_who_are_you = False
    $ dml_chose_why_do_you = False
    $ dml_chose_what_do_you = False
    $ dml_chose_how_did_you = False
    $ dml_chose_what_drives_your = False
    $ dml_chose_do_you_not = False
    $ dml_chose_what_is_your = False
    $ dml_chose_do_you_really = False
    $ dml_chose_how_do_you = False
    $ dml_chose_why_cant_you = False
    $ dml_chose_is_there_nothing = False
    $ dml_chose_what_would_happen = False

    $ dml_times_gotten += 1

    # Leading text
    scene bg Villain with fade
    n "The forest's atmosphere grew heavier as the princess and the hero ventured deeper, an unnatural darkness creeping in from all sides. The air was thick with the stench of decay, and the once vibrant trees were now withered and lifeless."
    n "The hero's hand hovered over his sword, eyes narrowing as the oppressive energy weighed down on them. He could sense it—an evil force lurking nearby, draining the life from everything it touched."
    play music "audio/5 Second Villian 3.mp3" loop volume 1.0 fadein 0.5
    scene bg villain_far_dml with dissolve
    n "From the shadows, a figure materialized, cloaked in dark robes that seemed to absorb the light around them. His eyes glowed with a malevolent energy, and a twisted smile spread across his face as he observed the pair."
    dml "Ah, the kingdom's pawns have arrived. Come to witness the grandeur of true power? You're just in time to see the culmination of my work!"
    
    if dml_times_gotten == 1: 
        pt "The Dark Magic Lord again... He's the source of all this corruption. We have to stop him before it's too late." 
    
    elif dml_times_gotten == 2: 
        pt "We've faced him before. We know his tricks, but he's more dangerous than ever. We can't let our guard down." 
    
    else: 
        pt "It's him again... We know what to expect, but we can't underestimate him. This has to end soon..."
    
    n "The Dark Magic Lord stepped forward, his presence exuding an overwhelming aura of arrogance and delusion. The hero instinctively moved in front of the princess, his stance protective but tense."
    h "Stay back, princess. His power may be great, but it's born of madness. We must be careful."
    dml "Madness? You dare call my work madness? This forest was dying long before I arrived. I am its salvation, its rebirth! But of course, you're too blind to see the truth."
    n "The Dark Magic Lord raised his hand, dark tendrils of magic swirling around his fingers, ready to strike at a moment's notice. The air buzzed with dangerous energy, and the forest seemed to tremble under his influence."
    dml "Enough talk. If you're so determined to stand in my way, then witness the power of the one true savior of this world!"

    jump dml_choices_1

    # Level 1 of choice tree
    label dml_choices_1:
        # Initial branch
        menu:
            "(Act) Challenge his authority":
                n "The princess stepped forward, her eyes blazing with determination as she faced the Dark Magic Lord. His presence was oppressive, a shadow that seemed to swallow the very light around him."
                p "Your reign of darkness ends here. You have no power over us!"
                n "The Dark Magic Lord's gaze settled on the princess, a cold smile curling his lips."
                dml "Bold words for a lost princess. Do you truly believe you can defy me?"
                n "The hero tightened his grip on his sword, ready to follow the princess's lead."
                h "I've faced worse than you, Dark Magic Lord"
                n "The Dark Magic Lord's laughter echoed through the darkened chamber, a chilling sound that made the air grow colder."
                dml "Very well. Let's see if your courage is enough to save you from your fate."

                jump dml_choices_2_1

            "(Act) Attempt to reason with him":
                n "The princess took a step forward, her voice calm but firm, trying to pierce through the aura of malevolence that surrounded the Dark Magic Lord."
                p "There's no need for more bloodshed. Whatever you seek, we can find another way."
                n "The Dark Magic Lord's eyes narrowed, his expression unreadable as he studied her."
                dml "Another way? Do you truly believe there is any path left but the one I've chosen?"
                n "The hero stood by, tense but ready, watching the Dark Magic Lord's every move."
                h "Princess, be careful. He's not one to listen to reason."
                n "The Dark Magic Lord's expression softened slightly, as if considering her words, but his eyes remained cold."
                dml "You misunderstand me, girl. I am beyond redemption. I walk the path of power, and no words will sway me from my destiny."

                jump dml_choices_2_2

            
            # Dialogue pool options

            "(Inquire) Who are you?" if not dml_chose_who_are_you:
                $ dml_chose_who_are_you = True
                call dml_who_are_you
                jump dml_choices_1

            "(Inquire) Why do you claim to be a hero?" if not dml_chose_why_do_you and dml_chose_who_are_you:
                $ dml_chose_why_do_you = True
                call dml_why_do_you
                jump dml_choices_1

            "(Inquire) What do you truly seek?" if not dml_chose_what_do_you and dml_chose_why_do_you:
                $ dml_chose_what_do_you = True
                call dml_what_do_you
                jump dml_choices_1

            "(Inquire) How did you come to wield such power?" if not dml_chose_how_did_you:
                $ dml_chose_how_did_you = True
                call dml_how_did_you
                jump dml_choices_1

            "(Inquire) What drives your obsession with magic?" if not dml_chose_what_drives_your and dml_chose_how_did_you:
                $ dml_chose_what_drives_your = True
                call dml_what_drives_your
                jump dml_choices_1

            "(Inquire) Do you not understand the consequences of your actions?" if not dml_chose_do_you_not and dml_chose_what_drives_your:
                $ dml_chose_do_you_not = True
                call dml_do_you_not
                jump dml_choices_1
            
            "(Inquire) What is your end goal?" if not dml_chose_what_is_your:
                $ dml_chose_what_is_your = True
                call dml_what_is_your
                jump dml_choices_1

            "(Inquire) Do you really believe this will save the world?" if not dml_chose_do_you_really and dml_chose_what_is_your:
                $ dml_chose_do_you_really = True
                call dml_do_you_really
                jump dml_choices_1

            "(Inquire) How do you justify the suffering you've caused?" if not dml_chose_how_do_you and dml_chose_do_you_really:
                $ dml_chose_how_do_you = True
                call dml_how_do_you
                jump dml_choices_1

            "(Inquire) Why can't you stop overusing magic?" if not dml_chose_why_cant_you:
                $ dml_chose_why_cant_you = True
                call dml_why_cant_you
                jump dml_choices_1

            "(Inquire) Is there nothing that would change your mind?" if not dml_chose_is_there_nothing and dml_chose_why_cant_you:
                $ dml_chose_is_there_nothing = True
                call dml_is_there_nothing
                jump dml_choices_1

            "(Inquire) What would happen if you did stop?" if not dml_chose_what_would_happen and dml_chose_is_there_nothing:
                $ dml_chose_what_would_happen = True
                call dml_what_would_happen
                jump dml_choices_1


    # Level 2 of choice tree
    label dml_choices_2_1:
        # Branching from "(Act) Challenge his authority"
        menu:
            "(Act) Engage in direct combat":
                scene bg villain_hero_charging_far_dml with dissolve
                n "The princess nodded to the hero, who lunged forward with his sword, aiming for the Dark Magic Lord's heart."
                p "Keep him distracted, hero! We have to break his focus!"
                n "The Dark Magic Lord raised a hand, summoning a wall of dark energy to block the hero's strike. The chamber shuddered with the force of their clash."
                scene bg villain_far_dml with dissolve
                dml "Is this the best you can muster? A feeble attack from a broken kingdom?"
                n "The hero pressed forward, determined, his sword glowing with a faint light as he pushed against the dark barrier."
                h "I'm just getting started."

                jump dml_choices_3_1
            "(Act) Use magic to weaken his power" if chose_magic:
                n "The princess closed her eyes, feeling the familiar pull of magic within her. She knew she had to weaken the Dark Magic Lord's grip on his dark power."
                p "Focus... draw from the forest, not from him."
                n "She extended her hand, channeling a beam of light toward the Dark Magic Lord. The beam pierced his shadowy form, causing him to stagger."
                dml "You think your pathetic magic can stand against mine?"
                n "The Dark Magic Lord's expression twisted in fury as he raised his hands to retaliate, summoning a torrent of dark energy to crush her light."
                p "Hold your ground, hero! We can't let him regain his strength!"

                jump dml_choices_3_2

            
            # Dialogue pool options

            "(Inquire) Who are you?" if not dml_chose_who_are_you:
                $ dml_chose_who_are_you = True
                call dml_who_are_you
                jump dml_choices_2_1

            "(Inquire) Why do you claim to be a hero?" if not dml_chose_why_do_you and dml_chose_who_are_you:
                $ dml_chose_why_do_you = True
                call dml_why_do_you
                jump dml_choices_2_1

            "(Inquire) What do you truly seek?" if not dml_chose_what_do_you and dml_chose_why_do_you:
                $ dml_chose_what_do_you = True
                call dml_what_do_you
                jump dml_choices_2_1

            "(Inquire) How did you come to wield such power?" if not dml_chose_how_did_you:
                $ dml_chose_how_did_you = True
                call dml_how_did_you
                jump dml_choices_2_1

            "(Inquire) What drives your obsession with magic?" if not dml_chose_what_drives_your and dml_chose_how_did_you:
                $ dml_chose_what_drives_your = True
                call dml_what_drives_your
                jump dml_choices_2_1

            "(Inquire) Do you not understand the consequences of your actions?" if not dml_chose_do_you_not and dml_chose_what_drives_your:
                $ dml_chose_do_you_not = True
                call dml_do_you_not
                jump dml_choices_2_1
            
            "(Inquire) What is your end goal?" if not dml_chose_what_is_your:
                $ dml_chose_what_is_your = True
                call dml_what_is_your
                jump dml_choices_2_1

            "(Inquire) Do you really believe this will save the world?" if not dml_chose_do_you_really and dml_chose_what_is_your:
                $ dml_chose_do_you_really = True
                call dml_do_you_really
                jump dml_choices_2_1

            "(Inquire) How do you justify the suffering you've caused?" if not dml_chose_how_do_you and dml_chose_do_you_really:
                $ dml_chose_how_do_you = True
                call dml_how_do_you
                jump dml_choices_2_1

            "(Inquire) Why can't you stop overusing magic?" if not dml_chose_why_cant_you:
                $ dml_chose_why_cant_you = True
                call dml_why_cant_you
                jump dml_choices_2_1

            "(Inquire) Is there nothing that would change your mind?" if not dml_chose_is_there_nothing and dml_chose_why_cant_you:
                $ dml_chose_is_there_nothing = True
                call dml_is_there_nothing
                jump dml_choices_2_1

            "(Inquire) What would happen if you did stop?" if not dml_chose_what_would_happen and dml_chose_is_there_nothing:
                $ dml_chose_what_would_happen = True
                call dml_what_would_happen
                jump dml_choices_2_1

    label dml_choices_2_2:
        # Branching from "(Act) Attempt to reason with him"
        menu:
            "(Act) Appeal to his lost humanity":
                n "The princess stepped closer, her voice soft yet firm, trying to reach the man buried beneath the darkness."
                p "You weren't always like this. There was a time when you cared for more than just power. Remember who you were."
                n "The Dark Magic Lord's eyes flickered, a brief moment of vulnerability crossing his face before it hardened once more."
                dml "I am what I must be. The past is dead, and so is the man you speak of."
                n "The hero glanced at the princess, sensing a flicker of hope, but not daring to believe it was real."
                h "There's still a chance, princess. Don't give up."
                n "The Dark Magic Lord's voice turned cold again, his momentary lapse gone as quickly as it appeared."
                dml "Enough of this sentiment. You waste your breath."

                jump dml_choices_3_3
            "(Act) Bargain for information":
                n "The princess knew she needed more than just force to deal with the Dark Magic Lord. She decided to try a different approach."
                p "What is it you truly want? There must be something more than just darkness and destruction."
                n "The Dark Magic Lord looked at her, intrigued by her boldness, though his eyes remained guarded."
                dml "You seek to bargain with me, princess? What could you possibly offer that would interest one such as I?"
                n "The hero shifted uneasily, unsure of where the princess was going with this, but trusting her instincts."
                h "Be careful, princess. He's not to be trusted."
                n "The princess met the Dark Magic Lord's gaze, her voice steady."
                p "Knowledge. Power. Freedom from the forest's grip. Name your price, and we'll see if we can meet it."
                n "The Dark Magic Lord's lips curled into a sinister smile, considering her offer carefully."
                dml "Very well, princess. Let us see what you are willing to pay for the answers you seek."

                jump dml_choices_3_4

            
            # Dialogue pool options

            "(Inquire) Who are you?" if not dml_chose_who_are_you:
                $ dml_chose_who_are_you = True
                call dml_who_are_you
                jump dml_choices_2_2

            "(Inquire) Why do you claim to be a hero?" if not dml_chose_why_do_you and dml_chose_who_are_you:
                $ dml_chose_why_do_you = True
                call dml_why_do_you
                jump dml_choices_2_2

            "(Inquire) What do you truly seek?" if not dml_chose_what_do_you and dml_chose_why_do_you:
                $ dml_chose_what_do_you = True
                call dml_what_do_you
                jump dml_choices_2_2

            "(Inquire) How did you come to wield such power?" if not dml_chose_how_did_you:
                $ dml_chose_how_did_you = True
                call dml_how_did_you
                jump dml_choices_2_2

            "(Inquire) What drives your obsession with magic?" if not dml_chose_what_drives_your and dml_chose_how_did_you:
                $ dml_chose_what_drives_your = True
                call dml_what_drives_your
                jump dml_choices_2_2

            "(Inquire) Do you not understand the consequences of your actions?" if not dml_chose_do_you_not and dml_chose_what_drives_your:
                $ dml_chose_do_you_not = True
                call dml_do_you_not
                jump dml_choices_2_2
            
            "(Inquire) What is your end goal?" if not dml_chose_what_is_your:
                $ dml_chose_what_is_your = True
                call dml_what_is_your
                jump dml_choices_2_2

            "(Inquire) Do you really believe this will save the world?" if not dml_chose_do_you_really and dml_chose_what_is_your:
                $ dml_chose_do_you_really = True
                call dml_do_you_really
                jump dml_choices_2_2

            "(Inquire) How do you justify the suffering you've caused?" if not dml_chose_how_do_you and dml_chose_do_you_really:
                $ dml_chose_how_do_you = True
                call dml_how_do_you
                jump dml_choices_2_2

            "(Inquire) Why can't you stop overusing magic?" if not dml_chose_why_cant_you:
                $ dml_chose_why_cant_you = True
                call dml_why_cant_you
                jump dml_choices_2_2

            "(Inquire) Is there nothing that would change your mind?" if not dml_chose_is_there_nothing and dml_chose_why_cant_you:
                $ dml_chose_is_there_nothing = True
                call dml_is_there_nothing
                jump dml_choices_2_2

            "(Inquire) What would happen if you did stop?" if not dml_chose_what_would_happen and dml_chose_is_there_nothing:
                $ dml_chose_what_would_happen = True
                call dml_what_would_happen
                jump dml_choices_2_2


    # Level 3 of choice tree
    label dml_choices_3_1:
        # Branching from "(Act) Engage in direct combat"
        menu:
            "(Act) Strike with the hero's sword" if not chose_magic:
                scene bg villain_hero_charging_far_dml with dissolve
                n "The hero moved with swift determination, his sword a blur of silver as he closed the distance between them."
                p "Go for his weak spot! He's vulnerable when he casts!"
                n "The hero nodded, his focus narrowing to a single point. He swung his blade in a powerful arc, aiming directly at the Dark Magic Lord's exposed side."
                dml "Foolish mortal! You think a mere sword can harm me?"
                scene bg villain_far_dml with dissolve
                n "But the blade connected, slicing through the dark tendrils that surrounded him. The Dark Magic Lord staggered back, surprise flashing in his eyes."
                h "You're not invincible. We can win this."
                n "The princess felt a surge of hope. The Dark Magic Lord's defenses were not impenetrable—they could be broken."

                jump dml_choices_4_1
            "(Act) Create an opening with a magic blast" if chose_magic:
                n "The princess felt the magic pulse within her, a surge of power that thrummed through her veins. She focused her energy, channeling a blast of light towards the Dark Magic Lord."
                p "Now, hero! While he's off balance!"
                n "The hero charged forward, sword raised as the blast of magic collided with the Dark Magic Lord. Shadows erupted around him, obscuring his form in a swirling mass of darkness."
                dml "You dare use magic against me? You will regret this!"
                n "The Dark Magic Lord conjured a shield of dark energy to absorb the impact. But the force of the blast was stronger than he anticipated, causing him to falter."
                h "I'm through playing games. Let's end this, princess!"
                n "The princess nodded, her heart racing as she prepared for the final push."

                jump dml_choices_4_2

    label dml_choices_3_2:
        # Branching from "(Act) Use magic to weaken his power"
        menu:
            "(Act) Seal his dark magic with a counterspell":
                n "The princess knew she needed to cut off the source of the Dark Magic Lord's power. She focused her energy, chanting a counterspell that would bind his dark magic."
                p "Stay back, hero. This might get dangerous."
                n "The air crackled with energy as the spell formed in her mind, a weave of light that shimmered against the encroaching darkness."
                dml "What are you doing? No—stop!"
                n "The Dark Magic Lord's voice was filled with sudden panic as the counterspell took hold, wrapping around his dark aura like chains. His power flickered, his connection to the darkness beginning to sever."
                h "It's working! Keep going, princess!"
                n "The princess's hands shook from the strain, until she could no longer hold on, losing control of the seal."

                jump dml_choices_4_3
            "(Act) Overwhelm him with a burst of light":
                n "The princess drew on the forest's magic, summoning a blinding burst of light to dispel the shadows around the Dark Magic Lord."
                p "Let the light cleanse this darkness!"
                n "The chamber flooded with brilliant light, banishing the shadows that clung to the Dark Magic Lord. He recoiled, shielding his eyes from the blinding glow."
                dml "No! This light... it's impossible!"
                n "The hero took advantage of the distraction, moving in with his sword to strike. But the Dark Magic Lord, though weakened, was not yet defeated."
                h "Push him back! We can break his hold!"
                n "The princess tried to maintain the burst of light, but she lost control, her magic failing to keep the Dark Magic Lord in check."

                jump dml_choices_4_4

    label dml_choices_3_3:
        # Branching from "(Act) Appeal to his lost humanity"
        menu:
            "(Act) Remind him of his past":
                n "The princess softened her tone, reaching for the remnants of the man the Dark Magic Lord used to be."
                p "I know there was a time when you weren't this... a time when you fought for something good."
                n "The Dark Magic Lord's eyes flickered with an emotion she couldn't quite place. His hand, raised to cast a spell, wavered."
                dml "You know nothing of me, girl. The past is a shadow, and shadows have no place in my realm."
                n "The hero, sensing the change in the Dark Magic Lord's demeanor, stepped closer, ready to strike if needed."
                h "You don't have to keep fighting. There's another way."
                n "But the Dark Magic Lord's face hardened again, his brief hesitation giving way to renewed resolve."
                dml "Enough of your prattle! You will die here, like all who oppose me."

                jump dml_choices_4_5
            "(Act) Challenge him to confront his own corruption":
                n "The princess's voice was firm, cutting through the tension like a blade."
                p "Look around you! Your so-called power is nothing but corruption. You're destroying everything you touch."
                n "The Dark Magic Lord's gaze darkened, his jaw tightening as he glared at her."
                dml "I do what I must. The weak perish, and the strong survive."
                n "The hero stood beside the princess, his sword ready, sensing the growing conflict within the Dark Magic Lord."
                h "And what are you, then? A ruler of ashes and bones?"
                n "The Dark Magic Lord's grip on his staff tightened, the shadows around him writhing with his anger."
                dml "Silence! You know nothing of power or what it takes to wield it."

                jump dml_choices_4_6

    label dml_choices_3_4:
        # Branching from "(Act) Bargain for information"
        menu:
            "(Act) Offer him something of value" if chose_magic:
                n "The princess decided to play on the Dark Magic Lord's insatiable greed and curiosity."
                p "I have something that you can't refuse. Something that could change everything for you."
                n "The Dark Magic Lord's eyes narrowed with interest, a calculating gleam flickering within."
                dml "Something I cannot refuse? You speak boldly, but I sense no lies... What is it you claim to possess?"
                n "The hero's grip on his sword tightened, prepared for whatever move the princess had planned."
                h "Careful, princess. He's not to be trusted."
                n "Intrigued by her offer, the Dark Magic Lord seemed momentarily caught off guard, his desire for knowledge outweighing his usual caution."

                jump dml_choices_4_7
            "(Act) Feign submission and plan a counterattack":
                n "The princess dropped to one knee, lowering her head in a gesture of submission."
                p "We surrender. Just... spare us."
                n "The Dark Magic Lord's lips curled into a satisfied smile, arrogance gleaming in his eyes."
                dml "At last, some sense from the fools who thought they could challenge me."
                n "The hero remained standing, his posture tense. The princess caught his eye, giving a subtle nod that only he would understand."
                h "Princess, no... we can't—"
                n "The princess cut him off with a sharp glance, signaling him to trust her plan. She knew the Dark Magic Lord's arrogance would be his undoing."
                p "Please... let us live, and we will serve you."
                n "As the Dark Magic Lord lowered his guard, the hero and princess prepared for their counterattack, ready to strike when the moment was right."

                jump dml_choices_4_8

    
    # Level 4 of choice tree
    label dml_choices_4_1:
        # Branching from "(Act) Strike with the hero's sword"
        menu:
            "(Act) Go for a decisive blow":
                n "The hero, seeing the Dark Magic Lord momentarily staggered, seized the opportunity to go for a decisive blow."
                p "Now! Strike him down before he can recover!"
                scene bg villain_hero_charging_far_dml with dissolve
                n "The hero's sword gleamed with a fierce light as he lunged forward, aiming directly for the Dark Magic Lord's heart."
                dml "You think you can defeat me so easily?"
                scene bg villain_far_dml with dissolve
                n "But the Dark Magic Lord was not so easily undone. He summoned a dark shield, barely managing to deflect the blow, yet the force sent him reeling."
                h "I've fought tougher than you. Your darkness won't prevail!"
                n "The princess watched, her breath held, knowing that this was their best chance to end the Dark Magic Lord's reign of terror once and for all."

                jump dml_choices_5_1
            "(Act) Use the environment to gain an advantage":
                n "The princess's eyes scanned the chamber, looking for anything that could turn the tide in their favor."
                p "Hero, the ledge above! If we can get him underneath it..."
                scene bg villain_hero_sword_facing_far_dml with dissolve
                n "The hero understood immediately, nodding as he feigned a strike, drawing the Dark Magic Lord's attention."
                h "Over here, shadow master!"
                n "As the Dark Magic Lord turned to face the hero, the princess focused her energy on a loose section of rock above him. With a forceful shout, she willed it to break free."
                dml "What are you—"
                scene bg villain_far_dml with dissolve
                n "The rock fell, crashing down toward the Dark Magic Lord. He narrowly dodged, but the disruption left him exposed."

                jump dml_choices_5_2

    label dml_choices_4_2:
        # Branching from "(Act) Create an opening with a magic blast"
        menu:
            "(Act) Follow up with a powerful strike":
                n "The princess knew that to capitalize on her magic blast, they needed to follow through with relentless force."
                p "Don't give him a chance to recover! Keep pressing the attack!"
                n "With a surge of determination, she unleashed another spell, a powerful arc of energy aimed to disorient the Dark Magic Lord."
                dml "You insolent wretch! Enough of your tricks!"
                n "The Dark Magic Lord struggled to maintain his focus, his dark barrier cracking under the sustained assault. The hero charged, his sword infused with the magic still lingering in the air."
                h "For the kingdom!"
                n "With a mighty swing, the hero aimed to land a devastating blow, one that would shatter the Dark Magic Lord's defenses for good."

                jump dml_choices_5_3
            "(Act) Distract him and go invisible":
                n "The princess's mind raced, knowing they needed a new strategy. She whispered a quick incantation, preparing to go invisible."
                p "Hero, keep his attention on you! I have a plan."
                scene bg villain_hero_sword_facing_far_dml with dissolve
                n "The hero nodded, stepping forward to challenge the Dark Magic Lord directly, his movements bold and aggressive."
                h "You've met your match, sorcerer!"
                n "While the Dark Magic Lord was focused on the hero, the princess vanished in a shimmer of light."
                dml "What—where did she go?"

                jump dml_choices_5_4

    label dml_choices_4_3:
        # Branching from "(Act) Seal his dark magic with a counterspell"
        menu:
            "(Act) Contain him in a magic circle":
                n "The princess began chanting a complex incantation, drawing a glowing circle of light around the Dark Magic Lord."
                p "This circle will hold him—if we can keep him inside!"
                scene bg villain_far_dml_magic_circle with dissolve
                n "The lines of the circle flared with power, rising into a shimmering barrier that began to close in around the Dark Magic Lord."
                dml "You think a simple barrier will hold me? I am darkness incarnate!"
                n "He lashed out with tendrils of shadow, but they fizzled against the bright energy of the circle. The princess poured more power into the spell, her voice unwavering."
                h "We have to keep him contained! Don't let him break through!"
                n "The circle tightened, its light growing brighter and more intense, forcing the Dark Magic Lord to his knees within its confines."

                jump dml_choices_5_5
            "(Act) Counter his curse":
                n "As the Dark Magic Lord prepared a curse, the princess felt a rush of intuition, knowing that she could turn the Dark Magic Lord's own magic against him."
                p "Your own darkness will be your undoing!"
                n "The princess knew that to take down the Dark Magic Lord, she would have to do it right."

                jump dml_choices_5_6

    label dml_choices_4_4:
        # Branching from "(Act) Overwhelm him with a burst of light"
        menu:
            "(Act) Channel all your magic into a final spell":
                n "The princess knew that to end this battle, she needed to summon every ounce of her power. Her heart pounded as she began to gather the magic within her, feeling it surge and swell like a storm."
                p "This has to end... now or never."
                n "She closed her eyes, drawing in a deep breath, and raised her hands to the sky. The air around her crackled with energy as she began to channel the full force of her magic."
                h "Princess, what are you doing?!"
                n "The hero watched in awe and concern as a blinding light began to form around the princess, growing brighter with every passing moment. The ground beneath them trembled under the weight of the power she was summoning."
                dml "Do you really think you can challenge my power with this... display?"
                n "The Dark Magic Lord's expression shifted from confident disdain to wary anticipation, sensing the immense magic gathering in the air."
                p "Get ready... for the final strike."
                n "The magic built to a crescendo, swirling around the princess like a hurricane of light and energy, her entire body glowing with the raw power she was channeling."

                jump dml_choices_5_7
            "(Act) Bind his power and offer a truce":
                n "The princess knew she needed to take control of the situation without risking their lives. She whispered an incantation, threads of light forming around the Dark Magic Lord."
                p "You don't have to keep fighting, Dark Magic Lord. We can end this without more bloodshed."
                scene bg villain_far_dml_chained_hands with dissolve
                n "The magic wove itself around him, binding his hands and feet with glowing chains. He struggled, but the light held firm."
                dml "You think you can bind me with such feeble magic?"
                n "The princess took a step closer, her voice calm but firm."
                p "Surrender now, and we can find another way. There is still a chance for peace, but only if you lay down your power."
                n "The Dark Magic Lord's eyes flickered with something—perhaps doubt, or a recognition of his own limitations in the face of this new magic."

                jump dml_choices_5_8

    label dml_choices_4_5:
        # Branching from "(Act) Remind him of his past"
        menu:
            "(Act) Appeal to his sense of honor":
                n "The princess stepped forward, her voice carrying a tone of earnestness and conviction."
                p "You were once a great warrior, a protector of your people. Is this truly how you wish to be remembered?"
                n "The Dark Magic Lord's gaze wavered, a flicker of something—maybe regret or memory—crossing his face."
                dml "That was... a long time ago. I am no longer that man."
                n "The hero tightened his grip on his sword, sensing the shift in the Dark Magic Lord's demeanor."
                h "But that man still exists within you. You can choose to honor that legacy instead of clinging to this darkness."
                n "For a moment, the Dark Magic Lord hesitated, his eyes distant as if lost in a memory of who he used to be."

                jump dml_choices_5_9
            "(Act) Remind him of the loved ones he lost":
                n "The princess's voice softened, taking on a tone of compassion."
                p "You've lost much in your pursuit of power. The ones you loved—do they not deserve to be remembered in a better way than this?"
                n "The Dark Magic Lord's expression darkened, but there was a flicker of pain in his eyes—a reminder of the humanity he had once abandoned."
                dml "They... they would never understand the choices I made. They are gone, lost to time and fate."
                n "The hero stepped forward, his voice steady and sincere."
                h "You can still honor their memory. Let go of this darkness, and perhaps, find peace."
                n "The Dark Magic Lord's hands trembled, the weight of his past seeming to bear down on him once more."

                jump dml_choices_5_10

    label dml_choices_4_6:
        # Branching from "(Act) Challenge him to confront his own corruption"
        menu:
            "(Act) Make him see the consequences of his actions" if chose_magic:
                n "The princess knew words alone would not be enough to reach him. She drew upon her magic, weaving a spell that would force the Dark Magic Lord to face the destruction he had caused."
                p "Look around you! See what your thirst for power has done!"
                n "The air shimmered, and images began to form—scenes of the forest dying, the rivers running dry, and the desolation spreading like a dark stain."
                dml "No... this is not..."
                n "The Dark Magic Lord's face twisted in shock as the images played out before him, a mirror of his own corruption."
                h "You have brought this upon yourself. It's not too late to change course."
                n "The Dark Magic Lord's eyes widened, the full weight of his actions crashing down upon him, breaking through the barriers of his denial."

                jump dml_choices_5_11
            "(Act) Push him to redeem himself" if not chose_magic:
                n "The princess's voice was firm, her words cutting through the tension like a knife."
                p "You still have a chance to make things right. Redeem yourself, and let go of this dark path."
                n "The Dark Magic Lord's gaze was cold, but there was a flicker of something—an emotion he had long buried."
                dml "Redemption... is a fool's game. I have come too far."
                n "The hero stepped beside the princess, his stance resolute."
                h "It's never too late to choose a different path. Even a dark magic lord can seek redemption."
                n "The Dark Magic Lord's hands clenched into fists, his mind seemingly torn between his past choices and a possible future."

                jump dml_choices_5_12

    label dml_choices_4_7:
        # Branching from "(Act) Offer him something of value"
        menu:
            "(Act) Offer to share forbidden knowledge":
                n "The princess kept her voice steady, sensing the Dark Magic Lord's insatiable curiosity and thirst for power."
                p "I can offer you something that no one else can—knowledge. Secrets of magic that even you do not possess."
                n "The Dark Magic Lord's eyes gleamed with interest, his posture relaxing just slightly."
                dml "Forbidden knowledge, you say? You speak as if you have something that could truly tempt me, girl."
                n "The hero shot the princess a wary glance, unsure of her plan but trusting her instinct."
                h "Be careful, princess. His desire for power knows no bounds."
                n "The princess continued, her words measured and calm, baiting the Dark Magic Lord's pride."
                p "Knowledge that could make you more powerful than ever before. But only if you are willing to listen."
                n "The Dark Magic Lord's expression shifted, a mixture of suspicion and intrigue. His desire for greater power was undeniable."
                dml "Very well, princess. Speak, and let us see if you truly have something worth my time."

                jump dml_choices_5_13
            "(Act) Offer to combine your powers":
                n "The princess knew that the Dark Magic Lord would be drawn to the idea of increasing his already immense power."
                p "What if we combined our magic? Think of what we could accomplish together, with your dark magic and my light."
                n "The Dark Magic Lord's eyes narrowed, his mind racing with the possibilities."
                dml "Combine our powers? You think you can match my strength, or that I would even need your help?"
                n "The hero tensed, gripping his sword tightly as he watched the princess carefully."
                h "Princess, he won't share power. He'll just take what he wants."
                n "The princess nodded subtly, acknowledging the hero's warning but pressing on with her plan."
                p "It's not about sharing, it's about expanding. With our combined abilities, we could wield a force that no one else could stand against."
                n "The Dark Magic Lord's expression wavered, his ambition and greed momentarily outweighing his suspicion."
                dml "An intriguing proposal... but know this, princess—I do not tolerate betrayal."

                jump dml_choices_5_14

    label dml_choices_4_8:
        # Branching from "(Act) Feign submission and plan a counterattack"
        menu:
            "(Act) Wait for the perfect moment to strike" if not chose_magic:
                n "The princess remained on her knees, feigning submission, her eyes carefully watching the Dark Magic Lord. His arrogance had grown with every moment they appeared to be defeated."
                dml "So, you finally understand your place. A wise decision, princess. You and your hero shall be spared... for now."
                n "The hero stood beside her, appearing defeated as well, but his eyes never left the Dark Magic Lord. He was waiting, every muscle tense, for the princess's signal."
                h "Stay calm... wait for it..."
                n "The Dark Magic Lord, sensing no immediate threat, lowered his guard even further, turning his attention away from them, his focus shifting back to his dark plans."
                p "Hero, be ready... we're only going to get one chance."
                n "The air around them was tense, the chamber filled with an uneasy silence as they prepared for the perfect moment to turn the tide in their favor."

                jump dml_choices_5_15
            "(Act) Manipulate him into lowering his guard":
                n "The princess's voice trembled with false humility, her posture one of submission, yet her mind was sharp and calculating."
                p "We see now that resistance is futile... Please, spare us, and we will serve you faithfully."
                n "The Dark Magic Lord's expression softened with a twisted smile, his pride swelling at their apparent capitulation."
                dml "Serve me? Perhaps you have some use after all. Perhaps I was too quick to dismiss your potential."
                n "The hero stood silently beside her, his body language deceptively relaxed, though he was poised to act at a moment's notice."
                h "Just keep him talking, princess... we need him distracted."
                n "The Dark Magic Lord turned away slightly, his confidence growing as he believed he had them under his control. The princess exchanged a quick glance with the hero, knowing the moment to act would soon come."
                p "Patience, hero... the time is near."
                n "They both remained ready, every second ticking by bringing them closer to the chance they needed to exploit the Dark Magic Lord's overconfidence."

                jump dml_choices_5_16


    # Level 5 of choice tree
    label dml_choices_5_1:
        # Branching from "(Act) Go for a decisive blow"
        menu:
            "(Act) Strike at his heart":
                n "The hero saw his chance—a brief moment where the Dark Magic Lord's defenses faltered. He gripped his sword tightly, preparing to deliver a strike aimed straight at the dark sorcerer's heart."
                p "Now, hero! Finish this while he's vulnerable!"
                n "The hero lunged forward, his blade gleaming in the dim light. With all his might, he drove the sword toward the Dark Magic Lord's chest, hoping to end the battle once and for all."
                dml "You dare—"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But as the blade pierced through, the Dark Magic Lord, with his last ounce of strength, raised his hand, a dark spell forming at his fingertips, aimed directly at the hero."
                n "Seeing the spell, the princess acted on pure instinct. She leaped in front of the hero, taking the full force of the dark magic meant for him."
                n "The spell struck the princess, sending a searing pain through her body. She fell to the ground, her vision blurring as the last of her strength faded away."
                n "The hero caught her as she collapsed, his eyes wide with shock and horror. The Dark Magic Lord's life slipped away as well, his final curse having cost him his last breath."
                n "The hero's heart shattered as he held the princess in his arms, her life slipping away with each passing moment. Though they had defeated the Dark Magic Lord, the victory was hollow, the price too great."
                n "The kingdom would mourn the loss of their brave princess, but the hero would carry her memory with him, forever haunted by the love they could never truly fulfill."
                n "And the hero lived happily ever—"

                jump sacrificed_princess
            "(Act) Overpower him with raw strength":
                n "The hero, fueled by determination and a fierce desire to protect the kingdom, summoned every ounce of his strength. With a mighty roar, he charged at the Dark Magic Lord, swinging his sword with raw, unstoppable power."
                p "We can do this! Together, we can end his reign!"
                n "The Dark Magic Lord's eyes widened in surprise as the hero's sword cleaved through his dark defenses, shattering the barriers he had conjured."
                dml "Impossible! I am invincible!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But the hero's attack did not relent. With one final, powerful strike, he knocked the Dark Magic Lord to the ground, the dark sorcerer's staff flying from his grasp."
                n "The Dark Magic Lord fell, his dark magic sputtering out as his body hit the ground, lifeless. The chamber grew silent, the oppressive darkness lifting as the sorcerer's power faded."
                n "With the Dark Magic Lord defeated, the princess and hero returned to the kingdom, triumphant. The people rejoiced, celebrating the end of a dark era and the dawn of a new beginning."
                n "The princess, hailed as a hero, ascended the throne, her wisdom and courage guiding the kingdom to a brighter future. By her side, the hero stood as her most trusted advisor and protector."
                n "Together, they would rule with compassion and strength, ensuring that the darkness would never again threaten their land."
                n "And the princess and hero lived happily ever—"

                jump inherited_throne

    label dml_choices_5_2:
        # Branching from "(Act) Use the environment to gain an advantage"
        menu:
            "(Act) Lure him into a trap":
                n "The princess's sharp eyes darted around the chamber, spotting a loose section of rock precariously balanced above the Dark Magic Lord."
                p "Hero, lead him under that ledge! We can use it to our advantage!"
                n "The hero nodded, understanding her plan. He taunted the Dark Magic Lord, baiting him into a rage-fueled charge."
                h "You're getting sloppy, old man! Come and face me!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The Dark Magic Lord, blinded by fury, took the bait, following the hero directly beneath the unstable ledge. With a swift motion, the princess sent a surge of magic toward the rocks, causing them to collapse."
                n "The rocks fell with a thunderous crash, burying the Dark Magic Lord beneath their weight. His cries of anger were quickly silenced by the debris, his dark magic unable to save him."                
                n "The chamber fell silent, the dust settling as the princess and hero stood victorious over the fallen foe. With the Dark Magic Lord's defeat, the oppressive darkness that had plagued the land lifted."
                n "Returning to the kingdom, they were greeted as saviors. The princess took her place on the throne, determined to rule with wisdom and justice, ensuring that no shadow would ever again fall upon her people."
                n "And by her side, the hero would remain, her steadfast companion and protector, as they would forge a new path for the kingdom's future."
                n "And the princess and hero lived happily ever—"

                jump inherited_throne
            "(Act) Have the hero distract him":
                n "The hero and the princess moved swiftly, using the shadows to their advantage."
                p "Hero, keep him distracted. I have an idea."
                scene bg villain_hero_charging_far_dml with dissolve
                n "The hero nodded, engaging the Dark Magic Lord with a flurry of strikes, his movements deliberate and precise, designed to keep the sorcerer's focus on him."
                h "You're not as powerful as you think, Dark Magic Lord!"
                n "As the Dark Magic Lord sneered and parried the hero's attacks, he began to conjure a final spell aimed directly at the hero."
                p "No! I won't let you harm him!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "Without a second thought, the princess leapt in front of the hero, taking the full brunt of the dark spell. Pain seared through her, but she stood her ground."
                n "The spell struck the princess, and she crumpled to the ground, her body shielding the hero from the fatal blow. Her breath came in ragged gasps, but a small smile crossed her lips as she looked at the hero one last time."
                n "The Dark Magic Lord's life ebbed away, his final curse taking its toll on him as well. The hero, tears streaming down his face, held the princess close, her sacrifice a painful reminder of the cost of their victory."
                n "Though they had defeated the darkness, the price had been too high. The hero would forever carry the memory of the princess's selfless act, her courage, and her love."
                n "And the hero lived happily ever—"

                jump sacrificed_princess

    label dml_choices_5_3:
        # Branching from "(Act) Follow up with a powerful strike"
        menu:
            "(Act) Channel dark energy for a finishing blow":
                n "The princess knew they had to end the battle quickly before the Dark Magic Lord could regain his strength. She drew upon the dark energy lingering in the chamber, channeling it into her magic."
                p "We can't hold back anymore. Hero, get ready!"
                n "The hero braced himself, his sword glowing faintly as he prepared to strike. The princess focused her energy, letting the dark magic course through her, amplifying her power."
                dml "You dare use my own magic against me? Foolish girl!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But the princess was resolute. With a fierce shout, she unleashed a surge of dark energy, aiming it directly at the Dark Magic Lord. The force of the blast engulfed him, tearing through his defenses."
                n "However, as the dark magic spread through the air, it began to corrupt everything it touched. The hero, too close to the blast, felt the dark energy seep into his veins, a shadow spreading across his skin."
                n "The Dark Magic Lord's body crumbled under the onslaught, his final breath escaping in a whisper of disbelief. The princess and hero had won, but at a terrible cost."
                n "The hero fell to his knees, his body convulsing as the dark energy took hold. He looked at the princess, fear and sorrow in his eyes."
                n "Realizing what was happening, the princess reached out to him, but it was too late. The hero, not wanting to become a monster, drove his sword into his own heart, ending his life before the transformation could be completed."
                n "The princess watched in horror as the hero's lifeless body fell to the ground, his sacrifice saving her from the darkness. Though they had defeated the Dark Magic Lord, the victory was hollow."
                n "The kingdom would remember the hero's final act of courage, but the princess would be haunted by the price they had paid."
                n "And the princess lived happily ever—"

                jump corrupted_hero
            "(Act) Use his own magic against him":
                n "The princess felt the pull of the Dark Magic Lord's magic, recognizing its twisted patterns. She knew that to defeat him, she would have to turn his own power back on him."
                p "Hero, keep him occupied! I have a plan!"
                n "The hero nodded, rushing forward to engage the Dark Magic Lord with a flurry of strikes, buying the princess time."
                h "You'll pay for what you've done, sorcerer!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "As the Dark Magic Lord focused on the hero, the princess began to weave a complex spell, mimicking the dark sorcery that filled the air. She twisted the magic, reversing its flow, sending it back toward its master."
                n "The Dark Magic Lord's eyes widened in shock as his own magic turned against him, the dark energy wrapping around him like a vice."
                n "But in his final act, he lashed out with a desperate curse, sending a dark bolt hurtling towards the hero. The bolt struck true, a lethal wound seeping with dark magic."
                n "The hero staggered, the dark curse spreading through his body, his strength fading fast. The princess, realizing what had happened, rushed to his side."
                n "As the hero's life ebbed away, the princess made a choice. She could not bear to live without him. She took his hand, tears streaming down her face."
                n "With a final, trembling breath, she whispered a spell, plunging her own dagger into her heart, choosing to follow him into the afterlife."
                n "The Dark Magic Lord's body crumbled to dust, his dark reign finally at an end. The forest, now free of his corruption, mourned the loss of its protectors."
                n "The princess and hero, united in death, would surely find peace in a world beyond this one, their souls forever intertwined."
                n "And the princess and hero died happily ever—"

                jump love_beyond_death

    label dml_choices_5_4:
        # Branching from "(Act) Distract him and go invisible"
        menu:
            "(Act) Strike from the shadows":
                n "The princess reappeared behind the Dark Magic Lord in a flash of light, her hands already moving to summon a spell. She knew she needed to end this quickly."
                p "Hero, now!"
                n "The hero charged forward from the front, his sword raised to strike. The Dark Magic Lord spun around, caught between the two attacks."
                dml "You think you can defeat me with simple tricks?!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But the princess was ready. She cast a spell, shrouding herself and the hero in shadows, making them nearly invisible in the dim chamber."
                n "The Dark Magic Lord, disoriented and unable to see his enemies clearly, unleashed a wild blast of dark magic, hoping to catch them in the attack."
                n "The princess nodded, her focus unwavering as she continued to weave shadows around them. But the Dark Magic Lord's magic was powerful and unpredictable."
                n "As the hero lunged to strike, a wild burst of dark energy surged from the Dark Magic Lord, colliding with a nearby stone pillar."
                n "The blast sent shards of stone flying through the air, tearing through the chamber and disrupting the delicate balance of magic within. The ground began to tremble, and the walls groaned under the pressure."
                n "The forest outside responded to the disruption, its ancient magic recoiling from the careless use of power. A deep rumble echoed through the trees as the forest's own magic turned against the intruders."
                n "The princess and hero, realizing their mistake too late, felt a wave of dark energy wash over them. A curse settled upon them, binding them to the forest, their forms forever altered."
                n "With the Dark Magic Lord defeated, they had no choice but to stay within the forest's borders, forever bound to protect it from any future misuse of magic."
                n "Though cursed, they found purpose in their new roles, their bond unbreakable even in their cursed forms."
                n "And the princess and hero lived happily ever—"

                jump forest_curse
            "(Act) Bind his magic permanently":
                n "The princess saw her chance as the Dark Magic Lord staggered, his focus momentarily broken by trick."
                p "We have to end this now! We can't let his darkness spread any further!"
                n "She drew upon the ancient magic of the forest, weaving a spell designed to bind the Dark Magic Lord's powers permanently. The hero kept him occupied, parrying his attacks and keeping him off balance."
                h "Hold him off, princess! I'm right behind you!"
                n "The air crackled with power as the spell took shape, glowing tendrils of light wrapping around the Dark Magic Lord's limbs, binding him in place."
                dml "No... I will not be contained!"
                n "He struggled against the bindings, but the magic was too strong. The forest seemed to aid the princess, its energy flowing through her, reinforcing the spell."
                n "As the Dark Magic Lord's power waned, the forest responded with a gentle hum, its ancient magic recognizing the princess's intent to protect."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "With one final surge of power, the princess sealed the Dark Magic Lord's magic, rendering him powerless. The forest, sensing the threat had passed, began to heal, its trees straightening, its leaves regaining their vibrant color."
                n "The princess and hero stood amidst the newfound calm, feeling the forest's gratitude in the gentle rustle of leaves around them."
                n "They chose to remain in the forest, dedicating themselves to its protection. The Dark Magic Lord's dark influence would never again threaten the land."
                n "As guardians of the forest, they would ensure that its ancient magic was never misused, standing as its eternal protectors."
                n "And the princess and hero lived happily ever—"

                jump forest_protectors

    label dml_choices_5_5:
        # Branching from "(Act) Contain him in a magic circle"
        menu:
            "(Act) Trap him within the circle forever":
                n "The princess tightened her focus, drawing on all her magical strength to reinforce the glowing circle of light that surrounded the Dark Magic Lord."
                p "This ends now. You'll never escape this prison of light!"
                n "The circle's walls shimmered with a blinding radiance, growing tighter and more impenetrable with every passing second. The Dark Magic Lord, realizing his peril, fought desperately against the magical barrier."
                dml "You think you can contain me? I am the master of all magic!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But no matter how much he struggled, the circle held firm, binding him within its confines. The forest around them seemed to tremble, its ancient magic resonating with the powerful spell."
                n "The princess felt it too—a deep, rumbling energy building within the earth itself, responding to the intense concentration of magic in one place."
                n "As the magic circle solidified around the Dark Magic Lord, the ground beneath them quaked, a powerful surge of energy rippling through the forest. The spell had unintended consequences, disturbing the natural balance of the ancient woods."
                n "The forest, angered by the disruption, unleashed a powerful curse upon all who had tampered with its magic. A thick fog rolled in, enveloping the princess and hero in a cold, unforgiving embrace."
                n "Bound by the curse, the princess and hero were forced to remain in the forest, their forms forever changed as they took on the roles of its eternal guardians, destined to protect it from any further misuse of magic."
                n "Though cursed, they found a sense of purpose, knowing they would forever defend the forest from the darkness that had once sought to destroy it."
                n "And the princess and hero lived happily ever—"

                jump forest_curse
            "(Act) Purify the dark magic within him":
                n "The princess knew that the Dark Magic Lord's power could not simply be contained; it had to be cleansed. She reached deep within herself, calling upon the purest magic she could summon."
                p "This darkness must end. We will cleanse this place of your corruption!"
                n "The circle around the Dark Magic Lord began to glow with a soft, golden light, purer and more potent than anything he had ever encountered. He recoiled, his eyes wide with fear and disbelief."
                dml "No... what is this light?! I will not be undone by such trickery!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The light intensified, flooding the chamber with warmth and brilliance. The dark tendrils that surrounded him began to dissolve, fading into nothingness as the purifying magic took hold."
                n "The princess's hands trembled with the effort, but she did not falter. The forest seemed to aid her, its energy flowing through her and amplifying the spell's power."
                n "With one final surge of light, the Dark Magic Lord's power was purified, his dark magic washed away in the cleansing glow. The forest, once tainted by his corruption, began to heal, its vibrant life returning as the darkness was purged."
                n "The princess and hero, now free of the dark influence, stood together in the clearing, feeling the forest's gratitude surround them like a warm breeze."
                n "They chose to stay within the forest, dedicating their lives to its protection, becoming its eternal guardians. The forest would flourish under their care, its ancient magic preserved and its beauty restored."
                n "Together, they would ensure that no darkness would ever again threaten this sacred place."
                n "And the princess and hero lived happily ever—"

                jump forest_protectors

    label dml_choices_5_6:
        # Branching from "(Act) Counter his curse"
        menu:
            "(Act) Seal the curse within yourself":
                n "The princess knew the curse was too dangerous to unleash, but perhaps she could contain it. With a steady breath, she channeled the dark energy into herself, her body absorbing the sinister magic."
                p "I will take this darkness into myself... to protect us all."
                n "The Dark Magic Lord's eyes widened in surprise, realizing what she intended to do."
                dml "You dare to harness my curse? It will consume you from within!"
                n "The princess winced as the curse surged through her veins, its dark tendrils wrapping around her very soul. The hero, seeing her struggle, rushed to her side."
                h "Princess, no! Don't do this alone!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But as he reached out to help her, the curse's malevolence seeped into him as well, drawn by the bond they shared. A dark transformation began, his features twisting in agony."
                n "The hero's form began to change, corrupted by the darkness now binding him. He fought against it, his will strong, but he knew the curse would eventually consume him entirely."
                n "In his final moments of clarity, the hero made a choice. He took the princess's hand, whispering his final words before plunging a dagger into his own heart to end the curse's hold."
                n "The princess, tears streaming down her face, watched as the hero's body crumpled to the ground, his sacrifice saving her from the darkness that threatened to engulf them both."
                n "Though the Dark Magic Lord was defeated, the cost was too great. The princess would carry the weight of the hero's sacrifice forever, her heart marked by the tragedy of their love."
                n "And the princess lived happily ever—"

                jump corrupted_hero
            "(Act) Redirect the curse into the environment":
                n "Realizing she could not contain the curse, the princess made a swift decision. She redirected the dark energy into the surrounding environment, hoping to spare them both from its effects."
                p "I'll send this darkness back to where it came from... into the forest itself."
                n "The curse spread outward, its dark tendrils creeping into the trees and soil, tainting the land around them. The forest groaned as if in pain, its magic reacting violently to the intrusion."
                dml "You think you can escape the consequences of wielding such power?"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The ground trembled, and a thick, unnatural fog began to rise from the earth, engulfing the princess and hero in a cold, clammy grip. The forest, now cursed, seemed to close in around them."
                n "The forest's ancient magic, now twisted by the dark curse, bound them to it, condemning them to remain within its borders for eternity."
                n "Bound by the curse, the princess and hero found themselves transformed, their forms shifting to match the dark magic that now tainted the forest. The once-vibrant woods turned dark and foreboding, a reflection of the curse that lay upon it."
                n "The princess and hero, now forever tied to the cursed land, chose to remain, seeking to protect what was left and to find redemption for the mistake they had made."
                n "Together, they would become the forest's eternal guardians, forever watching over the land they had inadvertently condemned."
                n "And the princess and hero lived happily ever—"

                jump forest_curse

    label dml_choices_5_7:
        # Branching from "(Act) Channel all your magic into a final spell"
        menu:
            "(Act) Release all your power at once":
                n "The princess knew this was the only way. She would have to release all her magic at once to defeat the Dark Magic Lord."
                p "I won't let this darkness spread any further. It ends now!"
                n "She raised her hands, the air crackling with immense magical energy. The hero watched, fear and admiration in his eyes."
                h "Princess, be careful!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "As the princess released the full force of her magic, the chamber erupted in a brilliant explosion of light. The Dark Magic Lord, caught in the epicenter, was obliterated, his dark form disintegrating into nothingness."
                n "The power of the blast was so great that it left the princess drained and lifeless on the chamber floor. The hero rushed to her side, his heart breaking as he cradled her still form."
                n "Desperate to save her, he resorted to forbidden magic, calling upon powers long deemed unnatural to bring her back. As her eyes fluttered open, the hero sighed in relief."
                n "But their victory came at a cost. The kingdom, upon learning of the hero's forbidden act, condemned him for his transgression against the natural order, banishing him forever."
                n "The princess, now alive but forever marked by the loss, watched as the hero was led away, knowing their love was forever tainted by the choices they had made."
                n "And the princess lived happily ever—"

                jump unfulfilled_love
            "(Act) Sacrifice your life to end the darkness":
                n "The princess, feeling the weight of the darkness closing in, knew what she had to do. She had to make the ultimate sacrifice to save them all."
                p "Hero... I'm sorry, but this is the only way."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero's eyes widened in horror as he realized what she intended to do."
                n "But she had already made up her mind. Summoning every last bit of her power, she prepared a final, fatal spell that would obliterate the Dark Magic Lord—and herself along with him."
                n "The princess unleashed the spell, a blinding beam of pure magic that engulfed the Dark Magic Lord. The chamber shook with the force of the spell as she poured all her energy into it."
                n "The spell's power was overwhelming, consuming both the Dark Magic Lord and the princess in its radiant light. As the magic dissipated, only silence remained, the princess's body lying lifeless where she had stood."
                n "The hero fell to his knees beside her, his heart shattered by the loss. Though they had won, the price was too great—his love lost forever."
                n "With the Dark Magic Lord defeated, the kingdom would be saved, but the hero would carry the burden of her sacrifice for the rest of his days."
                n "And the hero lived happily ever—"

                jump sacrificed_princess

    label dml_choices_5_8:
        # Branching from "(Act) Bind his power and offer a truce"
        menu:
            "(Act) Accept a temporary alliance":
                n "The princess held the magic binding the Dark Magic Lord, her voice steady and calm."
                p "We don't need to be enemies. Let's join forces, if only for a while, to protect what remains of this forest and our kingdom."
                n "The Dark Magic Lord's eyes narrowed, his expression inscrutable as he considered her words."
                dml "A temporary alliance? You dare to suggest we work together? I would never lower myself to work with the likes of you."
                n "The princess maintained her composure, sensing his hesitation. She knew his pride was his weakness, and any show of power might provoke him into accepting."
                p "You know as well as I do that we are stronger together, even if only for a short time. Think of what we could accomplish."
                n "The Dark Magic Lord seemed to consider her words, the glowing chains binding his hands tightening as he struggled internally."
                dml "Very well, princess. I will agree to your terms... for now."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "As he pretended to agree, The Dark Magic Lord struck a fatal blow, catching the princess off guard. The hero, outraged, immediately struck down the dark magic lord without a second thought."
                n "He would proceed to call upon forbidden magic to bring the princess back to life, knowing that he would not want to continue living without her."
                n "However, his actions would not go unnoticed. The kingdom, horrified by the use of dark arts, would exile the hero, condemning him for his unforgivable act."
                n "The princess, alive but forever changed, would be left to move on alone, haunted by the choices that led to this tragic end."
                n "And the princess lived happily ever—"

                jump unfulfilled_love
            "(Act) Force him into a magical vow":
                n "The princess tightened the magical chains around the Dark Magic Lord, her voice commanding and unyielding."
                p "Swear to leave this forest in peace. Swear on your magic, or you will never be free."
                n "The Dark Magic Lord glared at her, but he could feel the power of the vow binding him. He knew he had no choice."
                dml "You think you can force my hand with your pitiful spells? Very well, I swear... but know this, princess—I will not forget this insult."
                n "The princess held firm, her eyes locked onto his as the magical vow took effect, binding the Dark Magic Lord's powers to his promise."
                h "You made the right choice. Now, let's end this."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "With the vow in place, the Dark Magic Lord's power began to wane, his dark magic restrained by the binding spell. The forest seemed to breathe easier, its magic responding to the shift in power."
                n "With the Dark Magic Lord's vow secured, the forest slowly began to heal from the years of corruption. The princess and hero decided to stay, dedicating their lives to protecting the land and ensuring no one would ever again threaten its delicate balance."
                n "They would become the forest's guardians, their bond strengthened by their shared commitment to this new purpose."
                n "Together, they would vow to keep the forest safe, watching over it and nurturing its recovery with their combined strength."
                n "And the princess and hero lived happily ever—"

                jump forest_protectors

    label dml_choices_5_9:
        # Branching from "(Act) Appeal to his sense of honor"
        menu:
            "(Act) Challenge him to a duel of skill":
                n "The princess stepped forward, her voice filled with determination."
                p "If there's any honor left in you, you'll face us in a fair duel—one on one. No magic, just skill."
                n "The Dark Magic Lord's eyes narrowed, a spark of his former self shining through his darkened gaze."
                dml "A duel, you say? Very well, princess. I accept your challenge. Let it be known that you chose this end."
                scene bg villain_hero_sword_facing_far_dml with dissolve
                n "The hero tightened his grip on his sword, stepping in front of the princess to face the Dark Magic Lord."
                h "I'll take this one, princess. Stay back and be ready."
                scene bg villain_hero_charging_far_dml with dissolve
                n "The duel began with a clash of steel against steel, the Dark Magic Lord's blade swift and unforgiving. The hero fought bravely, matching him strike for strike."
                dml "You fight well... for a fool."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But as the battle raged on, the Dark Magic Lord's strength and skill began to overwhelm the hero, driving him to the ground. The Dark Magic Lord raised his blade for a fatal strike, a cruel smile on his lips."
                n "In a final act of love and bravery, the hero threw himself in front of the princess, taking the fatal blow meant for her. The Dark Magic Lord's sword pierced through his chest, ending his life in an instant."
                n "The princess's scream echoed through the chamber as the hero fell, his sacrifice saving her from certain death."
                n "Seizing the moment, the princess channeled all her remaining strength and struck back with the hero's sword, the blade finding its mark and ending the Dark Magic Lord's reign of terror once and for all."
                n "Though the kingdom was saved, the cost was too great. The hero's sacrifice would forever haunt the princess, his love and bravery a poignant reminder of what was lost."
                n "And the princess lived happily ever—"

                jump sacrificed_hero
            "(Act) Offer him a path to redemption":
                n "The princess's voice softened, filled with a sincerity that cut through the darkness surrounding them."
                p "You were once a hero, a protector of your people. It's not too late to change, to redeem yourself. Help us restore this kingdom."
                n "The Dark Magic Lord's eyes flickered with uncertainty, a conflict warring within him. The weight of his past sins seemed to press down on him, forcing him to confront what he had become."
                dml "Redeem myself? After all I've done... is it even possible?"
                n "The hero stepped forward, his voice firm but compassionate."
                h "It's never too late to turn back. We can rebuild this kingdom together. The choice is yours."
                n "The Dark Magic Lord hesitated, his hands trembling as he considered their offer."
                dml "Very well... I will try. But know this, princess—if I fail, the darkness will consume us all."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "With the Dark Magic Lord's agreement, the princess and hero returned to the kingdom, determined to restore what had been lost. The people, seeing the change in their once-great protector, welcomed him back cautiously, their hope rekindled."
                n "The princess took her place on the throne, ruling with wisdom and compassion, with the hero by her side. Together, they guided the Dark Magic Lord on his path to redemption, ensuring that the darkness would never return."
                n "Under their leadership, the kingdom flourished, its people united in their quest for a brighter future."
                n "And the princess and hero lived happily ever—"

                jump inherited_throne

    label dml_choices_5_10:
        # Branching from "(Act) Remind him of the loved ones he lost"
        menu:
            "(Act) Make him relive his past mistakes":
                n "The princess's voice was firm, her words like a dagger to the Dark Magic Lord's heart."
                p "Think of all those you've lost—their lives ruined by your lust for power. They would be horrified by what you've become."
                n "The Dark Magic Lord's face contorted in anguish, his dark aura flickering as painful memories resurfaced."
                dml "No... I did what I had to do. They... they would understand!"
                n "The hero stepped forward, his voice stern yet compassionate."
                h "They wouldn't want this, and you know it. It's time to stop running from your guilt."
                n "The Dark Magic Lord's eyes glistened with unshed tears, the weight of his actions crashing down upon him."
                dml "I... I cannot change what I've done. But I can atone, even if it means my end."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "Sensing a shift, the hero advanced with a resolute stance, ready to disarm the Dark Magic Lord. But as he stepped forward, the Dark Magic Lord suddenly lashed out, a final act of desperation."
                n "The Dark Magic Lord's final strike was aimed at the princess, his dark magic surging toward her. The hero, seeing her life in peril, leapt into the path of the attack."
                n "The hero's body absorbed the brunt of the spell, shielding the princess from the fatal blow. He fell to the ground, his life slipping away as the last of his strength left him."
                n "The princess screamed, her heart breaking as she watched him sacrifice himself for her. With a burst of fury, she grabbed the hero's sword and charged at the Dark Magic Lord."
                n "The blade found its mark, piercing the dark sorcerer's heart and ending his reign of terror once and for all."
                n "Though victorious, the kingdom's peace came at the cost of the hero's life, his sacrifice a solemn reminder of the price of redemption."
                n "And the princess lived happily ever—"

                jump sacrificed_hero
            "(Act) Offer him peace and forgiveness":
                n "The princess's voice softened, her tone filled with compassion and understanding."
                p "You've been lost in the darkness for so long. But it's not too late. Let us help you find peace and forgiveness."
                n "The Dark Magic Lord's expression faltered, his eyes clouded with a mix of longing and regret."
                dml "Peace... after all I've done? How could I ever be forgiven?"
                n "The hero stepped beside the princess, his gaze steady, his voice sincere."
                h "It's never too late to seek forgiveness. We can all find a way to make amends for our past mistakes."
                n "For a brief moment, hope seemed to flicker in the Dark Magic Lord's eyes. But as his hands trembled, a surge of dark magic burst from him, driven by his internal conflict."
                dml "No! You won't trap me in your lies!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The dark magic shot out, striking the hero directly in the chest. The princess's eyes widened in horror as she saw the curse begin to take hold, shadows creeping across the hero's skin."
                n "The hero staggered, the dark curse spreading rapidly through his body, his life slipping away with every breath. The princess, seeing there was no saving him, made a fateful decision."
                n "Knowing the hero would die within moments from the curse, the princess chose to take her own life, deciding to follow him into the afterlife rather than live without him."
                n "With a final, tearful embrace, they fell together, their hands clasped in a vow that even death could not break."
                n "The Dark Magic Lord, watching the scene unfold, was left to ponder the true cost of his actions, forever haunted by the love that chose death over his offered peace."
                n "And the princess and hero died happily ever—"

                jump love_beyond_death

    label dml_choices_5_11:
        # Branching from "(Act) Make him see the consequences of his actions"
        menu:
            "(Act) Show him the destruction he caused":
                n "The princess's magic wove through the air, bringing to life the full devastation of the Dark Magic Lord's actions."
                p "Look at the destruction you've caused! The forest dying, the people suffering—this is all on you."
                n "The images surrounded entered his mind, showing the Dark Magic Lord the withering trees, the dried-up rivers, the broken spirits of those he had harmed."
                dml "No... I didn't... I didn't mean for this..."
                n "The hero watched as the Dark Magic Lord's resolve began to crumble, his dark aura fading."
                h "It's not too late. Stop this madness before it consumes you completely."
                n "The Dark Magic Lord's eyes were filled with anguish, but as he reached for redemption, a dark tendril of magic lashed out, striking the hero."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero staggered, clutching his chest as the dark magic spread through him, his body beginning to wither. The princess, horrified, realized there was no saving him."
                n "Knowing the hero would soon die from the curse, the princess made the heartbreaking decision to take her own life, choosing to follow him into the afterlife."
                n "With a final breath, she whispered her love for him, their souls entwined as they slipped into eternal darkness together."
                n "And the princess and hero died happily ever—"

                jump love_beyond_death
            "(Act) Persuade him to change his ways":
                n "The princess's voice was gentle but firm, a beacon of light in the darkened chamber."
                p "You can still change. You have the power to heal instead of destroy. Use your magic to restore what you've broken."
                n "The Dark Magic Lord looked at her, torn between the darkness he had embraced for so long and the chance for redemption that lay before him."
                dml "To heal... after everything I've done... Could I even begin to atone?"
                n "The hero stepped forward, his voice steady and reassuring."
                h "You can start by helping us. Together, we can protect the forest and ensure it thrives once more."
                n "The Dark Magic Lord hesitated, his hands trembling as he fought against the darkness within him."
                dml "Very well... I will try. For the forest, and for those I've wronged."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "With the Dark Magic Lord's resolve to change, the forest began to heal. The princess, hero, and even the Dark Magic Lord himself decided to stay, dedicating their lives to protecting the forest and ensuring its survival."
                n "The three of them became unlikely guardians, each finding redemption and peace in their shared commitment to protecting the land from further harm."
                n "Together, they vowed to safeguard the forest, watching over it with newfound purpose and strength."
                n "And the princess and hero lived happily ever—"

                jump forest_protectors

    label dml_choices_5_12:
        # Branching from "(Act) Push him to redeem himself"
        menu:
            "(Act) Offer him a chance to make amends":
                n "The princess's voice remained steady, her eyes unwavering as she spoke directly to the Dark Magic Lord."
                p "You've caused great pain, but it's not too late to change. Help us rebuild, and make amends for the past."
                n "The Dark Magic Lord hesitated, the shadows flickering around him as he weighed her words. His grip on his staff loosened, his face showing a hint of vulnerability."
                dml "To make amends... after all I've done? Can I truly be forgiven?"
                n "The hero stepped beside the princess, his voice calm but insistent."
                h "You can't undo the past, but you can choose a different path forward. Help us restore what was lost."
                n "The Dark Magic Lord's eyes softened, his gaze shifting from the princess to the hero. The darkness around him seemed to waver, the shadows receding as if he was considering their offer."
                dml "Very well... I will try. But know this, if I falter, I will return to my old ways."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "With the Dark Magic Lord's promise to change, the princess and hero led him back to the kingdom, where they began the long and difficult task of rebuilding. The people, wary but hopeful, watched as their new leader guided them with wisdom and compassion."
                n "The princess took her place on the throne, her reign marked by strength and justice, with the hero always by her side as her trusted advisor and protector."
                n "Together, they would work to heal the land and its people, forging a new era of peace and prosperity for all."
                n "And the princess and hero lived happily ever—"

                jump inherited_throne
            "(Act) Convince him to give up on his ideology":
                n "The princess's eyes bore into the Dark Magic Lord, her voice fierce and unwavering."
                p "This isn't about power or control. You've lost sight of what truly matters. Give up this madness, or it will consume you."
                n "The Dark Magic Lord sneered, but there was a flicker of doubt in his eyes, a momentary hesitation."
                dml "You think I can simply walk away? My life, my power—everything I've built is for this."
                scene bg villain_hero_facing_far_dml with dissolve
                n "The hero stepped forward, his stance firm."
                h "You're on a path to destruction. End this now, before it's too late."
                n "For a moment, the Dark Magic Lord seemed to waver, his resolve shaken. But then, with a roar of fury, he lashed out with a burst of dark magic aimed at the princess."
                dml "Never! I will not be swayed by your weak words!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "In a desperate attempt to protect the princess, the hero threw himself in front of the dark magic, taking the full force of the attack. He collapsed to the ground, his life slipping away as the curse consumed him."
                n "The princess screamed, her heart shattering as she watched the hero's sacrifice. Fueled by her grief, she gathered all her strength and struck back with a powerful blow, ending the Dark Magic Lord's life in an instant."
                n "The battle was won, but the victory was hollow. The princess would carry the memory of the hero's sacrifice with her for the rest of her life, his final act of love a constant reminder of what was lost."
                n "And the princess lived happily ever—"

                jump sacrificed_hero

    label dml_choices_5_13:
        # Branching from "(Act) Offer to share forbidden knowledge"
        menu:
            "(Act) Unlock hidden power together":
                n "The princess's voice was calm, yet filled with a dangerous resolve."
                p "We could unlock a power unlike any this world has ever seen. Together, we could achieve greatness."
                n "The Dark Magic Lord's eyes gleamed with a mixture of curiosity and hunger for more power."
                dml "Unlock hidden power... an intriguing offer, princess. But can you handle the consequences?"
                n "The hero glanced at the princess, concern etched on his face, but she nodded reassuringly."
                p "I'm ready. Let's do this."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "They joined hands, their magic intertwining, a surge of dark energy swirling around them as they began the ritual to unlock the forbidden power."
                n "But as the power surged through them, it began to twist and corrupt. The hero cried out in agony, his body transforming, consumed by the darkness. Realizing what was happening, he used the last of his strength to push the princess away."
                n "With a final, desperate look, the hero plunged his sword into his own heart, ending his life before the darkness could fully take over."
                n "The princess, horrified by the outcome, was left to face the consequences of their actions. The Dark Magic Lord lay defeated, but the cost was too great."
                n "And the princess lived happily ever—"

                jump corrupted_hero
            "(Act) Betray him at the last moment":
                n "The princess smiled, a hint of deceit in her eyes."
                p "We can achieve power beyond measure... but only if you trust me."
                n "The Dark Magic Lord nodded, his guard lowering as he prepared to join his magic with hers."
                dml "Very well, princess. Show me this power you speak of."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But as their magic began to merge, the princess made her move. She summoned a burst of pure light, aiming it directly at the Dark Magic Lord's heart."
                n "Caught off guard, the Dark Magic Lord was struck down, his life extinguished by the princess's betrayal. But as he fell, he released a final curse, striking the princess down as well."
                n "The hero, desperate to save her, used forbidden magic to bring her back from the brink of death. The princess's eyes fluttered open, but their reunion was short-lived."
                n "The kingdom, discovering the hero's forbidden act, banished him for defying the natural laws. The princess, alive but forever marked by the events, was left to rule alone, her heart heavy with the price of their choices."
                n "And the princess lived happily ever—"

                jump unfulfilled_love

    label dml_choices_5_14:
        # Branching from "(Act) Offer to combine your powers"
        menu:
            "(Act) Fuse your magic with his":
                n "The princess felt a surge of determination. If they combined their magic, they could achieve unimaginable power—but it was a dangerous gamble."
                p "Together, our magic could reshape the world. Fuse your power with mine, and we will be unstoppable."
                n "The Dark Magic Lord's eyes flickered with interest, a twisted smile forming on his lips."
                dml "A tempting offer, princess. Let us see if your magic is worthy of mine."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The princess extended her hand, her magic flowing toward him, intertwining with the dark tendrils of his own power. For a moment, their combined magic crackled with raw energy."
                n "The hero screamed in agony as the corruption spread through his veins, his body beginning to transform into something monstrous. The princess, realizing what was happening, tried to pull back, but it was too late."
                n "In his final moments of clarity, the hero made a desperate choice. Rather than let the darkness consume him completely, he plunged his sword into his own chest, ending his life to save the princess from a terrible fate."
                n "The princess, her heart shattered by the loss, was left to face the consequences of their actions. The Dark Magic Lord lay defeated, but the victory felt hollow. The hero's sacrifice haunted her, a grim reminder of the price they had paid for power."
                n "And the princess lived happily ever—"

                jump corrupted_hero
            "(Act) Create a powerful but unstable bond":
                n "The princess knew the risks, but she also knew that combining their powers could be the key to defeating the Dark Magic Lord once and for all."
                p "We could form a bond stronger than anything in this forest. Together, we could harness a power unlike any other."
                n "The Dark Magic Lord's eyes gleamed with ambition, his desire for power outweighing his caution."
                dml "Very well, princess. Let us see what such a bond can achieve."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "They began the ritual, their magic intertwining in a volatile dance of light and darkness. The air crackled with energy as their powers fused into a single, unstable force."
                n "But the power they unleashed was too great for the forest to handle. The ground trembled, and the trees began to wither as the magic tore through the land."
                n "The forest, sensing the danger of this new and unstable power, lashed out with a curse. Dark roots erupted from the ground, ensnaring both the princess and the hero. Their bond had triggered the forest's wrath, and now they were trapped in its eternal grasp."
                n "Realizing the gravity of their mistake, the princess and hero vowed to spend their lives trying to heal the damage they had caused. Together, they became the forest's reluctant guardians, forever bound by the curse they had unwittingly unleashed."
                n "They would protect the forest from any who would seek to harm it, dedicating themselves to atoning for their actions, even as the curse kept them tethered to the land."
                n "And the princess and hero lived happily ever—"

                jump forest_curse

    label dml_choices_5_15:
        # Branching from "(Act) Wait for the perfect moment to strike"
        menu:
            "(Act) Ambush him when he's vulnerable":
                n "The princess and hero waited in silence, watching as the Dark Magic Lord's defenses began to falter. They knew this was their chance."
                p "Now, hero! Strike while he's distracted!"
                scene bg villain_hero_charging_far_dml with dissolve
                n "The hero moved swiftly, his sword raised high as he charged at the Dark Magic Lord from behind. The sorcerer, caught off guard, barely had time to react."
                h "For the kingdom!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But just as the hero's blade was about to strike, the Dark Magic Lord spun around, his eyes blazing with dark energy. He fired a bolt of magic directly at the princess, intent on taking her down with him."
                n "Seeing the attack, the hero threw himself in front of the princess, taking the full force of the dark magic. The spell pierced his chest, and he crumpled to the ground, his life fading away."
                n "The princess screamed in horror, her heart breaking as she watched the hero fall. She knew his sacrifice had saved her, but the cost was too great."
                n "Summoning her last reserves of strength, she delivered a final, decisive blow, ending the Dark Magic Lord’s life. The battle was won, but the victory was hollow."
                n "The hero's sacrifice would haunt her for the rest of her days, his final act of love and bravery a constant reminder of what was lost."
                n "And the princess lived happily ever—"

                jump sacrificed_hero
            "(Act) Strike him down with no hesitation":
                n "The princess saw her chance and acted without hesitation. With a swift motion, she signaled the hero to strike."
                p "Now, hero! Strike him down!"
                n "The hero moved with lightning speed, his sword aimed directly at the Dark Magic Lord's heart. The sorcerer, sensing the impending attack, prepared to retaliate."
                dml "Fools! You think you can defeat me so easily?"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "As the hero closed in, the Dark Magic Lord summoned a blast of dark magic, aiming it directly at him. The princess, seeing the danger, didn't hesitate."
                n "She threw herself in front of the hero, taking the full force of the attack. The dark magic struck her, searing through her body. She fell to the ground, her life slipping away with each passing second."
                n "The hero caught her as she fell, his eyes wide with horror. The Dark Magic Lord, weakened and exposed, was swiftly defeated by the hero's next strike, but the victory was bitter."
                n "The princess's sacrifice would forever be etched into the hero's soul, a painful reminder of her courage and love in their darkest hour."
                n "And the hero lived happily ever—"

                jump sacrificed_princess

    label dml_choices_5_16:
        # Branching from "(Act) Manipulate him into lowering his guard"
        menu:
            "(Act) Turn his own power against him" if chose_magic:
                n "The princess kept her voice calm, her words like honey laced with venom."
                p "You have great power, Dark Magic Lord. But what if you could wield it even more effectively? What if I could show you how?"
                n "The Dark Magic Lord's eyes glimmered with curiosity, his arrogance blinding him to the trap."
                dml "And what could you possibly know that I do not?"
                n "The princess subtly shifted her stance, preparing to channel his dark magic back at him."
                p "Let me demonstrate."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "In an instant, she turned his own power against him, using a clever incantation to redirect his dark energy back at its source."
                n "Caught in the backlash of his own magic, the Dark Magic Lord staggered, his strength failing him. In his desperation, he unleashed a wild, last-ditch spell toward the princess."
                n "The spell struck her with brutal force, darkness enveloping her as she fell to the ground, lifeless. The hero, his heart shattering at the sight, knew there was only one way to save her."
                n "With a trembling hand, he called upon forbidden magic, channeling a desperate incantation to bring the princess back from the brink of death. Dark energy swirled around them, the cost of his actions clear."
                n "The princess's eyes fluttered open, life flooding back into her as she realized what the hero had done. But their relief was short-lived; they both knew the consequences."
                n "Upon returning to the kingdom, the hero was immediately exiled for his forbidden act. The princess, alive but forever marked by his sacrifice, was left to rule alone, haunted by the love that could never truly be fulfilled."
                n "And the princess lived happily ever—"

                jump unfulfilled_love
            "(Act) Catch him off guard with an attack" if not chose_magic:
                n "The princess, sensing the moment was right, signaled to the hero with a quick glance. They had one chance to strike while the Dark Magic Lord's guard was down."
                p "Now, hero! Strike swiftly!"
                scene bg villain_hero_charging_far_dml with dissolve
                n "The hero moved like a shadow, closing the distance between himself and the Dark Magic Lord. His sword arced through the air, aiming for a critical blow."
                h "This ends now!"
                n "But the Dark Magic Lord, ever cunning, turned at the last moment. With a twisted smile, he unleashed a dark curse, a final act of spiteful vengeance."
                dml "If I am to fall, then you shall fall with me!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The dark energy coiled around the hero, the curse embedding itself deep into his very being. The hero staggered back, his face contorted in pain as the magic took hold."
                n "The princess watched in horror as the hero collapsed, the dark curse slowly draining his life away. She knew in her heart that the curse was irreversible and that he had mere moments left to live."
                n "Tears streamed down her face as she knelt beside him, cradling his head in her arms. The hero looked up at her, his breath shallow and weak, and managed a faint smile."
                n "Knowing she couldn't bear to live without him, the princess made a choice. She whispered a final, tearful goodbye before plunging her own sword into her heart, choosing to join him in death rather than face a future without him."
                n "Their bodies fell side by side, the curse's dark tendrils binding their souls together in the afterlife."
                n "And the princess and hero died happily ever—"

                jump love_beyond_death


    label dml_who_are_you:
        p "Who are you? Why do you insist on calling yourself a hero?"
        n "The Dark Magic Lord's grin widened, a mix of arrogance and self-delusion in his eyes."
        dml "Who am I? I am the one who holds the reins of true power. While others cower in fear, I've dared to reach for the heights that no one else can grasp."
        dml "You may see ruin, but I see progress—a path to a new world shaped by my vision alone."

        return

    label dml_why_do_you:
        p "Why do you claim to be a hero? How can you call yourself that after everything you've done?"
        n "The Dark Magic Lord's laughter echoed through the air, filled with a twisted sense of righteousness."
        dml "A hero? Of course, I am! I am the only one willing to do what must be done, to take the risks others fear. My methods may be harsh, but greatness demands sacrifice."
        dml "The forest, the land—they're just means to an end. Only a fool would let sentiment stand in the way of progress."

        return

    label dml_what_do_you:
        p "What is it you truly seek? What's the point of all this destruction?"
        n "The Dark Magic Lord's eyes gleamed with an almost fanatical fervor, his voice rich with self-conviction."
        dml "I seek perfection—a world free from weakness, shaped by pure strength and unyielding will."
        dml "Others fear what they don't understand, but I have embraced it. Through my magic, I will forge a realm where the strong prevail and the ignorant are cast aside."
                
        return

    label dml_how_did_you:
        p "How did you come to wield such power? What drives this obsession?"
        n "The Dark Magic Lord's expression shifted, pride dripping from every word."
        dml "My power was not simply given—it was earned through relentless pursuit and unshakable resolve. I sought knowledge where others dared not tread, unlocked secrets long buried."
        dml "My obsession? It is the same as any true visionary: to transcend the limitations imposed by lesser minds and carve my own destiny."

        return

    label dml_what_drives_your:
        p "What drives your obsession with magic? Why go to such lengths?"
        n "The Dark Magic Lord's voice was rich with disdain, as if the answer should be obvious."
        dml "Magic is the ultimate expression of will. With it, I can bend the world to my desires, reshape it into something worthy of my brilliance."
        dml "Those who fail to see its potential are blind fools, content to live in ignorance while I grasp at the very threads of reality."

        return

    label dml_do_you_not:
        p "Do you not understand the consequences of what you're doing? The forest is dying because of you!"
        n "The Dark Magic Lord waved his hand dismissively, his tone full of contempt."
        dml "Consequences? Small sacrifices for the greater good. The forest's suffering is but a temporary inconvenience compared to what I'll achieve."
        dml "People cling to the past, but I look to the future—a future where such trivialities will no longer matter. They'll thank me in the end, even if they're too blind to see it now."

        return

    label dml_what_is_your:
        p "What is your end goal? Where does all this lead?"
        n "The Dark Magic Lord's expression turned almost reverent, his eyes shining with grandiosity."
        dml "My goal is nothing short of ascension—a world where I reign supreme, where my vision is the only truth that remains."
        dml "This forest, this land—it's all just a stepping stone toward a greater reality, one where weakness and doubt have no place. I will become the legend that reshapes history itself."

        return

    label dml_do_you_really:
        p "Do you really believe this will save the world? You're destroying it in the process!"
        n "The Dark Magic Lord's voice was laced with condescension, as if speaking to a child."
        dml "Save the world? You think so small. I'm not interested in saving the world as it is—I'm forging a new one, a stronger one. Weakness must be purged for something greater to rise."
        dml "Destruction is merely the precursor to rebirth. Only through fire can the impurities be burned away, leaving behind a world worth ruling."

        return

    label dml_how_do_you:
        p "How do you justify the suffering you've caused? The lives you've ruined?"
        n "The Dark Magic Lord's eyes narrowed, irritation flickering beneath his arrogance."
        dml "Justify? I have no need to justify greatness. Those who suffer do so because they lack the strength to endure what is necessary."
        dml "I offer them a chance to be part of something monumental. If they can't see that, their suffering is merely the cost of progress."

        return

    label dml_why_cant_you:
        p "Why can't you stop overusing magic? You're killing everything around you!"
        n "The Dark Magic Lord's expression darkened, a flash of anger crossing his features."
        dml "Stop? You would have me give up the very source of my power? You know nothing! Magic is not something to be rationed or feared—it is to be seized and wielded without restraint."
        dml "To limit myself would be to deny my purpose. I won't be shackled by the fears of those too weak to grasp the potential I've unlocked."

        return

    label dml_is_there_nothing:
        p "Is there nothing that would make you change your mind? Isn't there another way?"
        n "The Dark Magic Lord's laughter was sharp and dismissive, filled with scorn."
        dml "Change my mind? I am beyond such weakness. I've long since cast aside doubt and hesitation. You ask me to turn back when I stand on the brink of greatness?"
        dml "There is no other way—only forward, toward the destiny that awaits me, a destiny free from the limits others impose on themselves."
        
        return

    label dml_what_would_happen:
        p "What would happen if you did stop? If you let go of this obsession?"
        n "The Dark Magic Lord's eyes blazed with a mixture of anger and fear, as if the very idea was an affront to his existence."
        dml "Stop? If I stopped, everything I've built would crumble! The power I've amassed would be for nothing, my legacy erased, leaving nothing but emptiness."
        dml "No—I will not let that happen. To stop is to fade into obscurity, to be forgotten like those who lacked the courage to seize their own destiny. I will not be one of them."

        return