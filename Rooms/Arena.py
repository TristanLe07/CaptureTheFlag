from GameFrame import Level, Globals, RedFlag, BlueFlag, TextObject, DangerZone,BotNumber
from GameFrame.Logo import Logo
from Objects import Red1, Red2, Red3, Red4, Red5
from Objects import Blue1, Blue2, Blue3, Blue4, Blue5


class Arena(Level):
    OUT_OF_BOUNDS = -1000

    def __init__(self, screen):
        Level.__init__(self, screen)

        self.set_background_image("background.png")

        self.init_bots()
        self.init_flags()
        self.init_team_name_and_logo()
        self.init_timer_and_score()
        self.init_jail_walls()

        # Sounds
        self.danger_siren = self.load_sound("danger_siren.ogg")
        Globals.background_music = self.load_sound("battle-music.ogg")
        Globals.background_music.play(-1)

    def init_bots(self):
        Globals.red_bots.append(Red1(self, Globals.SCREEN_WIDTH - 250, Globals.SCREEN_HEIGHT / 4))
        Globals.blue_bots.append(Blue1(self, 108, Globals.SCREEN_HEIGHT / 3))
        Globals.red_bots.append(Red2(self, Globals.SCREEN_WIDTH - 250, Globals.SCREEN_HEIGHT / 4 * 2))
        Globals.blue_bots.append(Blue2(self, 108, Globals.SCREEN_HEIGHT / 3 * 2))
        Globals.red_bots.append(Red3(self, Globals.SCREEN_WIDTH - 250, Globals.SCREEN_HEIGHT / 4 * 3))
        Globals.blue_bots.append(Blue3(self, 228, Globals.SCREEN_HEIGHT / 4))
        Globals.red_bots.append(Red4(self, Globals.SCREEN_WIDTH - 140, Globals.SCREEN_HEIGHT / 3))
        Globals.blue_bots.append(Blue4(self, 228, Globals.SCREEN_HEIGHT / 4 * 2))
        Globals.red_bots.append(Red5(self, Globals.SCREEN_WIDTH - 140, Globals.SCREEN_HEIGHT / 3 * 2))
        Globals.blue_bots.append(Blue5(self, 228, Globals.SCREEN_HEIGHT / 4 * 3))
        number = 1
        team = 'red'
        for i in range(len(Globals.red_bots)):
            self.add_room_object(Globals.red_bots[i])
            self.add_room_object(BotNumber(self,10,10,number,team))
            number +=1
        number = 1
        team = 'blue'
        for i in range(len(Globals.blue_bots)):
            self.add_room_object(Globals.blue_bots[i])
            Globals.blue_bots[i].rotate(180)
            self.add_room_object(BotNumber(self,10,10,number,team))
            number +=1
    def init_team_name_and_logo(self):
        # Team Names
        TEAM_NAME_MAX_WIDTH = 158

        red_first_string, red_second_string = TextObject.split_half_on_space(Globals.red_team_name)
        if len(red_second_string) > 0:
            self.red_name_text = TextObject(self, 0, Globals.SCREEN_HEIGHT - 56 - 5, red_first_string, 25)
            self.add_room_object(self.red_name_text)
            self.red_name_text.set_max_width(TEAM_NAME_MAX_WIDTH)
            self.red_name_text.x = Globals.SCREEN_WIDTH - 82 - self.red_name_text.get_text_width()

            self.red_name_text_second = TextObject(self, 0, Globals.SCREEN_HEIGHT - 56 + 15, red_second_string, 25)
            self.add_room_object(self.red_name_text_second)
            self.red_name_text_second.set_max_width(TEAM_NAME_MAX_WIDTH)
            self.red_name_text_second.x = Globals.SCREEN_WIDTH - 82 - self.red_name_text_second.get_text_width()
        else:
            self.red_name_text = TextObject(self, 0, Globals.SCREEN_HEIGHT - 56, Globals.red_team_name, 35)
            self.add_room_object(self.red_name_text)
            self.red_name_text.set_max_width(TEAM_NAME_MAX_WIDTH)
            self.red_name_text.x = Globals.SCREEN_WIDTH - 82 - self.red_name_text.get_text_width()

        blue_first_string, blue_second_string = TextObject.split_half_on_space(Globals.blue_team_name)
        if len(blue_second_string) > 0:
            self.blue_name_text = TextObject(self, 84, Globals.SCREEN_HEIGHT - 56 - 5, blue_first_string, 25)
            self.add_room_object(self.blue_name_text)
            self.blue_name_text.set_max_width(TEAM_NAME_MAX_WIDTH)

            self.blue_name_text_second = TextObject(self, 84, Globals.SCREEN_HEIGHT - 56 + 15, blue_second_string, 25)
            self.add_room_object(self.blue_name_text_second)
            self.blue_name_text_second.set_max_width(TEAM_NAME_MAX_WIDTH)
        else:
            self.blue_name_text = TextObject(self, 84, Globals.SCREEN_HEIGHT - 56, Globals.blue_team_name, 35)
            self.add_room_object(self.blue_name_text)
            self.blue_name_text.set_max_width(TEAM_NAME_MAX_WIDTH)

        # Team Logos
        blue_team_logo = Logo(self, 266, Globals.SCREEN_HEIGHT - 54, Globals.blue_team_logo, 44, 44)
        self.add_room_object(blue_team_logo)
        red_team_logo = Logo(self, 0, Globals.SCREEN_HEIGHT - 54, Globals.red_team_logo, 44, 44)
        self.add_room_object(red_team_logo)
        red_team_logo.x = Globals.SCREEN_WIDTH - 266 - red_team_logo.width

    def init_flags(self):
        Globals.red_flag = RedFlag(self, 200, Globals.SCREEN_HEIGHT / 2 - 26)
        Globals.blue_flag = BlueFlag(self, Globals.SCREEN_WIDTH - 232, Globals.SCREEN_HEIGHT / 2 - 26)
        self.add_room_object(Globals.red_flag)
        self.add_room_object(Globals.blue_flag)
        self.red_danger_zone = DangerZone(self, 0, -128)
        self.blue_danger_zone = DangerZone(self, 0, -128)
        self.can_update_red_danger = True
        self.can_update_blue_danger = True
        self.add_room_object(self.red_danger_zone)
        self.add_room_object(self.blue_danger_zone)

    def init_timer_and_score(self):
        # Timer countdown text
        self.counter = 3600
        self.seconds = 120
        text_minutes = int(self.seconds / 60)
        text_seconds = self.seconds % 60
        self.counter_text = TextObject(self, 0, 8, "{}:{:02d}".format(text_minutes, text_seconds), 40)
        self.add_room_object(self.counter_text)

        # Team scores text
        self.blue_score_text = TextObject(self, 0, 10, str(Globals.blue_enemy_side_time), 28, "moby_monospace")
        self.add_room_object(self.blue_score_text)
        self.blue_score_text.x = (Globals.SCREEN_WIDTH / 2) - 80 - self.blue_score_text.get_text_width()

        self.red_score_text = TextObject(
            self, (Globals.SCREEN_WIDTH / 2) + 86, 10, str(Globals.red_enemy_side_time), 28, "moby_monospace"
        )
        self.add_room_object(self.red_score_text)
        self.red_score_text.x = (Globals.SCREEN_WIDTH / 2) + 240 - self.red_score_text.get_text_width()

        self.set_timer(3600, self.timed_out)
        self.update_screen_text()

    def tick(self):
        self.counter -= 1

        if self.can_update_blue_danger:
            for bot in Globals.blue_bots:
                if bot.point_to_point_distance(bot.x, bot.y, Globals.blue_flag.x, Globals.blue_flag.y) < 50:
                    self.can_update_blue_danger = False
                    self.danger_siren.play()
                    self.set_timer(20, self.end_blue_danger)
                    break
        else:
            self.blue_danger_zone.x = Globals.blue_flag.x - 50
            self.blue_danger_zone.y = Globals.blue_flag.y - 50

        if self.can_update_red_danger:
            for bot in Globals.red_bots:
                if bot.point_to_point_distance(bot.x, bot.y, Globals.red_flag.x, Globals.red_flag.y) < 50:
                    self.can_update_red_danger = False
                    self.danger_siren.play()
                    self.set_timer(20, self.end_red_danger)
                    break
        else:
            self.red_danger_zone.x = Globals.red_flag.x - 50
            self.red_danger_zone.y = Globals.red_flag.y - 50

    def end_blue_danger(self):
        self.blue_danger_zone.y = -self.red_danger_zone.y_size
        self.can_update_blue_danger = True

    def end_red_danger(self):
        self.red_danger_zone.y = -self.blue_danger_zone.y_size
        self.can_update_red_danger = True

    def update_screen_text(self):
        self.seconds -= 1
        text_minutes = int(self.seconds / 60)
        text_seconds = self.seconds % 60
        self.counter_text.text = "{}:{:02d}".format(text_minutes, text_seconds)
        self.counter_text.update_text()
        self.counter_text.x = Globals.SCREEN_WIDTH / 2 - 48

        self.blue_score_text.text = f"{Globals.blue_enemy_side_time:06d}"
        self.blue_score_text.update_text()
        self.blue_score_text.x = (Globals.SCREEN_WIDTH / 2) - 80 - self.blue_score_text.get_text_width()

        self.red_score_text.text = f"{Globals.red_enemy_side_time:06d}"
        self.red_score_text.update_text()
        self.red_score_text.x = (Globals.SCREEN_WIDTH / 2) + 240 - self.red_score_text.get_text_width()

        if self.counter > 0:
            self.set_timer(30, self.update_screen_text)

    def init_jail_walls(self):
        self.blue_jail = Logo(
            self,
            self.OUT_OF_BOUNDS,
            self.OUT_OF_BOUNDS,
            "blue_jail_bars.png",
        )
        self.add_room_object(self.blue_jail)

        self.red_jail = Logo(
            self,
            self.OUT_OF_BOUNDS,
            self.OUT_OF_BOUNDS,
            "red_jail_bars.png",
        )
        self.add_room_object(self.red_jail)
        self.update_jail_walls()

    def update_jail_walls(self):
        # Update the jail walls every second
        blue_bots_in_jail = False
        red_bot_in_jail = False

        self.blue_jail.x = self.OUT_OF_BOUNDS
        self.blue_jail.y = self.OUT_OF_BOUNDS
        self.red_jail.x = self.OUT_OF_BOUNDS
        self.red_jail.y = self.OUT_OF_BOUNDS

        for bot in Globals.red_bots:
            if bot.jailed:
                self.red_jail.x = Globals.GAME_AREA_WIDTH_MAX - self.red_jail.width
                self.red_jail.y = Globals.GAME_AREA_HEIGHT_MAX - self.red_jail.height
                break

        for bot in Globals.blue_bots:
            if bot.jailed:
                self.blue_jail.x = Globals.GAME_AREA_WIDTH_MIN
                self.blue_jail.y = Globals.GAME_AREA_HEIGHT_MIN
                break

        self.set_timer(5, self.update_jail_walls)

    def timed_out(self):
        if Globals.red_enemy_side_time > Globals.blue_enemy_side_time:
            Globals.winner = Globals.RED_FLAG_WINNER
        elif Globals.blue_enemy_side_time > Globals.red_enemy_side_time:
            Globals.winner = Globals.BLUE_FLAG_WINNER
        else:
            Globals.winner = "Draw"
        self.running = False
