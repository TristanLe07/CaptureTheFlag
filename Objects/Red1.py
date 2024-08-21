from GameFrame import RedBot, Globals
from enum import Enum
import random

class STATE(Enum):
    MOVE_UP = 1
    MOVE_DOWN = 2

class Red1(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)
        self.initial_wait = random.randint(30, 90)
        self.wait_count = 0
        
    def tick(self):
        
        if self.x == 702:
            self.curr_state = STATE.MOVE_UP
        else:
            self.drive_forward(Globals.FAST)
            print(self.x)
            
        
        if self.curr_state == STATE.MOVE_UP:
            self.move_in_direction(180, 702)
            self.drive_forward(Globals.FAST)