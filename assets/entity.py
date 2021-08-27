import pygame


class Snake:
    COLOR = 0, 200, 0
    SIZE = 40
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

    def move(self):
        for index, part in reversed(list(enumerate(self.body[1:], 1))):
            part.x = self.body[index - 1].x
            part.y = self.body[index - 1].y
        self.body[0].move_ip(*[value * self.SIZE for value in self.DIRECTIONS[self.direction]])

    def key_handler(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.direction = 'left'
        if key[pygame.K_RIGHT]:
            self.direction = 'right'
        if key[pygame.K_UP]:
            self.direction = 'up'
        if key[pygame.K_DOWN]:
            self.direction = 'down'
    
    def draw(self, surface):
        for part in self.body:
            pygame.draw.rect(surface, self.COLOR, part)
