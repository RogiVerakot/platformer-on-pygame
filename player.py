import pygame
import os


class Player(pygame.sprite.Sprite):
    def load_animation_frames(self, folder_path, height=None):
        frames = []
        frame_files = sorted([f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))])
        print(frame_files)
        for frame_file in frame_files:
            frame_path = os.path.join(folder_path, frame_file)
            try:
                frame = pygame.image.load(frame_path).convert_alpha()

                if height is not None:  # Если задана высота
                    # Получаем исходные размеры
                    original_width, original_height = frame.get_size()
                    # Вычисляем пропорциональную ширину
                    aspect_ratio = original_width / original_height
                    target_width = int(height * aspect_ratio)
                    # Масштабируем
                    frame = pygame.transform.scale(frame, (target_width, height))

                frames.append(frame)
            except Exception as e:
                print(f"Failed to load frame {frame_path}: {e}")

        return frames

    def __init__(self, frames_folder_run="res_animation_run", height=73):  # Убрали width, оставили height
        super().__init__()
        # Основные свойства персонажа
        self.default_image = pygame.image.load('res/bob.png').convert_alpha()
        self.image = self.default_image
        self.rect = self.image.get_rect(midbottom=(100, 500))
        self.speed_y = 0
        self.speed_x = 0
        self.velocity = 0
        self.gravity = 0.8
        self.is_running = False
        self.facing_left = False
        self.jump_power = -18
        self.jumping = False
        self.on_ground = False
        self.max_fall_speed = 15
        self.on_slope = False
        self.slope_adjustment = 0
        self.max_speed = 5
        self.jump_power = -15
        self.gravity = 0.8
        self.max_fall_speed = 15

        # Загрузка анимации бега (теперь передаём только height)
        self.run_frames = self.load_animation_frames(frames_folder_run, height)
        self.current_run_frame = 0
        self.animation_speed = 0.2
        self.frame_counter = 0

        if not self.run_frames:
            print("Warning: No running animation frames loaded - using default image")
            self.run_frames = [self.default_image]
        self.slope_adjustment = 0  # Для плавного движения по склонам
        self.on_slope = False  # Флаг нахождения на склоне

    # Остальные методы (update_run_animation, update, jump) остаются без изменений



    def update_run_animation(self):
        if not self.is_running:
            self.image = self.default_image
            if self.facing_left:  # Если стоим, но смотрели влево
                self.image = pygame.transform.flip(self.image, True, False)
            return

        self.frame_counter += self.animation_speed
        if self.frame_counter >= 1:
            self.frame_counter = 0
            self.current_run_frame = (self.current_run_frame + 1) % len(self.run_frames)

        self.image = self.run_frames[self.current_run_frame]
        if self.facing_left:  # Применяем отражение если смотрим влево
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        keys = pygame.key.get_pressed()

        # Сброс скорости
        self.speed_x = 0
        self.is_running = False

        # Применение гравитации
        self.velocity += self.gravity
        self.rect.y += self.velocity

        # Обработка движения
        if keys[pygame.K_LEFT]:
            self.speed_x = -5
            self.is_running = True
            self.facing_left = True
            self.image = pygame.transform.flip(self.image, True, False)  # Отражаем изображение при движении влево
        if keys[pygame.K_RIGHT]:
            self.speed_x = 5
            self.is_running = True
            self.facing_left = False

        self.rect.x += self.speed_x
        if not self.on_ground:
            self.on_slope = False
            self.slope_adjustment = 0


        # Обновление анимации
        self.update_run_animation()

    def update_movement(self):
        # Обработка движения по склону
        if self.on_slope:
            self.rect.x += self.speed_x
            self.rect.y += self.slope_adjustment
        else:
            self.rect.x += self.speed_x
            self.rect.y += self.velocity

    def jump(self):
        self.velocity = -15


