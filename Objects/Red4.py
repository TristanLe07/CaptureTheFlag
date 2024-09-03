from GameFrame import RedBot, Globals
from enum import Enum
import random

class STATE(Enum):
    ATTEMPT_FLAG_CAPTURE = 1
    RETRY_DIFFERENT_ANGLE = 2
    RETURN_TO_BASE = 3
    IN_JAIL = 4
    JUKE_ENEMY = 5
    DISTRACT_ENEMY = 6

class Red4(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)
        self.curr_state = STATE.ATTEMPT_FLAG_CAPTURE
        self.random_offset = 0
        self.start_pos = (x, y)
        self.juke_direction = None

    def tick(self):
        # Check if the bot is jailed
        if self.jailed:
            self.curr_state = STATE.IN_JAIL

        if self.curr_state == STATE.ATTEMPT_FLAG_CAPTURE:
            # Approach the enemy flag with a random offset
            target_x = Globals.red_flag.x + self.random_offset
            target_y = Globals.red_flag.y + self.random_offset

            self.turn_towards(target_x, target_y, Globals.FAST)
            self.drive_forward(Globals.FAST)
            
            # Check if the bot has captured the flag
            if self.has_flag:
                self.curr_state = STATE.RETURN_TO_BASE
            else:
                # Detect if there is a nearby enemy bot
                for bot in Globals.blue_bots:
                    if self.point_to_point_distance(self.x, self.y, bot.x, bot.y) < 50:
                        self.curr_state = STATE.RETRY_DIFFERENT_ANGLE
                        break

        elif self.curr_state == STATE.RETRY_DIFFERENT_ANGLE:
            # Generate a new random offset for a different approach
            self.random_offset = random.randint(-100, 100)
            self.curr_state = STATE.ATTEMPT_FLAG_CAPTURE

        elif self.curr_state == STATE.RETURN_TO_BASE:
            # Return to the starting position after getting the flag
            self.turn_towards(self.start_pos[0], self.start_pos[1], Globals.FAST)
            self.drive_forward(Globals.FAST)

            # Check for nearby enemies to try and juke them
            if self.has_flag:
                for bot in Globals.blue_bots:
                    if self.point_to_point_distance(self.x, self.y, bot.x, bot.y) < 50:
                        self.curr_state = STATE.DISTRACT_ENEMY
                        break

            # If the bot no longer has the flag, attempt to recapture
            if not self.has_flag:
                self.curr_state = STATE.ATTEMPT_FLAG_CAPTURE

        elif self.curr_state == STATE.DISTRACT_ENEMY:
            # Perform a distraction maneuver
            self.distract_enemy()

        elif self.curr_state == STATE.JUKE_ENEMY:
            # Perform a juke maneuver
            self.perform_juke()

        elif self.curr_state == STATE.IN_JAIL:
            # Logic for being in jail
            if not self.jailed:
                self.curr_state = STATE.ATTEMPT_FLAG_CAPTURE

    def distract_enemy(self):
        # Move randomly to distract enemy bots
        if random.random() < 0.5:
            self.turn_left(Globals.FAST)
        else:
            self.turn_right(Globals.FAST)
        self.drive_forward(Globals.FAST)
        # After distracting, return to base
        self.set_timer(30, self.return_to_base)

    def perform_juke(self):
        # Perform a juke maneuver
        if self.juke_direction == -1:
            self.turn_left(Globals.FAST)
        else:
            self.turn_right(Globals.FAST)
        self.drive_forward(Globals.FAST)
        # After juking, return to base
        self.set_timer(30, self.return_to_base)

    def return_to_base(self):
        # Resume returning to base
        self.curr_state = STATE.RETURN_TO_BASE
        self.turn_towards(self.start_pos[0], self.start_pos[1], Globals.FAST)
