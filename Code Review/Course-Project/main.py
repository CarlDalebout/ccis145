import pygame
import sys
import random
import os
import menu

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 564, 317
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player Base
player_base_width, player_base_height = 20, HEIGHT // 10
player_base_x = 0
player_base_y = HEIGHT - player_base_height - 20
player_base_health = 100
player_spawn_interval = 60  # frames between unit spawns
player_spawn_timer = player_spawn_interval


# Enemy Base
enemy_base_width, enemy_base_height = 20, HEIGHT // 10
enemy_base_x = WIDTH - enemy_base_width
enemy_base_y = HEIGHT - player_base_height - 20
enemy_base_health = 100
enemy_spawn_interval = 90  # frames between enemy spawns
enemy_spawn_timer = enemy_spawn_interval

# Units
player_units = []
enemy_units = []

# Button
button_width, button_height = 200, 40
button_x, button_y = WIDTH // 2 - button_width // 2, 0 
button_color = (0, 255, 0)
button_clicked = False

# Load spearman image
spearman_image = pygame.image.load(os.path.join("images-sounds", "spear-man.png"))
spearman_image = pygame.transform.scale(spearman_image,(40,20))

# Load background image
background_image = pygame.image.load(os.path.join("images-sounds", "background.jpg"))
background_image = pygame.transform.scale(background_image, (564, 317))

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(os.path.join("images-sounds", "Era Warfare"))
clock = pygame.time.Clock()

# Initialize Pygame mixer
pygame.mixer.init()

# Load background music and battle sounds
background_music = pygame.mixer.Sound(os.path.join("images-sounds", "background-music.mp3"))
background_music.set_volume(0.3)
battle_cry_sound = pygame.mixer.Sound(os.path.join("images-sounds", "battle-cry.wav"))
battle_cry_sound.set_volume(10.0)
sword_strike_sound = pygame.mixer.Sound(os.path.join("images-sounds", "sword-strike.wav"))
sword_strike_sound.set_volume(1.0)


def check_collision(unit1, unit2):
    return (
        unit1[0] < unit2[0] + spearman_image.get_width()
        and unit1[0] + spearman_image.get_width() > unit2[0]
        and unit1[1] < unit2[1] + spearman_image.get_height()
        and unit1[1] + spearman_image.get_height() > unit2[1]
    )

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

# Menu loop
main_menu = menu.GameMenu()
main_menu.run()
        

#play music
background_music.play(-1)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button is clicked
            if button.rect.collidepoint(event.pos):
                button_clicked = True

    
    # Player base logic
    player_spawn_timer -= 1
    if player_spawn_timer <= 0 and button_clicked:
        player_units.append([player_base_x, player_base_y, 5, 10, True])  # x, y, speed, damage, moving
        player_spawn_timer = player_spawn_interval
        button_clicked = False
        # Play the battle cry sound
        battle_cry_sound.play()

    # Enemy base logic
    enemy_spawn_timer -= 1
    if enemy_spawn_timer <= 0:
        enemy_units.append([enemy_base_x - 40, player_base_y, -3, 10, True])  # x, y, speed, damage, moving
        enemy_spawn_timer = enemy_spawn_interval

    # Update units
    for unit in player_units:
        if unit[4]:  # Check if the unit is moving
            unit[0] += unit[2]
            if unit[0] > WIDTH - 50:  # reached enemy base
                unit[4] = False  # stop moving

    for unit in enemy_units:
        if unit[4]:  # Check if the unit is moving
            unit[0] += unit[2]
            if unit[0] < 0:  # reached player base
                unit[4] = False  # stop moving

    # Check for unit collisions
    for player_unit in player_units:
        for enemy_unit in enemy_units:
            if check_collision(player_unit, enemy_unit):
                player_unit[4] = False  # stop moving
                enemy_unit[4] = False  # stop moving

                player_unit[3] -= 1  # reduce player unit's health
                enemy_unit[3] -= 1   # reduce enemy unit's health

                # Play the sword strike sound
                sword_strike_sound.play()

                if player_unit[3] <= 0:
                    player_units.remove(player_unit)

                if enemy_unit[3] <= 0:
                    enemy_units.remove(enemy_unit)

    # Draw background
    screen.blit(background_image, (0, 0))

    # Draw player units
    for unit in player_units:
        screen.blit(spearman_image, (unit[0], unit[1]))

    # Draw enemy units
    for unit in enemy_units:
        screen.blit(spearman_image, (unit[0], unit[1]))

    # Draw everything else
    pygame.draw.rect(screen, RED, (player_base_x, player_base_y, player_base_width, player_base_height))
    pygame.draw.rect(screen, BLUE, (enemy_base_x, enemy_base_y, enemy_base_width, enemy_base_height))

    # Draw health bars
    pygame.draw.rect(screen, RED, (50, HEIGHT - 20, player_base_health * 2, 20))
    pygame.draw.rect(screen, BLUE, (WIDTH - 50 - enemy_base_health * 2, HEIGHT - 20, enemy_base_health * 2, 20))

    # Draw button
    button = Button(button_x, button_y, button_width, button_height, button_color, "Spawn Troops")
    button.draw(screen)

    # Check for game over
    if player_base_health <= 0 or enemy_base_health <= 0:
        print("Game Over!")
        background_music.stop()
        running = False

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
