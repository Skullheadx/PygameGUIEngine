import pygame
from color import Color
from rectangle import Rectangle


class Text:

    def __init__(self, x, y, text, font, font_size, color=Color.BLACK):
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.SysFont(font, self.font_size)
        self.color = color

        self.text_surface = self.font.render(self.text, True, self.color)

    def update(self):
        self.text_surface = self.font.render(self.text, True, self.color)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def set_text(self, text):
        self.text = text
        self.update()

    def set_font(self, font, font_size):
        self.font_size = font_size
        self.font = pygame.font.SysFont(font, font_size)
        self.update()

    def set_color(self, color):
        self.color = color
        self.update()

    def draw(self, screen):
        screen.blit(self.text_surface, (self.x, self.y))
