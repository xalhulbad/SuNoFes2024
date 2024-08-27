# Declares characters used in the game.

# Narrator
define n = Character("Narrator", what_color="#CCCCCC", who_bold=True, who_color="#AAAAAA")

# Princess
define p = Character("The Princess", what_color="#CCCCCC")
define pt = Character(None, who_color="#808080", what_color="#CCCCCC", what_italic=True) # Empty name, italicized text

# Hero
define h = Character("The Hero", what_color="#CCCCCC")
define ah = Character("Aware Hero", what_color="#CCCCCC")

# Villains
define v_type = None # Variable used for revealing villain type

define v = Character("Shadowy Figure", what_color="#CCCCCC") # Before villain type revealed
define s = Character("Shadowy Figure", what_color="#CCCCCC") # Alias for previous

define ff = Character("Femme Fatale", what_color="#CCCCCC")
define fh = Character("Fallen Hero", what_color="#CCCCCC")
define hu = Character("The Hunter", what_color="#CCCCCC")
define dml = Character("Dark Magic Lord", what_color="#CCCCCC")
define vs = Character("Vengeful Spirit", what_color="#CCCCCC")

# Voice (for cryptic stonehenge)
define voice = Character("Voice", what_color="#CCCCCC")