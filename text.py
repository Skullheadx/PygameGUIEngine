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
        self.text_color = color

        self.text_surface = self.font.render(self.text, True, self.text_color)

    def get_width(self):
        return self.text_surface.get_width()

    def get_height(self):
        return self.text_surface.get_height()

    def update_text(self):
        self.text_surface = self.font.render(self.text, True, self.text_color)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def set_text(self, text):
        self.text = text
        self.update_text()

    def set_font(self, font, font_size):
        self.font_size = font_size
        self.font = pygame.font.SysFont(font, font_size)
        self.update_text()

    def set_color(self, text_color):
        self.text_color = text_color
        self.update_text()

    def center(self, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.set_position(x - self.text_surface.get_width() / 2, y - self.text_surface.get_height() / 2)

    def draw(self, screen):
        screen.blit(self.text_surface, (self.x, self.y))


class Label(Text):

    def __init__(self, x, y, text, font, font_size, background_color, text_color, border_color=Color.BLACK,
                 border_width=0, border_radius=0, padding=10):
        super().__init__(x, y, text, font, font_size, text_color)
        self.background_color = background_color
        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.padding = padding

        self.width = self.text_surface.get_width() + self.padding * 2
        self.height = self.text_surface.get_height() + self.padding * 2
        self.rect = Rectangle(self.x - self.padding, self.y - self.padding, self.width, self.height,
                              self.background_color, self.border_color, self.border_width, self.border_radius)

    def get_width(self):
        return self.text_surface.get_width() + self.padding * 2

    def get_height(self):
        return self.text_surface.get_height() + self.padding * 2

    def set_position(self, x, y):
        super().set_position(x, y)
        self.rect.set_position(self.x - self.padding, self.y - self.padding)

    def move(self, dx, dy):
        super().move(dx, dy)
        self.rect.move(dx, dy)

    def update_text(self):
        super().update_text()
        self.width = self.text_surface.get_width() + self.padding * 2
        self.height = self.text_surface.get_height() + self.padding * 2
        self.rect.set_size(self.width, self.height)

    def draw(self, screen):
        self.rect.draw(screen)
        super().draw(screen)
