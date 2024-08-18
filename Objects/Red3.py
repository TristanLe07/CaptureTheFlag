from GameFrame import RedBot, Globals
from enum import Enum

class STATE(Enum):
    ENTER_ENEMY_TERRITORY = 1
    RETREAT_TO_SAFETY = 2
    WAIT = 3

class Red3(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)
        self.curr_state = STATE.ENTER_ENEMY_TERRITORY
        self.start_pos = (x, y)

    def tick(self):
        if self.curr_state == STATE.ENTER_ENEMY_TERRITORY:
            if self.x < Globals.GAME_AREA_BORDER:
                self.drive_forward(Globals.FAST)
            else:
                for bot in Globals.blue_bots:
                    if self.point_to_point_distance(self.x, self.y, bot.x, bot.y) < 50:
                        self.curr_state = STATE.RETREAT_TO_SAFETY
                        self.turn_towards(self.start_pos[0], self.start_pos[1], Globals.FAST)
                        break
        elif self.curr_state == STATE.RETREAT_TO_SAFETY:
            self.drive_forward(Globals.FAST)
            if self.x >= self.start_pos[0]:
                self.curr_state = STATE.WAIT
                self.set_timer(300, self.return_to_attack)

    def return_to_attack(self):
        self.curr_state = STATE.ENTER_ENEMY_TERRITORY
