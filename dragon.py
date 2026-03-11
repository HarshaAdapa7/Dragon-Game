import pygame
import random
from settings import *

class Dragon(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((70,70))
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100,800),100)

        self.speed = DRAGON_SPEED
        self.health = DRAGON_HEALTH

    def update(self):

        self.rect.x += random.choice([-1,1]) * self.speed

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH