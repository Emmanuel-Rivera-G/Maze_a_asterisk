# src/maze_a_asterisk/ui/menu.py
import pygame
import sys


class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.bg_color = (30, 30, 60)
        self.text_color = (255, 255, 255)

    def draw_text(self, text, y):
        render = self.font.render(text, True, self.text_color)
        rect = render.get_rect(center=(self.screen.get_width() // 2, y))
        self.screen.blit(render, rect)

    def show_main_menu(self):
        while True:
            self.screen.fill(self.bg_color)
            self.draw_text("🌟 Maze A* Pathfinder 🌟", 100)
            self.draw_text("Presiona S para START", 180)
            self.draw_text("Presiona Q para QUIT", 240)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit(); sys.exit()
                    if event.key == pygame.K_s:
                        return

    def prompt_obstacles(self, min_val=10, max_val=30):
        input_number = ""
        while True:
            self.screen.fill(self.bg_color)
            self.draw_text(f"Cantidad de obstáculos ({min_val}-{max_val}):", 120)
            self.draw_text(input_number, 180)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        try:
                            num = int(input_number)
                            if min_val <= num <= max_val:
                                return num
                            input_number = ""
                        except ValueError:
                            input_number = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_number = input_number[:-1]
                    elif event.unicode.isdigit():
                        input_number += event.unicode
