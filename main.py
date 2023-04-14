import pygame
from color import Color
from rectangle import Rectangle
from text import Text, Label
from button import Button
from container import VBoxContainer, HBoxContainer, GridContainer
from image import Image
from slider import Slider

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
delta = 0

a = Slider(100, 100, 100, 20, 0, 100, 50, Color.LIGHT_GRAY, Color.DARK_GRAY, 4, 5, 10)
b = Text(100, 100, "Slider", "Arial", 20, Color.BLACK)
c = VBoxContainer(100, 100, Color.LIGHT_GRAY, Color.DARK_GRAY, 4, 5, 10, 0, True, [b, a])

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill(Color.WHITE)
    b.set_text(f"Slider: {round(a.get_value())}")

    c.update()
    c.draw(screen)

    pygame.display.update()
    delta = clock.tick(60) / 1000  # Seconds since last frame

pygame.quit()
