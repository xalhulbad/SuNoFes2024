# Declares characters used in the game.

# Narrator
define n = Character("Narrator", what_color="#FFFFFF")

# Princess
define p = Character("The Princess", what_color="#FFC0CB")
define pt = Character(None, who_color="#808080", what_color="#C0C0C0", what_italic=True) # Empty name, italicized text

# Hero
define h = Character("The Hero", what_color="#DC143C")
define ah = Character("Aware Hero", what_color="#DC143C")

# Villains
define v_type = None # Variable used for revealing villain type

define v = Character("Shadowy Figure", what_color="#646464") # Before villain type revealed
define s = Character("Shadowy Figure", what_color="#646464") # Alias for previous

define ff = Character("Femme Fatale", what_color="#646464")
define fh = Character("Fallen Hero", what_color="#646464")
define hu = Character("The Hunter", what_color="#646464")
define dml = Character("Dark Magic Lord", what_color="#646464")
define vs = Character("Vengeful Spirit", what_color="#646464")

# Voice (for cryptic stonehenge)
define voice = Character("Voice", what_color="#FFFFFF")