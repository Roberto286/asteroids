from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH 
from circleshape import CircleShape
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50) 
        first_new_movement = self.velocity.rotate(random_angle)
        second_new_movement = self.velocity.rotate(random_angle * -1)
        first_new_radius = self.radius - ASTEROID_MIN_RADIUS
        second_new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_new = Asteroid(self.position.x, self.position.y, first_new_radius)
        second_new = Asteroid(self.position.x, self.position.y, second_new_radius)
        
        first_new.velocity = first_new_movement * 1.2
        second_new.velocity = second_new_movement * 1.2
