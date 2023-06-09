import pygame
from color import Color


class Rectangle:

    def __init__(self, x, y, width, height, background_color, border_color=Color.BLACK, border_width=0,
                 border_radius=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background_color = background_color

        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def set_background_color(self, background_color):
        self.background_color = background_color

    def set_border_color(self, border_color):
        self.border_color = border_color

    def collidepoint(self, point):
        return self.x <= point[0] <= self.x + self.width and self.y <= point[1] <= self.y + self.height

    def center(self, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.set_position(x - self.width / 2, y - self.height / 2)

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_color, (self.x, self.y, self.width, self.height),
                         border_radius=self.border_radius)
        pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), self.border_width,
                         border_radius=self.border_radius)
