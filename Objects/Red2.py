from GameFrame import RedBot, Globals
from enum import Enum
import random

class STATE(Enum):
    SEARCH_JAILED_BOT = 1
    FREE_JAILED_BOT = 2
    GUARD = 3
    
class Red2(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)
        self.initial_wait = random.randint(30, 90)
        self.wait_count = 0
        self.curr_state = STATE.SEARCH_JAILED_BOT

    def tick(self):
        if self.curr_state == STATE.SEARCH_JAILED_BOT:
            for bot in Globals.red_bots:
                if bot.jailed:
                    self.curr_state = STATE.FREE_JAILED_BOT
                    self.turn_towards(bot.x, bot.y, Globals.FAST)
                    print(self.curr_state)
                    break
                else:
                    self.turn_towards(Globals.blue_flag.x, Globals.blue_flag.y, Globals.FAST)
                    self.drive_forward(Globals.FAST)
                    pass
        elif self.curr_state == STATE.FREE_JAILED_BOT:
            self.drive_forward(Globals.FAST)
            for bot in Globals.red_bots:
                if self.point_to_point_distance(self.x, self.y, bot.x, bot.y) < 10:
                    self.curr_state = STATE.SEARCH_JAILED_BOT
                    print(self.curr_state)
                    pass