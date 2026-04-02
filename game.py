import pygame
import sys
from ui import Button, Text
from utils import random_color


class ClickGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Clicker Game")
        self.clock = pygame.time.Clock()

        self.score = 0
        self.running = True

        # Создаем UI элементы
        self.score_text = Text(400, 50, f"Score: {self.score}", 74)
        self.click_button = Button(400, 300, 200, 50, "CLICK ME!", self.on_click)

        print("Game initialized")

    def on_click(self):
        self.score += 1
        self.score_text.update_text(f"Score: {self.score}")
        print(f"Score: {self.score}")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.click_button.check_click(pygame.mouse.get_pos())

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.score_text.draw(self.screen)
        self.click_button.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()