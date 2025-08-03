import pygame
from player import *
from tiles import *
import os

pygame.init()
W = 800
H = 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

player = Player()
grassmid = GrassMid()
grassmid_2 = GrassMid_2()
grassmid_3 = GrassMid_3()
grassmid_4 = GrassMid_4()
grassmid_5 = GrassMid_5()
grassmid_6 = GrassMid_6()

grassright = GrassRight()
grasshillright = GrassHillRight()

grasshillright2 = GrassHillRight2()
# all_sprites = pygame.sprite.Group(player)

image = pygame.image.load("res/Free Platform Game Assets/Backgrounds/New Background ( Update 1.7 )/png/2048x1536/Background/NewBackground2048x1536.png")
image = pygame.transform.scale(image, (W, H))


class WaveAnimation:
    def __init__(self, position, frames_folder="res_animation", width=100, height=100):
        self.frames = []
        frame_files = sorted(os.listdir(frames_folder))

        for frame_file in frame_files:
            if frame_file.endswith(('.png', '.jpg', '.jpeg')):
                frame_path = os.path.join(frames_folder, frame_file)
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
wave_anim = WaveAnimation((550, 550), width=100, height=100)
wave_anim_2 = WaveAnimation((650, 550), width=100, height=100)
wave_anim_3 = WaveAnimation((750, 550), width=100, height=100)


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
        if keys[pygame.K_LEFT]:
            player.speed_x = -5
        if keys[pygame.K_RIGHT]:
            player.speed_x = 5
        player.rect.x += player.speed_x
        if keys[pygame.K_UP]:
            player.rect.y -= 50
    # all_sprites.update()
    # player.update()
    # wave.update()
    wave_anim.update()
    wave_anim_2.update()
    wave_anim_3.update()

    # grasscliffmid.update()
    # screen.fill("black")
    screen.blit(image, (0, 0))
    # all_sprites.draw(screen)
    screen.blit(grassmid.image, grassmid.rect)
    screen.blit(grassmid_2.image, grassmid_2.rect)
    screen.blit(grassmid_3.image, grassmid_3.rect)
    # screen.blit(grasscliffmid_4.image, grasscliffmid_4.rect)
    # screen.blit(grasscliffmid_5.image, grasscliffmid_5.rect)
    # screen.blit(grasscliffmid_6.image, grasscliffmid_6.rect)

    screen.blit(grassright.image, grassright.rect)
    screen.blit(grasshillright.image, grasshillright.rect)
    screen.blit(grasshillright2.image, grasshillright2.rect)
    # wave.draw(screen)
    wave_anim.draw(screen)
    wave_anim_2.draw(screen)
    wave_anim_3.draw(screen)
    # screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
