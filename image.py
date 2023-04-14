import pygame
from color import Color


class Image:

    def __init__(self, x, y, image_path, border_color=Color.BLACK, border_width=0):
        self.x = x
        self.y = y
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.border_color = border_color
        self.border_width = border_width

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

    def set_image(self, image_path):
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def set_border_color(self, border_color):
        self.border_color = border_color

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.width = width
        self.height = height

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), self.border_width)
