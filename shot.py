from circleshape import CircleShape


class Shot(CircleShape):
    velocity = 0
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pass

    def update(self):
        pass
