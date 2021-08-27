import sys, pygame

from pygame import Rect
from pygame import draw
from pygame.event import Event

from assets.entity import Snake


def main():
    SIZE = WIDTH, HEIGHT = 640, 480
    BLACK = 10, 10, 10

    SCREEN = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    snake = Snake()
    forma = Rect(40, 40, 40, 40)
    pygame.init()

    MOVE_EVENT = Event(666)
    pygame.time.set_timer(MOVE_EVENT, 250)

    while True:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event == MOVE_EVENT:
                snake.move()
        snake.draw(SCREEN)
        snake.key_handler()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
