from GameFrame import RoomObject,TextObject,Globals
import pygame
import os
class BotNumber(RoomObject):
    def __init__(
        self, room, x, y, number, team, text="Not Set", size=20, font="radio_stars",  bold=False, background=None):
        RoomObject.__init__(self, room, x, y)

        self.rendered_text = 0
        self.rect = 0
        self.number = number
        self.built_font = None
        self.text = text
        self.size = size
        self.font = font
        self.team = team
        self.bold = bold
        if self.team =='red':
            self.colour=( 255,0,0)
        elif self.team == 'blue':
            self.colour=(0,0, 255)
        self.text = str(self.number)
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

    def step(self):
        if self.team == 'red':

            bot = Globals.red_bots[self.number -1]
            self.x = bot.x + 50 
            self.y = bot.y - 5

        if self.team == 'blue':

            bot = Globals.blue_bots[self.number -1]
        
            self.x = bot.x - 35 
            self.y = bot.y - 5
