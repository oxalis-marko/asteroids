from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        
        pygame.draw.circle(screen, (255, 255, 255), self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        
        self.position += (self.velocity * dt)