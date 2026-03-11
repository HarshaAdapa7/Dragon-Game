import pygame
import sys

from settings import *
from player import Player
from dragon import Dragon
from fireball import Fireball

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dragon Hunter")

clock = pygame.time.Clock()

player = Player()
dragon = Dragon()

player_group = pygame.sprite.Group(player)
dragon_group = pygame.sprite.Group(dragon)
fireballs = pygame.sprite.Group()

font = pygame.font.SysFont(None,36)

score = 0

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                fireball = Fireball(player.rect.centerx,player.rect.top)
                fireballs.add(fireball)

    player_group.update()
    dragon_group.update()
    fireballs.update()

    hits = pygame.sprite.groupcollide(dragon_group,fireballs,False,True)

    for hit in hits:
        dragon.health -= 10
        score += 10

    if dragon.health <= 0:
        dragon.kill()
        dragon = Dragon()
        dragon_group.add(dragon)

    screen.fill((30,30,40))

    player_group.draw(screen)
    dragon_group.draw(screen)
    fireballs.draw(screen)

    score_text = font.render("Score: "+str(score),True,(255,255,255))
    screen.blit(score_text,(10,10))

    pygame.display.update()

pygame.quit()
sys.exit()