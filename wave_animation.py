import os
import pygame

class WaveAnimation:
    def __init__(self, position, frames_folder="./res_animation", width=None, height=100):
        self.frames = self.load_frames(frames_folder, width, height)
        if not self.frames:
            raise ValueError("No animation frames found in the specified folder")

        self.current_frame = 0
        self.animation_speed = 0.2
        self.frame_counter = 0
        self.position = position
        self.rect = self.frames[0].get_rect(center=position)

    def load_frames(self, frames_folder, width, height):
        frames = []
        for i in range(1, 17):
            frame_path = os.path.join(frames_folder, f"{i}-4x.png")
            try:
                frame = pygame.image.load(frame_path).convert_alpha()
                if width and height:
                    frame = pygame.transform.scale(frame, (width, height))
                frames.append(frame)
            except pygame.error as e:
                print(f"Ошибка загрузки кадра {frame_path}: {e}")
                raise SystemExit(f"Файл не найден: {frame_path}")  # Выход, если критично
        return frames

    def update(self):
        """Обновление анимации"""
        self.frame_counter += self.animation_speed
        if self.frame_counter >= 1:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def draw(self, surface):
        """Отрисовка текущего кадра"""
        surface.blit(self.frames[self.current_frame], self.rect)