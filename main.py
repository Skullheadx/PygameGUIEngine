import pygame
from color import Color
from rectangle import Rectangle
from text import Text, Label
from button import Button
from container import VBoxContainer, HBoxContainer, GridContainer
from image import Image

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
delta = 0

# Testing Text
# a = Text(100, 100, "Hello World", "Arial", 20, color=Color.RED)
# b = Label(100, 200, "Word hunt", "Imprint Shadow", 20, Color.RED, Color.BLACK, Color.BLACK, 1, 15)
# c = Rectangle(100, 300, 100, 100, (255, 0, 0))
# d = Button(100, 200, "Play", "Imprint Shadow", 40, Color.BLUE, Color.BLACK, Color.BLACK, 1, 15, 20,
#            lambda: print("Hello World"))
# e = Button(100, 300, "Quit", "Imprint Shadow", 40, Color.BLUE, Color.BLACK, Color.BLACK, 1, 15, 20,
#            lambda: print("Goodbye World"))
# f = HBoxContainer(400, 25, Color.WHITE, Color.BLACK, 1, 15, 20, 10, True, [d, e])
# f.add_child(a)
#
# g = Image(0, 0, "image.PNG", Color.BLACK, 5)
# g.resize(200, 200)
# f.add_child(c)

p = Rectangle(0, 0, 100, 100, Color.WHITE, Color.BLACK, 1, 0)
q = Text(0, 0, "Hello World", "Arial", 20, color=Color.RED)
r = Button(0, 0, "Play", "Imprint Shadow", 40, Color.BLUE, Color.BLACK, Color.BLACK, 1, 15, 20,
           lambda: print("Hello World"))
# s = Rectangle(0, 0, 100, 100, Color.BLUE, Color.BLACK, 1, 0)
s = Image(0, 0, "image.PNG", Color.BLACK, 5)
# s.resize(300, 200)
s.resize(100, 100)
t = GridContainer(100, 100, 2, 2,Color.LIGHT_GRAY,Color.BLACK, 1,15,10,20, children=[[p, q], [r, s]])
# t = VBoxContainer(100, 100, Color.LIGHT_GRAY, Color.BLACK, 1, 15, 10, 10, True, [p, q, r, s])

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((255, 255, 255))

    # a.draw(screen)
    # b.move(delta * 10, delta * 10)
    # b.set_text(str(round(clock.get_fps())) + " FPS")
    # b.draw(screen)
    # c.draw(screen)
    #
    # d.update()
    # d.draw(screen)
    #
    # e.update()
    # e.draw(screen)
    #
    # f.update()
    # f.move(delta * -40, 0)
    # f.draw(screen)
    #
    # g.move(0, delta * 25)
    # g.draw(screen)

    t.update()
    t.move(delta * 20, 0)
    t.draw(screen)

    pygame.display.update()
    delta = clock.tick(60) / 1000  # Seconds since last frame

pygame.quit()
