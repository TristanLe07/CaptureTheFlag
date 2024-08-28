from GameFrame import RedBot, Globals
from enum import Enum
import random

class STATE(Enum):
    ATTEMPT_FLAG_CAPTURE = 1
    RETRY_DIFFERENT_ANGLE = 2

class Red4(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)
        self.curr_state = STATE.ATTEMPT_FLAG_CAPTURE
        self.random_offset = 0

    def tick(self):
        if self.curr_state == STATE.ATTEMPT_FLAG_CAPTURE:
            # Calculate a random offset angle
            target_x = Globals.red_flag.x + self.random_offset
            target_y = Globals.red_flag.y + self.random_offset
            
            self.turn_towards(target_x, target_y, Globals.FAST)
            self.drive_forward(Globals.FAST)
            
            # If the bot gets the flag, return to base
            if self.has_flag:
                print("I HAVE THE FLAG!")
                self.turn_towards(702, 83, speed=Globals.FAST)
                self.drive_forward(Globals.FAST)
            else:
                # If near the flag but doesn't have it, switch to retrying from a different angle
                if self.point_to_point_distance(self.x, self.y, Globals.red_flag.x, Globals.red_flag.y) < 50:
                    self.curr_state = STATE.RETRY_DIFFERENT_ANGLE

        elif self.curr_state == STATE.RETRY_DIFFERENT_ANGLE:
            # Generate a new random angle offset for a different approach
            self.random_offset = random.randint(-100, 100)
            self.curr_state = STATE.ATTEMPT_FLAG_CAPTURE
