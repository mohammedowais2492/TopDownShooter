import pygame
import sys
from Player.player import Player

def initialize():
    #Initialize pygame
    pygame.init()

    #Constants
    FPS = 60

    # Set up the game window
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w - 50, info.current_h - 50
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption('Mexican Standoff')
    clock = pygame.time.Clock()

    # Create player instance
    player = Player(x = WIDTH // 2, y = HEIGHT // 2, width = 50, height = 50, color = (255, 0, 0))

    # Main game loop
    while True:
        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.shoot()

        # Get key states for movement
        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH, HEIGHT)

        player.update_bullets()

        # Draw everything
        screen.fill((30, 30, 30))
        player.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

initialize()


