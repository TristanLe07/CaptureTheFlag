from GameFrame import RedBot, Globals
from enum import Enum
import random

class STATE(Enum):
    MOVE_UP = 1
    MOVE_DOWN = 2
    MOVE_LEFT = 3

class Red1(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)
        self.curr_state = STATE.MOVE_LEFT
        
    def tick(self):
        if self.curr_state == STATE.MOVE_LEFT:
            if self.x <= 760:
                self.curr_state = STATE.MOVE_UP
            else:
                self.drive_forward(Globals.FAST)
            
        if self.curr_state == STATE.MOVE_UP:
            
            if self.y <= 70:
                self.curr_state = STATE.MOVE_DOWN
            else:
                self.turn_towards(760, 83, speed=Globals.FAST)
                self.drive_forward(Globals.FAST)

        if self.curr_state == STATE.MOVE_DOWN:
            if self.y >= 610:
                self.curr_state = STATE.MOVE_UP
            else:
                self.turn_towards(760, 720, speed=Globals.FAST)
                self.drive_forward(Globals.FAST)