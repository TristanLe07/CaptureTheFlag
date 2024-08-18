from GameFrame import RedBot, Globals
from enum import Enum

class STATE(Enum):
    MOVE_RIGHT = 1
    MOVE_DOWN = 2
    MOVE_LEFT = 3
    MOVE_UP = 4

class Red1(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)
        self.curr_state = STATE.MOVE_RIGHT

    def tick(self):
        if self.curr_state == STATE.MOVE_RIGHT:
            # Move right until reaching the right boundary of your side
            if self.x < (Globals.GAME_AREA_BORDER - 32):
                self.drive_forward(Globals.FAST)
            else:
                self.curr_state = STATE.MOVE_DOWN
                self.turn_towards(self.x, Globals.GAME_AREA_HEIGHT_MAX - 32)

        elif self.curr_state == STATE.MOVE_DOWN:
            # Move down until reaching the bottom boundary
            if self.y < Globals.GAME_AREA_HEIGHT_MAX - 32:
                self.drive_forward(Globals.FAST)
            else:
                self.curr_state = STATE.MOVE_LEFT
                self.turn_towards(Globals.GAME_AREA_WIDTH_MIN + 32, self.y)

        elif self.curr_state == STATE.MOVE_LEFT:
            # Move left until reaching the left boundary of your side
            if self.x > Globals.GAME_AREA_WIDTH_MIN + 32:
                self.drive_forward(Globals.FAST)
            else:
                self.curr_state = STATE.MOVE_UP
                self.turn_towards(self.x, Globals.GAME_AREA_HEIGHT_MIN + 32)

        elif self.curr_state == STATE.MOVE_UP:
            # Move up until reaching the top boundary
            if self.y > Globals.GAME_AREA_HEIGHT_MIN + 32:
                self.drive_forward(Globals.FAST)
            else:
                self.curr_state = STATE.MOVE_RIGHT
                self.turn_towards(Globals.GAME_AREA_BORDER - 32, self.y)
