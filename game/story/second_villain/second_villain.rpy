# Contains the code associated with portion of the game related to the "second villain encounter" scene.

label second_villain_start:
    # Jump to appropriate villain type
    if v_type == "hu":
        call hu_start

    elif v_type == "fh":
        call fh_start

    elif v_type == "ff":
        call ff_start

    elif v_type == "dml":
        call dml_start

    else:
        call vs_start

    return


label second_villain_test_aware_hero:
    # If we are on an aware hero route, and have not already triggered aware hero,
    # we want to immediately trigger it
    if routes_completed + 1 in aware_hero_routes:
        jump aware_hero

    return