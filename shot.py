from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    velocity = 0
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS 

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

