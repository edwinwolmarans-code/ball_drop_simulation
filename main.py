import pygame
import pymunk
import random

WIDTH = 800
HEIGHT = 800
FPS = 80

BACKGROUND = (238, 247, 255)
BLACK = (0, 0, 0)
COLOURS = [(20, 63, 107), (245, 83, 83), (254, 177, 57), (246, 245, 77), (242, 102, 171), (164, 89, 209), (44, 211, 225),
           (100, 153, 233), (158, 221, 255), (131, 111, 255), (21, 245, 186), (255, 32, 78), (5, 146, 18), (6, 208, 1)]


def new_ball(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 10)
    shape.density = 1
    shape.elasticity = 0.9
    space.add(body, shape)
    balls.append(shape)
    ball_colours.append(COLOURS[random.randint(0, 13)])
    return space


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

space = pymunk.Space()
space.gravity = (0, 400)

# create border segments
top_segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
top_segment_shape = pymunk.Segment(top_segment_body, (10, 10), (WIDTH-10, 10), 3)
top_segment_shape.elasticity = 0.9
space.add(top_segment_body, top_segment_shape)

right_segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
right_segment_shape = pymunk.Segment(right_segment_body, (WIDTH-10, 10), (WIDTH-10, HEIGHT-10), 3)
right_segment_shape.elasticity = 0.9
space.add(right_segment_body, right_segment_shape)

bottom_segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
bottom_segment_shape = pymunk.Segment(bottom_segment_body, (10, WIDTH-10), (HEIGHT-10, WIDTH-10), 3)
bottom_segment_shape.elasticity = 0.9
space.add(bottom_segment_body, bottom_segment_shape)

left_segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
left_segment_shape = pymunk.Segment(left_segment_body, (10, 10), (10, HEIGHT-10), 3)
left_segment_shape.elasticity = 0.9
space.add(left_segment_body, left_segment_shape)

balls = []
ball_colours = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for _ in range(random.randint(1, 5)):
                new_ball(space, event.pos)
    window.fill(BACKGROUND)

    # borders (top, right, bottom, left)
    pygame.draw.line(window, BLACK, (10, 10), (WIDTH-10, 10), 3)
    pygame.draw.line(window, BLACK, (WIDTH-10, 10), (WIDTH-10, HEIGHT-10), 3)
    pygame.draw.line(window, BLACK, (10, WIDTH-10), (HEIGHT-10, WIDTH-10), 3)
    pygame.draw.line(window, BLACK, (10, 10), (10, HEIGHT-10), 3)

    for ball in balls:
        x_position = int(ball.body.position[0])
        y_position = int(ball.body.position[1])
        pygame.draw.circle(window, ball_colours[balls.index(ball)], (x_position, y_position), 10)

    pygame.display.flip()
    clock.tick(FPS)
    space.step(1/FPS)

pygame.quit()







# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

