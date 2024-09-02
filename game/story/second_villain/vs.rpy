# Contains the code associated with portion of the game related to the "vengeful spirit" second villain encounter.

# Default Variables


# Flags for unlockable options

default vs_chose_who_are_you = False
default vs_chose_why_do_you_seek = False
default vs_chose_can_you_ever = False
default vs_chose_what_do_you = False
default vs_chose_why_do_you_blame = False
default vs_chose_isnt_there_a = False
default vs_chose_why_cant_you = False
default vs_chose_do_you_not = False
default vs_chose_cant_you_find = False
default vs_chose_what_will_you = False
default vs_chose_will_your_vengeance = False
default vs_chose_what_then = False

label vs_start:
    $ vs_chose_who_are_you = False
    $ vs_chose_why_do_you_seek = False
    $ vs_chose_can_you_ever = False
    $ vs_chose_what_do_you = False
    $ vs_chose_why_do_you_blame = False
    $ vs_chose_isnt_there_a = False
    $ vs_chose_why_cant_you = False
    $ vs_chose_do_you_not = False
    $ vs_chose_cant_you_find = False
    $ vs_chose_what_will_you = False
    $ vs_chose_will_your_vengeance = False
    $ vs_chose_what_then = False

    $ vs_times_gotten += 1

    # Leading text
    scene bg Villain with dissolve
    n "A cold wind swept through the forest as the princess and the hero moved forward, the trees seeming to close in around them. The once-familiar paths now felt foreign and threatening, shrouded in an eerie mist that clung to the ground like a living thing."
    n "The hero's grip tightened on his sword, his breath visible in the sudden chill. The forest was deathly silent, the usual sounds of life replaced by a foreboding stillness."
    play music "audio/5 Second Villian 3.mp3" loop volume 1.0 fadein 0.5
    scene bg villain_far_vs with dissolve
    n "Out of the mist, a figure began to take shape, its form shifting and flickering as if it were made of shadows. The air grew colder with each passing second, and a sense of dread settled over the princess and the hero."
    vs "You wander where you are not welcome... the kingdom's taint has stained this place for far too long. I am here to collect what is owed."
   
    if vs_times_gotten == 1: 
        pt "The Vengeful Spirit again...The forest's anger made flesh. We have to be careful; it's driven by pure rage." 
   
    elif vs_times_gotten == 2:
        pt "We've encountered this spirit before. Its anger is overwhelming, but we've survived it once-we can do it again."
   
    else: 
        pt "This spirit won't stop until it destroys us. We have to end this, once and for all."
   
    n "The Vengeful Spirit's presence was suffocating, its form constantly shifting as it glided closer. The hero instinctively stepped forward, placing himself between the princess and the malevolent entity."
    h "Stay back, princess. This spirit is more dangerous than any foe we've faced. We have to be ready for anything."
    vs "You think you can resist? The forest demands retribution, and you shall be the first to pay."
    n "The spirit's voice was a chilling whisper, echoing through the trees and seeping into their very bones. The mist around them thickened, the air growing colder with every word it spoke."
    vs "The forest has taken from the wicked before, and now it shall take from you. There is no escape from its wrath."

    jump vs_choices_1

    # Level 1 of choice tree
    label vs_choices_1:
        # Initial branch
        menu:
            "(Act) Stand your ground and challenge the spirit":
                n "The princess squared her shoulders, meeting the Vengeful Spirit's gaze with unwavering resolve. The hero tightened his grip on his sword, ready to defend her at a moment's notice."
                p "We're not afraid of you! If it's justice you seek, then we'll face it head-on!"
                h "Stay sharp, princess. It's more than just a spirit-it's the forest's fury given form."
                n "The spirit's voice echoed through the trees, cold and filled with ancient resentment."
                vs "Fools... You speak of justice, yet your kingdom's hands are drenched in blood. You'll find no mercy here, only retribution."

                jump vs_choices_2_1

            "(Act) Show empathy and attempt to reason with it":
                n "The princess took a deep breath, sensing the depth of pain and suffering in the spirit's presence. She stepped forward, her voice calm and sincere."
                p "You're hurting, I can feel it. We're not here to continue the cycle of pain-we want to help the forest heal."
                n "The spirit's form flickered, its shape twisting with a mixture of sorrow and rage."
                vs "Help? How can you speak of healing when you carry the same taint as those who defiled this land? The forest cries out for justice, not empty words!"
                h "Princess, be careful. It's trapped in its anger-it might not even want to listen."
                n "Despite the spirit's hostility, the princess could sense a lingering sorrow beneath the wrath. Perhaps there was a way to reach it."

                jump vs_choices_2_2
            

            # Dialogue pool options

            "(Inquire) Who are you?" if not vs_chose_who_are_you:
                $ vs_chose_who_are_you = True
                call vs_who_are_you
                jump vs_choices_1

            "(Inquire) Why do you seek vengeance?" if not vs_chose_why_do_you_seek and vs_chose_who_are_you:
                $ vs_chose_why_do_you_seek = True
                call vs_why_do_you_seek
                jump vs_choices_1

            "(Inquire) Can you ever be at peace?" if not vs_chose_can_you_ever and vs_chose_why_do_you_seek:
                $ vs_chose_can_you_ever = True
                call vs_can_you_ever
                jump vs_choices_1

            "(Inquire) What do you want from us?" if not vs_chose_what_do_you:
                $ vs_chose_what_do_you = True
                call vs_what_do_you
                jump vs_choices_1

            "(Inquire) Why do you blame us for the kingdom's sins?" if not vs_chose_why_do_you_blame and vs_chose_why_do_you_blame:
                $ vs_chose_why_do_you_blame = True
                call vs_why_do_you_blame
                jump vs_choices_1

            "(Inquire) Isn't there a way to break this cycle of hatred?" if not vs_chose_isnt_there_a and vs_chose_isnt_there_a:
                $ vs_chose_isnt_there_a = True
                call vs_isnt_there_a
                jump vs_choices_1
            
            "(Inquire) Why can't you let go of your anger?" if not vs_chose_why_cant_you:
                $ vs_chose_why_cant_you = True
                call vs_why_cant_you
                jump vs_choices_1

            "(Inquire) Do you not see the destruction your rage causes?" if not vs_chose_do_you_not and vs_chose_why_cant_you:
                $ vs_chose_do_you_not = True
                call vs_do_you_not
                jump vs_choices_1

            "(Inquire) Can't you find peace in the forest's renewal?" if not vs_chose_cant_you_find and vs_chose_cant_you_find:
                $ vs_chose_cant_you_find = True
                call vs_cant_you_find
                jump vs_choices_1

            "(Inquire) What will you do if you destroy us?" if not vs_chose_what_will_you:
                $ vs_chose_what_will_you = True
                call vs_what_will_you
                jump vs_choices_1

            "(Inquire) Will your vengeance ever be enough?" if not vs_chose_will_your_vengeance and vs_chose_what_will_you:
                $ vs_chose_will_your_vengeance = True
                call vs_will_your_vengeance
                jump vs_choices_1

            "(Inquire) What then? Will the forest be at peace?" if not vs_chose_what_then and vs_chose_will_your_vengeance:
                $ vs_chose_what_then = True
                call vs_what_then
                jump vs_choices_1


    # Level 2 of choice tree
    label vs_choices_2_1:
        # Branching from "(Act) Stand your ground and challenge the spirit"
        menu:
            "(Act) Have the hero strike first":
                n "The hero stepped forward without hesitation, raising his sword high. His eyes locked onto the shifting form of the Vengeful Spirit, ready to strike."
                scene bg villain_hero_sword_facing_far_vs with dissolve
                p "Now, hero! We have to take it down before it gathers more strength!"
                n "With a swift motion, the hero lunged, his blade slicing through the misty form. But the spirit's laughter echoed, chilling and distorted."
                scene bg villain_hero_charging_far_vs with dissolve
                vs "You think mere steel can harm me? I am bound to the forest, woven into its very essence."
                n "The hero's strike passed through the spirit harmlessly, leaving only a faint shimmer where it had been. The princess's heart sank as she realized this foe would require more than brute strength."
                scene bg villain_far_vs with dissolve

                jump vs_choices_3_1
            "(Act) Confront it with the truth of the kingdom's wrongdoings":
                n "The princess took a steady breath, determined to face the truth head-on. Her voice rang out clear and unwavering."
                p "You're right-the kingdom has done terrible things. They exploited the forest's magic, and the consequences have been devastating. But we're here to change that."
                n "The Vengeful Spirit paused, its shape flickering with uncertainty, as if the words had struck a chord deep within its tormented core."
                vs "Change? Your words are hollow, just like those who came before you. Promises of redemption mean nothing when the scars remain."
                h "Princess, it's listening-but we need more than words to reach it."
                n "The spirit's anger was undeniable, but for the first time, there was a hint of doubt in its voice, a sign that it might still be open to reason."

                jump vs_choices_3_2


            # Dialogue pool options

            "(Inquire) Who are you?" if not vs_chose_who_are_you:
                $ vs_chose_who_are_you = True
                call vs_who_are_you
                jump vs_choices_2_1

            "(Inquire) Why do you seek vengeance?" if not vs_chose_why_do_you_seek and vs_chose_who_are_you:
                $ vs_chose_why_do_you_seek = True
                call vs_why_do_you_seek
                jump vs_choices_2_1

            "(Inquire) Can you ever be at peace?" if not vs_chose_can_you_ever and vs_chose_why_do_you_seek:
                $ vs_chose_can_you_ever = True
                call vs_can_you_ever
                jump vs_choices_2_1

            "(Inquire) What do you want from us?" if not vs_chose_what_do_you:
                $ vs_chose_what_do_you = True
                call vs_what_do_you
                jump vs_choices_2_1

            "(Inquire) Why do you blame us for the kingdom's sins?" if not vs_chose_why_do_you_blame and vs_chose_why_do_you_blame:
                $ vs_chose_why_do_you_blame = True
                call vs_why_do_you_blame
                jump vs_choices_2_1

            "(Inquire) Isn't there a way to break this cycle of hatred?" if not vs_chose_isnt_there_a and vs_chose_isnt_there_a:
                $ vs_chose_isnt_there_a = True
                call vs_isnt_there_a
                jump vs_choices_2_1
            
            "(Inquire) Why can't you let go of your anger?" if not vs_chose_why_cant_you:
                $ vs_chose_why_cant_you = True
                call vs_why_cant_you
                jump vs_choices_2_1

            "(Inquire) Do you not see the destruction your rage causes?" if not vs_chose_do_you_not and vs_chose_why_cant_you:
                $ vs_chose_do_you_not = True
                call vs_do_you_not
                jump vs_choices_2_1

            "(Inquire) Can't you find peace in the forest's renewal?" if not vs_chose_cant_you_find and vs_chose_cant_you_find:
                $ vs_chose_cant_you_find = True
                call vs_cant_you_find
                jump vs_choices_2_1

            "(Inquire) What will you do if you destroy us?" if not vs_chose_what_will_you:
                $ vs_chose_what_will_you = True
                call vs_what_will_you
                jump vs_choices_2_1

            "(Inquire) Will your vengeance ever be enough?" if not vs_chose_will_your_vengeance and vs_chose_what_will_you:
                $ vs_chose_will_your_vengeance = True
                call vs_will_your_vengeance
                jump vs_choices_2_1

            "(Inquire) What then? Will the forest be at peace?" if not vs_chose_what_then and vs_chose_will_your_vengeance:
                $ vs_chose_what_then = True
                call vs_what_then
                jump vs_choices_2_1

    label vs_choices_2_2:
        # Branching from "(Act) Show empathy and attempt to reason with it"
        menu:
            "(Act) Appeal to its desire for justice":
                n "The princess's voice softened, carrying the weight of genuine concern and understanding."
                p "You seek justice, and I understand that pain. But is more destruction really the answer? The forest deserves more than a cycle of endless suffering."
                n "The mist swirled, and for a moment, the spirit's flickering form grew still. Its voice echoed with a bitterness tinged with regret."
                vs "Justice... It's all that remains for those who were wronged. But even justice fades in the face of time-leaving only echoes of grief."
                h "It's conflicted... but that grief is what's driving it. Maybe we can find a way to bring it peace."
                n "The princess felt a flicker of hope. The spirit's desire for justice was its anchor, but perhaps it could be shown a different path."

                jump vs_choices_3_3
            "(Act) Offer a way to ease its suffering":
                n "The princess's eyes softened with compassion as she stepped closer, her voice filled with empathy."
                p "You've carried this pain for so long. If there's any way to ease your suffering, let us help. We can't change the past, but maybe we can find a way forward."
                n "The spirit's form wavered, its edges blurring as if struggling between anger and sorrow."
                vs "Ease my suffering? What could you possibly offer me? The wounds of the past run too deep... and the forest's cries still echo in my soul."
                h "It's not rejecting us outright. There might still be a chance, princess."
                n "The spirit's voice trembled, filled with a deep, enduring pain. The princess knew that offering relief would require more than just words-it would need action."

                jump vs_choices_3_4


            # Dialogue pool options

            "(Inquire) Who are you?" if not vs_chose_who_are_you:
                $ vs_chose_who_are_you = True
                call vs_who_are_you
                jump vs_choices_2_2

            "(Inquire) Why do you seek vengeance?" if not vs_chose_why_do_you_seek and vs_chose_who_are_you:
                $ vs_chose_why_do_you_seek = True
                call vs_why_do_you_seek
                jump vs_choices_2_2

            "(Inquire) Can you ever be at peace?" if not vs_chose_can_you_ever and vs_chose_why_do_you_seek:
                $ vs_chose_can_you_ever = True
                call vs_can_you_ever
                jump vs_choices_2_2

            "(Inquire) What do you want from us?" if not vs_chose_what_do_you:
                $ vs_chose_what_do_you = True
                call vs_what_do_you
                jump vs_choices_2_2

            "(Inquire) Why do you blame us for the kingdom's sins?" if not vs_chose_why_do_you_blame and vs_chose_why_do_you_blame:
                $ vs_chose_why_do_you_blame = True
                call vs_why_do_you_blame
                jump vs_choices_2_2

            "(Inquire) Isn't there a way to break this cycle of hatred?" if not vs_chose_isnt_there_a and vs_chose_isnt_there_a:
                $ vs_chose_isnt_there_a = True
                call vs_isnt_there_a
                jump vs_choices_2_2
            
            "(Inquire) Why can't you let go of your anger?" if not vs_chose_why_cant_you:
                $ vs_chose_why_cant_you = True
                call vs_why_cant_you
                jump vs_choices_2_2

            "(Inquire) Do you not see the destruction your rage causes?" if not vs_chose_do_you_not and vs_chose_why_cant_you:
                $ vs_chose_do_you_not = True
                call vs_do_you_not
                jump vs_choices_2_2

            "(Inquire) Can't you find peace in the forest's renewal?" if not vs_chose_cant_you_find and vs_chose_cant_you_find:
                $ vs_chose_cant_you_find = True
                call vs_cant_you_find
                jump vs_choices_2_2

            "(Inquire) What will you do if you destroy us?" if not vs_chose_what_will_you:
                $ vs_chose_what_will_you = True
                call vs_what_will_you
                jump vs_choices_2_2

            "(Inquire) Will your vengeance ever be enough?" if not vs_chose_will_your_vengeance and vs_chose_what_will_you:
                $ vs_chose_will_your_vengeance = True
                call vs_will_your_vengeance
                jump vs_choices_2_2

            "(Inquire) What then? Will the forest be at peace?" if not vs_chose_what_then and vs_chose_will_your_vengeance:
                $ vs_chose_what_then = True
                call vs_what_then
                jump vs_choices_2_2


    # Level 3 of choice tree
    label vs_choices_3_1:
        # Branching from "(Act) Have the hero strike first"
        menu:
            "(Act) Try to overpower it with sheer force":
                n "The hero gritted his teeth and charged again, this time putting all his strength behind the swing. The blade cut through the air with a forceful whoosh."
                scene bg villain_hero_charging_far_vs with dissolve
                p "Don't hold back! We have to force it into submission!"
                n "The Vengeful Spirit flickered, its form barely shifting as the blade passed through it once more. A mocking laugh echoed from every direction."
                scene bg villain_far_vs with dissolve
                vs "Futile. You struggle against what cannot be touched by mortal hands. The forest's wrath is intangible-its vengeance eternal."
                n "The hero staggered back, his determination clear but his effort wasted. The princess realized that brute strength alone would never be enough against something so otherworldly."

                jump vs_choices_4_1
            "(Act) Use the hero as a decoy and plan a counterattack" if not chose_magic:
                n "The princess's mind raced as she formulated a quick plan. Her eyes locked onto the hero, and she signaled with a sharp nod."
                p "Distract it-keep it focused on you! I'll find an opening!"
                n "The hero understood immediately, charging at the spirit with fierce determination. His sword flashed in the dim light, each swing calculated to keep the spirit occupied."
                scene bg villain_hero_charging_far_vs with dissolve
                vs "You believe distraction will save you? Your tricks are meaningless against the forest's judgment."
                n "While the spirit was preoccupied with the hero's relentless assault, the princess waited for the perfect moment to strike."

                jump vs_choices_4_2

    label vs_choices_3_2:
        # Branching from "(Act) Confront it with the truth of the kingdom's wrongdoings"
        menu:
            "(Act) Acknowledge the kingdom's crimes and ask for mercy" if not chose_magic:
                n "The princess's voice wavered slightly as she spoke, but she refused to let fear overtake her."
                p "I know the kingdom's crimes are unforgivable. They've taken so much from this forest, from you. But please, show us mercy-not for the kingdom's sake, but for the sake of those who still believe in change."
                n "The Vengeful Spirit's form trembled, its voice carrying a bitter edge mixed with a deep sadness."
                vs "Mercy? Mercy was lost when the forest's lifeblood was drained by greed. You think mercy will restore what was taken?"
                h "She's trying to get through, but the wounds run deep. It won't be easy."
                n "The spirit's resistance was fierce, but there was a sliver of doubt. The princess knew she was treading a delicate line between earning its trust and provoking its wrath."

                jump vs_choices_4_3
            "(Act) Offer a solution through magic to mend the past" if chose_magic:
                n "The princess took a deep breath, her hands glowing faintly as she gathered her magic. Her voice was resolute, yet gentle."
                p "The kingdom's wrongs can't be undone, but we can try to heal what remains. There's a way to channel magic back into the forest, to restore some of what was lost. Let me try."
                n "The spirit's flickering form grew still, as if considering her words. Its voice softened, though it was still laced with mistrust."
                vs "You would dare use the same magic that poisoned this land to heal it? The forest's wounds run deeper than you know."
                h "Princess, be careful. Even the slightest misstep could push it further into its rage."
                n "The spirit's reaction was uncertain, but it hadn't outright rejected her offer. The princess felt a glimmer of hope-perhaps this was the key to reaching it."

                jump vs_choices_4_4

    label vs_choices_3_3:
        # Branching from "(Act) Appeal to its desire for justice"
        menu:
            "(Act) Convince it that the forest can still be healed":
                n "The princess's voice was filled with determination, her words earnest and sincere."
                p "The forest isn't beyond saving. Life still grows here, and the wounds can heal with time and care. You don't have to continue this cycle of vengeance."
                n "The spirit's form rippled, its voice hesitant and laced with sorrow."
                vs "Heal? The scars remain, no matter how much life returns. The pain is eternal-etched into every root and branch."
                h "It's struggling with its anger... but I think you might be getting through to it."
                n "The princess could sense the conflict within the spirit. Deep down, it yearned for peace, but the bitterness that fueled it was a powerful force."

                jump vs_choices_4_5
            "(Act) Offer to protect the forest as its guardian" if chose_magic:
                n "The princess raised her hands, a soft glow surrounding her as she made a solemn vow."
                p "If you can't let go of your mission, then let us take it on. We'll protect the forest in your place, ensuring that no one ever repeats the mistakes of the past."
                n "The spirit's voice wavered, its tone caught between bitterness and curiosity."
                vs "You would assume the burden of my wrath? To guard a forest stained by betrayal? Do you think you can bear such a curse?"
                h "Princess, you're offering to carry its anger... but that might bind us to this place forever."
                n "The spirit's presence grew more intense, as if weighing the sincerity of her offer. The princess could feel the weight of her decision-this path would be irreversible."

                jump vs_choices_4_6

    label vs_choices_3_4:
        # Branching from "(Act) Offer a way to ease its suffering"
        menu:
            "(Act) Share its burden by taking on some of its pain" if chose_magic:
                n "The princess's heart ached as she gazed at the tormented spirit. With a deep breath, she reached out with her magic, willing herself to absorb some of its anguish."
                p "You don't have to bear this pain alone. Let me share it, even if it means I'll carry some of your burden."
                n "The spirit's form shuddered, its voice laced with disbelief and a flicker of relief."
                vs "You would willingly take on the suffering of countless souls? You are either foolish or truly compassionate... But such a bond cannot be undone."
                h "Princess, you're playing with forces beyond our control. Are you sure about this?"
                n "The princess could feel the weight of the spirit's sorrow pressing down on her, mingling with her own emotions. This was a dangerous gamble, but it might be the only way to ease the spirit's rage."

                jump vs_choices_4_7
            "(Act) Propose a ritual to put its spirit to rest":
                n "The princess's voice was gentle, laced with the sincerity of one who wished for peace above all else."
                p "There's a way for you to finally rest-to let go of the pain and find peace. We can perform a ritual to free you from this torment, to end your suffering once and for all."
                n "The spirit's flickering form grew still, its voice a mix of curiosity and weariness."
                vs "Rest... after so many years of rage and sorrow... Could such a thing be possible? Or is this another false promise?"
                h "It's considering it, but we'll have to be careful. Spirits like this don't trust easily."
                n "The air around them grew tense, as if the spirit itself was pondering whether to accept the offer or cling to the hatred that had sustained it for so long."

                jump vs_choices_4_8

    
    # Level 4 of choice tree
    label vs_choices_4_1:
        # Branching from "(Act) Try to overpower it with sheer force"
        menu:
            "(Act) Exploit its moment of weakness" if not chose_magic:
                n "The princess watched the spirit carefully, searching for any hint of vulnerability in its shifting form. Her eyes locked onto a small, pulsating core within the swirling shadows-a fragment of the spirit that seemed more tangible than the rest."
                p "There-that's where we need to strike! Aim for the core while it's exposed!"
                scene bg villain_hero_charging_far_vs with dissolve
                n "The hero focused his attention on the faintly glowing spot, his movements swift and precise as he lunged forward. His blade passed through the shadows harmlessly until it connected with the core, sending a shockwave through the air."
                scene bg villain_far_vs with dissolve
                vs "You dare strike at the heart of my rage? Foolish, fragile beings!"
                n "Though the attack landed, the spirit's wrath only seemed to intensify, its form recoiling before lashing out with renewed fury."

                jump vs_choices_5_1
            "(Act) Lead it into a trap using the environment":
                n "An idea formed in the princess's mind-a way to momentarily trap the spirit in place."
                p "We can't face it head-on, not like this. We'll lure it into a cluster of roots-if we can get it tangled up, it might buy us time to strike."
                n "The hero nodded in understanding, moving cautiously as he baited the spirit toward the trap. The spirit followed, its movements erratic, but with an unmistakable hunger driving it forward."
                vs "You think the forest's own grasp will hold me? I am one with this land-I cannot be contained!"
                n "The princess and hero know that those words were no mere boast. If they wanted to defeat the vengeful spirit, they would surely have to do it the hard way."

                jump vs_choices_5_2

    label vs_choices_4_2:
        # Branching from "(Act) Use the hero as a decoy and plan a counterattack"
        menu:
            "(Act) Prepare to strike while it's focused on the hero":
                n "The princess signaled to the hero, urging him to draw the spirit's attention entirely toward himself. The hero charged forward, shouting a challenge as he swung his sword in wide, intimidating arcs."
                scene bg villain_hero_charging_far_vs with dissolve
                p "Keep it focused on you-don't let it see what I'm planning!"
                n "While the spirit fixated on the hero, the princess moved swiftly, circling around until she found an angle where the spirit's core was exposed."
                vs "My vengeance will be swift!"
                n "With the spirit's attention locked on the hero, the princess knew that this would be her chance."

                jump vs_choices_5_3
            "(Act) Feint and deliver a decisive blow":
                n "The princess devised a plan that relied on quick thinking and deception. She signaled for the hero to appear off-balance, feigning exhaustion as they took a few steps back."
                p "Pretend like you're struggling-make it think it has the upper hand."
                n "The hero played his role well, his breathing heavy as he stumbled back, appearing vulnerable and open to attack. The spirit's form surged forward, eager to capitalize on the apparent weakness."
                scene bg villain_hero_sword_facing_far_vs with dissolve
                vs "The forest's vengeance is relentless-you cannot escape it, no matter how you falter."
                n "But just as the spirit moved in for what it thought was an easy victory, the princess darted in from the side, aiming a strike directly at the core hidden within the swirling darkness."

                jump vs_choices_5_4

    label vs_choices_4_3:
        # Branching from "(Act) Acknowledge the kingdom's crimes and ask for mercy"
        menu:
            "(Act) Offer to atone for the kingdom's sins":
                n "The princess's voice was steady but filled with regret as she addressed the spirit directly."
                p "The kingdom has wronged the forest-I know that. If it means putting an end to this cycle of pain, I'll take on the burden of their sins myself."
                n "The spirit's form trembled, the shadows swirling more intensely as it considered her words."
                vs "You offer atonement for crimes that span generations. But words alone cannot cleanse the stain your people have left behind."
                h "Princess, this is a dangerous path. If it accepts your offer, you could be taking on something none of us can bear."
                n "The spirit seemed to be weighing her sincerity, its wrath clashing with a deep, lingering sorrow. The air grew tense as it pondered whether to accept her sacrifice."

                jump vs_choices_5_5
            "(Act) Promise to help the forest heal":
                n "The princess's tone softened, her words carrying a promise of hope."
                p "We can't undo what's been done, but we can help the forest heal. Let us be the ones to guide it back to life and protect it from harm."
                n "The spirit's voice was laced with bitterness, but there was a faint note of longing buried beneath."
                vs "Healing... the forest may regrow, but it will never forget. You seek to plant seeds where only rot remains."
                h "It's a fragile trust we're asking for. We'll need to prove that our intentions are true."
                n "The spirit's form wavered as it wrestled with the choice, the shadows darkening with both suspicion and faint hope."

                jump vs_choices_5_6

    label vs_choices_4_4:
        # Branching from "(Act) Offer a solution through magic to mend the past"
        menu:
            "(Act) Use a binding spell to contain its anger":
                n "The princess began weaving a spell, her hands glowing with soft light as she prepared to channel a binding spell designed to contain the spirit's rage."
                p "This magic is meant to hold back the fury that drives you-to keep it from consuming everything. Let me help you find peace."
                n "The spirit's form twisted violently, a mix of desperation and fury in its voice."
                vs "You think your magic can hold me? My rage has shattered stronger spells than yours!"
                h "Princess, this could backfire if the binding isn't strong enough-it might only make it angrier."
                n "The magic shimmered in the air, the spell teetering on the edge of success or catastrophe as the spirit's will clashed against the enchantment."

                jump vs_choices_5_7
            "(Act) Reverse the flow of magic to restore balance":
                n "The princess focused her magic, channeling energy to reverse the flow of magic within the clearing, aiming to restore balance to the area."
                p "The imbalance that created you can be corrected. If we can reverse the flow of magic, we might be able to restore what was lost."
                n "The spirit's voice grew softer, filled with an ancient sorrow."
                vs "Restore... balance? You cannot undo what is etched into the heart of the forest. The pain that birthed me cannot simply be reversed."
                h "It's listening, but we're on dangerous ground. If this fails, we could make things worse."
                n "The spirit's form flickered, torn between its desire for retribution and the hope that balance could somehow be restored."

                jump vs_choices_5_8

    label vs_choices_4_5:
        # Branching from "(Act) Convince it that the forest can still be healed"
        menu:
            "(Act) Persuade it to let go and find peace" if not chose_magic:
                n "The princess's voice took on a gentle tone, filled with compassion and understanding."
                p "You don't have to keep suffering. The forest can heal, and so can you. It's time to let go of the anger that binds you and find peace."
                n "The spirit's form wavered, its voice trembling with uncertainty."
                vs "Peace... after so much was lost? Such a gift is not for those created by hatred and sorrow."
                h "You might be reaching it, but it won't be easy to let go of what it was created for."
                n "The spirit's presence seemed to soften, its turmoil visible as it grappled with the idea of release after so long."

                jump vs_choices_5_9
            "(Act) Promise to carry on its mission of protecting the forest" if chose_magic:
                n "The princess's hands glowed faintly with magic as she made her offer."
                p "If you can't find peace, then let us take on your mission. We'll protect this forest, carry on your fight, and ensure balance is maintained."
                n "The spirit's form swirled with a mix of pride and distrust."
                vs "You would take on my burden and guard this place? But such a vow binds you to the forest eternally-are you willing to pay that price?"
                h "Princess, this promise might bind us as tightly as it does the spirit. Are we ready for that?"
                n "The spirit's eyes gleamed with interest, testing her resolve as it weighed the sincerity of her offer."

                jump vs_choices_5_10

    label vs_choices_4_6:
        # Branching from "(Act) Offer to protect the forest as its guardian"
        menu:
            "(Act) Bind its spirit to the forest":
                n "The princess reached out with her magic, preparing a ritual to bind the spirit permanently to the forest's essence."
                p "You don't have to wander in rage any longer. Be at peace as the forest's eternal guardian-where you belong."
                n "The spirit's form rippled, its voice a mix of relief and doubt."
                vs "Peace within the forest's embrace... Can you uphold the balance I once sought, without falling to the same greed that tainted others?"
                h "You're trying to seal its fate, but this ritual could backfire if the balance isn't perfect."
                n "The spirit's presence grew heavy as it considered the offer-a chance to rest at last, but at the cost of eternal vigilance."

                jump vs_choices_5_11
            "(Act) Assume its role in guarding the forest":
                n "The princess's voice was solemn as she made her offer, fully aware of the weight it carried."
                p "If you can't let go, then let us take on your role as the forest's protector. You can finally find rest, knowing it will be guarded."
                n "The spirit's form stilled, its voice tinged with both caution and curiosity."
                vs "You would willingly take on the mantle of my rage? Such a burden will tie you to this forest forever, just as it did me."
                h "This path could bind us to the forest for all time. Are you sure that's a future we can accept?"
                n "The spirit's gaze bore into hers, testing whether she truly understood the cost of her offer."

                jump vs_choices_5_12

    label vs_choices_4_7:
        # Branching from "(Act) Share its burden by taking on some of its pain"
        menu:
            "(Act) Absorb its suffering to break the cycle":
                n "The princess steeled herself, channeling her magic to take on the spirit's anguish and pain, hoping to break the cycle of vengeance once and for all."
                p "You've carried this burden for too long. Let me take on some of that suffering, so you can finally be free."
                n "The spirit's voice trembled with both desperation and disbelief."
                vs "You would bear the agony that shaped me? Once taken, such pain cannot be cast aside-it will twist and corrupt everything it touches."
                h "Princess, you're offering to take on something dark and dangerous-can we really handle that?"
                n "The air crackled with tension as the magic swirled around them, the spirit's pain seeking a new vessel, ready to be unleashed."

                jump vs_choices_5_13
            "(Act) Offer to merge your power with the spirit's":
                n "The princess's magic pulsed as she reached out to the spirit, offering to merge her power with its own."
                p "Together, we can protect this forest and end the cycle of vengeance. Share your power with me, and we can forge a new future."
                n "The spirit's form shimmered with conflicting emotions-pride, fear, and a deep-rooted anger."
                vs "Merge with me? You seek to intertwine your essence with what was born of hatred and sorrow? Such a bond cannot be easily broken."
                h "Princess, this could change you-are you ready for what that might mean?"
                n "The spirit hesitated, unsure whether to accept the offer, as the magic between them grew volatile, waiting for a decision."

                jump vs_choices_5_14

    label vs_choices_4_8:
        # Branching from "(Act) Propose a ritual to put its spirit to rest"
        menu:
            "(Act) Offer a final act of sacrifice" if not chose_magic:
                n "The princess's voice was firm, yet filled with a quiet acceptance of what she was about to offer."
                p "If it takes a sacrifice to put this spirit to rest, I'm ready to give everything. This ends here, for the sake of the forest."
                n "The spirit's form quivered, the shadows recoiling as it took in her words."
                vs "You would give your life to end this cycle? A noble offer... but one steeped in the very suffering you seek to escape."
                h "Princess, you can't just offer yourself like that-there has to be another way."
                n "The tension in the air grew palpable as the spirit considered the offer, weighing whether to accept her sacrifice."

                jump vs_choices_5_15
            "(Act) Channel the ritual's energy to free it" if chose_magic:
                n "The princess drew on her magic, channeling the ritual's energy to cleanse the spirit and free it from its endless torment."
                p "This ritual can purify the pain that binds you. Let the forest heal, and let your spirit find peace at last."
                n "The spirit's voice was laced with both gratitude and caution."
                vs "Freedom from suffering... yet this magic you wield holds its own dangers. Are you sure it will not create new wounds in the forest you seek to heal?"
                h "This kind of magic is risky-we might end up doing more harm than good."
                n "The spirit's form flickered between acceptance and doubt, the ritual's power building to a critical point as the decision loomed."

                jump vs_choices_5_16


    # Level 5 of choice tree
    label vs_choices_5_1:
        # Branching from "(Act) Exploit its moment of weakness"
        menu:
            "(Act) Strike it down with determination":
                n "The princess's eyes narrowed as she spotted the faint core within the spirit's swirling shadows. It was a fleeting opening-one they couldn't afford to miss."
                p "Now, hero! Strike at its heart!"
                n "The hero's grip tightened on his sword as he charged, channeling all his strength into one decisive blow. His blade cut through the air, connecting with the spirit's core, sending shockwaves rippling through the clearing."
                scene bg villain_hero_charging_far_vs with dissolve
                vs "You dare...!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The vengeful spirit's voice echoed with rage and despair as its form began to unravel, shadows splintering into fragments of mist."
                n "But just as it started to dissipate, the spirit's eyes locked onto the hero, hatred blazing. A dark curse surged from the fading mist, aimed directly at him."
                n "Without a moment's hesitation, the princess threw herself in front of the hero, the curse striking her instead. Pain seared through her as darkness wrapped around her like tendrils of icy fire."                
                n "The curse claimed the princess's life, her sacrifice saving the hero but costing her everything. With the vengeful spirit finally vanquished, the forest began to return to a fragile peace."
                n "The hero, left kneeling beside her lifeless form, could only mourn the price of their victory. Though he returned to the kingdom as a protector, the emptiness left by her loss would haunt him forever."
                n "And the hero lived happily ever-"

                jump sacrificed_princess
            "(Act) Use the hero's courage to finish it off":
                n "The hero squared his shoulders, determination burning in his eyes as he prepared for one final attack. The princess watched, her heart pounding with both hope and fear."
                p "You can do this! I know you can-just one more strike!"
                n "The hero charged forward, aiming for the spirit's core, but the shadows swirled violently, deflecting his blow. His sword barely grazed the spirit as it retaliated with a surge of dark energy."
                scene bg villain_hero_charging_far_vs with dissolve
                vs "Your courage is commendable, but it is futile. The forest's vengeance cannot be quelled by a mere mortal!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero stumbled back, his strength faltering as the spirit loomed over him, ready to deliver a fatal strike. The princess's breath caught in her throat-she couldn't just stand by and watch."
                n "Without hesitation, the princess grabbed a thick branch from the forest floor. With all her might, she swung the branch directly at the spirit's core, shattering it with a burst of energy."
                n "The spirit's form fractured, its malevolent presence dissolving into mist. As it faded, the forest grew still, the tension lifting as its wrath was finally put to rest."
                n "With the spirit defeated, the princess knelt beside the hero. He looked at her with a mix of awe and gratitude, realizing that it was her courage, not his, that had saved them both."
                n "Returning to the kingdom, they faced their future with a renewed bond. The princess had proven that her strength went beyond any royal title, and the hero knew he was lucky to have her by his side."
                n "And the princess and hero lived happily ever-"

                jump saved_hero

    label vs_choices_5_2:
        # Branching from "(Act) Lead it into a trap using the environment"
        menu:
            "(Act) Distract and outrun it" if not chose_magic:
                n "The princess's mind raced-there had to be a way to escape without getting caught in the spirit's fury. Fighting it head-on wasn't an option."
                p "We can't hold it here for long. We'll have to outrun it-create a distraction and break for the edge of the forest!"
                n "The hero nodded, determination flashing in his eyes. He rushed forward, taunting the spirit and leading it away from their planned escape route. The spirit followed, its form flickering with rage as it chased him."
                vs "You think you can flee from the forest's wrath? There is no escape for those marked by its curse!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "While the spirit was fixated on the hero, the princess focused her magic, causing nearby roots and vines to erupt from the ground. The sudden burst of movement caught the spirit's attention, giving them the split-second they needed to slip away."
                n "The hero dashed back toward the princess, and together they sprinted through the dense undergrowth. The spirit's enraged howls echoed behind them, but the path ahead cleared as the forest itself seemed to guide them to safety."  
                n "After narrowly escaping the spirit's grasp, the princess and hero found themselves at the forest's edge, where the kingdom lay in sight. Their trial had not only tested their strength, but also their wit and trust in one another."
                n "Returning to the kingdom, the princess was welcomed as a leader who had tamed the forest's rage. With the hero by her side, she ascended to the throne, ruling with the wisdom gained from their harrowing journey."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne
            "(Act) Teleport away while it's distracted" if chose_magic:
                n "The princess's magic pulsed as she concentrated, her mind racing for a way out. The spirit was too strong to defeat directly-they needed to escape."
                p "It's too dangerous to keep fighting. Let's teleport out of here while it's distracted!"
                n "The hero gave a quick nod, trusting her judgment. As the spirit lashed out with wild fury, they used the momentary chaos to gather their energy."
                vs "You cannot run from the forest's wrath! It will follow you wherever you go!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "Ignoring the spirit's threats, the princess focused on the spell, visualizing a safe place away from the cursed forest. With a flash of light, they vanished just as the spirit's rage reached its peak, leaving only empty shadows in their wake."        
                n "Safe from the spirit's vengeance, the princess and hero decided to leave the kingdom behind. They knew that the power they wielded would never be accepted by those who feared magic, so they chose a life of freedom instead."
                n "Together, they forged a new path away from the expectations of the kingdom, living in peace and harmony, free from the burdens of the past."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after

    label vs_choices_5_3:
        # Branching from "(Act) Prepare to strike while it's focused on the hero"
        menu:
            "(Act) Land a decisive blow":
                n "The hero charged forward with unwavering resolve, his strikes relentless against the spirit's ethereal form. But with every swing, it became clear that his blade alone could not deliver the final blow."
                vs "You struggle in vain, hero. The forest's wrath is endless-your strength means nothing."
                n "The spirit's voice dripped with malice as it unleashed a wave of dark energy, knocking the hero off his feet. He struggled to rise, the malevolent force pressing down on him with crushing weight."
                p "No! Hero, stay with me!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The princess's heart pounded in her chest. She knew that if she didn't act now, the hero would be overwhelmed. Without hesitation, she grabbed the branch she'd prepared earlier and rushed in."
                n "As the spirit focused on the hero, she aimed directly for the glowing core within its shadows, striking with all her might. The impact sent a shockwave through the clearing, shattering the core and causing the spirit to writhe in agony."
                n "The spirit's form crumbled away, its anger dissolving into nothingness. The princess knelt beside the hero, helping him to his feet. He looked at her, gratitude and admiration shining in his eyes."
                n "With the spirit vanquished, the princess and hero returned to the kingdom, their bond stronger than ever. Together, they faced whatever challenges lay ahead, knowing they could count on each other no matter the odds."
                n "And the princess and hero lived happily ever-"

                jump saved_hero
            "(Act) Strike it down while it's distracted":
                n "The hero's relentless attacks held the spirit's attention, allowing the princess to circle around unnoticed. Her heart pounded as she eyed the core-the one part of the spirit that was vulnerable to physical strikes."
                p "This is our chance... I have to end it now!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "With the spirit fully focused on the hero, the princess crept closer, every step silent as she approached the pulsing core. The hero gave it everything he had, driving the spirit further back and leaving it exposed."
                n "Suddenly, the princess lunged forward, swinging the branch with all her strength. The strike connected with the core, shattering it with a sharp, resounding crack."
                n "The spirit's form flickered, its hold on the forest weakening before it dissolved into nothingness. The dark presence that had haunted the woods was finally gone."
                n "With the vengeful spirit's defeat, the princess and hero returned to the kingdom as champions. The people, recognizing her strength and wisdom, crowned her queen, and the hero stood beside her as her most trusted advisor."
                n "As ruler, the princess led with both compassion and authority, ensuring that the mistakes of the past would never be repeated. The kingdom flourished under her reign, protected by the very hero who had once saved it."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne

    label vs_choices_5_4:
        # Branching from "(Act) Feint and deliver a decisive blow"
        menu:
            "(Act) Deliver a fatal strike":
                n "The princess's heart raced as the hero stumbled back, his feigned weakness luring the spirit into a vulnerable position. It surged forward, ready to claim victory, completely unaware of the trap they had set."
                p "Now! This is our only chance!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero barely had time to recover as the princess rushed in with a makeshift weapon, aiming directly for the glowing core at the spirit's center. But just as she struck, the spirit lashed out with a curse, its final act of defiance."
                n "The curse wrapped around the hero like tendrils of shadow, draining his strength. He collapsed, his breath shallow and his eyes clouding over as the curse tightened its grip."
                n "Desperation gripped the princess as she knelt beside him, tears streaming down her face. She knew there was no way to save him-the curse would claim him within moments."
                n "There was only one choice she could make. With trembling hands, the princess took up the hero's fallen sword and drove it through her own heart, collapsing beside him as darkness closed in around them both."
                n "The forest grew silent as the vengeful spirit faded, its wrath extinguished at last. The princess and hero, united in love even in death, found peace in each other's arms as their souls left the mortal world behind."
                n "And the princess and hero died happily ever-"

                jump love_beyond_death
            "(Act) Overwhelm it with precision":
                n "The hero put on a convincing show of exhaustion, stumbling back as the spirit advanced, eager to exploit his apparent weakness. But the spirit's relentless pursuit pushed him to the brink, its tendrils of dark energy coiling around him."
                vs "You are but a feeble mortal, no match for the forest's fury. Your resistance is meaningless."
                n "The hero's strength faltered as the spirit closed in, tightening its grip. The situation was slipping out of control, and the princess knew that if she didn't act now, the hero wouldn't survive."
                p "Hero, hold on! I won't let you go down like this!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "With fierce determination, the princess charged in, aiming for the pulsing core. She swung her makeshift weapon-a branch she'd grabbed earlier-right at the spirit's vulnerable spot, striking with pinpoint precision."
                n "The core shattered, and the spirit's form began to dissolve, its once-powerful presence now reduced to a fading wisp. The hero collapsed to his knees, gasping for breath as the dark energy released its hold on him."
                n "The princess helped him up, relief washing over her as the danger passed. She had saved him in the nick of time, turning what could have been a tragic end into a hard-fought victory."
                n "The forest grew quiet as the spirit's wrath faded into oblivion. Returning to the kingdom, the princess and hero stood side by side, their bond cemented by the trials they had faced together."
                n "And the princess and hero lived happily ever-"

                jump saved_hero

    label vs_choices_5_5:
        # Branching from "(Act) Offer to atone for the kingdom's sins"
        menu:
            "(Act) Offer your life as penance":
                n "The princess's voice trembled as she spoke, her resolve clear even as she faced the spirit's rage."
                p "If my life can atone for the kingdom's sins, then take it. Let this be the end of the suffering."
                n "The hero's eyes widened in alarm, but before he could intervene, the spirit surged forward, its tendrils of darkness wrapping around the princess."
                vs "So, you offer your life willingly? A sacrifice to satisfy the forest's wrath... Perhaps this is what was needed all along."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero struggled to reach her, but the spirit's grip tightened, siphoning away the princess's life force. Her breath grew shallow as the darkness closed in, the air thick with sorrow and inevitability."
                n "The princess's final breath left her lips as the spirit's wrath was quelled. The forest fell eerily silent, its anger dissipated with the princess's sacrifice."
                n "The hero knelt beside her lifeless body, grief-stricken and powerless. Though the spirit was gone, victory came at a devastating cost."
                n "With tears in his eyes, the hero swore to honor her memory, even as he struggled with the emptiness left behind."
                n "And the hero lived happily ever-"

                jump sacrificed_princess
            "(Act) Convince it that the kingdom can change":
                n "The princess's voice rang with conviction as she made her plea, hope shining through her words."
                p "The kingdom has learned from its mistakes. We're not the people who caused this pain, and we can make sure it never happens again. But we need the chance to prove that change is possible."
                n "The spirit's form flickered, the bitterness in its voice wavering as it considered her words."
                vs "Promises of change are nothing without action. Yet... perhaps there is truth in your conviction. Could this cycle finally end?"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The shadows that surrounded the spirit began to fade, its form becoming more ethereal and transparent. It no longer held the same malice-it was as though a burden had been lifted."
                n "With the spirit's wrath quelled, the princess and hero returned to the kingdom. Her words had carried the hope of a future where the past's mistakes wouldn't be repeated."
                n "In time, the princess took her place as queen, leading with the wisdom gained from the trials they had faced. By her side, the hero stood as her protector and trusted companion, ensuring that the kingdom remained just and fair."
                n "The kingdom flourished under their rule, the forest thriving in harmony with the people once more."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne

    label vs_choices_5_6:
        # Branching from "(Act) Promise to help the forest heal"
        menu:
            "(Act) Forge a pact to protect the forest":
                n "The princess's voice was calm, but resolute, as she extended her hand, offering a binding promise."
                p "We can't undo what was done, but we can make a pact to protect this forest from now on. Let us be its guardians, ensuring its recovery and peace."
                n "The spirit's form flickered, its ancient sorrow mingling with the faintest hint of hope."
                vs "A pact... One born not from power, but from genuine intent. Perhaps the forest might accept such a promise. Yet, such a burden is not easily carried."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The spirit's voice softened, its anger slowly dissipating as it weighed her offer. The darkness that once choked the forest began to recede, as if the land itself was responding to her words."
                n "With the spirit's wrath finally put to rest, the forest began its long journey of healing. The princess and hero returned to the kingdom, where her unwavering dedication to protecting both the land and her people led her to take the throne."
                n "As queen, she honored the pact made in the forest, ensuring that the mistakes of the past would not be repeated. By her side, the hero stood as her protector and advisor, helping her maintain balance and peace."
                n "Together, they ruled with wisdom and compassion, safeguarding both the kingdom and the natural world."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne
            "(Act) Use the hero's loyalty as a guarantee":
                n "The princess's voice was steady as she looked to the hero, drawing strength from their bond."
                p "If you can't trust words alone, then trust this-he's fought alongside me through every challenge. We're committed to protecting this forest, no matter the cost."
                n "The spirit's gaze shifted to the hero, studying him with a mix of curiosity and suspicion."
                vs "Loyalty forged in hardship... Perhaps that is the only bond strong enough to sway the forest's judgment. Yet loyalty alone cannot heal what was lost."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero stepped forward, determination clear in his eyes as he nodded in agreement. But just as the spirit began to soften, it lashed out in a sudden burst of energy, seeking to test that loyalty one final time."
                n "The princess sprang into action, going after the spirit with quick reflexes and decisive action. With a desperate strike aimed at its vulnerable core, she shattered the remnants of its wrath, freeing the forest from its grip."
                n "The hero staggered but remained standing, saved by her intervention. The bond between them had only grown stronger in the face of such trials."
                n "With the spirit's threat ended, they returned to the kingdom, their unity a testament to the strength of trust and loyalty."
                n "And the princess and hero lived happily ever-"

                jump saved_hero

    label vs_choices_5_7:
        # Branching from "(Act) Use a binding spell to contain its anger"
        menu:
            "(Act) Contain its wrath within yourself":
                n "The princess's magic flared brightly, intensifying as she struggled to hold the spirit's rage within the confines of her spell."
                p "I can contain this, but I need to channel the anger somewhere safe..."
                n "The spirit's form twisted violently, resisting the containment as the dark energy surged. The hero stepped closer, his eyes filled with determination."
                h "Princess, focus on me-I'll take the burden! I can handle it!"
                n "Without hesitation, the princess directed the flow of the malevolent energy into the hero. For a moment, everything seemed stable, the spirit's wrath subdued within his grasp."
                vs "Foolish mortals, thinking they can bear the weight of centuries of torment..."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But then, something went wrong. The dark energy began to corrupt the hero's body, warping it into something monstrous. The hero's gaze turned wild, his breath ragged as he fought to maintain control."
                n "Realizing what was happening, the hero made a heartbreaking decision. With the last remnants of his willpower, he turned the corrupted energy inward, causing his body to shatter as he sacrificed himself to save the princess."
                n "The spirit's presence faded, but the cost was too great. The hero's final act was one of selflessness, ensuring that his corruption did not spread."
                n "The princess was left alone, her heart heavy with grief. The victory was hollow, and the forest's silence echoed the emptiness within her."
                n "And the princess lived happily ever-"

                jump corrupted_hero
            "(Act) Teleport away while it's distracted":
                n "The princess quickly realized that containing the spirit's wrath was a losing battle. She knew they needed to escape before things spiraled out of control."
                p "We can't hold it forever. Hero, get ready-I'll teleport us out of here the moment it falters!"
                n "The hero nodded, trusting her judgment as he prepared for the escape. The spirit's fury intensified, but the princess's quick thinking allowed her to spot a momentary lapse in its focus."
                vs "You think you can flee from the forest's judgment? There is no escape for those marked by its pain!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But before the spirit could unleash its full power, the princess seized the opportunity. In an instant, she cast the teleportation spell, whisking them both away to safety."
                n "They reappeared far from the cursed clearing, the air no longer thick with malice. The spirit's wrath was left behind, unable to pursue them beyond the forest's borders."
                n "The princess and hero decided to leave the kingdom behind, knowing that they would be shunned for magic they used. In time, they found a place where they could live freely, unburdened by the past."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after

    label vs_choices_5_8:
        # Branching from "(Act) Reverse the flow of magic to restore balance"
        menu:
            "(Act) Redirect its pain to heal the forest":
                n "The princess channeled her magic into reversing the flow of dark energy, attempting to soothe the spirit's pain by turning it into something restorative for the forest."
                p "We can heal this place, turn pain into life-let this be the end of the suffering!"
                n "The spirit's form wavered, its voice laced with sorrow and uncertainty."
                vs "You seek to twist the very essence of my creation... to turn agony into renewal. Such a concept is both foolish and... tempting."
                n "The magic wove through the clearing, causing the withered plants to stir with newfound energy. But the spirit's wrath remained strong, clinging to the hatred that had sustained it for so long."
                h "Princess, the forest is responding, but the spirit isn't letting go-it's still driven by vengeance!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "As the magic surged, the spirit suddenly lashed out, aiming its full fury at the princess. In its final moments, it struck her down, its last act of vengeance delivered."
                n "The hero watched in horror as the princess fell, her life slipping away in an instant. Desperate and unwilling to accept her death, he resorted to forbidden magic, pouring everything he had into bringing her back. The dark energy surged, defying nature itself as it restored the princess to life."
                n "The spirit's curse was lifted, and the forest began to heal. But the hero's actions had sealed his fate-the kingdom could not forgive the use of such forbidden magic."
                n "Though the princess lived, the hero was banished, forced to leave her behind. She would have to move on alone, her heart forever scarred by the loss."
                n "And the princess lived happily ever-"

                jump unfulfilled_love
            "(Act) Try to defeat it with magic":
                n "The princess channeled all her remaining magic into a focused blast, determined to end the spirit's wrath once and for all."
                p "This ends here-let the forest find peace!"
                n "The spirit's form recoiled, struggling against the surge of light. But just as the magic struck its core, the spirit released one final curse, latching onto the hero."
                vs "If I must fade... I will not go alone..."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero gasped in pain as the curse began to take hold, his life force draining rapidly. The princess's heart sank as she realized the curse was fatal, and there was no time to save him."
                n "The princess made a heartbreaking choice. If the hero was doomed, she would not let him face death alone. Taking his hand, she whispered a final goodbye before the curse claimed them both."
                n "As the darkness closed in, the spirit's wrath finally faded, leaving only peace in its wake. The forest began to heal, free from the hatred that had bound it for so long."
                n "In death, the princess and hero found the peace that had eluded them in life. United even in the afterlife, they would never be separated again."
                n "And the princess and hero died happily ever-"

                jump love_beyond_death

    label vs_choices_5_9:
        # Branching from "(Act) Persuade it to let go and find peace"
        menu:
            "(Act) Guide it to the afterlife":
                n "The princess's voice was soft yet unwavering as she reached out with compassion and understanding."
                p "It's time to let go of the anger that binds you. I'll help you find peace... even if it means sacrificing myself to do so."
                n "The spirit's form wavered, its rage flickering like a dying flame. But just as it began to dissolve, a final surge of malevolence erupted from its core."
                vs "Peace... is for those untouched by betrayal. You shall taste the sorrow that I carry."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The spirit lashed out with one final, desperate curse, a bolt of dark energy aimed directly at the hero. Without hesitation, the princess threw herself in front of him, taking the full brunt of the curse."
                n "The curse tore through the princess, and she crumpled to the ground as the spirit's remaining energy dispersed. The hero's cry of anguish echoed through the clearing as he caught her in his arms, the life draining from her eyes."
                n "With the spirit finally laid to rest, the forest grew calm, but the victory was hollow. The hero was left to grieve, holding the princess in his arms as he whispered her name."
                n "And the hero lived happily ever-"

                jump sacrificed_princess
            "(Act) Let it fade away peacefully":
                n "The princess's voice was filled with compassion as she urged the spirit to release its pain."
                p "You've suffered long enough. It's time to let go and find the peace you deserve. I'll help you-let us both move on together."
                n "The spirit's form flickered, its anger softening into sorrow. It hesitated, as if finally considering the release it had long denied itself."
                vs "Peace... I have yearned for it, but never believed it was within reach. Perhaps... in letting go, I can finally be free."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But as the spirit's energy began to dissolve, it unleashed a final curse, its hatred lingering even as it sought rest. The curse struck the hero, a dark poison spreading through his veins."
                n "The hero's time was short-mere moments before the curse would claim him. The princess, unable to bear losing him, made a desperate decision."
                n "With tears in her eyes, the princess held the hero close and plunged a dagger into her own heart. They collapsed together, their souls entwined as they drifted into the afterlife. The spirit's curse faded into nothingness, leaving only the memory of their love behind."
                n "And the princess and hero died happily ever-"

                jump love_beyond_death

    label vs_choices_5_10:
        # Branching from "(Act) Promise to carry on its mission of protecting the forest"
        menu:
            "(Act) Become its successor":
                n "The princess's magic intertwined with the spirit's, her vow to protect the forest binding their destinies together."
                p "You can rest now-I'll take on your mission and ensure the forest is guarded for generations to come."
                n "The spirit's form shimmered with gratitude and acceptance as it slowly faded, leaving its strength and purpose in the hands of the princess and hero."
                vs "You have chosen a path of vigilance. May your resolve never waver, for the forest's future now rests with you."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The energy of the forest shifted, recognizing the princess and hero as its new guardians. They felt a deep connection to the land, a bond that would shape their lives from that moment on."
                n "The princess and hero chose to stay within the forest, vowing to protect it from those who would seek to exploit it. With the spirit at rest and the forest thriving, they found a new purpose as its stewards."
                n "They never returned to the kingdom, knowing that their duty lay in safeguarding the delicate balance of nature."
                n "And the princess and hero lived happily ever-"

                jump forest_protectors
            "(Act) Betray and teleport away":
                n "The princess's magic flared as she prepared to carry out her plan. Just as the spirit began to trust her, she whispered the incantation for a teleportation spell."
                p "I'm sorry... but this is a burden I can't carry."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "In a flash of light, the princess and hero vanished, leaving the spirit behind. Its anger roared through the clearing, but they were already far from its reach."
                n "The princess and hero found themselves in a distant land, far from the kingdom and the forest's lingering fury. They knew that returning home was no longer an option-the magic they had used would never be welcome back in the kingdom."
                n "Instead, they chose to build a new life together, free from the expectations and dangers that once haunted them."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after

    label vs_choices_5_11:
        # Branching from "(Act) Bind its spirit to the forest"
        menu:
            "(Act) Ensure it remains as a guardian":
                n "The princess channeled her magic into a complex spell, weaving the spirit's essence back into the heart of the forest."
                p "This forest has been your home and prison. I'll ensure that your purpose as its guardian remains, but without the hatred that once consumed you."
                n "The spirit's form shimmered, its rage softening into a sense of peace as the spell took hold."
                vs "To remain as the guardian... free from anger... Perhaps, this is the fate I was always meant to have."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The magic anchored the spirit's essence within the forest, no longer driven by vengeance but by a deep connection to the land."
                n "With the spirit's power restored to its rightful purpose, the forest thrived once more. The princess and hero chose to stay, their new role as protectors forever entwined with the land they had saved."
                n "They never returned to the kingdom, knowing that their place was now within the forest, safeguarding its balance and ensuring that peace endured."
                n "And the princess and hero lived happily ever-"

                jump forest_protectors
            "(Act) Trap it forever within the forest's bounds":
                n "The princess's magic surged as she prepared a ritual that would trap the spirit permanently within the depths of the forest."
                p "You'll remain here, bound to the forest, unable to harm anyone again. This is where your wrath ends."
                n "The spirit's form twisted in fury as the spell took hold, lashing out in desperation. But the ritual's magic was stronger, ensnaring the spirit within the forest's roots."
                vs "You dare imprison me? The forest and I are one-if I must suffer, so will everything within these woods!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "As the spell completed, a dark shockwave rippled through the area, corrupting the very ground beneath their feet. The hero stumbled back, but the tainted energy clung to him, warping his form."
                n "The spirit's essence was sealed away, but the hero was not untouched. The corruption began to change him, his body twisting under its influence. Realizing he was becoming a monster, he made a final, selfless decision."
                n "With one last look at the princess, he plunged his sword into his chest, ending the transformation before it could fully take hold. The princess was left alone, the victory tainted by unbearable loss."
                n "And the princess lived happily ever-"

                jump corrupted_hero

    label vs_choices_5_12:
        # Branching from "(Act) Assume its role in guarding the forest"
        menu:
            "(Act) Take on its duties eternally":
                n "The princess's magic intertwined with the spirit's essence as she made her vow."
                p "You've carried this burden long enough. I'll take on your role as the forest's protector, ensuring that its peace is maintained."
                n "The spirit's form shimmered with a mix of relief and respect as it accepted her offer."
                vs "To guard this forest for eternity... It is a path few would choose, but one that requires true devotion. May your resolve remain unbroken."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The forest's energy shifted, welcoming the princess and hero as its new guardians. The spirit's essence faded into the land itself, leaving behind its wisdom and strength."
                n "With the spirit's purpose fulfilled, the princess and hero chose to remain in the forest, dedicating their lives to its protection. They became part of the forest's cycle, ensuring that it would never again fall into darkness."
                n "They knew that their place was no longer in the kingdom-they were now the eternal stewards of the forest, bound by their vow."
                n "And the princess and hero lived happily ever-"

                jump forest_protectors
            "(Act) Bind yourself to the forest in a tragic pact":
                n "The princess prepared to make a tragic vow, binding herself to the forest's essence and taking on the spirit's eternal burden."
                p "I'll carry the weight of your sorrow and protect this land-even if it means losing everything else."
                n "The spirit's form flickered with dark approval, its energy converging as it prepared to seal the pact. But just as the ritual neared completion, the spirit lashed out with a final surge of fury, striking the princess down."
                vs "You wish to take my place? Then die as I did, bound to this cursed land!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The princess's body crumpled to the ground, her life fading away as the spirit's wrath consumed her. The hero, overcome with despair, rushed to her side, tears filling his eyes as he realized she was gone."
                n "Driven by desperation, the hero called upon forbidden magic, a power he knew would come with dire consequences. His hands trembled as he chanted the incantation, pouring every ounce of his will into bringing her back."
                n "The magic worked-life returned to the princess as her eyes fluttered open, but the cost was immense. The dark power that revived her was noticed by the kingdom, leading to the hero's immediate banishment."
                n "With the hero cast out, the princess was left to carry on her duty as the forest's guardian, alone and burdened by the knowledge of the sacrifice he made. She would have to move on without the one who had saved her, bound to the forest by a tragic fate."
                n "And the princess lived happily ever-"

                jump unfulfilled_love

    label vs_choices_5_13:
        # Branching from "(Act) Absorb its suffering to break the cycle"
        menu:
            "(Act) Let its power corrupt you":
                n "The princess channeled her magic, absorbing the full weight of the spirit's suffering. The dark energy flooded her senses, overwhelming her with the torment and rage that had driven the spirit for so long."
                p "I can feel... everything. The anger, the sorrow... it's all consuming me!"
                n "The hero rushed forward, trying to pull her back, but it was too late. The spirit's power clung to her, twisting her magic into something dark and uncontrollable."
                h "Princess! Fight it-don't let it take you!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But as the darkness spread, it latched onto the hero, corrupting him as well. His eyes darkened, a sinister glow overtaking his once-noble gaze."
                n "The hero, unable to resist the corruption, felt his humanity slipping away. In a final, desperate act of love, he turned his blade on himself, ending his life before he could fully transform into something monstrous."
                n "The princess, who was able to break free from the spirit's grasp, could only watch in horror as the hero's lifeless body fell before her."
                n "The cost of breaking the cycle was too great-she was left alone, haunted by the darkness she had unleashed."
                n "And the princess lived happily ever-"

                jump corrupted_hero
            "(Act) Take on its rage and become twisted":
                n "The princess opened herself to the spirit's wrath, embracing the rage that had driven it for centuries. As the fury took root in her heart, it began to change her, twisting her emotions into something dark and unrecognizable."
                p "The hatred... it's overwhelming. I can barely hold on..."
                n "The hero could see the transformation taking place-the once-compassionate princess was now consumed by the very anger she had tried to soothe. He reached out, desperate to save her from herself."
                h "Princess, snap out of it! This isn't who you are!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "But the rage had taken hold. The princess lashed out, her magic warping into something wild and uncontrollable. In the chaos, the spirit struck one final blow, killing her as she succumbed to the darkness."
                n "In his grief, the hero resorted to forbidden magic to bring her back, knowing the consequences that awaited him. The princess returned to life, but the kingdom's elders deemed his actions unforgivable, banishing him from the land."
                n "Left to rule alone, the princess was burdened by the knowledge that the hero had sacrificed everything for her."
                n "Though she regained her life, the love they once shared was lost forever, torn apart by the darkness that had claimed them."
                n "And the princess lived happily ever-"

                jump unfulfilled_love

    label vs_choices_5_14:
        # Branching from "(Act) Offer to merge your power with the spirit's"
        menu:
            "(Act) Form a dark bond with the spirit":
                n "The princess reached out, offering to merge her magic with the spirit's, hoping to forge a new bond that would end the cycle of vengeance."
                n "But as the two powers intertwined, something went wrong-her magic twisted and corrupted by the spirit's hatred."
                p "No... this power... it's too much. I can't control it!"
                n "The spirit's voice echoed in her mind, a mixture of pride and malice as it sensed the change in her."
                vs "You sought to share my burden-now you will carry it forever. The curse has become part of you."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero watched in horror as the princess's aura darkened, her once-bright magic now tainted by the spirit's malevolence. The corruption spread to him as well, turning his thoughts and emotions into something monstrous."
                n "Unable to fight the darkness within, the hero made a heartbreaking decision. In his final act, he sacrificed himself to save the princess, severing the bond and ending his life before the corruption fully took hold."
                n "The princess was left alone, her heart heavy with guilt and sorrow. The spirit's curse had been broken, but the price was the hero's life-and the lingering stain of darkness that would haunt her forever."
                n "And the princess lived happily ever-"

                jump corrupted_hero
            "(Act) Fuse your essence with its wrath":
                n "The princess let her magic flow freely, allowing it to merge with the spirit's wrath. The connection was immediate and powerful, their energies fusing into something dark and uncontrollable."
                p "I can feel its hatred... every wound, every betrayal. It's taking over..."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero watched in horror as the spirit's fury consumed the princess, warping her very essence. But before he could act, the spirit struck a final, fatal blow, killing her as she succumbed to the darkness."
                n "Desperate to save her, the hero invoked forbidden magic, bringing the princess back from the brink of death. But the kingdom's elders condemned his actions, banishing him for violating the natural order."
                n "The princess, now alive but burdened by the consequences, had to live with the knowledge that the hero was lost to her forever. Though she survived, their love was torn apart by the curse she had sought to end."
                n "And the princess lived happily ever-"

                jump unfulfilled_love

    label vs_choices_5_15:
        # Branching from "(Act) Offer a final act of sacrifice"
        menu:
            "(Act) Give your life to save the hero":
                n "The princess saw the spirit's wrath bearing down on the hero, its dark tendrils coiling like vipers ready to strike. Without hesitation, she stepped between them, her voice filled with unwavering resolve."
                p "I won't let you take him. If a life must be sacrificed... let it be mine!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The hero's eyes widened in horror as the princess shielded him with her body, absorbing the full force of the spirit's deadly curse."
                n "Her knees buckled, but she refused to falter, determined to save him even at the cost of her own life."
                n "The curse struck the princess with merciless precision, draining the life from her in an instant. The hero, powerless to stop it, could only watch as the light in her eyes faded, her sacrifice complete."
                n "With her final breath, the spirit's rage dissipated, leaving only silence in its wake. The hero fell to his knees, grief-stricken but alive-saved by the one person he couldn't protect."
                n "Though he would carry the weight of her loss forever, her sacrifice had ensured that he survived to carry on her legacy."
                n "And the hero lived happily ever-"

                jump sacrificed_princess
            "(Act) Die together to free the spirit":
                n "As the battle reached its peak, the spirit unleashed one final, devastating curse aimed directly at the hero. The princess knew there was no way to save him this time-the curse would claim his life within moments."
                p "If this is how it ends, then I'm staying by your side. We face this together, no matter what."
                h "I wouldn't have it any other way, princess. If we go, we go together."
                n "Hand in hand, they stepped forward, both fully accepting the fate that awaited them. The spirit paused, its wrath momentarily subdued by the sight of their unwavering unity."
                vs "You would both choose death, rather than fight? Perhaps... that is the peace this forest has been denied for so long."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The curse struck true, claiming both their lives in an instant. But in their final moments, the spirit's wrath began to fade, its hatred quelled by the sacrifice of two souls bound by love."
                n "The forest grew still as the spirit's form dissolved into the mist, its vengeance finally sated. The princess and hero passed into the afterlife together, their bond unbroken even in death."
                n "And the princess and hero died happily ever-"

                jump love_beyond_death

    label vs_choices_5_16:
        # Branching from "(Act) Channel the ritual's energy to free it"
        menu:
            "(Act) Purify the spirit and the forest":
                n "The princess channeled her magic, focusing the ritual's energy into a cleansing light. She could feel the pain and suffering that had twisted the spirit, and she willed the magic to heal the wounds that had festered for so long."
                p "Let this be the end of your torment. Find peace, and let the forest be whole again."
                n "The spirit's form wavered, its rage dimming as the light washed over it. For the first time, there was no malice in its voice-only a weary acceptance."
                vs "Peace... at last. Guard this forest well, so that it never knows such pain again."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "As the spirit faded into the earth, the forest came alive with renewed energy. The trees stood taller, their leaves glowing with vibrant colors as life returned to the land."
                n "The princess and hero knew they could not return to the kingdom-they were bound to this forest now, its protectors and stewards."
                n "Together, they vowed to safeguard the balance the spirit had once sought to preserve, ensuring that no harm would befall the forest again."
                n "And the princess and hero lived happily ever-"

                jump forest_protectors
            "(Act) Teleport away while it's distracted":
                n "The princess saw an opening-one final chance to escape before the spirit's wrath closed in. Her magic flared as she reached out, pulling the hero to her side."
                p "We can't win this battle, but we can still get out of here. Hold on tight!"
                n "With a surge of energy, she activated a teleportation spell, whisking them away just as the spirit lunged forward in a final, futile attempt to claim them."
                vs "You cannot run forever..."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen
                n "The forest was left behind as the princess and hero reappeared on the edge of the kingdom. Though they had escaped with their lives, they knew they could never return to the kingdom-the magic they used was no longer welcome there."
                n "Instead, they chose a simpler life, free from the kingdom's expectations and the forest's dangers. Together, they embraced a future of freedom, far from the battles that once defined them."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after

    
    label vs_who_are_you:
        p "Who are you? What keeps you tied to this place?"
        n "The air grew heavy, the Vengeful Spirit's voice echoing like a mournful wail carried by the wind."
        vs "Who am I? I am the remnant of agony, the embodiment of all who were wronged by your kind."
        vs "I am vengeance given form-a force born from the sorrow and hatred that you, and those like you, have sown in this forest."

        return

    label vs_why_do_you_seek:
        p "Why do you seek vengeance? What do you hope to gain from all this?"
        n "The Vengeful Spirit's voice was laced with bitter resentment, each word dripping with malice."
        vs "Vengeance is not something I seek-it is all that I am. My purpose is to repay suffering with suffering, to make those who took from the forest feel the same anguish they inflicted."
        vs "There is no gain, no peace-only the cycle of pain that must be completed."

        return

    label vs_can_you_ever:
        p "Can you ever be at peace? Is there no end to your suffering?"
        n "A sorrowful whisper filled the air, tinged with regret and despair."
        vs "Peace? There is no peace for something like me. I am bound to this place, sustained by the rage that created me."
        vs "The forest still bleeds from wounds that have not healed. Until that pain fades, I will remain-caught between life and death, forever haunted by what was lost."

        return

    label vs_what_do_you:
        p "What do you want from us? Why do you target us specifically?"
        n "The forest seemed to groan in response, the Vengeful Spirit's voice barely above a whisper."
        vs "You carry the taint of the kingdom, the mark of those who desecrated what was pure. You may not bear the guilt, but you carry the stain."
        vs "I want you to feel the same fear and hopelessness that those who suffered felt. Your mere presence here disturbs the fragile balance I seek to restore."

        return

    label vs_why_do_you_blame:
        p "Why do you blame us for what the kingdom did? We're not the ones who hurt you."
        n "The Vengeful Spirit's voice crackled like brittle leaves, filled with bitter resolve."
        vs "You are part of the kingdom, are you not? The same kingdom that tore the heart from this forest, that exploited magic for greed and gain."
        vs "It matters not that you weren't there-it is your legacy that carries the burden. As long as the kingdom stands, so too will the sins it carries."

        return

    label vs_isnt_there_a:
        p "Isn't there a way to break this cycle of hatred? Does it have to end in more suffering?"
        n "A hollow laugh echoed in the distance, filled with hopelessness."
        vs "Break the cycle? The damage is already done. The forest remembers. It cannot forgive what was taken."
        vs "There is no salvation for those who carry the kingdom's blood. Only through destruction can the balance be restored, and only through pain can the forest find peace."
        
        return
    
    label vs_why_cant_you:
        p "Why can't you let go of your anger? The forest could heal if you did."
        n "The Vengeful Spirit's voice trembled, a mix of sorrow and fury woven into its tone."
        vs "Let go? The anger is all I have left. It's the only thing that keeps me from fading into nothingness."
        vs "The forest's wounds run deep, and my rage is a reflection of that pain. As long as the scars remain, so too will the hatred that keeps me bound to this place."
        
        return

    label vs_do_you_not:
        p "Do you not see the destruction your rage is causing? You're only making things worse."
        n "The forest groaned under an unseen weight, the Vengeful Spirit's response heavy with bitterness."
        vs "Destruction? What I do is nothing compared to what the kingdom did. You think my actions are unjust, but they are only a fraction of the devastation wrought by your people."
        vs "If the forest must suffer further for balance to be restored, then so be it. There is no redemption without reckoning."

        return

    label vs_cant_you_find:
        p "Can't you find peace in the forest's renewal? Life is returning-why can't that be enough?"
        n "A soft, sorrowful whisper lingered in the air, as if the spirit itself was yearning for something lost."
        vs "Renewal? The forest's life ebbs and flows, but the scars remain beneath the surface. I am not part of that renewal-I am bound to the shadows left behind."
        vs "I cannot find peace in what grows above while the roots below remain poisoned by greed and betrayal."

        return

    label vs_what_will_you:
        p "What will you do if you destroy us? Will it really bring you satisfaction?"
        n "The wind howled softly, as if mourning the question itself."
        vs "Satisfaction? There is no satisfaction, only the fulfillment of what must be done. The kingdom took and took, leaving ruin in its wake. Ending you is just a small step in restoring balance."
        vs "But even that will not undo the past. It will only bring me a momentary relief-a fleeting reminder that justice, however twisted, was served."

        return

    label vs_will_your_vengeance:
        p "Will your vengeance ever be enough? Or will you just keep taking lives?"
        n "The Vengeful Spirit's voice wavered, a rare hint of doubt creeping through its wrath."
        vs "Enough? How can it ever be enough when the land remains scarred, when those who caused the suffering still draw breath?"
        vs "But you may be right...perhaps no amount of vengeance will truly mend what was broken. Yet it's the only purpose I have left-the only way I know to ensure the forest's pain isn't forgotten."

        return

    label vs_what_then:
        p "What happens after your vengeance is complete? Will the forest finally be at peace?"
        n "The forest fell silent for a moment, as if the spirit itself was unsure how to answer."
        vs "Peace...such a distant concept. The forest may heal in time, but I will not be here to see it. When my purpose is fulfilled, I will fade like mist at dawn."
        vs "Perhaps then, the forest will find its peace, even if I never will. But until that day comes, my rage will not rest."

        return
