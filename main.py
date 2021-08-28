import assets
import sys, pygame

from pygame import Rect
from pygame import draw
from pygame.event import Event

from assets.entity import Snake, Food


def main():
    SIZE = WIDTH, HEIGHT = 640, 480
    BLACK = 10, 10, 10

    SCREEN = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(320, 320)
    pygame.init()

    MOVE_EVENT = Event(666)
    pygame.time.set_timer(MOVE_EVENT, 100)

    while True:
        has_collision = False
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event == MOVE_EVENT:
                snake.move()
                has_collision = snake.has_collision(food.body)
        if has_collision:
            snake.increment()
            food.reposition(SCREEN)
        food.draw(SCREEN)
        snake.draw(SCREEN)
        snake.key_handler()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
