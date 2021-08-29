import sys, pygame

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

    gameover = False
    snake_increment = False
    snake_collision = False
    while not gameover:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event == MOVE_EVENT:
                is_move_possible = snake.move(SCREEN)
                if not is_move_possible:
                    gameover = True
                snake_collision = snake.has_collision(*snake.body[1:])
                snake_increment = snake.has_collision(food.body)
        if snake_collision:
            gameover = True
        if snake_increment:
            snake.increment()
            snake_increment = False
            food.reposition(SCREEN)
        food.draw(SCREEN)
        snake.draw(SCREEN)
        snake.key_handler()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
