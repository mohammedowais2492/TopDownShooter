import math
import pygame
import random

from Stars.shooting_star import ShootingStar
from Stars.star import Star

class Background:
    def __init__(self, width, height, number_of_stars):
        self.stars = []
        self.shooting_stars = []
        colors = [(255, 255, 255), (180, 180, 255), (200, 200, 200)]

        for _ in range(number_of_stars):
            base_x = random.randint(0, width)
            self.stars.append(Star(
                base_x = base_x,
                x = base_x,
                y = random.randint(0, height),
                speed = random.uniform(0.5, 2.0),
                color = random.choice(colors),
                phase = random.uniform(0, 2 * math.pi),
                size = random.randint(1, 2)
            ))

    def draw(self, screen, width, height):
        time_offset = pygame.time.get_ticks() / 1000

        for star in self.stars:
            star.draw(screen, width, height, time_offset)

        if random.random() < 0.02:
            self.shooting_stars.append(ShootingStar(width, height))

        for star in self.shooting_stars:
            star.update()
            star.draw(screen)
            if star.is_expired():
                self.shooting_stars.remove(star)