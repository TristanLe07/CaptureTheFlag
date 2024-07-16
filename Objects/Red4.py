from GameFrame import RedBot, Globals
from enum import Enum


class STATE(Enum):
    WAIT = 1
    ATTACK = 2


class Red4(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)

        self.curr_state = STATE.WAIT
        print(f"Red 4 X: {self.x}")
        print(f"Red 4 Y: {self.y}")
        print(Globals.GAME_AREA_WIDTH_MAX)

    def tick(self):
        self.drive_backward()
        print(self.x, self.y)
        if self.x == Globals.GAME_AREA_WIDTH_MAX:
            self.turn_left(Globals.FAST)