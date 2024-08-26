# Contains the code associated with portion of the game related to the "cryptic stonehenge" scene.

# Default variables
default cryptic_choices1_seen = set()
default cryptic_choices1_chosen = 0

# Flags for unlockable options
default dml_lore_shown = False
default fh_lore_shown = False
default ff_lore_shown = False
default hu_lore_shown = False
default vs_lore_shown = False

default what_truths_checked = False
default stone_gravings_examined = False
default can_decipher_runes = False

label cryptic_start:
    n "The encounter with the shadowy figure left the princess and the hero with a feeling of determination as they continued to make their way deeper into the woods."
    n "The forest loomed tall and dark, its branches knitting together like gnarled fingers against the twilight sky. Each step they took was a reminder of the dangers that lay ahead. As the canopy opened, a glade revealed itself, bathed in an otherworldly glow."
    scene bg Cryptic with fade
    n "In the centre of the clearing stood a circle of ancient stones, each etched with runes that shimmered with a faint, iridescent light. The stones formed a boundary between the known world and the mysteries beyond, inviting the unwary to uncover their secrets."
    n "Here, in this sacred place, time felt suspended, and the air thrummed with an unspoken power. The princess and the hero paused at the edge of the stone circle, drawn to its enigmatic presence."
    p "It feels like we've stepped into another world. These stones... they're unlike anything I've seen before."
    h "There's something ancient about this place, something that reaches beyond time. Do you sense it too?"
    p "Yes, it's as if the stones are whispering secrets of the past, urging us to listen."
    n "As they walked among the stones, the ground beneath their feet seemed to pulse with a quiet energy. The princess felt a strange pull, an invisible thread connecting her to the heart of the circle."
    n "The air was thick with potential, as if waiting for a choice to be made. The light of the setting sun danced across the stone surfaces, illuminating symbols that promised knowledge and power to those brave enough to seek them."
    p "It's strange how familiar this place feels."
    h "Maybe it's fate guiding our steps. Either way, we should be cautious."
    p "Of course. But there's a reason we've been led here, and I intend to find out why."
    h "Then let's explore, but remember, some doors are better left unopened."

    $ cryptic_choices1_chosen = 0

    label cryptic_choices1:
        while cryptic_choices1_chosen < 3:
            $ cryptic_choices1_chosen += 1

            menu:
                set cryptic_choices1_seen
                # Tells renpy to hide choices in this set (prevents same option showing up twice)

                # Choices available from the start:
                "(Thought) What is this place?":
                    call cryptic_what_is_this
                    jump cryptic_choices1

                "(Thought) The air feels charged with an unfamiliar energy.":
                    call cryptic_air_feels_charged
                    jump cryptic_choices1
                
                "(Thought) What secrets are hidden here?":
                    call cryptic_what_secrets
                    jump cryptic_choices1

                "(Thought) I can feel something calling to me…":
                    call cryptic_i_can_feel
                    jump cryptic_choices1

                "(Thought) Can we find anything useful here?":
                    call cryptic_can_we_find
                    jump cryptic_choices1

                "(Act) Listen to the whispers of the stones" if (v_type == 'dml' and not dml_lore_shown) or (v_type == 'fh' and not fh_lore_shown) or (v_type == 'ff' and not ff_lore_shown) or (v_type == 'hu' and not hu_lore_shown) or (v_type == 'vs' and not vs_lore_shown):
                    call cryptic_listen_to_whispers
                    $ cryptic_choices1_seen.remove("(Act) Listen to the whispers of the stones") # We want this to possibly appear for other villain types
                    jump cryptic_choices1

                "(Act) Circle around the stones":
                    $ cryptic_choices1_seen.remove("(Act) Circle around the stones")

                    jump cryptic_circle_around_stones


                # Choices available after first route completed:
                "(Act) Haven’t we been here before?" if routes_completed > 0:
                    call cryptic_havent_we_been
                    jump cryptic_choices1

                "(Thought) What truths did I miss before?" if routes_completed > 0:
                    call cryptic_what_truths_did
                    jump cryptic_choices1

                "(Act) Examine the stone engravings" if routes_completed > 0 and what_truths_checked:
                    call cryptic_examine_stone_engravings
                    jump cryptic_choices1

                "(Act) Try to decipher the runes" if routes_completed > 0 and stone_gravings_examined:
                    call cryptic_try_to_decipher
                    jump cryptic_choices1

                "(Act) Focus on the largest stone" if routes_completed > 0 and stone_gravings_examined:
                    call cryptic_focus_on_largest
                    jump cryptic_choices1

                "(Thought) I remember the path I took before, do I dare to try a different one?" if routes_completed > 0:
                    call cryptic_i_remember_path
                    jump cryptic_choices1


                # Choices available after second route completed:
                "(Thought) Am I destined to repeat everything until I make the right choice?" if routes_completed > 1:
                    call cryptic_am_i_destined
                    jump cryptic_choices1

                "(Thought) Will I find the answers I seek this time?" if routes_completed > 1:
                    call cryptic_will_i_find
                    jump cryptic_choices1

                "(Thought) Could this be the key to breaking free from the endless cycle?" if routes_completed > 1:
                    call cryptic_could_this_be
                    jump cryptic_choices1

                "(Thought) The air seems heavier with each visit, as if the stones remember." if routes_completed > 1:
                    call cryptic_air_seems_heavier
                    jump cryptic_choices1
                
        # If we get here then the player did not choose "(Act) Circle around the stones" within 3 choices

        h "We shouldn't waste too much time here. Let's look around and see if we can find anything useful for the rest of the journey home."

        # Force player to choose "(Act) Circle around the stones"
        menu:
            "(Act) Circle around the stones":
                jump cryptic_circle_around_stones

    label cryptic_what_is_this:
        n "The princess stood at the edge of the stone circle, her eyes tracing the arc of ancient monoliths rising from the earth. Shadows danced across their surfaces, whispering tales of forgotten eras."
        n "Her heart thudded with a mix of awe and trepidation, a sense of familiarity tugging at the edges of her memory."

        if routes_completed > 0:
            pt "Could these stones hold the key to understanding this world... and my place in it?"
            n "The wind swirled gently, carrying with it the scent of moss and the crispness of the cold air. The princess felt a shiver run down her spine, a connection to the stones that defied logic yet felt utterly undeniable."

        n "The wind swirled gently, carrying with it the scent of moss and the crispness of the cold air. The princess felt a shiver run down her spine, a connection to the stones that defied logic yet felt utterly undeniable."
        return

    label cryptic_air_feels_charged:
        n "A palpable energy crackled in the air, as if the very essence of magic hung in invisible threads around them. The princess paused, closing her eyes to better sense the vibrations that hummed through her bones."
        pt "This energy... it's almost alive. I can feel it pulsing, waiting for someone to unlock its secrets."
        pt "What could this energy mean for us? With magic banished by the kingdom, is this energy a friend or foe in our quest?"
        n "As she opened her eyes, a flicker of light danced across the stones, momentarily illuminating the mysterious symbols etched into their surfaces."
        return

    label cryptic_what_secrets:
        n "The stones towered silently, guardians of untold secrets, their surfaces etched with cryptic symbols that seemed to shift and shimmer with every glance."
        n "The princess felt an irresistible pull toward them, as if they beckoned her to uncover the mysteries they guarded."
        pt "These stones must hold secrets beyond my imagination. But what price will they demand for their revelation?"
        n "She took a tentative step closer, the ground beneath her feet firm yet yielding, as though guiding her to the heart of the circle where knowledge awaited."
        return

    label cryptic_i_can_feel:
        n "A gentle yet insistent whisper threaded through the rustling leaves, weaving an invitation only the princess could hear. It spoke not in words, but in feelings and impressions, urging her to heed its call."
        pt "This call... it's as if the stones know me, as if they’re reaching out across the veil of time to connect with me."
        n "The pull grew stronger, resonating with the rhythm of her heart. She hesitated, caught between fear and curiosity, knowing that whatever lay ahead was woven into her destiny."
        return

    label cryptic_can_we_find:
        n "The promise of discovery shimmered in the air, mingling with the scent of moss and earth. The stones loomed, not as obstacles, but as keepers of potential answers, waiting to be unlocked."
        pt "Every journey needs tools, knowledge. Perhaps here lies something to aid us, to guide us on our quest."
        pt "In a world of mysteries, even the smallest clue could be the key to our freedom."
        return

    label cryptic_listen_to_whispers:
        if v_type == "dml":
            n "The air around the stone circle seemed to grow still, as if the very forest held its breath. A faint, ethereal whisper reached the princess, carrying with it a tale from long ago."
            voice "Once, a man of great intellect delved into the forbidden arts, seeking to harness powers beyond mortal ken. His ambition knew no bounds, for he believed himself destined to reshape the world."
            voice "Yet, in his quest for greatness, he ignored the signs—the withering leaves, the dying streams—as his unchecked magic drained the forest’s life."
            voice "Blinded by his own perceived heroism, he cast aside all warnings, seeing only his reflection in the mirror of power."
            voice "Every day, the forest grew weaker, a silent testament to the cost of his blind ambition. Despite his hubris leaving behind a barren land and a legacy of ruin, he continues to believe in his grand destiny."
            n "The whisper faded, leaving a sense of desolation in its wake. The stones seemed to mourn the loss of vitality, a silent testimony to the cost of hubris and unchecked ambition."
            $ dml_lore_shown = True

        elif v_type == "fh":
            n "A chill ran through the air as the princess felt a presence, a whisper carried by the wind. It was as if the forest itself was speaking to her, sharing a story etched in sorrow."
            voice "There once was once a valiant protector, a knight whose skill was unmatched, his loyalty unwavering. But betrayal came from within the very kingdom he swore to defend."
            voice "Falsely accused and cast out, his heart turned cold. The forest became his refuge, his training ground, as he vowed to exact vengeance on those who wronged him."
            voice "Now, the blade that once served justice is stained with bitterness, striking fear into the hearts of those who remind him of his betrayal."
            n "The stones seemed to echo with the knight’s sorrow and anger, their silent vigil a reminder of how loyalty can be twisted into vengeance."
            $ fh_lore_shown = True

        elif v_type == "ff":
            n "As the princess tuned into the subtle hum of the stone circle, a soft, insidious whisper filled her mind, laced with the sweet yet poisonous tone of intrigue."
            voice "There once served in the kingdom’s grand halls, a courtesan with a talent for uncovering secrets hidden behind closed doors. Her beauty masked a sharp mind, adept at uncovering secrets and wielding them as tools of influence."
            voice "With each whisper overheard, she grew bolder, weaving webs of manipulation among the kingdom’s elite. However, her machinations eventually caught up with her, leading to her exile."
            voice "Now, in the shadows of the forest, she continues her games, using her knowledge to break minds and spirits. The forest echoes with her laughter, sweet as honey, yet sharp as a dagger."
            n "The stones seemed to vibrate with a cunning energy, the forest around her whispering of the dangers of underestimating those who listen more than they speak."
            $ ff_lore_shown = True

        elif v_type == "hu":
            n "The princess felt a deep, resonant hum from the stones, as if the very earth was imparting its wisdom. A voice, steady and solemn, filled her thoughts."
            voice "In the depths of the forest, there dwelled a guardian, silent and steadfast. Once a protector, he vowed to preserve the sanctity of the wilds."
            voice "His arrows were swift and true, his silence a testament to his resolve. He believed that magic belongs to the earth and must not be abused by man, a creed that guided his every step."
            voice "He witnessed the encroachment of civilization, the exploitation of the forest's gifts, and grew disillusioned with mankind. Now, he hunts those who defile the natural order, seeing himself as the forest's avenger."
            n "The whisper faded, leaving behind a sense of reverence and caution. The stones seemed to share the hunter's belief, the air around them filled with the silent promise of protection."
            $ hu_lore_shown = True

        else:
            n "A cold breeze swept through the clearing, carrying with it a mournful whisper. The princess felt a shiver, as if the air itself was imbued with sorrow and rage."
            voice "Born from the anguish and wrath of those who suffered unjustly, a being lingered where the forest's magic was strongest. Once, this land was vibrant, filled with life and joy, until greed and misuse of magic drained its essence."
            voice "The forest responded, creating an entity that embodied its pain and anger. It seeked to punish those from the kingdom, those it holds responsible for the desecration."
            voice "It moved through the trees, unseen, possessing the living to exact its vengeance. Now, its presence is a warning, a reminder that nature’s gifts are not to be exploited."
            n "The stones felt cold under her touch, their surfaces seeming to pulse with a quiet fury. The forest around her rustled with a somber energy, a testament to the consequences of humanity's transgressions against nature."
            $ vs_lore_shown = True

        return

    label cryptic_circle_around_stones:
        n "The princess felt an inexplicable pull as she began to circle the ancient stones, her curiosity urging her to explore every corner of this mysterious place."
        n "As she moved around the perimeter, the soft crunch of leaves underfoot seemed to echo in harmony with the subtle hum of magic in the air."
        h "These stones seem to be guiding us, leading us somewhere. Do you sense it too?"
        p "Yes, there's a path here, like the stones are pointing us toward something... something important."
        n "As they continued their path around the circle, the gentle glow of a light caught the princess’s eye. Emerging from behind one of the larger stones stood a small pile of rubble, the remnants of a once majestic stone pillar."
        n "Atop the debris sat a glowing gem that seemed to pulse with an inner fire, the final remnant of an area that, for the longest time, bloomed with magic."
        p "Look over there, do you see it? That glowing gem on the rubble —it’s unlike anything I’ve ever seen."
        if routes_completed > 0:
            pt "Except not really. This gem again…"
        h "It’s beautiful, but I wonder what it means. Could it be the source of the magic we’ve been sensing?"
        p "Perhaps. It feels like it’s alive, humming with power. We need to take a closer look."
        menu:
            "(Act) Examine the glowing gem":
                n "As the princess examined the glowing gem, its radiant light seemed to draw her in, pulsing with a mysterious energy that hinted at the power it contained."
                n "The gem lay cradled atop the pillar, its glow casting intricate patterns on the stone circle around them."
                p "This gem is filled with destructive magic, the kind that we could use in case of any danger. But if we take it, we risk banishment from the kingdom forever."
                h "It’s true. The kingdom has outlawed magic for generations, fearing its power. Taking it could mean leaving behind everything we've ever known."
                p "Yet, this power could be exactly what we need to defend ourselves, especially if we encounter the shadowy figure again."
                p "They seemed dangerous the last time we encountered them, and magic could be our greatest ally if we were to face them again."
                n "The gem's glow seemed to intensify, a beacon of potential strength and danger. The forest whispered around them, its voice a mixture of temptation and caution, reminding them of both the promise and peril of the choice before them."
                p "Maybe if we use the gem only when necessary, we could find some forgiveness. If it saves us from danger, perhaps the kingdom will understand."
                h "Perhaps. Desperate times might call for desperate measures, but we must weigh the cost. Magic could save us or seal our fate."
                n "The princess felt the weight of this decision, her heart torn between the lure of power and the fear of exile. The gem offered strength and safety, but also the possibility of losing everything she had ever known."
                pt "A crossroads…"

                menu:
                    "(Act) Take the gem":
                        jump cryptic_take_gem
                    
                    "(Act) Leave the gem":
                        jump cryptic_leave_gem

    label cryptic_havent_we_been:
        p "Haven’t we been here before?"
        h "No, I don’t think so. I’ve only heard legends of these stones. Why, have you?"
        n "The hero glanced around, his expression one of mild curiosity and confusion. To him, this was just another stop on their journey, a mysterious place among many."
        p "It just feels familiar, like I've seen this place in a dream."
        pt "So he doesn’t remember this place. Strange. It’s as if the past never happened, but somehow I remember it."
        return

    label cryptic_what_truths_did:
        n "The princess paused, her gaze sweeping across the circle of stones as if seeing them anew. Each monolith stood as a sentinel, guarding the secrets of ages past, the stories they had shared, and those yet to be revealed." 
        n "Her heart beat with a rhythm that matched the pulse of magic in the air, a reminder of the wisdom she had glimpsed but not yet grasped."
        pt "I've been here before, but there’s so much I didn’t see. What truths lie hidden, waiting for me to uncover them?"
        n "The whispers of the forest seemed more urgent now, as if imploring her to delve deeper, to seek out the truths she had missed. Her mind raced with possibilities, the tantalizing promise of answers shimmering just beyond her reach."
        pt "These stones are more than just markers of time; they might hold the key to understanding this place. I must look closer, listen harder."
        n "The runes etched into the stone glowed softly, casting an inviting light that beckoned her closer. She felt a thrill of determination, a burning desire to uncover the knowledge that had eluded her during her previous visit."
        
        $ what_truths_checked = True
        
        return

    label cryptic_examine_stone_engravings:
        n "The princess moved closer to the stones, her curiosity piqued by the intricate patterns carved into their surfaces. The engravings seemed to pulse with a life of their own, whispering secrets of ages long past."
        pt "These engravings... I didn’t pay much attention to them before, but they’re more than just decorations. There's a language here, a story waiting to be told. But what does it say?"
        n "She traced her fingers over the cool stone, feeling the grooves beneath her touch. The symbols danced beneath her fingertips, shifting as if to invite her to read the tale they told."
        p "These markings... they're like nothing I've ever seen before. They're calling out to be understood, to share their secrets."
        n "The hero stepped closer, peering at the runes with a mix of skepticism and intrigue. He could feel the weight of history in the air, the silent voices of those who had come before echoing around them."
        h "It's like they're telling a story, isn’t it? Maybe a legend or a warning."
        n "The forest seemed to hold its breath, the rustle of leaves and the song of the wind fading into a stillness that focused all attention on the stones." 
        n "The engravings shimmered subtly, drawing the princess further into their spell, urging her to delve deeper."
        
        $ stone_gravings_examined = True
        
        return

    label cryptic_try_to_decipher:
        if can_decipher_runes:
            n "As the princess focused on the runes, a warm glow enveloped the engravings. The symbols, once mysterious and cryptic, now seemed to unravel their secrets before her eyes, forming words and phrases in her mind."
            n "It was as though the stones themselves had awakened, eager to share their long-forgotten tale."
            p "Look at this, these runes... I can understand them. They’re telling a story of what this place once was."
            h "Really? What does it say? What happened here?"
            p "It speaks of a time when this area was vibrant, alive with magic that flowed freely to the people of the kingdom. The stones offered their power to those who lived in the kingdom, fostering growth and prosperity."
            p "This place was once a sanctuary, a source of magic that blessed the kingdom. People came from all around to harness the energy that these stones provided."
            h "It must have been incredible, a true wonder of the kingdom. But what happened to it?"
            n "The symbols shifted, revealing a darker chapter in the story. The air around the princess grew heavy with the weight of past misdeeds, the vibrant colors fading to dull greys as the tale unfolded."
            p "Over time, the kingdom grew greedy. They began to take more than what was offered, exploiting the magic for their own gain. The balance was disrupted, and the stones began to weaken."
            n "As the princess continued to read, the vision darkened further, showing the stones gradually wearing down, their surfaces eroding under the strain of their abuse."
            n "The once-thriving circle became a shadow of its former self, a monument to the consequences of unchecked ambition."
            p "The stones started to crumble, their magic fading as the kingdom's greed consumed them. What was once a place of wonder became a reminder of what was lost."
            h "So that's why it's like this now. The abuse of magic took its toll, leaving behind only these remnants."
            p "Yes. The only magic remaining was that which could only be used for destruction. That must be why the kingdom chose to ban the use of magic."
            h "Agreed. Many outcasts of the kingdom continue to exploit this destructive magic for their own selfish gains. That must be why the stones remain in the state they’re in today."
            n "The final runes glowed softly, a gentle reminder of the circle's former glory. As the glow of the runes faded, the princess felt a newfound resolve settle within her."
            n "The stones had shared their story, and now it was up to her and the hero to ensure that the lessons of the past were not forgotten."
        else:
            n "The princess approached the stone, running her fingers over the intricate engravings. The runes seemed to shimmer and shift beneath her touch, whispering secrets in a language just beyond her comprehension."
            p "I can't read these runes, but I sense there's a way to understand them. It feels like the answer is close."
            h "Maybe there's something nearby that can help you decipher them. Perhaps a clue hidden on one of the stones?"
            p "Yes, something within this place might hold the key. We should look around, there could be a connection we’re missing."
            n "Determined to uncover the truth, she felt a newfound resolve stirring within her. Somewhere nearby lay the key to unlocking the mysteries etched in ancient script."
            
            $ cryptic_choices1_seen.remove("(Act) Try to decipher the runes")

        return

    label cryptic_focus_on_largest:
        n "The princess approached the largest stone at the center of the circle, drawn to its imposing presence. Unlike the others, this stone towered above her, its surface covered in intricate patterns that seemed to pulse with a subtle, inner light."
        p "This one seems to be the centerpiece, the source of whatever magic lies within this place. It feels almost... alive."
        h "Do you sense anything from it? Maybe it holds a connection to the other stones."
        p "Yes, it’s like it’s trying to share something with me. I can feel its energy resonating inside."
        n "She placed her hand gently on the stone's cool surface, feeling a faint vibration that thrummed through her fingertips and into her core. The engravings glowed with an ethereal light, casting soft reflections on her face."
        n "For a moment, the world around her faded, and she felt as though she were standing at the edge of a vast ocean of knowledge, its waves lapping at the shore of her understanding."
        pt "There's a power here, an ancient wisdom reaching out. I feel like I'm standing at the threshold of something profound."
        p "I can almost sense the stories this stone could tell, the wisdom it has gathered over the centuries."
        h "Do you think it can help us find what we're looking for?"
        p "I think it already has. Somehow, I feel more connected to this place than before. As if I've been granted a glimpse into its past."
        n "As they stepped back from the stone, the light slowly dimmed, yet its presence remained, a guiding force that would aid them in unraveling the mysteries of the forest. The path ahead seemed clearer now, illuminated by the wisdom she had gained."
        
        $ can_decipher_runes = True

        return

    label cryptic_i_remember_path:
        n "The familiar stones loomed before her, each step around the circle echoing with the weight of past decisions. The princess recalled the choices she had made, the path she had walked that had led her back here." 
        n "A sense of déjà vu clung to her, and yet, the air was thick with possibility, whispering of paths not yet taken."
        pt "I've walked this path before, felt the pull of these stones and their silent guidance. But is there another way, a path I’ve yet to discover?"
        n "She paused, the cool breeze ruffling her hair, carrying with it the faintest hint of the choices she had left unmade. The forest seemed to hold its breath, awaiting her decision with bated anticipation."
        pt "The same choices will lead to the same end, but what if I dare to choose differently? What if the path less taken is the one that leads to freedom?"
        n "Her heart raced with a mix of fear and excitement, the promise of uncharted territory calling to her, urging her to step off the beaten path."
        return

    label cryptic_am_i_destined:
        n "The stones stood tall and silent, sentinels of time watching her with ancient eyes. Each visit to this sacred circle felt both new and hauntingly familiar, a testament to the endless cycle she found herself trapped within."
        n "The air hummed with a quiet energy, a reminder of the choices she had made and the consequences they had wrought."
        pt "I keep getting pulled back, over and over, a constant in the ever-repeating story of my life. Am I fated to wander this loop until I finally choose correctly?"
        n "A breeze rustled through the trees, carrying with it whispers of times gone by, echoes of her previous decisions. She felt the weight of her past choices pressing down on her, each one a reminder of paths taken and the results they yielded."
        pt "Is this a test, a puzzle to be solved? Must I navigate these choices until I finally unlock the secret of escaping this endless cycle?"
        n "The realization settled upon her shoulders, a burden and a challenge, urging her to break the chains that bound her to this fate. The stones seemed to lean in, expectant and watchful, waiting to see if she would rise to the occasion."
        return

    label cryptic_will_i_find:
        n "The circle of stones surrounded her, a timeless audience to her journey. Each visit brought with it a new sense of determination, a fresh resolve to seek the answers that had so far eluded her."
        n "The air crackled with potential, as if the very atmosphere was holding its breath, waiting for her to uncover the truth."
        pt "Every time I stand here, I feel the weight of unanswered questions pressing down on me. Will this be the time I finally discover the truth?"
        n "The forest seemed to lean closer, the rustling leaves a gentle encouragement to press forward, to dig deeper. The runes on the stones glimmered faintly, teasing her with glimpses of the knowledge they held."
        pt "I’ve walked this path before, seen these stones, heard their whispers. But every visit just creates more and more questions."
        n "A sense of purpose filled her, pushing her to keep seeking, to keep asking the questions that might lead to her salvation."
        return

    label cryptic_could_this_be:
        pt "Every step I take feels like retracing old paths. But these stones... they seem different somehow. Could they hold the answer to escaping this never-ending loop?"
        n "The princess's gaze lingered on the largest stone, its runes glowing softly in the twilight. A sense of purpose welled up inside her, a desperate hope that this time, she might find the clue she needed."
        pt "I've come so far, but is this the right path? Or just another dead end? I can't give up now. There has to be a way to break free."
        n "The princess steeled herself, her resolve firm. Whatever secrets these stones held, she was determined to uncover them."
        return

    label cryptic_air_seems_heavier:
        pt "This place feels more oppressive every time I come here. It's like the stones are watching, remembering... But how could that be possible?"
        n "She looked around, noting the subtle changes in the air—heavier, more charged with each visit. The forest around the clearing was silent, as if holding its breath."
        pt "These stones, they're not just rocks. They carry the weight of history, of every step I've taken here. Do they know something I don't?"
        n "The air felt almost suffocating, a tangible reminder of the choices she had made and the ones she had yet to make. The princess couldn't shake the feeling that the stones were aware of her struggles, her repeated attempts to change her fate."
        return

    label cryptic_take_gem:
        n "With determination in her eyes, the princess reached out and grasped the gem, feeling its warmth spread through her fingers and into her core. The stone pulsed with life, an ancient energy intertwining with her very being."
        p "I’ll take the risk. This power might be the only way to get home safely, especially if the shadowy figure we encountered earlier returns."
        h "Then we must use it wisely. The kingdom might see our need and forgive us if it means defeating a greater evil."
        n "As the gem settled into her grasp, its glow softened to a gentle hum, a steady promise of protection and strength."
        n "A vision entered the minds of her and the hero, showing them all sorts of dark magic that could be used with the power of the gem."
        n "As the vision faded, the princess felt a sense of resolve, ready to face whatever lay ahead with this newfound power."
        n "With the power of the gem, she believed they could overcome any threat they would face in the forest."
        n "The stones vibrated subtly, their runes glowing with a renewed brilliance, as if expressing silent approval. The forest seemed to come alive, the leaves rustling in a harmonious melody, welcoming the princess’s choice."
        n "The princess continued on her journey with the hero, content with her decision to take the magical gem with her."

        $ chose_magic = True
        return

    label cryptic_leave_gem:
        n "The princess hesitated, her hand hovering above the gem as she contemplated the weight of its potential. Despite its allure, she felt the heavy burden of the kingdom’s laws and the consequences of defying them."
        p "No. The risk is too great. If we use this magic, we may never be welcomed back into the kingdom."
        h "Perhaps you're right. Even with the threat of danger, we can find another way. Magic isn’t the only path to victory."
        n "She stepped back from the pillar, the gem's glow dimming as she relinquished the promise of power. Her heart ached with the decision, but she knew it was the right one for her and for her future."
        p "We should be able to get back to the kingdom without magic. Even if we encounter the shadowy figure again, we don’t need magic to defeat them."
        h "True. If we survive without magic, we’ll have no regrets. The kingdom will see our strength, and that might be its own reward."
        n "As they turned away from the gem, a cold, still silence settled over the clearing. The air grew heavy, the forest’s quiet discontent noticeable, as though it mourned the loss of a connection that could have been."
        n "The journey ahead loomed, full of uncertainty, but as the princess continued on her way home with the hero, she felt a quiet assurance in her decision to uphold the laws she’d grown to respect."

        $ chose_magic = False
        return