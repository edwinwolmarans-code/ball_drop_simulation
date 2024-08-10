import pygame
import pymunk

WIDTH = 800
HEIGHT = 800
FPS = 80

BACKGROUND = 255, 250, 244
BLACK = (0, 0, 0)
BlUE = (158, 221, 255)
RED = (255, 32, 78)


def new_ball(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 10)
    shape.density = 1
    shape.elasticity = 0.9
    space.add(body, shape)
    balls.append(shape)
    return space


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

space = pymunk.Space()
space.gravity = 0, 200

balls = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_ball(space, event.pos)
    window.fill(BACKGROUND)

    for ball in balls:
        x_position = int(ball.body.position[0])
        y_position = int(ball.body.position[1])
        pygame.draw.circle(window, RED, (x_position, y_position), 10)

    pygame.display.flip()
    clock.tick(FPS)
    space.step(1/FPS)

pygame.quit()







# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

