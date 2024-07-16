from GameFrame import RoomObject, Globals


class Flag(RoomObject):
    FLAG_SIZE = 32

    def __init__(self, room, x, y, image_file_name, flag_winner):
        RoomObject.__init__(self, room, x, y)
        self.flag_winner = flag_winner
        flag_image = self.load_image(image_file_name)
        self.set_image(flag_image, self.FLAG_SIZE, self.FLAG_SIZE)

        self.depth = 0

    def step(self):
        if (
            self.flag_winner == Globals.RED_FLAG_WINNER
            and self.x > Globals.SCREEN_WIDTH / 2
            or self.flag_winner == Globals.BLUE_FLAG_WINNER
            and self.x < Globals.SCREEN_WIDTH / 2 - self.FLAG_SIZE
        ):
            Globals.winner = self.flag_winner
            self.room.running = False
