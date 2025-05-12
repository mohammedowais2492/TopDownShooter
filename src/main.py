import pygame
import sys
from Player.player import Player
from Enemy.basic_enemy import BasicEnemy
import random

def spawn_enemy(width):
    x = random.randint(0, width - 50)
    return BasicEnemy(
        x = x,
        y = 0,
        width = 50,
        height = 50,
        color = (0, 255, 0),
        speed = 2
    )

def initialize():
    #Initialize pygame
    pygame.init()

    #Constants
    FPS = 60

    score = 0
    font = pygame.font.SysFont("comicsans", 36)

    # Set up the game window
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w - 50, info.current_h - 50
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption('Mexican Standoff')
    clock = pygame.time.Clock()

    # Create player instance
    player = Player(x = WIDTH // 2, y = HEIGHT // 2, width = 50, height = 50, color = (255, 0, 0))

    # Create an enemy instance
    enemies = [spawn_enemy(WIDTH) for _ in range(3)]

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

        for enemy in enemies:
            for bullet in player.bullets:
                if bullet.get_rect().colliderect(enemy.get_rect()):
                    player.bullets.remove(bullet)
                    enemies.remove(enemy)
                    enemies.append(spawn_enemy(WIDTH))
                    score += 1
                    break

        # Draw everything
        screen.fill((30, 30, 30))
        player.draw(screen)
        for enemy in enemies:
            enemy.move()
            enemy.draw(screen)
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        clock.tick(FPS)

initialize()


