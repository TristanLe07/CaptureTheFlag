import os
import pygame
from GameFrame import RoomObject


class TextObject(RoomObject):
    def __init__(
        self, room, x, y, text="Not Set", size=60, font="radio_stars", colour=(0, 0, 0), bold=False, background=None
    ):
        RoomObject.__init__(self, room, x, y)

        self.rendered_text = 0
        self.rect = 0
        self.built_font = None
        self.text = text
        self.size = size
        self.font = font
        self.colour = colour
        self.bold = bold
        self.background = background
        self.update_text()

    def update_text(self):
        if self.font == "radio_stars":
            self.built_font = pygame.font.Font(os.path.join("Fonts", "radio_stars.otf"), self.size)
        elif self.font == "pixel_code":
            self.built_font = pygame.font.Font(os.path.join("Fonts", "pixel_code.otf"), self.size)
        elif self.font == "share-tech-mono-regular":
            self.built_font = pygame.font.Font(os.path.join("Fonts", "share-tech-mono-regular.ttf"), self.size)
        elif self.font == "moby_monospace":
            self.built_font = pygame.font.Font(os.path.join("Fonts", "moby_monospace.otf"), self.size)
        else:
            self.built_font = pygame.font.SysFont(self.font, self.size, self.bold)
        self.rendered_text = self.built_font.render(self.text, False, self.colour, self.background)
        self.image = self.rendered_text
        self.width, self.height = self.built_font.size(self.text)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_text_width(self):
        return self.built_font.size(self.text)[0]

    # Attempt to resize the font size and matin a max width, spit into two lines where desired
    def set_max_width(self, max_desired_width, should_split_where_possible=True):
        if self.get_text_width() < max_desired_width:
            return True

        self.y += 1
        self.size -= 1
        self.update_text()

        return self.set_max_width(max_desired_width, should_split_where_possible)

    @staticmethod
    def split_half_on_space(string):
        """Try and split a string around the midpoint

        Return 2 string on a space given it is at least 12 chars and the space is not near the edges of string.
        """
        if len(string) < 10:
            return string, ""
        half = len(string) // 2
        split_location = 0
        for i in range(half - 2):
            if string[half + i] == " ":
                split_location = half + i
                break
            if string[half - i] == " ":
                split_location = half - i
                break
        if split_location == 0:
            return string.strip(), ""

        return string[:split_location].strip(), string[split_location:].strip()
