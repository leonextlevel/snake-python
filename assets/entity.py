import pygame
from random import randint


class Model:
    SIZE = 40


class Food(Model):
    COLOR = 100, 0, 0

    def __init__(self, x, y) -> None:
        self.body = pygame.Rect(x, y, self.SIZE, self.SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.COLOR, self.body)

    def reposition(self, surface):
        x = randint(0, (surface.get_width() // self.SIZE) - 1) * self.SIZE
        y = randint(0, (surface.get_height() // self.SIZE) - 1) * self.SIZE
        self.body.x = x
        self.body.y = y


class Snake(Model):
    COLOR = 0, 200, 0
    DIRECTIONS = {
        'left': (-1, 0),
        'right': (1, 0),
        'up': (0, -1),
        'down': (0, 1),
    }

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.speed = 2
        self.direction = 'right'
        self.body = [
            pygame.Rect(self.x + self.SIZE, self.y, self.SIZE, self.SIZE),
            pygame.Rect(self.x, self.y, self.SIZE, self.SIZE),
            pygame.Rect(self.x, self.y, self.SIZE, self.SIZE),
            pygame.Rect(self.x, self.y, self.SIZE, self.SIZE),
        ]

    def increment(self):
        self.body.append(self.body[-1].copy())

    def move(self, surface):
        for index, part in reversed(list(enumerate(self.body[1:], 1))):
            part.x = self.body[index - 1].x
            part.y = self.body[index - 1].y
        self.body[0].move_ip(
            *[
                value * self.SIZE
                for value in self.DIRECTIONS[self.direction]
            ]
        )
        # Verifica se bateu na parede
        if (
            self.body[0].x < 0 or
            self.body[0].x > surface.get_width() - self.SIZE or
            self.body[0].y < 0 or
            self.body[0].y > surface.get_height() - self.SIZE
        ):
            # Sinaliza que mover não é possivel
            return False
        return True
        

    def has_collision(self, *objs):
        for obj in objs:
            if self.body[0].colliderect(obj):
                return True
        return False

    def key_handler(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.direction != 'right':
            self.direction = 'left'
        if key[pygame.K_RIGHT] and self.direction != 'left':
            self.direction = 'right'
        if key[pygame.K_UP] and self.direction != 'down':
            self.direction = 'up'
        if key[pygame.K_DOWN] and self.direction != 'up':
            self.direction = 'down'

    def draw(self, surface):
        for part in self.body:
            pygame.draw.rect(surface, self.COLOR, part)
