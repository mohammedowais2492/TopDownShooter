import pygame

"""
This class represents the basic enemy type in the game.
"""
class BasicEnemy:
    """
    Constructor for the BasicEnemy.
    """
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    """
    Method to move the enemy. The enemy always moves downward.
    """
    def move(self):
        self.y += self.speed

    """
    Method to draw the enemy
    """
    def draw(self, screen):
        bottom_point = (self.x + self.width // 2, self.y + self.height)
        top_left = (self.x, self.y)
        top_right = (self.x + self.width, self.y)

        pygame.draw.polygon(screen, self.color, [bottom_point, top_left, top_right])


    """
    Method to get the enclosing rectangle of the enemy
    """
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
