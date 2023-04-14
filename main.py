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

a = Slider(100, 100, 100, 20, 0, 100, 50, Color.LIGHT_GRAY, Color.DARK_GRAY, 1, 1, 0, 15, False)
b = Text(100, 100, "Slider", "Arial", 20, Color.BLACK)
d = Button(100, 100, "Button", "arial", 15, Color.BLACK, Color.LIGHT_GRAY, Color.DARK_GRAY, 4, 5, 10, False,
           lambda: print("Button clicked!"))
e = Image(100, 100, "image.PNG", Color.BLUE, 1)
e.resize(100, 100)
c = GridContainer(10, 10, 2, 2, Color.LIGHT_GRAY, Color.DARK_GRAY, 1, 5, 10, 20, [[a, b], [d, e]])
c.center(x=640 / 2, y=480 / 2)

g = Label(100, 100, "Label", "Arial", 20, Color.BLACK, Color.LIGHT_GRAY, 1, 5, 10, 20)
h = Text(100, 100, "Text", "Arial", 20, Color.BLACK)
i = Rectangle(100, 100, 100, 100, Color.LIGHT_GRAY, Color.DARK_GRAY, 1, 5)
f = VBoxContainer(30, 30, Color.LIGHT_GRAY, Color.DARK_GRAY, 1, 5, 10, 20, True, [g, h, i])

j = Button(100, 100, "Button1", "arial", 15, Color.RED, Color.BLACK, Color.BLACK, 4, 5, 10, True,
           lambda: print("Button1 clicked!"))
k = Button(100, 100, "Button2", "arial", 15, Color.BLACK, Color.LIGHT_GRAY, Color.DARK_GRAY, 4, 5, 10, False,
           lambda: print("Button2 clicked!"))
l = Button(100, 100, "Button3", "arial", 15, Color.BLACK, Color.LIGHT_GRAY, Color.DARK_GRAY, 4, 5, 10, False,
           lambda: print("Button3 clicked!"))
m = Button(100, 100, "Button4", "arial", 15, Color.BLACK, Color.LIGHT_GRAY, Color.DARK_GRAY, 4, 5, 10, False,
           lambda: print("Button4 clicked!"))
n = HBoxContainer(30, 400, Color.LIGHT_GRAY, Color.DARK_GRAY, 1, 5, 10, 20, True, [j, k, l, m])
n.center(x=640 / 2)
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill(Color.WHITE)
    b.set_text(f"Slider: {round(a.get_value())}")

    c.update()
    c.draw(screen)

    f.move(delta * 5, 0)
    f.update()
    f.draw(screen)

    n.update()
    n.draw(screen)

    pygame.display.update()
    delta = clock.tick(120) / 1000  # Seconds since last frame

pygame.quit()
