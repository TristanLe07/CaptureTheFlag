from GameFrame import RedBot, Globals
from enum import Enum

class STATE(Enum):
    SEARCH_JAILED_BOT = 1
    FREE_JAILED_BOT = 2

class Red2(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)
        self.curr_state = STATE.SEARCH_JAILED_BOT

    def tick(self):
        if self.curr_state == STATE.SEARCH_JAILED_BOT:
            for bot in Globals.red_bots:
                if bot.jailed:
                    self.curr_state = STATE.FREE_JAILED_BOT
                    self.turn_towards(bot.x, bot.y, Globals.FAST)
                    break
        elif self.curr_state == STATE.FREE_JAILED_BOT:
            self.drive_forward(Globals.FAST)
            for bot in Globals.red_bots:
                if self.point_to_point_distance(self.x, self.y, bot.x, bot.y) < 10:
                    self.curr_state = STATE.SEARCH_JAILED_BOT
                    break
