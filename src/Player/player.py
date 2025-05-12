import pygame

"""
This class represents the player in this game. Each player has its own position on the 2d plane, a tuple representing 
the color, width, height and movement speed.
"""
class Player:
    """
    Constructor for the Player class.
    """
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.speed = 5 # initial speed is 5 for all players

    """
    Method for player movement.
    """
    def move(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.x - self.speed >= 0:
                self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # This check is needed to ensure the right edge of the player is within boundary limits
            if self.x + self.speed + self.width <= screen_width:
                self.x += self.speed
        # In pygame, the origin is the top left corner of the screen and for this reason we subtract on upward
        # movement and add on downward movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y - self.speed >= 0:
                self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # This check is needed to ensure the bottom edge of the player is within boundary limits
            if self.y + self.speed + self.height <= screen_height:
                self.y += self.speed

    """
    Method for drawing the player sprite on the screen.
    """
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

