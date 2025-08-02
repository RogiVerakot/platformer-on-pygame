import pygame
from player import *

pygame.init()
W = 800
H = 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

player = Player()
# all_sprites = pygame.sprite.Group(player)

running = True
while running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_LEFT]:
            player.speed_x = -5
        if keys[pygame.K_RIGHT]:
            player.speed_x = 5
        player.rect.x += player.speed_x
        if keys[pygame.K_UP]:
            player.rect.y -= 50
    # all_sprites.update()
    player.update()

    screen.fill("black")
    # all_sprites.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
