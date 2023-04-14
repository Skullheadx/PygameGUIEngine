import pygame
from color import Color
from rectangle import Rectangle
from text import Text, Label
from button import Button


class Container:
    def __init__(self, x, y, width, height, background_color=Color.WHITE, border_color=Color.BLACK, border_width=0,
                 border_radius=0, padding=10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background_color = background_color
        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.padding = padding

        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def draw(self, screen):
        # Draw background
        pygame.draw.rect(screen, self.background_color, (self.x, self.y, self.width, self.height), 0, self.border_radius)

        # Draw border
        pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), self.border_width,
                         self.border_radius)

        # Draw children
        for child in self.children:
            child.draw(screen)