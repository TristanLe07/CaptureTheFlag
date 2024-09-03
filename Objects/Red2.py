from GameFrame import RedBot, Globals
from enum import Enum
import random

class STATE(Enum):
    SEARCH_JAILED_BOT = 1
    FREE_JAILED_BOT = 2
    GUARD_FLAG = 3

class Red2(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)
        self.initial_wait = random.randint(30, 90)
        self.wait_count = 0
        self.curr_state = STATE.SEARCH_JAILED_BOT

    def tick(self):
        if self.curr_state == STATE.SEARCH_JAILED_BOT:
            jailed_bots = [bot for bot in Globals.red_bots if bot.jailed]
            if jailed_bots:
                target_bot = jailed_bots[0]  # Take the first jailed bot found
                self.turn_towards(target_bot.x, target_bot.y, Globals.FAST)
                self.drive_forward(Globals.FAST)
                self.curr_state = STATE.FREE_JAILED_BOT
            else:
                # If no jailed bots, guard the flag
                self.guard_flag()

        elif self.curr_state == STATE.FREE_JAILED_BOT:
            self.drive_forward(Globals.FAST)
            # Check if close to the jailed bot
            for bot in Globals.red_bots:
                if self.point_to_point_distance(self.x, self.y, bot.x, bot.y) < 10:
                    self.curr_state = STATE.SEARCH_JAILED_BOT
                    break

    def guard_flag(self):
        # Move towards the flag and stay around it
        self.turn_towards(Globals.blue_flag.x, Globals.blue_flag.y, Globals.FAST)
        self.drive_forward(Globals.FAST)


