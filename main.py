import pygame
from rectangle import Rectangle

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
delta = 0

# Testing Rectangle
r = Rectangle(100, 100, 100, 100, (255, 0, 0))
r2 = Rectangle(200, 200, 100, 100, (0, 255, 0), (0, 0, 255), 5, 10)
r3 = Rectangle(300, 300, 100, 100, (0, 0, 255), (255, 0, 0), 5, 10)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((255, 255, 255))

    r.draw(screen)
    r2.draw(screen)
    r3.move(delta * 10, delta * 10)
    r3.draw(screen)

    pygame.display.update()
    delta = clock.tick(60) / 1000  # Seconds since last frame

pygame.quit()
