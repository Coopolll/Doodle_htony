class object:  # обьекты игры
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_info(self):
        return [self.x, self.y, self.width, self.height]
