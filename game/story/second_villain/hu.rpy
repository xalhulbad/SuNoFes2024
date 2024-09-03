# Contains the code associated with portion of the game related to the "hunter" second villain encounter.

# Default variables


# Flags for unlockable options
default hu_chose_who_are_you = False
default hu_chose_why_after_us = False
default hu_chose_kingdom_abolished_magic = False
default hu_chose_what_your_mission = False
default hu_chose_why_guard_forest = False
default hu_chose_how_become_hunter = False
default hu_chose_why_cant_let_us_pass = False
default hu_chose_have_you_always_been_alone = False
default hu_chose_how_long_been_here = False
default hu_chose_why_didnt_chase_us_before = False
default hu_chose_we_went_by_mistake = False

label hu_start:
    # Reset dialogue pool flags
    $ hu_chose_who_are_you = False
    $ hu_chose_why_after_us = False
    $ hu_chose_kingdom_abolished_magic = False
    $ hu_chose_what_your_mission = False
    $ hu_chose_why_guard_forest = False
    $ hu_chose_how_become_hunter = False
    $ hu_chose_why_cant_let_us_pass = False
    $ hu_chose_have_you_always_been_alone = False
    $ hu_chose_how_long_been_here = False
    $ hu_chose_why_didnt_chase_us_before = False
    $ hu_chose_we_went_by_mistake = False

    $ hu_times_gotten += 1
    
    # Leading text
    scene bg Villain with fade
    n "The forest's dense canopy loomed overhead as the princess and the hero cautiously moved forward, the familiar tension thickening the air. It felt as if the forest itself was holding its breath."
    n "The princess and hero could see the kingdom now, a sign that they were getting close."
    n "A twig snapped beneath the hero's foot, sending a flock of birds scattering into the sky. The sudden noise only served to heighten the tension between them."
    n "The hero tightened his grip on his sword, scanning the surroundings with a wary gaze. His instincts told him that danger was near, and he wasn't wrong."
    play music "audio/5 Second Villian 3.mp3" loop volume 1.0 fadein 0.5
    scene bg villain_far_hu with dissolve
    n "From the shadows, a figure emerged, cloaked in the dark hues of the forest."
    n "His presence was as ominous as ever, and the bow in his hand gleamed with a readiness that set both the princess and hero on edge."
    hu "You've ventured deep into the forest again. It seems you haven't learned your lesson."

    if hu_times_gotten == 1:
        pt "The Hunter again... I was hoping we wouldn't have to run into him a second time."
    
    elif hu_times_gotten == 2:
        pt "Another encounter with the hunter... Will things go differently this time?"

    else:
        pt "Let's just get this over with."

    scene bg villain_hero_facing_far_hu with dissolve
    n "The Hunter stepped closer, his movements deliberate and precise. The hero instinctively moved to place himself between the princess and The Hunter, ready to defend her with his life."
    h "Stay back, princess. We won't back down, but we don't want to fight."
    hu "How predictable. But the forest demands respect, and you are trespassing. Prepare yourselves-your choices have consequences."

    jump hu_choices_1

    # Level 1 of choice tree
    label hu_choices_1:
        # Initial branch
        menu:
            "(Act) Tell hero to brandish sword":
                scene bg villain_hero_sword_facing_far_hu with dissolve
                n "The princess signaled the hero, who drew his sword with a swift motion. The blade caught the moonlight, its sharp edge glinting dangerously."
                p "Stay sharp. He's not someone we can take lightly."
                h "Understood. I'll follow your lead."

                jump hu_choices_2_1

            "(Act) Try to reason with The Hunter":
                n "Stepping forward with careful intent, the princess raised her hand, hoping for a non-violent resolution. The forest stilled as she locked eyes with the figure."
                p "We don't have to be enemies. Let's talk first."
                h "Be careful, princess. He doesn't seem the type to listen."
                n "The Hunter's cold gaze remained fixed on them, his expression unreadable, as if calculating their every move."

                jump hu_choices_2_2


            # Dialogue pool options

            "(Inquire) Who are you?" if not hu_chose_who_are_you:
                $ hu_chose_who_are_you = True
                call hu_who_are_you
                jump hu_choices_1

            "(Inquire) Why are you after us?" if not hu_chose_why_after_us and hu_chose_who_are_you:
                $ hu_chose_why_after_us = True
                call hu_why_after_us
                jump hu_choices_1

            "(Inquire) The kingdom abolished its use of magic." if not hu_chose_kingdom_abolished_magic and hu_chose_why_after_us:
                $ hu_chose_kingdom_abolished_magic = True
                call hu_kingdom_abolished_magic
                jump hu_choices_1


            "(Inquire) What is your mission?" if not hu_chose_what_your_mission:
                $ hu_chose_what_your_mission = True
                call hu_what_your_mission
                jump hu_choices_1

            "(Inquire) Why do you guard this forest?" if not hu_chose_why_guard_forest and hu_chose_what_your_mission:
                $ hu_chose_why_guard_forest = True
                call hu_why_guard_forest
                jump hu_choices_1

            "(Inquire) How did you become The Hunter?" if not hu_chose_how_become_hunter and hu_chose_why_guard_forest:
                $ hu_chose_how_become_hunter = True
                call hu_how_become_hunter
                jump hu_choices_1


            "(Inquire) Why can't you just let us pass?" if not hu_chose_why_cant_let_us_pass:
                $ hu_chose_why_cant_let_us_pass = True
                call hu_why_cant_let_us_pass
                jump hu_choices_1

            "(Inquire) Have you always been alone?" if not hu_chose_have_you_always_been_alone and hu_chose_why_cant_let_us_pass:
                $ hu_chose_have_you_always_been_alone = True
                call hu_have_you_always_been_alone
                jump hu_choices_1

            "(Inquire) How long have you been here?" if not hu_chose_how_long_been_here and hu_chose_have_you_always_been_alone:
                $ hu_chose_how_long_been_here = True
                call hu_how_long_been_here
                jump hu_choices_1


            "(Inquire) Why didn't you chase us before?" if not hu_chose_why_didnt_chase_us_before:
                $ hu_chose_why_didnt_chase_us_before = True
                call hu_why_didnt_chase_us_before
                jump hu_choices_1

            "(Inquire) We went there by mistake. We meant no harm!" if not hu_chose_we_went_by_mistake and hu_chose_why_didnt_chase_us_before:
                $ hu_chose_we_went_by_mistake = True
                call hu_we_went_by_mistake
                jump hu_choices_1


    # Level 2 of choice tree
    label hu_choices_2_1:
        # Branching from "(Act) Tell hero to brandish sword"
        menu:
            "(Act) Charge at The Hunter":
                n "The hero tightened his grip on the sword, heart pounding as he prepared to rush forward."
                p "Go for it! We'll create an opening!"
                scene bg villain_hero_charging_far_hu with dissolve
                n "With a fierce cry, the hero charged at The Hunter."
                n "But as he closed in, The Hunter moved with inhuman speed, dodging the strike effortlessly. The hero's momentum carried him forward, causing him to stumble."
                scene bg villain_hero_sword_facing_far_hu with dissolve
                n "Before he could recover, The Hunter struck, sweeping the hero's legs out from under him and sending him crashing to the ground."
                hu "Predictable."
                n "The Hunter's voice was a cold whisper, almost mocking. However, the hero quickly rolled back to his feet, gritting his teeth as he prepared for another attempt."
                n "The princess remained alert, scanning the surroundings for a way to turn the tide."

                jump hu_choices_3_1

            "(Act) Wait for him to make a move":
                n "The princess held her breath, signaling the hero to wait. The tension between them and The Hunter was palpable, like a taut wire ready to snap."
                h "He's watching us closely. Be ready."
                n "The Hunter stood motionless, his eyes never leaving the pair. Suddenly, he notched an arrow in one smooth motion. The hero barely managed to raise his shield in time, deflecting the deadly shot."
                hu "Hesitation is fatal in the forest."
                n "The princess could feel the weight of The Hunter's stare, his posture calm yet ready to strike at any moment. They needed to decide their next move before he acted again."

                jump hu_choices_3_2

            
            # Dialogue pool options

            "(Inquire) Who are you?" if not hu_chose_who_are_you:
                $ hu_chose_who_are_you = True
                call hu_who_are_you
                jump hu_choices_2_1

            "(Inquire) Why are you after us?" if not hu_chose_why_after_us and hu_chose_who_are_you:
                $ hu_chose_why_after_us = True
                call hu_why_after_us
                jump hu_choices_2_1

            "(Inquire) The kingdom abolished its use of magic." if not hu_chose_kingdom_abolished_magic and hu_chose_why_after_us:
                $ hu_chose_kingdom_abolished_magic = True
                call hu_kingdom_abolished_magic
                jump hu_choices_2_1


            "(Inquire) What is your mission?" if not hu_chose_what_your_mission:
                $ hu_chose_what_your_mission = True
                call hu_what_your_mission
                jump hu_choices_2_1

            "(Inquire) Why do you guard this forest?" if not hu_chose_why_guard_forest and hu_chose_what_your_mission:
                $ hu_chose_why_guard_forest = True
                call hu_why_guard_forest
                jump hu_choices_2_1

            "(Inquire) How did you become The Hunter?" if not hu_chose_how_become_hunter and hu_chose_why_guard_forest:
                $ hu_chose_how_become_hunter = True
                call hu_how_become_hunter
                jump hu_choices_2_1


            "(Inquire) Why can't you just let us pass?" if not hu_chose_why_cant_let_us_pass:
                $ hu_chose_why_cant_let_us_pass = True
                call hu_why_cant_let_us_pass
                jump hu_choices_2_1

            "(Inquire) Have you always been alone?" if not hu_chose_have_you_always_been_alone and hu_chose_why_cant_let_us_pass:
                $ hu_chose_have_you_always_been_alone = True
                call hu_have_you_always_been_alone
                jump hu_choices_2_1

            "(Inquire) How long have you been here?" if not hu_chose_how_long_been_here and hu_chose_have_you_always_been_alone:
                $ hu_chose_how_long_been_here = True
                call hu_how_long_been_here
                jump hu_choices_2_1


            "(Inquire) Why didn't you chase us before?" if not hu_chose_why_didnt_chase_us_before:
                $ hu_chose_why_didnt_chase_us_before = True
                call hu_why_didnt_chase_us_before
                jump hu_choices_2_1

            "(Inquire) We went there by mistake. We meant no harm!" if not hu_chose_we_went_by_mistake and hu_chose_why_didnt_chase_us_before:
                $ hu_chose_we_went_by_mistake = True
                call hu_we_went_by_mistake
                jump hu_choices_2_1

    label hu_choices_2_2:
        # Branching from "(Act) Try to reason with The Hunter"
        menu:
            "(Act) Appeal to The Hunter's morality":
                n "The princess softened her tone, hoping to reach some fragment of humanity in the steely-eyed figure before them."
                p "You don't have to do this. You must have reasons beyond violence. We can find another way."
                h "He might be more reasonable than he looks, but don't drop your guard."
                n "The Hunter's expression flickered, just for a moment. His grip on the bow tightened, but his gaze didn't waver."
                hu "Morality is for those who aren't bound by a mission. You misunderstand what drives me."
                n "The princess held her ground, uncertain if her words had made any impact or merely delayed the inevitable."

                jump hu_choices_3_3

            "(Act) Offer a bargain":
                n "The princess carefully chose her words, sensing that The Hunter was not driven solely by blind anger."
                p "There's no need for this to end badly for either of us. What if we made a deal instead?"
                n "The Hunter's gaze remained cold, though there was a flicker of curiosity beneath his hardened expression."
                hu "A deal, you say? And what could you possibly have to offer?"
                n "The princess met his eyes steadily, letting the weight of her resolve show."
                p "I'm sure there's something you want. Let's talk and see if we can reach an agreement."
                n "The Hunter was silent for a long moment, as if weighing her words carefully. His grip on his bow eased slightly, but his wariness remained."
                hu "You think you're clever, trying to bargain with me. I'll humor you-for now. Speak, and I'll consider what you have to say."
                n "The princess knew that she had his attention, but what she offered next would be crucial."     

                jump hu_choices_3_4


            # Dialogue pool options

            "(Inquire) Who are you?" if not hu_chose_who_are_you:
                $ hu_chose_who_are_you = True
                call hu_who_are_you
                jump hu_choices_2_2

            "(Inquire) Why are you after us?" if not hu_chose_why_after_us and hu_chose_who_are_you:
                $ hu_chose_why_after_us = True
                call hu_why_after_us
                jump hu_choices_2_2

            "(Inquire) The kingdom abolished its use of magic." if not hu_chose_kingdom_abolished_magic and hu_chose_why_after_us:
                $ hu_chose_kingdom_abolished_magic = True
                call hu_kingdom_abolished_magic
                jump hu_choices_2_2


            "(Inquire) What is your mission?" if not hu_chose_what_your_mission:
                $ hu_chose_what_your_mission = True
                call hu_what_your_mission
                jump hu_choices_2_2

            "(Inquire) Why do you guard this forest?" if not hu_chose_why_guard_forest and hu_chose_what_your_mission:
                $ hu_chose_why_guard_forest = True
                call hu_why_guard_forest
                jump hu_choices_2_2

            "(Inquire) How did you become The Hunter?" if not hu_chose_how_become_hunter and hu_chose_why_guard_forest:
                $ hu_chose_how_become_hunter = True
                call hu_how_become_hunter
                jump hu_choices_2_2


            "(Inquire) Why can't you just let us pass?" if not hu_chose_why_cant_let_us_pass:
                $ hu_chose_why_cant_let_us_pass = True
                call hu_why_cant_let_us_pass
                jump hu_choices_2_2

            "(Inquire) Have you always been alone?" if not hu_chose_have_you_always_been_alone and hu_chose_why_cant_let_us_pass:
                $ hu_chose_have_you_always_been_alone = True
                call hu_have_you_always_been_alone
                jump hu_choices_2_2

            "(Inquire) How long have you been here?" if not hu_chose_how_long_been_here and hu_chose_have_you_always_been_alone:
                $ hu_chose_how_long_been_here = True
                call hu_how_long_been_here
                jump hu_choices_2_2


            "(Inquire) Why didn't you chase us before?" if not hu_chose_why_didnt_chase_us_before:
                $ hu_chose_why_didnt_chase_us_before = True
                call hu_why_didnt_chase_us_before
                jump hu_choices_2_2

            "(Inquire) We went there by mistake. We meant no harm!" if not hu_chose_we_went_by_mistake and hu_chose_why_didnt_chase_us_before:
                $ hu_chose_we_went_by_mistake = True
                call hu_we_went_by_mistake
                jump hu_choices_2_2


    # Level 3 of choice tree
    label hu_choices_3_1:
        # Branching from "(Act) Charge at The Hunter"
        menu:
            "(Act) Strike with precision":
                n "The princess saw an opening and urged the hero forward."
                p "Focus! One clean strike!"
                scene bg villain_hero_charging_close_hu with dissolve
                n "The hero adjusted his grip, aiming for a precise blow to disarm The Hunter. But as the sword arced towards its mark, The Hunter's reflexes kicked in. He twisted away, the sword grazing his cloak but finding no flesh."
                scene bg villain_hero_sword_facing_far_hu with dissolve
                hu "Precision means nothing without timing."
                n "The hero cursed under his breath, realizing the gap in their skill." 
                n "The Hunter's counterattack was swift and decisive, leaving them once again on the defensive."
                
                jump hu_choices_4_1

            "(Act) Use the environment":
                n "The princess's eyes darted around the forest, searching for anything that could turn the tide."
                p "Use the trees! We need to get creative here."
                scene bg villain_far_hu with dissolve
                n "The hero took the hint, weaving between the thick trunks, trying to bait The Hunter into a disadvantage."
                n "The Hunter's gaze followed every move, unblinking and relentless. A snapped branch underfoot caused The Hunter to tense, his bow drawn with alarming speed."
                hu "The forest is mine, not yours."
                n "The words were barely spoken before an arrow streaked toward the hero. He narrowly dodged it, but it was clear-The Hunter's awareness of the terrain was far superior."

                jump hu_choices_4_2

    label hu_choices_3_2:
        # Branching from "(Act) Wait for him to make a move"
        menu:
            "(Act) Shoot an arrow":
                scene bg villain_hero_bow_aiming_far_hu with dissolve
                n "The princess nodded at the hero, and he swiftly readied an arrow. He pulled the bowstring taut, eyes focused on The Hunter."
                p "Aim true. We can't afford to miss."
                scene bg villain_hero_facing_far_hu with dissolve
                n "The hero loosed the arrow, but The Hunter moved like a shadow, evading the shot with barely a shift in his posture. The arrow embedded itself uselessly into a tree."
                hu "You'll have to do better than that."
                n "The Hunter remained poised, eyes cold and unreadable. The princess's mind raced-she knew they couldn't afford many more misses. What would be their next move?"

                jump hu_choices_4_3

            "(Act) Look for an escape route":
                n "The princess scanned the forest, searching for an opening. The Hunter's presence was unyielding, his gaze locked onto them like a predator."
                p "I see a way through, but it's tight. If we time it right, we can get out of here before he strikes again."
                h "We'll have to move fast if it comes to that. I'm ready when you are."
                n "The narrow path they spotted led deeper into the woods, offering a slim chance of escape." 
                n "The princess and hero exchanged a glance, knowing that taking the route could be risky but might be their best option if things got worse."

                jump hu_choices_4_4

    label hu_choices_3_3:
        # Branching from "(Act) Appeal to The Hunter's morality"
        menu:
            "(Act) Invoke his sense of duty":
                n "The princess's voice took on a firmer edge as she tried to reach The Hunter's sense of duty."
                p "You claim to be on a mission, but is it really worth losing yourself over? There's a higher path, a greater purpose."
                h "Even someone like him must have principles."
                n "The Hunter's eyes narrowed slightly, a flicker of something deeper beneath the cold exterior."
                hu "My duty is clear, and it is not swayed by ideals. You think words alone can change that?"
                n "There was no wavering in his stance, but the princess couldn't shake the feeling that some part of her message had reached him."

                jump hu_choices_4_5

            "(Act) Challenge his honor":
                n "The princess straightened, her voice sharp with defiance."
                p "You hide behind your mission, but what honor is there in slaughtering those who haven't wronged you? Is this really the legacy you want?"
                n "The Hunter's expression darkened, his grip tightening on his bow."
                h "Careful, princess. Pushing him might make things worse."
                hu "Legacy? I'm not concerned with such things. I do what must be done."
                n "The tension spiked as The Hunter's focus locked onto the princess. She had struck a nerve, but it was unclear whether that would lead to hesitation-or violence."

                jump hu_choices_4_6

    label hu_choices_3_4:
        # Branching from "(Act) Offer a bargain"
        menu:
            "(Act) Offer yourself in exchange":
                n "The princess took a bold step forward, raising her chin in defiance."
                p "Take me, then. Let the hero go. You've been watching us-surely you know I'm more valuable."
                n "The hero's eyes widened in alarm, but The Hunter simply tilted his head, considering her offer."
                hu "Bold, but foolish. Do you really place so little value on your own life?"
                n "His eyes were calculating, weighing the princess's resolve against his own motives."
                h "Don't do this! There's got to be another way!"
                p "We don't have time to argue! Let me handle this."
                n "The hero's hand tightened around his sword, ready to act if things went wrong. Despite his outward calm, The Hunter's expression hinted at a willingness to accept her proposal, though doubt and calculation lingered in his eyes."

                jump hu_choices_4_7

            "(Act) Promise him freedom in the kingdom":
                n "The princess took a step closer, her voice calm and persuasive."
                p "You don't have to be trapped out here. You could live freely in the kingdom. There's a place for someone like you, where you don't have to hunt or be hunted."
                h "Be cautious, princess. He's still dangerous, even if he listens."
                n "The Hunter's eyes narrowed, suspicion clear in his gaze."
                hu "The kingdom? A place where I'd be caged by rules and watched by those who don't understand me? You make an interesting offer, but I'm not one to trust so easily."
                n "Though skeptical, there was a flicker of interest in his voice. The princess could tell he was considering her words, even if his caution hadn't lessened."

                jump hu_choices_4_8


    # Level 4 of choice tree
    label hu_choices_4_1:
        # Branching from "(Act) Strike with precision"
        menu:
            "(Act) Disarm The Hunter":
                scene bg villain_hero_charging_far_hu with dissolve
                n "The hero lunged forward with renewed determination, aiming to knock the bow from The Hunter's grasp."
                scene bg villain_hero_facing_close_hu with dissolve
                n "The clash of movements was swift, but the hero ultimately lost his sword in the struggle."
                p "No!"
                n "Without his weapon, the hero would not be able to stand up to The Hunter. The situation was dire-the next decision would have to be quick and decisive."

                jump hu_choices_5_1

            "(Act) Strike and retreat":
                n "The princess and hero exchanged a glance-the situation was too dangerous for a prolonged fight. The hero shifted his stance, preparing to make one decisive strike before they made their escape."
                p "We can't keep this up. Strike now and pull back!"
                scene bg villain_hero_charging_far_hu with dissolve
                n "With a swift motion, the hero aimed a powerful blow at The Hunter, intending to create just enough distance to flee." 
                n "The Hunter's eyes flashed as he parried, but the hero's follow-up attack came swiftly. The princess prepared herself-the window to escape was small, and they had to act fast."

                jump hu_choices_5_2

    label hu_choices_4_2:
        # Branching from "(Act) Use the environment"
        menu:
            "(Act) Lure the Hunter into a trap":
                n "The princess's gaze darted across the clearing, spotting a potential area where they could set a trap. She quickly caught the hero's attention, gesturing subtly."
                p "Over there-we can lead him into a trap, but we have to work together."
                n "The hero nodded, immediately catching onto the plan. He shifted his stance, carefully maneuvering toward the spot. The Hunter remained focused on them, unaware that he was being led into a strategy."
                n "The groundwork was laid, but the trap itself wasn't ready yet. They would need to be precise in executing it."
                
                jump hu_choices_5_3

            "(Act) Create a distraction with magic" if chose_magic:
                n "The princess whispered under her breath, channeling magic into her fingertips. They needed to disorient The Hunter just enough to gain the upper hand."
                p "This will blind him for just a moment-be ready!"
                n "The hero tensed, preparing to act as soon as the spell was cast. The princess unleashed a burst of light, the energy flaring up between them and The Hunter."
                n "For an instant, The Hunter's vision was obscured, but the effectiveness of the tactic would only be clear once the light faded."

                jump hu_choices_5_4

    label hu_choices_4_3:
        # Branching from "(Act) Shoot an arrow"
        menu:
            "(Act) Nock another arrow":
                scene bg villain_hero_bow_aiming_far_hu with dissolve
                n "The hero quickly reached for another arrow, his focus narrowing on The Hunter. He knew the next shot had to be perfect-any hesitation could cost them."
                p "Be quick-he's already preparing!"
                n "The Hunter's speed was unreal. Before the hero could even draw back his bowstring, The Hunter had already notched an arrow of his own." 
                n "Both sides were poised to strike, eyes locked in a deadly standoff. The princess felt her pulse quicken-who would be first to release?"

                jump hu_choices_5_5

            "(Act) Switch to a different tactic":
                p "We need to change our approach! Go in close!"
                h "Got it-cover me!"
                scene bg villain_hero_sword_facing_far_hu with dissolve
                n "The hero charged in, sword drawn, attempting to engage The Hunter in melee combat. The princess stayed back, watching for an opening."
                scene bg villain_hero_charging_far_hu with dissolve
                n "The Hunter's eyes gleamed-he recognized the shift in their tactics and adjusted his stance, ready for the close-quarters battle that was about to begin."

                jump hu_choices_5_6

    label hu_choices_4_4:
        # Branching from "(Act) Look for an escape route"
        menu:
            "(Act) Escape using magic" if chose_magic:
                n "The princess's mind raced-there had to be a way to escape using the limited magic she had at her disposal. She whispered a quick incantation under her breath, preparing a spell that could teleport them out of danger."
                p "I can get us out of here, but we'll need to act fast!"
                h "I trust you-just give the signal!"
                n "The energy crackled at her fingertips as she visualized their escape. The Hunter remained focused, unaware of the spell building in the air around him. This was their moment, and they couldn't afford to miscalculate."

                jump hu_choices_5_7

            "(Act) Distract him":
                n "The princess leaned closer to the hero, her voice low and urgent as they devised a distraction."
                p "Pretend there's something else in the forest-something big. He won't ignore it."
                h "Let's go with a bear-he's got to take that seriously."
                n "The hero snapped a branch underfoot and rustled the leaves, making it seem like a large creature was approaching."
                h "Did you hear that? Could be a bear."
                n "The Hunter's eyes flicked toward the sound, his posture shifting as he assessed the situation. His attention wavered just long enough for the princess and hero to prepare their next move."

                jump hu_choices_5_8

    label hu_choices_4_5:
        # Branching from "(Act) Invoke his sense of duty"
        menu:
            "(Act) Remind him of his vows":
                n "The princess's voice rang out with conviction, aiming to reach whatever remnants of honor still lay buried within The Hunter."
                p "You took an oath once, didn't you? To protect, not destroy. Do those vows mean nothing to you now?"
                n "For a fleeting moment, The Hunter's gaze flickered with something almost like doubt. His grip on his weapon remained firm, but there was a faint hesitation-a crack in his icy resolve."
                hu "Vows... they were made for a different time. But you think words can bind me now?"
                n "The princess felt the shift in the air-she was close to breaking through, but whether it would be enough was still uncertain."

                jump hu_choices_5_9

            "(Act) Make him rethink his mission":
                n "The princess's voice softened, appealing to The Hunter's sense of purpose."
                p "You're on a mission, but have you ever questioned if it's really the right one? You don't have to follow orders blindly. There's still time to change."
                h "Even someone like him has to wonder if it's all worth it."
                n "The Hunter's eyes narrowed as he considered her words, his expression unreadable."
                hu "My mission... is all that I am. But there's doubt in every warrior's heart, isn't there?"
                n "The princess held her breath, sensing a moment of internal conflict within The Hunter. She could see it-the tension between his duty and the uncertainty lingering beneath the surface."

                jump hu_choices_5_10

    label hu_choices_4_6:
        # Branching from "(Act) Challenge his honor"
        menu:
            "(Act) Confront him about his methods" if not chose_magic:
                n "The princess took a step forward, her voice steady but edged with challenge."
                p "You hide behind this mission, but how does it feel to rely on tactics like ambushes and tricks? Is that really what you want to be known for?"
                n "The Hunter's expression hardened, his gaze locking onto hers with a dangerous intensity."
                h "Careful, princess. This is risky."
                hu "You question my methods? In a world where hesitation means death? I'll do what I must, regardless of what you think."
                n "The words carried the weight of finality, but there was undeniable tension. The princess's challenge had touched a nerve, and how The Hunter responded would shape the path ahead."

                jump hu_choices_5_11

            "(Act) Accuse him of cowardice":
                n "The princess's gaze sharpened, her voice cutting through the tension."
                p "You talk of honor, yet you hide in the shadows, afraid to face us directly. Is this how a true warrior acts?"
                n "The Hunter's grip tightened on his bow, anger flashing in his eyes."
                h "Princess, careful..."
                hu "You think I'm a coward? You know nothing of what it takes to survive in this forest."
                n "The air grew thick with tension, as The Hunter's fury ignited. The princess's words had struck deep, but it remained to be seen whether this would drive him to rash action or a more calculated response."

                jump hu_choices_5_12

    label hu_choices_4_7:
        # Branching from "(Act) Offer yourself in exchange"
        menu:
            "(Act) Sacrifice yourself" if not chose_magic:
                n "The princess took a deliberate step forward, her gaze never leaving The Hunter's. Each step was slow and measured, a show of her unwavering resolve."
                p "If this is what it takes to end this, then so be it."
                h "Don't do this! We can find another way!"
                n "The hero's protest fell on deaf ears as the princess continued her approach. The Hunter watched her closely, his eyes narrowing with both suspicion and curiosity."
                n "The air was thick with tension, the outcome of her sacrifice still hanging in the balance."

                jump hu_choices_5_13

            "(Act) Feign submission and use magic" if chose_magic:
                n "The princess's gaze didn't waver as she let out a breath, lowering her hands in a calculated gesture of surrender."
                p "If you want me, then take me. But there's more at play here than you realize."
                n "The hero's grip tightened on his weapon, eyes filled with worry, but he held back, trusting that the princess had a plan. The Hunter watched her with calculating eyes, still wary of deception."
                hu "You think I can't see through your games? But I'm willing to see where this goes."
                n "The stage was set, and the tension was razor-sharp. The princess's gambit could either work in their favor or end in disaster-what happened next depended entirely on her next move."

                jump hu_choices_5_14

    label hu_choices_4_8:
        # Branching from "(Act) Promise him freedom in the kingdom"
        menu:
            "(Act) Convince him to abandon his mission" if not chose_magic:
                n "The princess's voice was steady, each word carefully chosen to plant a seed of doubt in The Hunter's mind."
                p "You've lived alone out here for so long, bound by this mission. But it doesn't have to be that way. In the kingdom, you could have freedom and purpose beyond just hunting."
                h "He's listening, princess. Keep going."
                n "The Hunter's eyes narrowed, suspicion still etched in every line of his face, but there was also a spark of curiosity."
                hu "Freedom and purpose? You speak as if those things are within my reach. But I've seen what the kingdom offers-can it truly be so different now?"
                n "His skepticism remained, but the princess could tell that the idea of a life beyond the forest had taken root, even if just barely. How she proceeded would determine if that seed would grow-or be crushed."

                jump hu_choices_5_15

            "(Act) Betray him":
                n "The princess leaned in toward the hero, her voice a whisper."
                p "We'll play along for now, but when the time's right, we'll turn the tables."
                h "Understood. I'll be ready when you are."
                n "The Hunter remained unaware of their whispered plan, his attention still focused on the offer of freedom in the kingdom."
                n "The princess's decision to betray him was a dangerous gamble, but it was one she was willing to take if it meant achieving their goal."

                jump hu_choices_5_16


    # Level 5 of choice tree
    label hu_choices_5_1:
        # Branching from "(Act) Disarm The Hunter"
        menu:
            "(Act) Use the hero's sword":
                n "The Hunter's focus was entirely on the hero, oblivious to the princess's presence. She knew that this was her moment to act."
                p "I won't let you harm him. This ends now."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero's sword gleamed as the princess grasped it, the weight unfamiliar in her hands but her resolve unwavering."
                n "The princess's strike was swift and true. The Hunter fell lifeless to the forest floor, his threat extinguished."
                n "With the danger passed, the princess immediately turned her attention to the hero, tending to his wounds with the care and urgency of someone who had nearly lost everything."
                n "In the quiet aftermath, the forest seemed to breathe again, its oppressive grip finally released."
                n "The princess and the hero, having survived the ordeal, would soon return to the kingdom. There, they would heal, their bond strengthened by the trials they had faced together."
                n "And the princess and hero lived happily ever-"

                jump saved_hero

            "(Act) Fire a spell at the hunter" if chose_magic:
                n "The princess, seeing her chance, summoned the dark energy within her, channeling it into a powerful spell."
                n "His entire attention being on the hero, the Hunter didn't see the magic coming."
                p "This ends now!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The spell struck The Hunter with unrelenting force, the dark energy crackling through his body. But as the magic surged, tendrils of it lashed out unpredictably, striking the hero as well."
                n "The Hunter fell lifeless to the forest floor, his grip on the hero finally released. But the victory was short-lived."
                n "The hero, now tainted by the dark magic, gasped in pain as the corruption took hold, twisting his body and mind in monstrous ways."
                n "His eyes met the princess's, filled with both agony and determination."
                n "Desperate to save her, the hero fought against the transformation. But the corruption was relentless, warping his flesh and thoughts with each passing moment."
                n "In one final act of love, he raised his sword, and before the darkness could consume him fully, he plunged the blade into his own heart."
                n "The hero's body crumpled, the forest falling silent once more. The princess could only watch, her heart breaking as she knelt beside him, powerless to stop the inevitable."
                n "The forest, once again, claimed another victim to its dark magic, leaving the princess alone with her grief."
                n "Still, the princess was now free from the threat of The Hunter, and would be able to continue her life in peace."
                n "And the princess lived happily ever-"

                jump corrupted_hero

    label hu_choices_5_2:
        # Branching from "(Act) Strike and retreat"
        menu:
            "(Act) Deal a decisive blow and escape":
                n "The hero and princess exchanged a glance, understanding the urgency of the moment. With a determined nod, the hero tightened his grip on the sword, knowing this strike could be their last chance to turn the tide."
                p "Now, while he's off balance-go for it!"
                n "The hero lunged forward, his blade aimed at The Hunter's exposed side. The strike was clean, precise, and it sent The Hunter staggering back."
                scene bg villain_hero_charging_far_hu
                n "But the hero didn't linger. He swiftly retreated, grabbing the princess's hand as they bolted for the cover of the dense trees."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The blow had been enough to incapacitate The Hunter, giving the princess and hero the precious seconds they needed to escape."
                n "As they fled deeper into the forest, The Hunter's strength waned, and he eventually succumbed to his injuries, leaving the forest at peace once more."
                n "The princess and hero emerged from the forest, their bond stronger and their path clear. The princess, now with a newfound sense of purpose and courage, would rise to her predestined role of becoming queen."
                n "Together with the hero, who she knew would be her lifelong partner, she would guide the kingdom through the uncertainty ahead, her ascent to the throne marking the beginning of a new era."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne

            "(Act) Strike with magic and escape" if chose_magic:
                n "As they prepared to retreat, the princess called upon her magic, her hands glowing with dark energy. She knew this would be their last chance to escape, but the cost would be great."
                p "This is our only shot-stay close!"
                n "The hero nodded, understanding the risk as the princess unleashed the magic. The dark energy surged toward The Hunter, catching him off guard and sending him reeling."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "But as the spell hit its mark, a portion of the dark magic arced back, striking the hero as they fled."
                n "The magic worked, paralyzing The Hunter so that he could no longer fight, but the unintended side effect was devastating."
                n "The hero, corrupted by the dark magic, felt his body twisting, transforming into something monstrous."
                n "His once-strong resolve crumbled under the weight of the corruption, his thoughts darkening as the magic consumed him."
                n "The princess, realizing too late what had happened, watched in horror as the hero struggled against the transformation."
                n "In his final act of love and desperation, the hero ended his life before the darkness could fully claim him, sparing the princess from the monster he was becoming."
                n "The dark magic had claimed yet another of its victims. Despite this, the threat of The Hunter was finally gone, and the princess would surely be able to move on."
                n "And the princess lived happily ever-"

                jump corrupted_hero

    label hu_choices_5_3:
        # Branching from "(Act) Lure the Hunter into a trap"
        menu:
            "(Act) Use a snare trap" if not chose_magic:
                n "The princess spotted an exposed root system nearby-an ideal spot to set a snare. She signaled to the hero, who nodded in understanding."
                n "With careful, deliberate steps, the hero maneuvered The Hunter toward the trap."
                p "Lead him this way-this is our chance!"
                n "The hero feigned retreat, drawing The Hunter closer until the snare was in place."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The moment The Hunter stepped into the trap, the roots tightened around his legs, causing him to stumble."
                n "The trap had caught The Hunter off guard, but his strength was greater than they anticipated. In his final moments of desperation, The Hunter broke free, delivering a fatal blow to the hero."
                n "With The Hunter's final breath, he shot one last arrow straight at the princess's heart. However, the hero, knowing this was his end, jumped in front of the princess, sacrificing himself for good to block the arrow."
                n "The princess, filled with grief, knelt beside the hero as his life slipped away. The forest grew eerily quiet, as if mourning the loss of the hero who had fought so valiantly."
                n "With The Hunter dead, the princess was finally at peace, but the price was a heavy one. The princess would carry the weight of the hero's sacrifice with her as she returned to the kingdom alone."
                n "Nevertheless, she would surely have to move on, even if the hero could not be there with her."
                n "And the princess lived happily ever-"

                jump sacrificed_hero

            "(Act) Trap him using magic" if chose_magic:
                n "With a quick incantation, the princess summoned the power of the forest to her aid. The magic flowed through her, and she directed it toward The Hunter, crafting an arcane trap that would hold him fast."
                p "The forest itself will be your prison!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The magic weaved through the air, surrounding The Hunter in glowing, ethereal chains. He struggled, but the bindings were too strong, tightening around him with each attempt to break free."
                n "The enchanted bindings held The Hunter with unyielding strength, rendering him powerless as he slowly suffocated until he could no longer breathe."
                n "With The Hunter dead, the tension seemed to lift as the threat was neutralized. The princess and hero, exhausted but victorious, left The Hunter's body behind them, the weight of their journey beginning to ease."
                n "As they emerged from the trees, they knew their path forward was clear. The princess would explore the world together with the hero, no longer bound by rules and expectations."
                n "The princess and hero would live a life together in peace, away from the kingdom that rejected the magic that saved them from The Hunter."
                n "The bonds they forged in the forest would guide them through the challenges that lay ahead, and they would face them side by side."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after

    label hu_choices_5_4:
        # Branching from "(Act) Create a distraction with magic"
        menu:
            "(Act) Use a flashy spell to blind him":
                n "The princess whispered an incantation, focusing on a spell that would create a burst of light bright enough to blind The Hunter. As the energy gathered in her hands, she glanced at the hero, who was ready to strike."
                p "This will give us the opening we need-be ready!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "With a swift motion, the princess released the spell. A brilliant flash of light exploded in front of The Hunter, blinding him for good."
                n "The spell worked perfectly, leaving The Hunter unable to see. As he stumbled, the hero took the opportunity to strike, knowing that The Hunter would struggle to fight back without his incredible vision."
                n "Disoriented and helpless, The Hunter collapsed as the hero struck him, his life slipping away as the magic faded."
                n "With the threat finally eliminated, the princess and hero took a moment to catch their breath. The forest, once thick with tension, seemed to relax as the danger passed."
                n "The path forward was clear-they would leave behind the life of duty and expectations that awaited them in the kingdom."
                n "Instead, they would seek out a new life, guided by the magic that had saved them and the bond that had grown between them."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after

            "(Act) Start a fire to get his attention":
                n "The princess scanned the surroundings, her eyes landing on a patch of dry underbrush. Summoning a small flame, she carefully fed it until it grew, knowing the fire would spread quickly and draw The Hunter's attention."
                p "This will create the distraction we need-be ready to move!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The flames caught instantly, spreading with alarming speed through the dry forest. The Hunter turned, his focus shifting to the growing inferno, just as the princess had hoped."
                n "The fire spread rapidly, consuming the forest in its wake. The Hunter, distracted by the flames, was caught in the blaze and perished as the fire raged on."
                n "But the flames, fueled by careless magic, unleashed an ancient, dark force that had been long dormant beneath the forest floor."
                n "The forest became twisted, corrupted by the destructive power they had unleashed."
                n "As the flames died down, the princess and hero found themselves bound to the now-cursed forest, their lives intertwined with the land they had scarred."
                n "The weight of their mistake was heavy, but they vowed to learn from their carelessness."
                n "Instead of despair, they resolved to protect what was left of the forest, to nurture and heal the land they had inadvertently harmed."
                n "Though they could never leave, they would strive to be better, living with the consequences of their actions and dedicating themselves to the forest's recovery."
                n "And the princess and hero lived happily ever-"

                jump forest_curse
    
    label hu_choices_5_5:
        # Branching from "(Act) Nock another arrow"
        menu:
            "(Act) Jump in front of the hero":
                n "The hero notched another arrow, his eyes locked on The Hunter as he prepared to release. But the princess noticed something-the glint of The Hunter's arrow already aimed directly at the hero."
                p "No!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "Without hesitation, the princess threw herself in front of the hero, shielding him with her own body just as The Hunter's arrow was released."
                n "The arrow struck true, embedding itself deep into the princess's chest as she fell to the ground."
                n "The hero's arrow, fired in that same instant, struck The Hunter, who collapsed as well, finally defeated. The forest grew eerily silent, the echoes of battle fading into nothingness."
                n "The hero knelt beside the princess, his heart breaking as her life slipped away. The princess, with her final breath, knew that her sacrifice had saved him, and that was all she had ever wanted."
                n "Though the hero was now free from The Hunter's wrath, he would carry the weight of her sacrifice for the rest of his days. She had ensured his safety at the cost of her own life, a choice made out of pure love and selflessness."
                n "The hero would eventually move on, knowing exactly what he would do if the same situation ever happened again."
                n "He would not hesitate to give up his life for someone he cared about, just as the princess had selflessly done for him."
                n "And the hero lived happily ever-"

                jump sacrificed_princess

            "(Act) Light the area on fire with magic" if chose_magic:
                n "As the hero prepared another arrow, the princess realized they needed a more drastic measure. Summoning her magic, she focused on the area around them, whispering an incantation that would ignite the forest floor."
                p "This will buy us time-brace yourself!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "Flames erupted around them, spreading rapidly through the underbrush. The Hunter, caught off guard, faltered as the fire closed in, surrounding him in a ring of flames."   
                n "The fire spread quickly, fueled by the dry wood and leaves. The Hunter, distracted by the flames, was consumed by the blaze, leaving only ashes behind."
                n "But the fire's destruction didn't end there. The flames unleashed a dark, ancient magic buried deep within the forest, corrupting the land and binding the princess and hero to the twisted remnants of what once was."
                n "Realizing their mistake, the princess and hero vowed to atone for their carelessness."
                n "They would remain in the cursed forest, not as rulers, but as its guardians, dedicating their lives to restoring what they had damaged."
                n "Though they were trapped, they resolved to learn from their past, striving to be better stewards of the land that now held them."
                n "And the princess and hero lived happily ever-"

                jump forest_curse

    label hu_choices_5_6:
        # Branching from "(Act) Switch to a different tactic"
        menu:
            "(Act) Charge at him with sword":
                n "The hero realized that their current approach wasn't enough. Lowering his bow, he drew his sword and looked to the princess."
                p "We have to take him down directly. Stay close!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "With a nod, the hero charged at The Hunter, his sword aimed for a decisive strike. The Hunter, caught off guard by the sudden shift, barely had time to react."
                n "The hero's strike was swift and true, cutting down The Hunter before he could launch another attack. With their enemy defeated, the forest fell silent, the tension evaporating as quickly as it had come."
                n "The princess and hero, having survived yet another trial, knew their journey wasn't over."
                n "Together, they emerged from the forest, their bond unbreakable. The princess, her courage and strength tested, would soon rise to her rightful place as queen."
                n "With the hero by her side, she would guide the kingdom into a new era, her experiences in the forest shaping her rule with wisdom and resolve."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne

            "(Act) Try to use magic" if chose_magic:
                n "The hero hesitated, realizing that brute force wouldn't be enough. The princess, sensing the shift, began to channel her magic, her hands glowing with dark energy."
                p "I'll draw on the magic-we have no other choice!"
                n "As the princess unleashed her magic, The Hunter moved with inhuman speed, his arrow already aimed and released before she could react."
                n "The arrow struck the princess, piercing her heart as she fell to the ground, her magic dissipating."
                h "No!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "In a moment of sheer desperation, the hero rushed to her side. With The Hunter still advancing, the hero grasped the dark magic that lingered in the air, defying everything he knew."
                n "He channeled the forbidden power, using it to strike down The Hunter, who collapsed, lifeless, before he could claim another victim."
                n "The hero, driven by love and despair, did the unthinkable-he used the dark magic to resurrect the princess. As her life was restored, the forbidden act was complete, an act that defied the very laws of the kingdom."
                n "The princess awoke, her eyes meeting the hero's, filled with gratitude and love, but also with the weight of what had just transpired."
                n "Word of the hero's actions spread quickly. The kingdom, bound by its rigid principles, could not tolerate such defiance of nature."
                n "Despite the hero's noble intentions, the kingdom decreed his banishment, condemning him for using forbidden magic."
                n "The princess, desperate to stand by his side, tried to defy the kingdom's ruling, but her pleas fell on deaf ears."
                n "The princess would have to live the rest of her life alone in the kingdom, where they would constantly reinforce their ideals upon her."
                n "And the princess lived happily ever-"

                jump unfulfilled_love

    label hu_choices_5_7:
        # Branching from "(Act) Escape using magic"
        menu:
            "(Act) Teleport away using magic":
                n "The princess felt the magic surge through her as she focused on the spell that would teleport them both out of danger. The Hunter, relentless in his pursuit, was closing in quickly."
                p "Hold on to me-this is our only way out!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero grabbed her hand just as the magic activated, a bright light enveloping them both as the spell took effect. In an instant, they vanished from the forest, leaving The Hunter grasping at empty air."
                n "The teleportation spell had worked flawlessly, transporting the princess and hero far beyond The Hunter's reach. They reappeared in a tranquil meadow, the danger of the forest left far behind."
                n "The princess and hero, now free from the kingdom's expectations and the forest's dangers, found themselves in a place where they could truly begin anew."
                n "Together, they made the choice to forge a life beyond the borders of the kingdom, embracing the freedom that came with leaving the past behind."
                n "The magic that had saved them became a part of their new life, guiding them as they explored the world and built a future free from the constraints of duty and tradition."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after

            "(Act) Light the trees on fire":
                n "With The Hunter closing in, the princess knew they needed a drastic distraction. She summoned her magic, focusing on the trees surrounding them, and whispered an incantation that would ignite the forest itself."
                p "We need to buy ourselves time-brace yourself!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The flames leaped to life, rapidly spreading through the dense underbrush. The Hunter, startled by the sudden inferno, was forced to step back, momentarily distracted by the growing blaze."
                n "The fire spread uncontrollably, consuming the trees and everything in its path. The Hunter, unable to escape the flames, was engulfed and destroyed, leaving only ashes in his wake."
                n "However, the fire's devastation did not stop there. The ancient forest, once a sanctuary, became corrupted by the dark magic that fueled the flames, binding the princess and hero to its charred remains."
                n "The princess and hero, realizing the magnitude of their mistake, vowed to make amends for the destruction they had caused."
                n "They chose to stay within the cursed forest, dedicating themselves to restoring what they had ruined, learning from their carelessness and striving to be better stewards of the land."
                n "Though they could never leave, they found purpose in their new role, determined to protect and heal the forest they had nearly destroyed."
                n "And the princess and hero lived happily ever-"

                jump forest_curse

    label hu_choices_5_8:
        # Branching from "(Act) Distract him"
        menu:
            "(Act) Catch him off guard with magic" if chose_magic:
                n "The princess and hero whispered urgently to each other, devising a plan to catch The Hunter off guard. The princess began to gather her magic, the energy crackling at her fingertips as she prepared to strike."
                p "I'll distract him-be ready to move!"
                n "The hero nodded, positioning himself to take advantage of the moment. As the princess unleashed her magic, the energy surged toward The Hunter, who had barely noticed her spellcasting."
                n "But The Hunter moved faster than anticipated, dodging the attack and releasing an arrow that struck the princess down before she could react."
                h "No!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero, his heart breaking, watched as the princess fell. Desperation and grief flooded him as he rushed to her side. Ignoring the consequences, the hero grasped the remnants of the dark magic, using it to strike down The Hunter in a final, desperate act."
                n "The forbidden power consumed him, but he didn't care. He used the last of his strength to resurrect the princess, bringing her back to life."
                n "The hero's actions, born from love and despair, defied the kingdom's most sacred laws. Although he had saved the princess, the use of such forbidden magic came at a great cost."
                n "The kingdom, upon learning of his actions, decreed his immediate banishment, branding him as a threat to their way of life."
                n "The princess, though alive, was left to endure the kingdom's harsh judgment alone. Confined within its walls, she would face the rest of her days under the watchful eye of those who sought to break her spirit."
                n "And the princess lived happily ever-"

                jump unfulfilled_love

            "(Act) Escape while you can":
                n "The princess and hero exchanged a glance, realizing that their only chance of survival was to retreat. With The Hunter closing in, they made a split-second decision to escape into the thickest part of the forest."
                p "We need to get out of here-now!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero led the way, guiding the princess through the dense underbrush as The Hunter pursued them. They dodged arrows and leaped over obstacles, using every bit of their agility and cunning to stay ahead of their relentless foe."
                n "The chase was grueling, but eventually, they managed to lose The Hunter in the labyrinth of trees. As the forest grew quieter, they realized they had escaped his reach."
                n "The danger was behind them, but the lessons they had learned would stay with them forever. Emerging from the forest, the princess knew that she had been forever changed by the experience."
                n "Returning to the kingdom, the princess's newfound strength and resolve would guide her as she ascended to the throne."
                n "The hero, her loyal companion, stood by her side, ready to help lead the kingdom into a new era."
                n "Together, they would rule with wisdom and compassion, their bond unshaken by the trials they had faced."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne

    label hu_choices_5_9:
        # Branching from "(Act) Remind him of his vows"
        menu:
            "(Act) Change his mind about magic" if chose_magic:
                n "The princess's voice was firm as she tried to reach the humanity within The Hunter."
                p "You once had vows, principles you lived by. Think about what this mission is turning you into. Is the magic really something to fear, or could it be a force for good?"
                n "The Hunter's eyes narrowed, a cold resolve hardening his expression."
                hu "You're naive to think that magic can be anything but destructive. My mission is clear, and it won't be swayed by your words."
                n "The princess, sensing the danger, tried to react, but The Hunter was too fast. He released his arrow, the deadly projectile striking the princess before she could even raise her defenses."
                h "No!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero rushed to her side, his heart shattering as the princess collapsed. In his desperation, he grabbed hold of the dark magic that lingered in the air, channeling it to defeat The Hunter in a final, devastating blow."
                n "The hero's grief was all-consuming, and in his desperation, he did the unthinkable. Using the forbidden magic, he resurrected the princess, defying the natural order and the kingdom's most sacred laws."
                n "Though her life was restored, the cost was immense. The kingdom, learning of the hero's transgression, decreed his banishment."
                n "Despite the princess's pleas, she was confined to the kingdom's walls, forced to live under the oppressive gaze of those who sought to break her spirit."
                n "Their love, though powerful, was not enough to overcome the kingdom's rigid laws."
                n "The hero, exiled and alone, would never be able to return to the princess's side. The princess, left behind, would endure the rest of her days under the watchful eye of the kingdom, her heart heavy with the knowledge of what they had lost."
                n "And the princess lived happily ever-"

                jump unfulfilled_love

            "(Act) Create a path for his redemption" if not chose_magic:
                n "The princess took a step closer, her voice filled with compassion and resolve."
                p "There's still a chance for you to find redemption. You don't have to follow this path to its end. Let us help you."
                n "The Hunter's eyes flickered with something close to regret, but it was quickly replaced by cold resolve."
                hu "Redemption? It's too late for that."
                n "As The Hunter raised his bow, it was clear he had made his decision. He aimed directly at the hero, his intent lethal."
                p "No!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The princess, acting on pure instinct, threw herself in front of the hero just as The Hunter released his arrow. The arrow found its mark, piercing her heart."
                n "The princess's sacrifice was immediate and final. She crumpled to the ground, her life slipping away as the hero caught her in his arms."
                n "The Hunter, momentarily stunned by her selflessness, hesitated just long enough for the hero to deliver a final, fatal blow. The Hunter's life ended in that instant, but the cost was too great."
                n "The hero knelt beside the princess, his heart breaking as her final breath left her. Though The Hunter was defeated, the victory felt hollow."
                n "The hero would carry the memory of the princess's sacrifice with him for the rest of his life, her selfless act of love forever etched into his soul."
                n "The kingdom would mourn her loss, but her story would live on, inspiring those who heard it."
                n "And the hero lived happily ever-"

                jump sacrificed_princess

    label hu_choices_5_10:
        # Branching from "(Act) Make him rethink his mission"
        menu:
            "(Act) Change his mind about magic" if chose_magic:
                n "The princess's voice was gentle but firm, aiming to reach the part of The Hunter that still questioned his orders."
                p "You've been following orders for so long, but have you ever stopped to question if they're right? Magic isn't inherently evil-it's how we use it that matters."
                n "The Hunter's expression darkened, any hint of doubt crushed under the weight of his unwavering resolve."
                hu "Your words are meaningless. Magic is a curse, and you're foolish to think otherwise."
                n "The princess tried to react, but The Hunter was too quick. With lethal precision, he released an arrow that struck the princess down, her body crumpling to the ground."
                h "No!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero, consumed by grief and rage, acted without thinking. He grasped the dark magic that lingered in the air, using it to strike down The Hunter with a devastating blow."     
                n "In the aftermath, the hero did what the kingdom considered unforgivable-he used the dark magic to resurrect the princess, bringing her back from the brink of death."
                n "Though the princess's life was restored, the hero's defiance of the kingdom's sacred laws sealed his fate. He was banished, marked as a danger to their way of life."
                n "The princess, though alive, was confined to the kingdom, where she would live under constant scrutiny, her freedom taken from her as punishment for their defiance."
                n "The love between the princess and the hero was strong, but not strong enough to overcome the rigid laws that bound them. Separated by the kingdom's decree, they would live the rest of their days apart, their love unfulfilled."
                n "And the princess lived happily ever-"

                jump unfulfilled_love

            "(Act) Persuade him to leave the forest" if not chose_magic:
                n "The princess's voice softened, appealing to The Hunter's sense of reason."
                p "You don't have to keep fighting. There's a life beyond this forest, beyond these orders. You can choose to walk away."
                n "The Hunter's eyes narrowed, his anger flaring as he rejected her words."
                hu "You think I can just walk away? You know nothing of what I've sacrificed!"
                n "The hero stepped forward to intervene, but The Hunter, consumed by rage, turned his weapon on him, striking the hero down with a swift blow."
                h "Ugh...!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The princess's heart pounded as she saw the hero fall, wounded by The Hunter's attack. Without hesitation, she picked up a fallen branch, giving her the chance to act."
                n "The Hunter, focused on the hero, was oblivious to the princess's movement. She tightened her grip on the makeshift weapon and lunged forward, her determination unwavering."
                n "The princess's strike was precise and powerful, catching The Hunter off guard. He collapsed, lifeless, his threat extinguished at last."
                n "With the danger passed, the princess rushed to the hero's side, her hands trembling as she tended to his wounds with the care and urgency of someone who had nearly lost everything."
                n "In the quiet aftermath, the forest seemed to release its oppressive grip, the tension easing as peace returned."
                n "The princess and hero, having survived the ordeal, would soon leave the forest behind. Their bond, forged in the fires of battle, would guide them forward as they returned to the kingdom, knowing that together, they could face whatever came next."
                n "And the princess and hero lived happily ever-"

                jump saved_hero

    label hu_choices_5_11:
        # Branching from "(Act) Confront him about his methods"
        menu:
            "(Act) Make him doubt his actions":
                n "The princess's voice was steady, challenging The Hunter with a conviction that cut through the tension."
                p "You hide behind this mission, but have you ever stopped to think about what you're really doing? Is this the path you truly want to follow, or are you just afraid to change?"
                n "The Hunter's eyes narrowed, his anger boiling over. Before the princess could react, he struck out, injuring the hero with a swift, brutal attack."
                h "Ugh...!"
                n "The hero staggered back, clutching his wound as he fell to the ground. The princess's heart raced, fear and anger warring within her as she stood between The Hunter and the hero."
                p "Is this what you wanted? To hurt innocent people who were only trying to return home? You're no warrior-you're just a coward running from your own doubts!"
                n "The Hunter's expression faltered, her words piercing through his cold exterior. Doubt flickered in his eyes as he hesitated, the weight of her accusations sinking in."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "Seizing the moment, the princess reached for the hero's sword, her resolve hardening. The Hunter, lost in his own doubts, didn't react in time. With one swift motion, the princess struck, the blade finding its mark."
                n "The princess's strike was decisive, ending The Hunter's life before he could cause any more harm. The forest grew still as his body fell to the ground, the oppressive tension finally lifting."
                n "With The Hunter defeated, the princess immediately turned her attention to the hero, tending to his wounds with the care and urgency of someone who had nearly lost everything."
                n "As the danger faded, the princess and hero knew they had survived yet another trial together. Their bond, forged in the fires of battle, had only grown stronger."
                n "They would soon return to the kingdom, carrying with them the lessons learned and the unbreakable connection they shared."
                n "And the princess and hero lived happily ever-"

                jump saved_hero

            "(Act) Anger him":
                n "The princess's voice was sharp, her words meant to provoke rather than soothe."
                p "You think this makes you strong? Attacking those who haven't wronged you? You're nothing but a coward, hiding behind your mission because you're too afraid to face the truth!"
                n "The Hunter's eyes flashed with fury, her words piercing through the thin veneer of control he held. His grip on his weapon tightened as rage overtook him."
                hu "Enough! You don't know anything about me!"
                n "The Hunter, driven by anger, launched a reckless attack. The hero, realizing the danger, moved to intercept the blow, but The Hunter's strike was too swift and powerful."
                h "Get back!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero stepped in front of the princess, taking the brunt of the attack meant for her. With a final, desperate effort, he pushed The Hunter back, delivering a fatal blow even as he fell to the ground, mortally wounded."
                n "The hero's sacrifice was immediate and absolute. He gave his life to protect the princess, striking down The Hunter with a final act of courage. The forest fell silent, the echoes of battle fading into the stillness."
                n "The princess, heartbroken, knelt beside the hero as his life slipped away. The Hunter's threat was ended, but the cost was more than she could bear."
                n "Though she would eventually return to the kingdom, the memory of the hero's sacrifice would stay with her forever, a constant reminder of the love and loyalty that had defined their journey."
                n "And the princess lived happily ever-"

                jump sacrificed_hero

    label hu_choices_5_12:
        # Branching from "(Act) Accuse him of cowardice"
        menu:
            "(Act) Force him into a corner":
                n "The princess's voice rang out, sharp and accusing, as she stared down The Hunter."
                p "You call yourself a warrior, but all I see is a coward, too afraid to face his own doubts. You hide behind orders because you're too weak to think for yourself!"
                n "The Hunter's expression twisted with anger, her words cutting deep. His usual cold composure began to crack, replaced by a fierce, reckless determination."
                hu "I'll show you who's weak!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero, sensing the shift in The Hunter's demeanor, braced himself for the impending attack. The Hunter, driven by rage, charged forward, his actions fueled by the need to prove himself."
                n "The Hunter's reckless attack was his undoing. In his fury, he left himself vulnerable, allowing the hero to counter with a decisive strike."
                n "The Hunter fell, defeated by his own impulsive actions. The princess rushed to the hero's side, helping him to his feet, relief flooding her as the immediate danger passed."
                n "With The Hunter's threat eliminated, the princess and hero took a moment to recover. Their bond, tested by the trials they had faced, was stronger than ever."
                n "They knew that together, they could overcome any challenge. They would return to the kingdom, carrying the lessons they had learned in the forest with them."
                n "And the princess and hero lived happily ever-"

                jump saved_hero

            "(Act) Use magic to overpower him" if chose_magic:
                n "The princess's voice dripped with defiance, her words meant to provoke The Hunter."
                p "You think you're powerful? You think you can defeat us? You're nothing compared to the magic we wield!"
                n "The Hunter's eyes blazed with anger at her challenge, but before he could react, the princess began to channel the dark magic that lingered in the air."
                h "Princess, be careful!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "Ignoring the hero's warning, the princess unleashed the magic, directing it toward The Hunter. The dark energy overwhelmed him, his resistance crumbling under its sheer force."
                n "The magic worked, overpowering The Hunter and bringing him to his knees. But the victory came at a terrible price. The dark magic, wild and uncontrollable, arced back toward the hero, corrupting him in the process."
                n "His body began to twist and warp as the magic took hold, transforming him into something monstrous."
                n "The hero, realizing what was happening, fought against the transformation with all his strength. In a final act of love and desperation, he ended his life before the darkness could fully consume him."
                n "The princess, though free from The Hunter's threat, was left to face the world alone, the weight of the hero's sacrifice heavy on her heart."
                n "And the princess lived happily ever-"

                jump corrupted_hero

    label hu_choices_5_13:
        # Branching from "(Act) Sacrifice yourself"
        menu:
            "(Act) Give in to the Hunter":
                n "The princess's heart pounded as she stepped forward, her eyes never leaving The Hunter."
                p "If it's me you want, then take me. Just let him go."
                n "The hero's eyes widened in alarm, but the princess held up a hand, silencing him. She knew this was the only way to protect him, even if it meant sacrificing herself."
                n "The Hunter, his expression unreadable, lowered his weapon slightly as he considered her offer."
                hu "You would give your life for his? Foolish, but... noble."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The princess took another step forward, her resolve unwavering. As she approached The Hunter, he suddenly lunged forward, his intent lethal."
                n "The Hunter's strike was swift and deadly, ending the princess's life in an instant. She crumpled to the ground, her sacrifice complete."
                n "The hero, his heart breaking, could only watch as the life drained from her eyes. In a final, desperate act of love, the hero struck down The Hunter, ending the threat for good."
                n "But the victory was hollow, the cost too great."
                n "The princess's sacrifice would forever haunt the hero, a reminder of the love and courage she had shown in her final moments."
                n "And the hero lived happily ever-"

                jump sacrificed_princess

            "(Act) Feign surrender":
                n "The princess's gaze didn't waver as she let out a breath, lowering her hands in a calculated gesture of surrender."
                p "If you want me, then take me. But there's more at play here than you realize."
                n "The hero's grip tightened on his weapon, eyes filled with worry, but he held back, trusting that the princess had a plan."
                n "The Hunter watched her with calculating eyes, still wary of deception."
                hu "You think I can't see through your games? But I'm willing to see where this goes."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The princess waited for the right moment, her heart pounding as The Hunter drew closer. Then, with a sudden burst of movement, she grabbed the hero's sword and lunged at The Hunter, catching him off guard."
                n "The princess's attack was swift and deadly. The Hunter, caught by surprise, couldn't defend himself in time. Her blade struck true, ending his life before he could react."
                n "With The Hunter defeated, the princess turned to the hero, her breath coming in short gasps as the reality of what she had done settled in."
                n "Together, they would return to the kingdom, their bond stronger for having survived such a harrowing ordeal."
                n "The princess, having proven her courage and resolve, would soon rise to her rightful place as queen."
                n "And the princess and hero lived happily ever-"

                jump inherited_throne
    
    label hu_choices_5_14:
        # Branching from "(Act) Feign submission and use magic"
        menu:
            "(Act) Teleport away":
                n "The princess whispered a spell under her breath, channeling the magic that would transport them both far away from this place."
                n "The Hunter, unaware of her intentions, kept his focus on her, confident in his control over the situation."
                p "Just trust me-this will get us out of here."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero nodded, grabbing her hand as the magic began to swirl around them. With a flash of light, they vanished from the forest, leaving The Hunter grasping at nothing."
                n "The teleportation spell worked flawlessly, whisking the princess and hero far beyond The Hunter's reach. They reappeared in a peaceful glade, the dangers of the forest left far behind."
                n "The princess and hero, free at last from the threats that had pursued them, found solace in their newfound freedom."
                n "They would choose a life away from the kingdom, where they could live without the expectations that had once bound them."
                n "And the princess and hero lived happily ever-"

                jump happily_ever_after

            "(Act) Shoot a fireball at him":
                n "The princess's hands crackled with energy as she prepared to unleash a fireball. She knew this would be their last chance to escape, but the cost might be great."
                p "I'll distract him with this-be ready to move!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero watched with tense anticipation as the princess summoned the fireball, her focus intense. With a swift motion, she hurled the blazing projectile toward The Hunter, aiming to catch him off guard."
                n "The fireball exploded on impact, engulfing The Hunter in flames. The forest around them caught fire as well, the flames spreading rapidly through the dry underbrush."
                n "The Hunter, consumed by the fire, was destroyed, but the flames did not stop there. The fire, fueled by dark magic, unleashed an ancient curse that twisted the very fabric of the forest."
                n "The princess and hero, realizing their mistake too late, found themselves bound to the cursed forest. The dark magic they had used had become their prison, chaining them to the land they had unintentionally corrupted."
                n "Though they were trapped, they found purpose in their new role as guardians of the forest."
                n "And the princess and hero lived happily ever-"

                jump forest_curse

    label hu_choices_5_15:
        # Branching from "(Act) Convince him to abandon his mission"
        menu:
            "(Act) Offer a path to freedom outside the forest":
                n "The princess's voice was gentle, offering The Hunter a way out."
                p "You don't have to keep fighting. There's a life beyond this forest, a place where you can be free from all of this. You can leave this behind."
                n "The Hunter's expression twisted in anger, his eyes narrowing with fury."
                hu "Leave the forest? You don't understand anything! This forest is all I have!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The Hunter, consumed by rage at the thought of abandoning his mission and the only life he knew, swiftly turned his weapon on the hero, his intent deadly."
                n "As The Hunter released his arrow, the princess acted without thinking, throwing herself in front of the hero. The arrow struck her, its lethal force taking her down instantly."
                n "The princess's sacrifice was immediate and absolute. The arrow found its mark, ending her life in an instant."
                n "The hero, filled with grief and rage, struck down The Hunter in retaliation, ending the threat but at a price too heavy to bear."
                n "The hero knelt beside the fallen princess, her life slipping away as he held her close. Though The Hunter was defeated, the victory was hollow, the cost far too great."
                n "The hero would return to the kingdom, carrying the memory of her sacrifice with him for the rest of his life. For the rest of his life, he would remember the love and courage she had shown in her final moments."
                n "And the hero lived happily ever-"

                jump sacrificed_princess

            "(Act) Promise a new life, only to betray him":
                n "The princess's voice was smooth, weaving a vision of a new life that she never intended to fulfill."
                p "There's a place for you beyond this forest, where you can live freely. You don't have to keep following orders-there's a better life waiting for you."
                n "The Hunter's suspicion flickered, but the promise of freedom was tempting."
                hu "A new life... free from all of this?"
                n "The princess nodded, keeping her voice steady, even as she prepared for what must come next."
                p "Yes, but you have to trust me. Lower your weapon, and we can leave this place together."
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The Hunter hesitated, then slowly began to lower his weapon. The princess saw her chance and signaled to the hero, who struck swiftly, the blade cutting deep."
                n "The Hunter, realizing too late that he had been deceived, was mortally wounded. With his dying breath, he pulled an arrow from his quiver and aimed it at the princess."
                n "The hero, seeing The Hunter's final act of vengeance, moved without hesitation. He threw himself in front of the princess, taking the arrow meant for her."
                n "The Hunter's life ended as the hero collapsed, the arrow buried deep in his chest."
                n "The princess caught the hero as he fell, her heart breaking as his life slipped away. Though they had defeated The Hunter, the cost was too great."
                n "The hero's sacrifice would forever haunt the princess, a constant reminder of the love and loyalty that had defined their journey."
                n "His death would serve as a grim reminder to not let her guard down until the battle was truly over. She would return to the kingdom alone, carrying his memory with her always."
                n "And the princess lived happily ever-"

                jump sacrificed_hero

    label hu_choices_5_16:
        # Branching from "(Act) Betray him"
        menu:
            "(Act) Strike while he has his guard down":
                n "The princess and hero exchanged a subtle glance, knowing this was their moment to strike. The Hunter, lulled into a false sense of security, had let his guard down."
                p "Now, while he's distracted!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero moved swiftly, his blade flashing in the dim light of the forest. The strike landed true, mortally wounding The Hunter."
                n "But with his dying breath, The Hunter pulled an arrow from his quiver, aiming it at the princess."
                n "The hero, seeing the danger, acted without hesitation. He threw himself in front of the princess, taking the arrow meant for her."
                n "The Hunter's life ended as the hero collapsed, the arrow buried deep in his chest."
                n "The hero's life ended in that moment, his sacrifice securing The Hunter's defeat. The princess, heartbroken, knelt beside the hero's lifeless body, her grief overwhelming as the reality of what had transpired set in."
                n "The forest grew silent, the battle's echoes fading into nothingness."
                n "Though The Hunter was defeated, the price was too great. The hero's sacrifice would forever haunt the princess, a constant reminder of the love and loyalty that had defined their journey."
                n "His death would serve as a grim reminder to not let her guard down until the battle was truly over. She would return to the kingdom alone, carrying his memory with her always."
                n "And the princess lived happily ever-"

                jump sacrificed_hero

            "(Act) Turn the tables with a magic-assisted ruse" if chose_magic:
                n "The princess's voice was calm, her hands subtly gathering magic as she prepared to make her move."
                p "You've underestimated us. Now, you'll see the true power we wield."
                n "The Hunter's confidence faltered as the magic crackled in the air. The princess unleashed a spell, a dazzling display meant to disorient him, giving the hero the chance to strike."
                h "Now, while he's distracted!"
                if routes_completed + 1 in aware_hero_routes:
                    jump aware_hero
                scene bg blackscreen with fade
                n "The hero moved quickly, his blade aimed for The Hunter's heart. But as the magic swirled around them, something went wrong."
                n "The dark energy, wild and uncontrollable, arced back toward the hero, corrupting him in the process."
                n "The hero's strike landed, defeating The Hunter, but the victory came at a terrible cost. The dark magic took hold of the hero, twisting his form into something monstrous."
                n "He fought against the transformation, but it was too strong. In a final, desperate act of love, the hero ended his life before the darkness could fully consume him, sparing the princess from the monster he was becoming."
                n "The princess, now free from The Hunter's threat, was left to face the world alone, the weight of the hero's sacrifice heavy on her heart."
                n "The dark magic had claimed another victim, a harsh reminder of the dangers they had faced and the choices they had made."
                n "She would have to move on without the hero, his sacrifice a grim reminder of her choice to attempt to control forces beyond her understanding."
                n "And the princess lived happily ever-"

                jump corrupted_hero


    # Dialogue pool options

    label hu_who_are_you:
        p "Who are you? Why do you stalk us like this?"
        n "The Hunter's eyes narrowed, his expression unreadable as he responded."
        hu "I am the guardian of this forest, the one who ensures that its secrets remain untouched. I was once part of your kingdom, but I saw the truth behind its falsehoods. Now, I serve only the forest."

        return
    
    label hu_why_after_us:
        p "Why are you after us? We've done nothing to harm you."
        n "The Hunter's voice was cold, filled with barely restrained anger."
        hu "You carry the stench of the kingdom, a place that has abused the gifts of magic for far too long."
        hu "Whether you wield it or not, your presence here is a threat. I will not allow you to defile this forest as your kind has done before."

        return

    label hu_kingdom_abolished_magic:
        p "The kingdom no longer uses magic! They abolished it long ago. Why can't you let go of the past?"
        n "The Hunter's eyes narrowed, his expression hardening as he responded."
        hu "Abolished? Do you think that changes what your kingdom has done? The scars left by your people's greed are etched into the very bones of this forest. Magic was twisted, corrupted by those who sought power above all else."
        n "The Hunter's voice grew colder, his anger palpable."
        hu "Words and decrees mean nothing to me. You cannot erase the past with a simple law. The kingdom's sins cannot be undone, and I will never forgive those who bear its mark."
        hu "I will not allow your kind to tread where they do not belong."

        return

    label hu_what_your_mission:
        p "What is your mission?"
        n "The Hunter's gaze hardened, his words laced with a sense of duty."
        hu "My mission is simple-to protect the forest from all who would exploit it. I hunt those who threaten its balance, those who think they can take from it without consequence. You are no different."

        return

    label hu_why_guard_forest:
        p "Why do you guard this forest so fiercely? What's so special about it?"
        n "The Hunter's voice took on a reverent tone as he spoke of the forest."
        hu "This forest is sacred, a place where magic thrives in its purest form." 
        hu "Unlike your kingdom, which sought to twist and corrupt it for power, I guard it to preserve its beauty and ensure that it remains untouched by human greed."

        return

    label hu_how_become_hunter:
        p "How did you become The Hunter? Why take on this role?"
        n "The Hunter's voice was filled with conviction, as if he had made this decision long ago."
        hu "I chose this path when I saw what the kingdom was doing-abusing the magic that should have been revered. I could no longer stand by and watch as they twisted nature's gifts for their own gain." 
        hu "So, I left, vowing to protect the forest from all who would harm it. The title of 'Hunter' was not given to me; I took it upon myself to ensure that no one else would repeat the kingdom's mistakes."

        return

    label hu_why_cant_let_us_pass:
        p "Why can't you just let us pass? We're not here to harm the forest."
        n "The Hunter's expression darkened, his grip tightening on his weapon."
        hu "Let you pass? So you can return to your kingdom and bring others here, to exploit what remains pure?"
        n "No. The forest has suffered enough at the hands of your kind. I will not allow you to defile it further. Your journey ends here."

        return

    label hu_have_you_always_been_alone:
        p "Have you always been alone out here?"
        n "The Hunter's expression briefly softened, a hint of something unspoken in his gaze."
        hu "Alone? Perhaps. But solitude is a small price to pay for the peace this forest offers."
        hu "I walked away from the kingdom long ago, abandoning the lies they told. Here, I found purpose, even if it meant leaving everything behind."

        return

    label hu_how_long_been_here:
        p "How long have you been in this forest?"
        n "The Hunter seemed to ponder the question for a moment before answering."
        hu "Time... it's lost its meaning here. I have been here long enough to see the forest grow and change, long enough to witness the kingdom's rise and fall. The forest has become my life, and I will remain here until my last breath."

        return

    label hu_why_didnt_chase_us_before:
        p "Why didn't you chase us before? You could have stopped us then."
        n "The Hunter's gaze darkened, his expression unreadable as he responded."
        hu "I thought you were different, that perhaps you were not like the others. I saw something in you-a potential to walk away, to leave this forest unscathed and in peace. So I let you go, hoping you would not return."
        n "The Hunter's voice grew colder, his anger barely restrained."
        hu "But you proved me wrong. You ventured to the sacred place-a place where no outsider should tread. By doing so, you've shown your true nature, that you cannot be trusted."
        hu "I will not make the same mistake twice. You've crossed a line, and I will not allow you to leave this forest alive."

        return

    label hu_we_went_by_mistake:
        p "We didn't mean to go there! It was a mistake. We meant no harm!"
        n "The Hunter's eyes narrowed, his expression unyielding as he responded."
        hu "A mistake? Perhaps. But intent matters little now. The fact remains that you've seen the sacred place. Its power is beyond your understanding, and even a fleeting glimpse could tempt you to exploit it."
        n "The Hunter's voice hardened, filled with a deep-seated resolve."
        hu "Whether you meant harm or not, you've been exposed to something that should remain untouched by human hands. I cannot risk letting you leave, knowing what you've seen."
        hu "The magic of the forest is not yours to wield, and I cannot afford to let you live with that knowledge. I must protect the forest, even if it means ending your lives."

        return