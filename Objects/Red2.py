from GameFrame import RedBot, Globals
import random


class Red2(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)
        self.initial_wait = random.randint(30, 90)
        self.wait_count = 0

    def tick(self):
        if self.has_flag:
           self.turn_towards(Globals.blue_flag.x, Globals.blue_flag.y, Globals.FAST)
        else:
           self.turn_towards(Globals.red_flag.x, Globals.red_flag.y, Globals.FAST)

        self.drive_forward(Globals.FAST)