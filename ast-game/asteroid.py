from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position,self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        split_v1 = self.velocity.rotate(split_angle)
        split_v2 = self.velocity.rotate(-split_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_rad)
        ast2 = Asteroid(self.position.x, self.position.y, new_rad)
        ast1.velocity = split_v1 * 1.2
        ast2.velocity = split_v2 * 1.2