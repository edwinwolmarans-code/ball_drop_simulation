import pygame
import pymunk

WIDTH = 800
HEIGHT = 800
FPS = 80

BACKGROUND = 255, 250, 244
BLACK = (0, 0, 0)
BlUE = (158, 221, 255)
RED = (255, 32, 78)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill(BACKGROUND)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
  






# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

