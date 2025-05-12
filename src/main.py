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
        speed =3
    )

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

    # Create an enemy instance
    enemy = BasicEnemy(x = WIDTH // 2, y = 0, width = 50, height = 50, color = (0, 255, 0), speed = 2)
    enemy_respawn_time = None

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

        if enemy:
            for bullet in player.bullets:
                if bullet.get_rect().colliderect(enemy.get_rect()):
                    player.bullets.remove(bullet)
                    enemy = None
                    enemy_respawn_time = pygame.time.get_ticks() + 1000
                    break

        if not enemy and enemy_respawn_time:
            if pygame.time.get_ticks() >= enemy_respawn_time:
                enemy = spawn_enemy(WIDTH)
                enemy_respawn_time = None

        # Draw everything
        screen.fill((30, 30, 30))
        player.draw(screen)
        if enemy:
            enemy.move()
            enemy.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

initialize()


