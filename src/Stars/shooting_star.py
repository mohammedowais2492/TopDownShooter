import pygame
import random

"""
This class represents a shooting star.
"""
class ShootingStar:
    def __init__(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.dx = random.uniform(3, 6)
        self.dy = random.uniform(3, 6)
        self.lifetime = 60

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.lifetime -= 1

    def draw(self, screen):
        end_x = self.x - 10
        end_y = self.y - 5
        pygame.draw.line(screen, (255, 255, 200), (self.x, self.y), (end_x, end_y), 2)

    def is_expired(self):
        return self.lifetime <= 0