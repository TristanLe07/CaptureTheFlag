from GameFrame import RoomObject


class DangerZone(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.x_size = 128
        self.y_size = 128
        self.set_image(self.load_image("danger_circle.png"), self.x_size, self.y_size)