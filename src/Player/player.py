import pygame
from pygame import time
from Bullet.bullet import Bullet

"""
This class represents the player in this game. Each player has its own position on the 2d plane, a tuple representing 
the color, width, height, movement speed, time the last bullet was shot and cooldown before the next bullet can be shot.
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
        self.bullets = []
        self.bullet_speed = 10
        self.last_shot_time = 0
        self.cooldown = 300

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
        for bullet in self.bullets:
            bullet.draw(screen)


    """
    Method for shooting.
    """
    def shoot(self):
        current_time = time.get_ticks()
        if current_time - self.last_shot_time >= self.cooldown:
            bullet = Bullet(
                x = self.x + self.width // 2 - 5,
                y = self.y,
                width = 10,
                height = 20,
                color = (255, 255, 0),
                speed = self.bullet_speed
            )
            self.bullets.append(bullet)
            self.last_shot_time = current_time

    """
    Method to update and remove bullets.
    """
    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.y + bullet.height < 0:
                self.bullets.remove(bullet)
