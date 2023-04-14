import pygame
from color import Color
from text import Label


class Button(Label):
    cooldown = 0.2 # seconds
    def __init__(self, x, y, text, font, size, text_color=Color.BLACK, background=Color.WHITE, border_color=Color.BLACK,
                 border_width=1, border_radius=0, padding=10, func=None):
        super().__init__(x, y, text, font, size, text_color, background, border_color, border_width, border_radius, padding)
        self.is_hover = False
        self.is_pressed = False
        self.is_clicked = False

        self.func = func

        self.hover_color = Color.darken(self.background_color, 20)
        self.pressed_color = Color.darken(self.background_color, 40)

        self.last_click = 0
        self.still_pressed = False


    def update(self):
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()

        self.is_hover = self.rect.collidepoint(mouse_pos)
        self.is_clicked = self.is_hover and not mouse_pressed and self.is_pressed
        self.is_pressed = self.is_hover and mouse_pressed

        if self.still_pressed and not self.is_pressed:
            self.still_pressed = False

        if self.is_pressed:
            if pygame.time.get_ticks() - self.last_click > self.cooldown * 1000 and not self.still_pressed:
                self.still_pressed = True
                self.last_click = pygame.time.get_ticks()

                self.rect.set_background_color(self.pressed_color)
                if self.func is not None:
                    self.func()

        elif self.is_hover:
            self.rect.set_background_color(self.hover_color)
        else:
            self.rect.set_background_color(self.background_color)

    def draw(self, screen):
        self.rect.draw(screen)
        super().draw(screen)
