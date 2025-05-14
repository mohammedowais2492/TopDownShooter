import random

"""
Python class for the stars in the background of the game screen.
"""
class Stars:
    STAR_COLORS = [(255, 255, 255), (180, 180, 255), (200, 200, 200)]

    def __init__(self, width, height):
        self.stars = []
        self.number_of_stars = 50
        for _ in range(self.number_of_stars):
            self.stars.append(
                {
                    'x': random.randint(0, width),
                    'y': random.randint(0, height),
                    'speed': random.uniform(0.5, 2.0),
                    'size': random.randint(1, 2),
                    'color': random.choice(Stars.STAR_COLORS)
                }
            )
