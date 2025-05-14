import math
import random

import pygame

"""
Python class for a regular star.
"""
class Star:
    def __init__(self, base_x, x, y, speed, size, color, phase):
        self.base_x = base_x
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.color = color
        self.phase = phase

    def draw(self, screen, width, height, time_offset):
        self.y += self.speed
        if self.y > height:
            self.y = 0
            self.base_x = random.randint(0, width)
            self.phase = random.uniform(0, 2 * math.pi)

        self.x = self.x + math.sin(self.phase + time_offset) * 2

        brightness = int(100 + 155 * abs(math.sin(time_offset + self.phase)))
        color = (brightness, brightness, brightness)

        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
