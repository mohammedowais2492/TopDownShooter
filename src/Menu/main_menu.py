import pygame

"""
Class for the main menu of the game.
"""
class MainMenu:
    def __init__(self, screen, options, font, spacing = 60):
        self.screen = screen
        self.options = options
        self.font = font
        self.spacing = spacing
        self.selected_index = 0

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    return self.selected_index
        return None

    def draw(self):
        width, height = self.screen.get_size()
        for idx, option in enumerate(self.options):
            color = (255, 255, 0) if idx == self.selected_index else (255, 255, 255)
            text_surface = self.font.render(option, True, color)
            x = width // 2 - text_surface.get_width() // 2
            y = height // 2 + idx * self.spacing
            self.screen.blit(text_surface, (x, y))