# import pygame
# import os
#
# i = 0
#
# class Player(pygame.sprite.Sprite):
#     def load_animation_frames(self, folder_path):
#         global i
#         frames = []
#         frame_files = sorted(os.listdir(folder_path))
#
#         for frame_file in frame_files:
#             if frame_file.endswith(('.png', '.jpg', '.jpeg')):
#                 frame_path = os.path.join(folder_path, f"{i}.png")
#                 i += 1
#                 if i >= 18:
#                     i = 0
#                 try:
#                     frame = pygame.image.load(frame_path).convert_alpha()
#                     if width is not None and height is not None:
#                         frame = pygame.transform.scale(frame, (width, height))
#                     frames.append(frame)
#                 except:
#                     print(f"Failed to load frame: {frame_path}")
#
#         return frames
#     def __init__(self, frames_folder_run="res_animation_run", width = 73, height = 73):
#         super().__init__()
#         # Основные свойства персонажа
#         self.image = pygame.image.load('res/bob.png')
#         self.rect = self.image.get_rect(midbottom=(100, 500))
#         self.speed_x = 0
#         self.velocity = 0
#         self.gravity = 0.1
#         self.is_running = False
#
#         # Загрузка анимации бега
#         self.run_frames = self.load_animation_frames(frames_folder_run)
#         self.current_run_frame = 0
#         self.animation_speed = 0.2
#         self.frame_counter = 0
#
#         # if not self.run_frames:
#         #     raise ValueError("No running animation frames found in the specified folder")
#
#     def update_run_animation(self):
#         if not self.is_running:
#             self.image = pygame.image.load('res/bob.png')
#             return
#
#         self.frame_counter += self.animation_speed
#         if self.frame_counter >= 1:
#             self.frame_counter = 0
#             self.current_run_frame = (self.current_run_frame + 1) % len(self.run_frames)
#
#         # Используем текущий кадр анимации бега
#         self.image = self.run_frames[self.current_run_frame]
#
#     def update(self):
#         keys = pygame.key.get_pressed()
#
#         # Сброс скорости
#         self.speed_x = 0
#         self.is_running = False
#
#         # Применение гравитации
#         self.velocity += self.gravity
#         self.rect.y += self.velocity
#
#         # Обработка движения
#         if keys[pygame.K_LEFT]:
#             self.speed_x = -5
#             self.is_running = True
#         if keys[pygame.K_RIGHT]:
#             self.speed_x = 5
#             self.is_running = True
#
#         self.rect.x += self.speed_x
#
#         # Обновление анимации
#         self.update_run_animation()
#
#     def jump(self):
#         self.velocity = -5

# class WaveAnimation:
#     def __init__(self, position, frames_folder="res_animation", width=100, height=100):
#         global i
#         self.frames = []
#         frame_files = sorted(os.listdir(frames_folder))
#
#         for frame_file in frame_files:
#             if frame_file.endswith(('.png', '.jpg', '.jpeg')):
#                 frame_path = f'{frames_folder}\{i}-4x.png'
#                 i += 1
#                 if i >= 17:
#                     i = 1
#                 frame = pygame.image.load(frame_path).convert_alpha()
#                 if width is not None and height is not None:
#                     frame = pygame.transform.scale(frame, (width, height))
#                 self.frames.append(frame)
#
#         if not self.frames:
#             raise ValueError("No animation frames found in the specified folder")
#
#         self.current_frame = 0
#         self.animation_speed = 0.2
#         self.frame_counter = 0
#         self.position = position
#         self.rect = self.frames[0].get_rect(center=position)
#
#     def set_position(self, x, y):
#         self.position = (x, y)
#         self.rect.center = (x, y)
#
#     def update(self):
#         self.frame_counter += self.animation_speed
#         if self.frame_counter >= 1:
#             self.frame_counter = 0
#             self.current_frame = (self.current_frame + 1) % len(self.frames)
#
#     def draw(self, surface):
#         surface.blit(self.frames[self.current_frame], self.rect)