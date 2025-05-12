import pygame

"""
Class to represent a bullet.
"""
class Bullet:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    """
    Method for bullet movement.
    """
    def move(self):
        self.y -= self.speed

    """
    Method to draw the bullet on the screen.
    """
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    """
    Method to get the enclosing rectangle of the bullet.
    """
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)