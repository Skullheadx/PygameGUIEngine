import pygame
from color import Color
from rectangle import Rectangle


class Slider:
    slider_thickness = 4
    def __init__(self, x, y, width, height, min_val=0, max_val=100, default=0, background_color=Color.WHITE,
                 slider_color=Color.BLACK, border_color=Color.BLACK, border_width=1, border_radius=0, padding=15):
        self.x = x
        self.y = y
        self.background_color = background_color
        self.slider_color = slider_color
        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.padding = padding
        self.width = width + 2 * self.padding
        self.height = height + 2 * self.padding

        self.value = default
        self.min_value = min_val
        self.max_value = max_val

        self.rect = Rectangle(self.x - self.padding, self.y - self.padding, self.width, self.height,
                              self.background_color,
                              self.border_color, self.border_width, self.border_radius)
        self.is_hover = False
        self.is_pressed = False
        self.is_clicked = False

        self.hover_color = Color.darken(self.background_color, 20)
        self.pressed_color = Color.darken(self.background_color, 40)

        self.last_click = 0
        self.still_pressed = False
        self.click_disabled = False

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = max(min(value, self.max_value), self.min_value)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.set_position(x - self.padding, y - self.padding)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.move(dx, dy)

    def set_background_color(self, background_color):
        self.background_color = background_color

    def set_slider_color(self, slider_color):
        self.slider_color = slider_color

    def update(self):
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()

        self.is_hover = self.rect.collidepoint(mouse_pos)
        if mouse_pressed and not self.is_hover:
            self.click_disabled = True
        if self.click_disabled:
            if not mouse_pressed:
                self.click_disabled = False
            else:
                if self.is_hover:
                    self.rect.set_background_color(self.hover_color)
                else:
                    self.rect.set_background_color(self.background_color)
                return
        self.is_clicked = self.is_hover and not mouse_pressed and self.is_pressed
        self.is_pressed = self.is_hover and mouse_pressed

        if self.is_pressed:
            self.rect.set_background_color(self.pressed_color)
            self.set_value(self.min_value + (self.max_value - self.min_value) * (
                    mouse_pos[0] - self.x) / (self.width - 2 * self.padding))
        elif self.is_hover:
            self.rect.set_background_color(self.hover_color)
        else:
            self.rect.set_background_color(self.background_color)

    def draw(self, screen):
        self.rect.draw(screen)
        pygame.draw.line(screen, self.border_color, (self.x, self.y + (self.height - 2 * self.padding) // 2),
                         (self.x + self.width - 2 * self.padding, self.y + (self.height - 2 * self.padding) // 2), 3)
        pygame.draw.rect(screen, self.slider_color,
                         (self.x + (self.width - 2 * self.padding) * (self.value - self.min_value) / (self.max_value - self.min_value) - self.slider_thickness//2,
                          self.y, self.slider_thickness, self.height - 2 * self.padding))
