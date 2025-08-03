import pygame
import os
i = 0
class Player(pygame.sprite.Sprite):
    def __init__(self, frames_folder_2="res_animation_run"):#, width=avto, height=100):
        super().__init__()
        global i
        self.image = pygame.image.load('res/bob.png')
        # self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(midbottom=(100, 500))
        self.speed_x = 0

        self.frames_2 = []
        frame_files_2 = sorted(os.listdir(frames_folder_2))

        for frame_file_2 in frame_files_2:
            if frame_file_2.endswith(('.png', '.jpg', '.jpeg')):
                frame_path_2 = f'{frames_folder_2}\{i}.png'
                i += 1
                if i >= 18:
                    i = 0
                frame_2 = pygame.image.load(frame_path_2).convert_alpha()
                # if width is not None and height is not None:
                    # frame = pygame.transform.scale(frame, (width, height))
                self.frames_2.append(frame_2)

        if not self.frames_2:
            raise ValueError("No animation frames found in the specified folder")

        self.current_frame_2 = 0
        self.animation_speed_2 = 0.2
        self.frame_counter_2 = 0
        # self.position = position
        # self.rect = self.frames[0].get_rect(center=position)


    def update(self):
        keys = pygame.key.get_pressed()
        self.speed_x = 0
        self.velocity = 0
        self.gravity = 1
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        if keys[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x

        self.frame_counter_2 += self.animation_speed_2
        if self.frame_counter_2 >= 1:
            self.frame_counter_2 = 0
            self.current_frame_2 = (self.current_frame_2 + 1) % len(self.frames_2)

    def draw(self, surface_2):
        surface_2.blit(self.frames_2[self.current_frame_2], self.rect)

    def jump(self):
        self.velocity = -5

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