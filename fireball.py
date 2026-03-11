import pygame
from settings import *

class Fireball(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.Surface((10,20))
        self.image.fill((255,165,0))

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):

        self.rect.y -= FIREBALL_SPEED

        if self.rect.bottom < 0:
            self.kill()