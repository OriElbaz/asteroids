import pygame
from circleshape import CircleShape
from constants import LINE_WDITH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WDITH)
    
    def update(self, dt):
        self.position += self.velocity * dt
        