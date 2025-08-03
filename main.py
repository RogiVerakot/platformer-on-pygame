import pygame
from player import *
from tiles import *
import os

pygame.init()
W = 1000
H = 800
i = 1
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

player = Player()
grassmid = GrassMid()
grassmid_2 = GrassMid_2()
grassmid_3 = GrassMid_3()
grass856x1112 = Grass856x1112()
grass1056x1012 = Grass1056x1012()
grass856x912 = Grass856x912()
grass656x812 = Grass656x812()
grass456x712 = Grass456x712()

grassright = GrassRight()
grasshillright = GrassHillRight()

grasshillright2 = GrassHillRight2()
# grass_2 = Grass_2
# all_sprites = pygame.sprite.Group(player)

image = pygame.image.load("res/Free Platform Game Assets/Backgrounds/New Background ( Update 1.7 )/png/2048x1536/Background/NewBackground2048x1536.png")
image = pygame.transform.scale(image, (W, H))


class WaveAnimation:
    def __init__(self, position, frames_folder="res_animation", width=100, height=100):
        global i
        self.frames = []
        frame_files = sorted(os.listdir(frames_folder))

        for frame_file in frame_files:
            if frame_file.endswith(('.png', '.jpg', '.jpeg')):
                frame_path = f'{frames_folder}\{i}-4x.png'
                i += 1
                if i >= 17:
                    i = 1
                frame = pygame.image.load(frame_path).convert_alpha()
                if width is not None and height is not None:
                    frame = pygame.transform.scale(frame, (width, height))
                self.frames.append(frame)

        if not self.frames:
            raise ValueError("No animation frames found in the specified folder")

        self.current_frame = 0
        self.animation_speed = 0.2
        self.frame_counter = 0
        self.position = position
        self.rect = self.frames[0].get_rect(center=position)

    def set_position(self, x, y):
        self.position = (x, y)
        self.rect.center = (x, y)

    def update(self):
        self.frame_counter += self.animation_speed
        if self.frame_counter >= 1:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def draw(self, surface):
        surface.blit(self.frames[self.current_frame], self.rect)
wave_anim = WaveAnimation((550, 750), width=100, height=100)
wave_anim_2 = WaveAnimation((650, 750), width=100, height=100)
wave_anim_3 = WaveAnimation((750, 750), width=100, height=100)
wave_anim_4 = WaveAnimation((850, 750), width=100, height=100)
wave_anim_5 = WaveAnimation((950, 750), width=100, height=100)

# 656, 1012
try:
    wave = WaveAnimation((W // 2, H // 2), "res_animation")
except ValueError as e:
    print(e)
    pygame.quit()
    exit()

running = True
while running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_UP]:
            player.velocity = 0
            player.rect.y -= 120
        else:
            player.velocity += player.gravity
    # all_sprites.update()
    player.update()
    # wave.update()
    wave_anim.update()
    wave_anim_2.update()
    wave_anim_3.update()
    wave_anim_4.update()
    wave_anim_5.update()

    # grasscliffmid.update()
    # screen.fill("black")
    screen.blit(image, (0, 0))
    # all_sprites.draw(screen)
    screen.blit(grassmid.image, grassmid.rect)
    screen.blit(grassmid_2.image, grassmid_2.rect)
    screen.blit(grassmid_3.image, grassmid_3.rect)
    screen.blit(grass856x1112.image, grass856x1112.rect)

    # screen.blit(grasscliffmid_4.image, grasscliffmid_4.rect)
    # screen.blit(grasscliffmid_5.image, grasscliffmid_5.rect)
    # screen.blit(grasscliffmid_6.image, grasscliffmid_6.rect)

    screen.blit(grassright.image, grassright.rect)
    screen.blit(grasshillright.image, grasshillright.rect)
    screen.blit(grasshillright2.image, grasshillright2.rect)
    screen.blit(grass1056x1012.image, grass1056x1012.rect)
    screen.blit(grass856x912.image, grass856x912.rect)
    screen.blit(grass656x812.image, grass656x812.rect)
    screen.blit(grass456x712.image, grass456x712.rect)
    # screen.blit(grass_2.image, grass_2.rect)
    # wave.draw(screen)
    # player.draw(screen)
    wave_anim.draw(screen)
    wave_anim_2.draw(screen)
    wave_anim_3.draw(screen)
    wave_anim_4.draw(screen)
    wave_anim_5.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
