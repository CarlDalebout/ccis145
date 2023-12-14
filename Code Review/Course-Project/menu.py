import pygame
import sys

class GameMenu:
    def __init__(self):
        self.width, self.height = 564, 317
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game Menu")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

    def show_menu(self):
        self.screen.fill((255, 255, 255))

        text = self.font.render("Press Space to start", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(text, text_rect)

        text = self.font.render("Press 'R' for Rules", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 + 0))
        self.screen.blit(text, text_rect)

        text = self.font.render("Press 'S' for Score", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 + 50))
        self.screen.blit(text, text_rect)

        pygame.display.flip()

    def start_game(self):
        print("Game is starting...")
        # Add your game logic here

    def show_rules(self):
        print("Game Rules:")
        # Add your rules here

    def show_score(self):
        print("Game Score:")
        # Add your scoring logic here

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start_game()
                        running = False
                    elif event.key == pygame.K_r:
                        self.show_rules()
                    elif event.key == pygame.K_s:
                        self.show_score()

            self.show_menu()
            self.clock.tick(30)


if __name__ == "__main__":
    pygame.init()
    game_menu = GameMenu()
    game_menu.run()
