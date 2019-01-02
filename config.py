import pygame

# ----------
# dimensions

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# ----------

ROTATIONAL_THRUST = 5  # deg to veg
THRUST = 1

# ----------
# Colours

COLOUR_DEFAULT = (255, 255, 255)
COLOUR_BACKGROUND = (0, 0, 0)

# ----------
# fonts

FONTS = {
    'heading': ('fonts/Amatic-Bold.ttf', 72),
    'button': ('fonts/Amatic-Bold.ttf', 32),
    'default': ('fonts/Amatic-Bold.ttf', 25),
}

# ----------

def init_fonts():
    """
    initialise fonts - this must be called after pygame.init()
    """
    for key, args in FONTS.items():
        FONTS[key] = pygame.font.Font(*args)
