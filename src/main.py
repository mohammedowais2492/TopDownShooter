import pygame
import sys
from Player.player import Player
from Enemy.basic_enemy import BasicEnemy
from Background.background import Background
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

    player_health = 5
    score = 0
    font = pygame.font.SysFont("comicsans", 36)
    game_over_font = pygame.font.SysFont("comicsans", 72)

    # Set up the game window
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w - 50, info.current_h - 50
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption('Alien Invaders')
    clock = pygame.time.Clock()
    background_img = pygame.image.load("../resources/Background.png").convert()
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

    # Create player instance
    player = Player(x = WIDTH // 2, y = HEIGHT // 2, width = 50, height = 50, color = (255, 0, 0))

    # Create an enemy instance
    enemies = [spawn_enemy(WIDTH) for _ in range(3)]

    # Create the background instance
    background = Background(WIDTH, HEIGHT, 150)

    show_main_menu(screen, WIDTH, HEIGHT, background_img)

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
            if enemy.get_rect().colliderect(player.get_rect()):
                enemies.remove(enemy)
                enemies.append(spawn_enemy(WIDTH))
                player_health -= 1
            elif enemy.y > HEIGHT:
                enemies.remove(enemy)
                enemies.append(spawn_enemy(WIDTH))
                player_health -= 1

        # Draw everything
        screen.fill((0, 0, 0))
        background.draw(screen, WIDTH, HEIGHT)
        player.draw(screen)
        for enemy in enemies:
            enemy.move()
            enemy.draw(screen)
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        health_text = font.render("Health: " + str(player_health), True, (255, 255, 255))
        screen.blit(health_text, (10, 40))
        game_over = False
        if player_health <= 0:
            game_over = True
        pygame.display.flip()
        clock.tick(FPS)
        while game_over:
            screen.blit(background_img, (0, 0))
            game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
            final_score_text = game_over_font.render("Final Score: " + str(score), True, (200, 200, 200))
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 60))
            screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    game_over = False
                    player_health = 5
                    score = 0
                    player.bullets.clear()

                    enemies = [spawn_enemy(WIDTH) for _ in range(3)]

                    player.x = WIDTH // 2 - player.width // 2
                    player.y = HEIGHT // 2 - player.height // 2
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    game_over = False
                    player_health = 5
                    score = 0
                    player.bullets.clear()

                    enemies = [spawn_enemy(WIDTH) for _ in range(3)]

                    player.x = WIDTH // 2 - player.width // 2
                    player.y = HEIGHT // 2 - player.height // 2
                    show_main_menu(screen, WIDTH, HEIGHT, background_img)

"""
Function to show the main menu.
"""
def show_main_menu(screen, width, height, background_img):
    waiting = True
    while waiting:
        screen.fill((0, 0, 0))
        title_font =  pygame.font.SysFont("comicsans", 72)
        title_text = title_font.render("Alien Invaders", True, (255, 255, 255))
        start_text = title_font.render("Press any key to start", True, (255, 255, 255))

        screen.blit(background_img, (0, 0))

        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 2 - 60))
        screen.blit(start_text, (width // 2 - start_text.get_width() // 2, height // 2))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False


initialize()


