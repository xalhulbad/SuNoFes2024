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

    # Leading text
    n "A cold wind swept through the forest as the princess and the hero moved forward, the trees seeming to close in around them. The once-familiar paths now felt foreign and threatening, shrouded in an eerie mist that clung to the ground like a living thing."
    n "The hero’s grip tightened on his sword, his breath visible in the sudden chill. The forest was deathly silent, the usual sounds of life replaced by a foreboding stillness."
    n "Out of the mist, a figure began to take shape, its form shifting and flickering as if it were made of shadows. The air grew colder with each passing second, and a sense of dread settled over the princess and the hero."
    vs "You wander where you are not welcome... the kingdom’s taint has stained this place for far too long. I am here to collect what is owed."
   
    if vs_times_gotten == 1: 
        pt "The Vengeful Spirit again… The forest’s anger made flesh. We have to be careful; it’s driven by pure rage." 
   
    elif vs_times_gotten == 2:
        pt "We’ve encountered this spirit before. Its anger is overwhelming, but we’ve survived it once—we can do it again."
   
    else: 
        pt "This spirit won’t stop until it destroys us. We have to end this, once and for all."
   
    n "The Vengeful Spirit’s presence was suffocating, its form constantly shifting as it glided closer. The hero instinctively stepped forward, placing himself between the princess and the malevolent entity."
    h "Stay back, princess. This spirit is more dangerous than any foe we’ve faced. We have to be ready for anything."
    vs "You think you can resist? The forest demands retribution, and you shall be the first to pay."
    n "The spirit’s voice was a chilling whisper, echoing through the trees and seeping into their very bones. The mist around them thickened, the air growing colder with every word it spoke."
    vs "The forest has taken from the wicked before, and now it shall take from you. There is no escape from its wrath."

    jump vs_choices_1

    # Level 1 of choice tree
    label vs_choices_1:
        # Initial branch
        menu:
            "(Act) Stand your ground and challenge the spirit":
                jump vs_choices_2_1

            "(Act) Show empathy and attempt to reason with it":
                jump vs_choices_2_2
            

            # Dialogue pool options

            "(Speak) Who are you?" if not vs_chose_who_are_you:
                $ vs_chose_who_are_you = True
                call vs_who_are_you
                jump vs_choices_1

            "(Speak) Why do you seek vengeance?" if not vs_chose_why_do_you_seek and vs_chose_who_are_you:
                $ vs_chose_why_do_you_seek = True
                call vs_why_do_you_seek
                jump vs_choices_1

            "(Speak) Can you ever be at peace?" if not vs_chose_can_you_ever and vs_chose_why_do_you_seek:
                $ vs_chose_can_you_ever = True
                call vs_can_you_ever
                jump vs_choices_1

            "(Speak) What do you want from us?" if not vs_chose_what_do_you:
                $ vs_chose_what_do_you = True
                call vs_what_do_you
                jump vs_choices_1

            "(Speak) Why do you blame us for the kingdom’s sins?" if not vs_chose_why_do_you_blame and vs_chose_why_do_you_blame:
                $ vs_chose_why_do_you_blame = True
                call vs_why_do_you_blame
                jump vs_choices_1

            "(Speak) Isn’t there a way to break this cycle of hatred?" if not vs_chose_isnt_there_a and vs_chose_isnt_there_a:
                $ vs_chose_isnt_there_a = True
                call vs_isnt_there_a
                jump vs_choices_1
            
            "(Speak) Why can’t you let go of your anger?" if not vs_chose_why_cant_you:
                $ vs_chose_why_cant_you = True
                call vs_why_cant_you
                jump vs_choices_1

            "(Speak) Do you not see the destruction your rage causes?" if not vs_chose_do_you_not and vs_chose_why_cant_you:
                $ vs_chose_do_you_not = True
                call vs_do_you_not
                jump vs_choices_1

            "(Speak) Can’t you find peace in the forest’s renewal?" if not vs_chose_cant_you_find and vs_chose_cant_you_find:
                $ vs_chose_cant_you_find = True
                call vs_cant_you_find
                jump vs_choices_1

            "(Speak) What will you do if you destroy us?" if not vs_chose_what_will_you:
                $ vs_chose_what_will_you = True
                call vs_what_will_you
                jump vs_choices_1

            "(Speak) Will your vengeance ever be enough?" if not vs_chose_will_your_vengeance and vs_chose_what_will_you:
                $ vs_chose_will_your_vengeance = True
                call vs_will_your_vengeance
                jump vs_choices_1

            "(Speak) What then? Will the forest be at peace?" if not vs_chose_what_then and vs_chose_will_your_vengeance:
                $ vs_chose_what_then = True
                call vs_what_then
                jump vs_choices_1


    # Level 2 of choice tree
    label vs_choices_2_1:
        # Branching from "(Act) Stand your ground and challenge the spirit"
        menu:
            "(Act) Have the hero strike first":
                jump vs_choices_3_1
            "(Act) Confront it with the truth of the kingdom’s wrongdoings":
                jump vs_choices_3_2


            # Dialogue pool options

            "(Speak) Who are you?" if not vs_chose_who_are_you:
                $ vs_chose_who_are_you = True
                call vs_who_are_you
                jump vs_choices_2_1

            "(Speak) Why do you seek vengeance?" if not vs_chose_why_do_you_seek and vs_chose_who_are_you:
                $ vs_chose_why_do_you_seek = True
                call vs_why_do_you_seek
                jump vs_choices_2_1

            "(Speak) Can you ever be at peace?" if not vs_chose_can_you_ever and vs_chose_why_do_you_seek:
                $ vs_chose_can_you_ever = True
                call vs_can_you_ever
                jump vs_choices_2_1

            "(Speak) What do you want from us?" if not vs_chose_what_do_you:
                $ vs_chose_what_do_you = True
                call vs_what_do_you
                jump vs_choices_2_1

            "(Speak) Why do you blame us for the kingdom’s sins?" if not vs_chose_why_do_you_blame and vs_chose_why_do_you_blame:
                $ vs_chose_why_do_you_blame = True
                call vs_why_do_you_blame
                jump vs_choices_2_1

            "(Speak) Isn’t there a way to break this cycle of hatred?" if not vs_chose_isnt_there_a and vs_chose_isnt_there_a:
                $ vs_chose_isnt_there_a = True
                call vs_isnt_there_a
                jump vs_choices_2_1
            
            "(Speak) Why can’t you let go of your anger?" if not vs_chose_why_cant_you:
                $ vs_chose_why_cant_you = True
                call vs_why_cant_you
                jump vs_choices_2_1

            "(Speak) Do you not see the destruction your rage causes?" if not vs_chose_do_you_not and vs_chose_why_cant_you:
                $ vs_chose_do_you_not = True
                call vs_do_you_not
                jump vs_choices_2_1

            "(Speak) Can’t you find peace in the forest’s renewal?" if not vs_chose_cant_you_find and vs_chose_cant_you_find:
                $ vs_chose_cant_you_find = True
                call vs_cant_you_find
                jump vs_choices_2_1

            "(Speak) What will you do if you destroy us?" if not vs_chose_what_will_you:
                $ vs_chose_what_will_you = True
                call vs_what_will_you
                jump vs_choices_2_1

            "(Speak) Will your vengeance ever be enough?" if not vs_chose_will_your_vengeance and vs_chose_what_will_you:
                $ vs_chose_will_your_vengeance = True
                call vs_will_your_vengeance
                jump vs_choices_2_1

            "(Speak) What then? Will the forest be at peace?" if not vs_chose_what_then and vs_chose_will_your_vengeance:
                $ vs_chose_what_then = True
                call vs_what_then
                jump vs_choices_2_1

    label vs_choices_2_2:
        # Branching from "(Act) Show empathy and attempt to reason with it"
        menu:
            "(Act) Appeal to its desire for justice":
                jump vs_choices_3_3
            "(Act) Offer a way to ease its suffering":
                jump vs_choices_3_4


            # Dialogue pool options

            "(Speak) Who are you?" if not vs_chose_who_are_you:
                $ vs_chose_who_are_you = True
                call vs_who_are_you
                jump vs_choices_2_2

            "(Speak) Why do you seek vengeance?" if not vs_chose_why_do_you_seek and vs_chose_who_are_you:
                $ vs_chose_why_do_you_seek = True
                call vs_why_do_you_seek
                jump vs_choices_2_2

            "(Speak) Can you ever be at peace?" if not vs_chose_can_you_ever and vs_chose_why_do_you_seek:
                $ vs_chose_can_you_ever = True
                call vs_can_you_ever
                jump vs_choices_2_2

            "(Speak) What do you want from us?" if not vs_chose_what_do_you:
                $ vs_chose_what_do_you = True
                call vs_what_do_you
                jump vs_choices_2_2

            "(Speak) Why do you blame us for the kingdom’s sins?" if not vs_chose_why_do_you_blame and vs_chose_why_do_you_blame:
                $ vs_chose_why_do_you_blame = True
                call vs_why_do_you_blame
                jump vs_choices_2_2

            "(Speak) Isn’t there a way to break this cycle of hatred?" if not vs_chose_isnt_there_a and vs_chose_isnt_there_a:
                $ vs_chose_isnt_there_a = True
                call vs_isnt_there_a
                jump vs_choices_2_2
            
            "(Speak) Why can’t you let go of your anger?" if not vs_chose_why_cant_you:
                $ vs_chose_why_cant_you = True
                call vs_why_cant_you
                jump vs_choices_2_2

            "(Speak) Do you not see the destruction your rage causes?" if not vs_chose_do_you_not and vs_chose_why_cant_you:
                $ vs_chose_do_you_not = True
                call vs_do_you_not
                jump vs_choices_2_2

            "(Speak) Can’t you find peace in the forest’s renewal?" if not vs_chose_cant_you_find and vs_chose_cant_you_find:
                $ vs_chose_cant_you_find = True
                call vs_cant_you_find
                jump vs_choices_2_2

            "(Speak) What will you do if you destroy us?" if not vs_chose_what_will_you:
                $ vs_chose_what_will_you = True
                call vs_what_will_you
                jump vs_choices_2_2

            "(Speak) Will your vengeance ever be enough?" if not vs_chose_will_your_vengeance and vs_chose_what_will_you:
                $ vs_chose_will_your_vengeance = True
                call vs_will_your_vengeance
                jump vs_choices_2_2

            "(Speak) What then? Will the forest be at peace?" if not vs_chose_what_then and vs_chose_will_your_vengeance:
                $ vs_chose_what_then = True
                call vs_what_then
                jump vs_choices_2_2


    # Level 3 of choice tree
    label vs_choices_3_1:
        # Branching from "(Act) Have the hero strike first"
        menu:
            "(Act) Try to overpower it with sheer force":
                jump vs_choices_4_1
            "(Act) Use the hero as a decoy and plan a counterattack" if not chose_magic:
                jump vs_choices_4_2

    label vs_choices_3_2:
        # Branching from "(Act) Confront it with the truth of the kingdom’s wrongdoings"
        menu:
            "(Act) Acknowledge the kingdom’s crimes and ask for mercy" if not chose_magic:
                jump vs_choices_4_3
            "(Act) Offer a solution through magic to mend the past" if chose_magic:
                jump vs_choices_4_4

    label vs_choices_3_3:
        # Branching from "(Act) Appeal to its desire for justice"
        menu:
            "(Act) Convince it that the forest can still be healed":
                jump vs_choices_4_5
            "(Act) Offer to protect the forest as its guardian" if chose_magic:
                jump vs_choices_4_6

    label vs_choices_3_4:
        # Branching from "(Act) Offer a way to ease its suffering"
        menu:
            "(Act) Share its burden by taking on some of its pain" if chose_magic:
                jump vs_choices_4_7
            "(Act) Propose a ritual to put its spirit to rest":
                jump vs_choices_4_8

    
    # Level 4 of choice tree
    label vs_choices_4_1:
        # Branching from "(Act) Try to overpower it with sheer force"
        menu:
            "(Act) Exploit its moment of weakness" if not chose_magic:
                jump vs_choices_5_1
            "(Act) Lead it into a trap using the environment":
                jump vs_choices_5_2

    label vs_choices_4_2:
        # Branching from "(Act) Use the hero as a decoy and plan a counterattack"
        menu:
            "(Act) Prepare to strike while it’s focused on the hero":
                jump vs_choices_5_3
            "(Act) Feint and deliver a decisive blow":
                jump vs_choices_5_4

    label vs_choices_4_3:
        # Branching from "(Act) Acknowledge the kingdom’s crimes and ask for mercy"
        menu:
            "(Act) Offer to atone for the kingdom’s sins":
                jump vs_choices_5_5
            "(Act) Promise to help the forest heal":
                jump vs_choices_5_6

    label vs_choices_4_4:
        # Branching from "(Act) Offer a solution through magic to mend the past"
        menu:
            "(Act) Use a binding spell to contain its anger":
                jump vs_choices_5_7
            "(Act) Reverse the flow of magic to restore balance":
                jump vs_choices_5_8

    label vs_choices_4_5:
        # Branching from "(Act) Convince it that the forest can still be healed"
        menu:
            "(Act) Persuade it to let go and find peace" if not chose_magic:
                jump vs_choices_5_9
            "(Act) Promise to carry on its mission of protecting the forest" if chose_magic:
                jump vs_choices_5_10

    label vs_choices_4_6:
        # Branching from "(Act) Offer to protect the forest as its guardian"
        menu:
            "(Act) Bind its spirit to the forest":
                jump vs_choices_5_11
            "(Act) Assume its role in guarding the forest":
                jump vs_choices_5_12

    label vs_choices_4_7:
        # Branching from "(Act) Share its burden by taking on some of its pain"
        menu:
            "(Act) Absorb its suffering to break the cycle":
                jump vs_choices_5_13
            "(Act) Offer to merge your power with the spirit’s":
                jump vs_choices_5_14

    label vs_choices_4_8:
        # Branching from "(Act) Propose a ritual to put its spirit to rest"
        menu:
            "(Act) Offer a final act of sacrifice" if not chose_magic:
                jump vs_choices_5_15
            "(Act) Channel the ritual’s energy to free it" if chose_magic:
                jump vs_choices_5_16


    # Level 5 of choice tree
    label vs_choices_5_1:
        # Branching from "(Act) Exploit its moment of weakness"
        menu:
            "(Act) Strike it down with determination":
                jump sacrificed_princess
            "(Act) Use the hero’s courage to finish it off":
                jump saved_hero

    label vs_choices_5_2:
        # Branching from "(Act) Lead it into a trap using the environment"
        menu:
            "(Act) Distract and outrun it" if not chose_magic:
                jump inherited_throne
            "(Act) Teleport away while it's distracted" if chose_magic:
                jump happily_ever_after

    label vs_choices_5_3:
        # Branching from "(Act) Prepare to strike while it’s focused on the hero"
        menu:
            "(Act) Land a decisive blow":
                jump saved_hero
            "(Act) Strike it down while it’s distracted":
                jump inherited_throne

    label vs_choices_5_4:
        # Branching from "(Act) Feint and deliver a decisive blow"
        menu:
            "(Act) Deliver a fatal strike":
                jump love_beyond_death
            "(Act) Overwhelm it with precision":
                jump saved_hero

    label vs_choices_5_5:
        # Branching from "(Act) Offer to atone for the kingdom’s sins"
        menu:
            "(Act) Offer your life as penance":
                jump sacrificed_princess
            "(Act) Convince it that the kingdom can change":
                jump inherited_throne

    label vs_choices_5_6:
        # Branching from "(Act) Promise to help the forest heal"
        menu:
            "(Act) Forge a pact to protect the forest":
                jump inherited_throne
            "(Act) Use the hero’s loyalty as a guarantee":
                jump saved_hero

    label vs_choices_5_7:
        # Branching from "(Act) Use a binding spell to contain its anger"
        menu:
            "(Act) Contain its wrath within yourself":
                jump corrupted_hero
            "(Act) Teleport away while it's distracted":
                jump happily_ever_after

    label vs_choices_5_8:
        # Branching from "(Act) Reverse the flow of magic to restore balance"
        menu:
            "(Act) Redirect its pain to heal the forest":
                jump unfulfilled_love
            "(Act) Try to defeat it with magic":
                jump love_beyond_death

    label vs_choices_5_9:
        # Branching from "(Act) Persuade it to let go and find peace"
        menu:
            "(Act) Guide it to the afterlife":
                jump sacrificed_princess
            "(Act) Let it fade away peacefully":
                jump love_beyond_death

    label vs_choices_5_10:
        # Branching from "(Act) Promise to carry on its mission of protecting the forest"
        menu:
            "(Act) Become its successor":
                jump forest_protectors
            "(Act) Betray and teleport away":
                jump happily_ever_after

    label vs_choices_5_11:
        # Branching from "(Act) Bind its spirit to the forest"
        menu:
            "(Act) Ensure it remains as a guardian":
                jump forest_protectors
            "(Act) Trap it forever within the forest’s bounds":
                jump corrupted_hero

    label vs_choices_5_12:
        # Branching from "(Act) Assume its role in guarding the forest"
        menu:
            "(Act) Take on its duties eternally":
                jump forest_protectors
            "(Act) Bind yourself to the forest in a tragic pact":
                jump unfulfilled_love

    label vs_choices_5_13:
        # Branching from "(Act) Absorb its suffering to break the cycle"
        menu:
            "(Act) Let its power corrupt you":
                jump corrupted_hero
            "(Act) Take on its rage and become twisted":
                jump unfulfilled_love

    label vs_choices_5_14:
        # Branching from "(Act) Offer to merge your power with the spirit’s"
        menu:
            "(Act) Form a dark bond with the spirit":
                jump corrupted_hero
            "(Act) Fuse your essence with its wrath":
                jump unfulfilled_love

    label vs_choices_5_15:
        # Branching from "(Act) Offer a final act of sacrifice"
        menu:
            "(Act) Give your life to save the hero":
                jump sacrificed_princess
            "(Act) Die together to free the spirit":
                jump love_beyond_death

    label vs_choices_5_16:
        # Branching from "(Act) Channel the ritual’s energy to free it"
        menu:
            "(Act) Purify the spirit and the forest":
                jump forest_protectors
            "(Act) Teleport away while it's distracted":
                jump happily_ever_after

    
    label vs_who_are_you:
        return
    label vs_why_do_you_seek:
        return
    label vs_can_you_ever:
        return
    label vs_what_do_you:
        return
    label vs_why_do_you_blame:
        return
    label vs_isnt_there_a:
        return
    label vs_why_cant_you:
        return
    label vs_do_you_not:
        return
    label vs_cant_you_find:
        return
    label vs_what_will_you:
        return
    label vs_will_your_vengeance:
        return
    label vs_what_then:
        return