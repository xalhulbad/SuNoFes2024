# Contains the code associated with portion of the game related to the "tower" scene.

# Default variables
default tower_choices1_seen = set()

# TODO: discuss if old options should be hidden after routes are completed, with too many options they go off the screen

label tower_start:
    # Start narration of tower scene
    n "Once upon a time, in a forgotten corner of the kingdom, there stood a tower. It loomed high, shrouded in mystery. The moonlight filtered through its narrow, arched window, casting a pale glow on the cold, damp walls."
    n "There sat the princess, her delicate fingers tracing the rough stone sill. Her eyes, though tired, held a spark of hope. She knew that someone would come for her, as the stories always promised."

    label tower_choices1: # First tower choice
        while len(tower_choices1_seen) < 4: # Stop after 4 choices have been chosen
            menu: 
                set tower_choices1_seen
                # Tells renpy to hide choices in this set (prevents same option showing up twice)

                # Choices available from the start:
                "(Thought) It’s been so long…":
                    call tower_so_long
                    $ tower_choices1_seen.add("(Thought) It’s been so long…")
                    jump tower_choices1
                    
                "(Act) Inspect the dusty room":
                    call tower_inspect_room
                    $ tower_choices1_seen.add("(Act) Inspect the dusty room")
                    jump tower_choices1

                "(Act) Sit on the wooden bed":
                    call tower_sit_bed
                    $ tower_choices1_seen.add("(Act) Sit on the wooden bed")
                    jump tower_choices1

                "(Act) Attempt to open the door":
                    call tower_attempt_open_door
                    $ tower_choices1_seen.add("(Act) Attempt to open the door)")
                    jump tower_choices1

                "(Thought) Why is there no escape?":
                    call tower_why_no_escape
                    $ tower_choices1_seen.add("(Thought) Why is there no escape?")
                    jump tower_choices1

                "(Thought) What secrets does this tower hold…":
                    call tower_what_secrets
                    $ tower_choices1_seen.add("(Thought) What secrets does this tower hold…")
                    jump tower_choices1

                "(Thought) What lies beyond these walls?":
                    call tower_what_lies_beyond_walls
                    $ tower_choices1_seen.add("(Thought) What lies beyond these walls?")
                    jump tower_choices1

                "(Act) Sleep.": # Progresses the game
                    jump tower_go_to_sleep # No call because we don't want to return


                # Choices available after first route completed:
                "(Thought) I’m back." if routes_completed > 0:
                    call tower_im_back
                    $ tower_choices1_seen.add("(Thought) I’m back.")
                    jump tower_choices1

                "(Thought) Was it all a dream?" if routes_completed > 0:
                    call tower_was_it_a_dream
                    $ tower_choices1_seen.add("(Thought) Was it all a dream?")
                    jump tower_choices1

                "(Thought) I remember being rescued…" if routes_completed > 0:
                    call tower_remember_rescued
                    $ tower_choices1_seen.add("(Thought) I remember being rescued…")
                    jump tower_choices1

                
                # Choices available after second route completed:
                "(Thought) I can’t believe I’m back here again." if routes_completed > 1:
                    call tower_cant_believe_back_again
                    $ tower_choices1_seen.add("(Thought) I can’t believe I’m back here again.")
                    jump tower_choices1
                
                "(Thought) Could my emotions be causing this… anomaly?" if routes_completed > 1:
                    call tower_emotions_causing
                    $ tower_choices1_seen.add("(Thought) Could my emotions be causing this… anomaly?")
                    jump tower_choices1

                "(Thought) Is there a lesson to be learned?" if routes_completed > 1:
                    call tower_lesson_to_be_learned
                    $ tower_choices1_seen.add("(Thought) Is there a lesson to be learned?")
                    jump tower_choices1

                "(Thought) What if the hero holds the key to truly breaking free?" if routes_completed > 1:
                    call tower_hero_holds_key
                    $ tower_choices1_seen.add("(Thought) What if the hero holds the key to truly breaking free?")
                    jump tower_choices1

                "(Thought) Maybe the tower itself is enchanted." if routes_completed > 1:
                    call tower_enchanted
                    $ tower_choices1_seen.add("(Thought) Maybe the tower itself is enchanted.")
                    jump tower_choices1

                "(Thought) Blending realities…" if routes_completed > 1:
                    call tower_blending_realities
                    $ tower_choices1_seen.add("(Thought) Blending realities…")
                    jump tower_choices1


                # Choices available after an encounter with the aware hero:
                "(Thought) Does he... know?" if aware_hero_met:
                    call tower_does_he_know
                    $ tower_choices1_seen.add("(Thought) Does he... know?")
                    jump tower_choices1

                "(Thought) Him? A way out?" if aware_hero_met:
                    call tower_way_out
                    $ tower_choices1_seen.add("(Thought) Him? A way out?")
                    jump tower_choices1

                "(Thought) Who is he really?" if aware_hero_met:
                    call tower_who_is_he
                    $ tower_choices1_seen.add("(Thought) Who is he really?")
                    jump tower_choices1

                "(Thought) Why is this happening to us?" if aware_hero_met:
                    call tower_why_is_this_happening
                    $ tower_choices1_seen.add("(Thought) Why is this happening to us?")
                    jump tower_choices1


        # If we get here then the player did not choose "(Act) Sleep" within 4 choices

        n "The moon rose higher, bathing the tower in a soft, ghostly light as the stars twinkled above."

        # Force player to choose "(Act) Sleep"
        menu:
            "(Act) Sleep.": # Progresses the game
                    jump tower_go_to_sleep # No call because we don't want to return


    # Tower choices that are available from the start:
    label tower_so_long:
        pt "Another night in this forsaken place. How long has it really been, waiting for a rescue that seems to never come? Waiting for a way out of this…"
        n "As the moon climbed higher in the sky, its silvery light bathed the tower in an ethereal glow. The princess took a deep breath. She knew that her hero would arrive soon, bringing with him what hoped to be a final escape."
        pt "I will be ready."
        return

    label tower_inspect_room:
        n "Dust particles danced in the air, illuminated by the soft light, and the air was heavy with the scent of moss and old stone. The distant howl of wolves echoed through the night, adding to the eerie stillness."
        n "Inside the tower, the room was sparsely furnished, with only a simple wooden bed, a worn-out rug, and a small table holding a flickering candle."
        menu:
            "(Act) Inspect the dusty table":
                call tower_inspect_table
        return
        
        label tower_inspect_table:
            n "The candle on the small table flickered, casting fleeting shadows that danced across the room. The princess's thoughts were filled with both hope and doubt, wondering about the future that awaited her. She longed for change, for a way out of her predicament."
            pt "The stories always end with the princess being saved."
            pt "There must be a way out."
            return

    label tower_sit_bed:
        n "The bed creaked softly as she sat down, the old wood groaning. She ran her hand over the rough blanket, her thoughts drifting to nights of restless sleep and dreams of freedom."
        pt "This bed has held me through countless nights. It’s a reminder of my captivity but also a testament to my endurance."
        pt "I won't let this tower be my end."
        return

    label tower_attempt_open_door:
        n "The princess approached the heavy wooden door, its surface worn and scratched from countless attempts to open it. She grasped the iron handle, pulling with all her might."
        n "The door didn’t budge, its hinges creaking in protest. She let out a frustrated sigh, her hope waning with each futile attempt."
        pt "Locked, as always. This door is my prison, a barrier between me and the world."
        pt "There must be a way to break free."
        if routes_completed > 0:
            menu:
                "(Act) Check the door again":
                    call tower_check_door_again
        return

    label tower_why_no_escape:
        n "The oppressive silence of the tower echoed her thoughts, each one a plea for freedom that went unanswered. The weight of her captivity felt suffocating."
        pt "No matter where I turn, there’s no escape. These walls, this door, this bed... they all serve to remind me that I’m trapped."
        pt "Why can’t I find a way out?" 
        return

    label tower_what_secrets:
        n "Her eyes scanned the room, taking in every shadow and corner, her mind racing with possibilities. But all she saw was the familiar, unchanging interior of her prison."
        pt "This tower has stood for ages. What secrets does it hold?"
        pt "Apparently, none that I can find."
        return

    label tower_what_lies_beyond_walls:
        n "The princess's gaze drifted towards the narrow window, her mind wandering to the world outside. She imagined the vast forests, the bustling villages, and the open skies."
        pt "What is out there, beyond these confining walls? A life I’ve never known, a journey of discovery..."
        return

    label tower_go_to_sleep:
        n "As she lay down, the soft glow of the candle flickered and dimmed, casting long shadows on the cold stone walls. The princess's thoughts, whether filled with hope or the weight of repeated days, slowly quieted."
        n "As exhaustion overtook her, the princess's eyelids grew heavy, and she slowly drifted off to sleep."
        
        if aware_hero_met and romance >= 70:
            pt "A warmth in the cold of night."
            pt "I'll see you soon..."
            pt "my hero."
        elif aware_hero_met:
            pt "Hero…"
            pt "I will find out soon enough..."
        elif routes_completed >= 1:
            pt "Here we go again."

        $ tower_choices1_seen.clear() # Reset seen choices for next route
 
        return # End of tower scene


    # Tower choices that are available only after first route completed:
    label tower_im_back:
        pt "I’m back. Everything is gone... my wounds, my possessions, even the signs of my struggle."
        pt "It’s like it never happened." 
        n "The princess’s eyes widened as she took in her surroundings, the cold and unyielding walls of the tower greeting her once more."
        return

    label tower_check_door_again:
        pt "Maybe the door is different now. Maybe I can get out..."
        n "She rushed to the door, her hands trembling as she tried the handle once more."
        n "But to no avail."
        return
    
    label tower_was_it_a_dream:
        pt "Was it all a dream? Did I imagine being rescued? No, it felt too real. But why am I here again?"
        n "Doubt crept in as the princess questioned the reality of her memories, the line between dream and reality blurring."
        return

    label tower_remember_rescued:
        pt "I remember being rescued... It was real. It felt so real. How can I be back here now?"
        n "The princess's heart pounded as she recalled memories of the past, vivid and undeniable."
        n "No doubt, the stress was getting to her."
        return

    
    # Tower choices that are available only after second route completed:
    label tower_cant_believe_back_again:
        pt "I can’t believe I’m back here again. How many times must I go through this?"
        n "The princess’s frustration boiled over, the same surroundings greeting her once more."
        return

    label tower_emotions_causing:
        pt "Could my emotions be influencing the loop? Do I need to feel… a certain way to break free?"
        n "She pondered whether her own feelings might hold the key to her predicament."
        return

    label tower_lesson_to_be_learned:
        pt "Is this all merely a lesson? Is escape simply a reward?"
        pt "Maybe I’m missing something crucial."
        n "The princess considered that her imprisonment might be a test, teaching her something important about herself and her fate."
        return
    
    label tower_hero_holds_key:
        pt "What if the hero is the answer?"
        pt "Maybe I need to change how I interact with him."
        n "Her mind raced with the idea that her savior will be integral to her escape."
        return

    label tower_enchanted:
        pt "Could it be that there is a spell binding me here…"
        n "The princess glanced around at the ancient stones, considering the possibility of hidden magic within the walls."
        return

    label tower_blending_realities:
        pt "No scratches, no bruises... nothing to show for my struggles."
        pt "How many times have I been through this?"
        pt "How long has it… truly been?"
        n "The tower stood silent and unchanged, oblivious to the princess's inner turmoils."
        return


    # Tower choices that are available only after an encounter with the aware hero:
    label tower_does_he_know: 
        pt "Does he know about this… replaying of events? The retelling of stories past? He acts like he’s hiding something, but how much does he really know?"
        n "The princess's thoughts lingered on the hero who might come to save her, a mixture of suspicion and curiosity in her eyes."
        return
    
    label tower_way_out: 
        pt "What if he knows the way out? Why is he still here?"
        pt "There is something he knows. He must tell me."
        n "The princess’s resolve hardened."
        return

    label tower_who_is_he: 
        pt "Who is he really? Could he be more than just my savior in this story?"
        n "Her mind was filled with questions, her curiosity about the hero who may finally save her overwhelming."
        return

    label tower_why_is_this_happening: 
        pt "Why is this happening? Is there a reason we’re stuck in this endless cycle? Who designed this?"
        n "A sense of urgency filled the princess as she pondered the purpose behind her situation."
        return
