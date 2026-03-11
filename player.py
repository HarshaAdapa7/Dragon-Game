import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2, HEIGHT-60)

        self.speed = PLAYER_SPEED

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed