import pygame
import os
from player import Player
from tiles import GrassMid, Grass, GrassRight, GrassHillRight, GrassHillRight2


class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1000, 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Platformer Game")
        self.clock = pygame.time.Clock()
        self.running = True

        # Загрузка ресурсов
        self.load_assets()

        # Инициализация игровых объектов
        self.init_game_objects()

    def load_assets(self):
        """Загрузка всех ресурсов игры"""
        # Фон
        bg_image = pygame.image.load(
            "res/Free Platform Game Assets/Backgrounds/New Background ( Update 1.7 )/png/2048x1536/Background/NewBackground2048x1536.png")
        self.background = pygame.transform.scale(bg_image, (self.WIDTH, self.HEIGHT))

    def init_game_objects(self):
        """Инициализация игровых объектов"""
        # Инициализация игрока с анимацией бега
        self.player = Player(frames_folder_run="res_animation_run", height=73)

        # Создание платформ
        self.platforms = [
            GrassMid(150, 800), GrassMid(250, 800), GrassMid(350, 800),
            Grass(250, 300), Grass(650, 700), Grass(850, 600),
            GrassHillRight(750, 400), Grass(450, 400), GrassRight(450, 800),
            GrassHillRight(50, 700), GrassHillRight2(50, 800)
        ]

        # Инициализация анимаций волн
        self.wave_animations = [
            WaveAnimation((x, 750), width=100, height=100)
            for x in range(550, 951, 100)
        ]

    def handle_events(self):
        """Обработка событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.player.on_ground:
                        self.player.jump()
                        self.player.on_ground = False

    def handle_input(self):
        """Обработка ввода игрока"""
        keys = pygame.key.get_pressed()

        # Горизонтальное движение обрабатывается в player.update()
        # Прыжок обрабатывается в handle_events()

    def update(self):
        """Обновление состояния игры"""
        # Обновление игрока (включая анимацию)
        self.player.update()

        # Проверка коллизий с платформами
        self.player.on_ground = False
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect):
                self.handle_collision(platform)

        # Границы экрана
        self.handle_screen_bounds()

        # Обновление анимаций волн
        for wave in self.wave_animations:
            wave.update()

        def update(self):
            # Применяем гравитацию
            if not self.player.on_ground:
                self.player.velocity += self.player.gravity
                self.player.velocity = min(self.player.velocity, self.player.max_fall_speed)

            # Сохраняем старую позицию
            old_x, old_y = self.player.rect.x, self.player.rect.y

            # Пробное перемещение
            self.player.rect.x += self.player.speed_x
            self.player.rect.y += self.player.velocity

            # Сбрасываем состояние перед проверкой коллизий
            self.player.on_ground = False
            self.player.on_slope = False

            # Проверяем коллизии
            for platform in self.platforms:
                if self.player.rect.colliderect(platform.rect):
                    self.handle_collision(platform)

            # Если после коллизии позиция не изменилась - значит было столкновение
            if self.player.rect.x == old_x:
                self.player.speed_x = 0
            if self.player.rect.y == old_y and self.player.velocity != 0:
                self.player.velocity = 0

    def handle_collision(self, platform):
        # Для склонов - специальная обработка
        if hasattr(platform, 'is_slope') and platform.is_slope:
            return self.handle_slope_collision(platform)

        # Для обычных платформ - стандартная обработка
        return self.handle_standard_collision(platform)

    def handle_standard_collision(self, platform):
        # Вычисляем глубину проникновения по осям
        dx = min(self.player.rect.right - platform.rect.left,
                 platform.rect.right - self.player.rect.left)
        dy = min(self.player.rect.bottom - platform.rect.top,
                 platform.rect.bottom - self.player.rect.top)

        # Определяем направление коллизии
        if dx < dy:  # Горизонтальная коллизия
            if self.player.rect.centerx < platform.rect.centerx:
                self.player.rect.right = platform.rect.left  # Слева
            else:
                self.player.rect.left = platform.rect.right  # Справа
            self.player.speed_x = 0
        else:  # Вертикальная коллизия
            if self.player.velocity > 0:
                self.player.rect.bottom = platform.rect.top  # Сверху
                self.player.velocity = 0
                self.player.on_ground = True
            else:
                self.player.rect.top = platform.rect.bottom  # Снизу
                self.player.velocity = 0
        return True

    def handle_slope_collision(self, platform):
        # Проверяем находится ли игрок в пределах платформы по X
        if not (platform.rect.left <= self.player.rect.centerx <= platform.rect.right):
            return False

        # Вычисляем высоту склона в текущей позиции игрока
        slope_y = platform.slope_k * self.player.rect.centerx + platform.slope_b

        # Определяем направление подхода к склону
        approaching_from_left = self.player.rect.right <= platform.rect.left + 10
        approaching_from_bottom = self.player.rect.top >= platform.rect.bottom - 10

        # Запрещаем заход снизу и слева
        if approaching_from_bottom or approaching_from_left:
            # Отталкиваем игрока от платформы
            if approaching_from_bottom:
                self.player.rect.top = platform.rect.bottom
                self.player.velocity = 0
            if approaching_from_left:
                self.player.rect.right = platform.rect.left
                self.player.speed_x = 0
            return False

        # Обычная обработка сверху
        if self.player.rect.bottom > slope_y:
            self.player.rect.bottom = slope_y
            self.player.velocity = 0
            self.player.on_ground = True
            self.player.on_slope = True

            # Плавное движение вверх по склону при движении вправо
            if self.player.speed_x > 0:
                self.player.rect.y -= 1
            return True
        return False

    def handle_screen_bounds(self):
        """Обработка границ экрана"""
        if self.player.rect.left < 0:
            self.player.rect.left = 0
        if self.player.rect.right > self.WIDTH:
            self.player.rect.right = self.WIDTH
        if self.player.rect.bottom > self.HEIGHT:
            self.player.rect.bottom = self.HEIGHT
            self.player.velocity = 0
            self.player.on_ground = True

    def render(self):
        """Отрисовка игры"""
        # Фон
        self.screen.blit(self.background, (0, 0))

        # Платформы
        for platform in self.platforms:
            if 0 <= platform.rect.y <= self.HEIGHT:
                self.screen.blit(platform.image, platform.rect)

        # Анимации волн
        for wave in self.wave_animations:
            wave.draw(self.screen)

        # Игрок (анимация обрабатывается внутри класса Player)
        self.screen.blit(self.player.image, self.player.rect)

        pygame.display.flip()

    def check_right_slope_collision(self, platform):
        # Проверяем находится ли игрок в пределах платформы по X
        if not (platform.rect.left <= self.player.rect.centerx <= platform.rect.right):
            return False

        # Вычисляем высоту склона в точке X игрока
        slope_ratio = (self.player.rect.centerx - platform.rect.left) / platform.rect.width
        slope_height = platform.rect.bottom - (platform.rect.height * slope_ratio)

        # Проверяем только если игрок выше склона
        if self.player.rect.bottom > slope_height:
            self.player.rect.bottom = slope_height
            self.player.velocity = 0
            self.player.on_ground = True
            self.player.on_slope = True

            # Плавное движение вверх по склону
            if self.player.speed_x > 0:  # Движение вправо
                self.player.rect.y -= 1  # Небольшое смещение вверх
            return True
        return False


    def run(self):
        """Главный игровой цикл"""
        while self.running:
            self.handle_events()
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()


class WaveAnimation:
    def __init__(self, position, frames_folder="res_animation", width=None, height=None):
        self.frames = self.load_frames(frames_folder, width, height)
        if not self.frames:
            raise ValueError("No animation frames found in the specified folder")

        self.current_frame = 0
        self.animation_speed = 0.2
        self.frame_counter = 0
        self.position = position
        self.rect = self.frames[0].get_rect(center=position)

    def load_frames(self, frames_folder, width, height):
        """Загрузка кадров анимации"""
        frames = []
        try:
            for i in range(1, 17):
                frame_path = os.path.join(frames_folder, f"{i}-4x.png")
                frame = pygame.image.load(frame_path).convert_alpha()
                if width and height:
                    frame = pygame.transform.scale(frame, (width, height))
                frames.append(frame)
        except Exception as e:
            print(f"Error loading animation frames: {e}")
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


if __name__ == "__main__":
    game = Game()
    game.run()

# import pygame
# import os
# from player import Player
# from tiles import GrassMid, Grass, GrassRight, GrassHillRight, GrassHillRight2
#
#
# class Game:
#     def __init__(self):
#         pygame.init()
#         self.WIDTH, self.HEIGHT = 1000, 800
#         self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
#         pygame.display.set_caption("Platformer Game")
#         self.clock = pygame.time.Clock()
#         self.running = True
#
#         # Загрузка ресурсов
#         self.load_assets()
#
#         # Инициализация игровых объектов
#         self.init_game_objects()
#
#     def load_assets(self):
#         """Загрузка всех ресурсов игры"""
#         # Фон
#         bg_image = pygame.image.load(
#             "res/Free Platform Game Assets/Backgrounds/New Background ( Update 1.7 )/png/2048x1536/Background/NewBackground2048x1536.png")
#         self.background = pygame.transform.scale(bg_image, (self.WIDTH, self.HEIGHT))
#
#     def init_game_objects(self):
#         """Инициализация игровых объектов"""
#         self.player = Player()
#
#         # Создание платформ
#         self.platforms = [
#             GrassMid(150, 800), GrassMid(250, 800), GrassMid(350, 800),
#             Grass(250, 300), Grass(650, 700), Grass(850, 600),
#             Grass(650, 500), Grass(450, 400), GrassRight(450, 800),
#             GrassHillRight(50, 700), GrassHillRight2(50, 800)
#         ]
#
#         # Инициализация анимаций волн
#         self.wave_animations = [
#             WaveAnimation((x, 750), width=100, height=100)
#             for x in range(550, 951, 100)
#         ]
#
#     def handle_events(self):
#         """Обработка событий"""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#
#     def handle_input(self):
#         """Обработка ввода игрока"""
#         keys = pygame.key.get_pressed()
#
#         # Горизонтальное движение
#         self.player.speed_x = 0
#         if keys[pygame.K_LEFT]:
#             self.player.speed_x = -5
#         if keys[pygame.K_RIGHT]:
#             self.player.speed_x = 5
#
#         # Прыжок
#         if keys[pygame.K_UP] and (self.player.on_ground or not self.player.jumping):
#             self.player.speed_y = self.player.jump_power
#             self.player.jumping = True
#             self.player.on_ground = False
#
#     def update(self):
#         """Обновление состояния игры"""
#         # Гравитация
#         if not self.player.on_ground:
#             self.player.speed_y = min(self.player.speed_y + self.player.gravity,
#                                       self.player.max_fall_speed)
#
#         # Обновление позиции игрока
#         self.player.rect.x += self.player.speed_x
#         self.player.rect.y += self.player.speed_y
#
#         # Обновление анимации бега (добавленная строка)
#         self.player.update_run_animation()
#
#         # Проверка коллизий с платформами
#         self.player.on_ground = False
#         for platform in self.platforms:
#             if self.player.rect.colliderect(platform.rect):
#                 self.handle_collision(platform)
#
#         # Границы экрана
#         self.handle_screen_bounds()
#
#         # Обновление анимаций волн
#         for wave in self.wave_animations:
#             wave.update()
#     def handle_collision(self, platform):
#         """Обработка столкновений игрока с платформой"""
#         if self.player.speed_y > 0:  # Падение вниз
#             self.player.rect.bottom = platform.rect.top
#             self.player.speed_y = 0
#             self.player.on_ground = True
#             self.player.jumping = False
#         elif self.player.speed_y < 0:  # Движение вверх
#             self.player.rect.top = platform.rect.bottom
#             self.player.speed_y = 0
#
#     def handle_screen_bounds(self):
#         """Обработка границ экрана"""
#         if self.player.rect.left < 0:
#             self.player.rect.left = 0
#         if self.player.rect.right > self.WIDTH:
#             self.player.rect.right = self.WIDTH
#         if self.player.rect.bottom > self.HEIGHT:
#             self.player.rect.bottom = self.HEIGHT
#             self.player.on_ground = True
#             self.player.jumping = False
#
#     def render(self):
#         """Отрисовка игры"""
#         # Фон
#         self.screen.blit(self.background, (0, 0))
#
#         # Платформы
#         for platform in self.platforms:
#             if 0 <= platform.rect.y <= self.HEIGHT:
#                 self.screen.blit(platform.image, platform.rect)
#
#         # Анимации волн
#         for wave in self.wave_animations:
#             wave.draw(self.screen)
#
#         # Игрок - используем текущее изображение из анимации
#         # Предполагаем, что player имеет метод get_current_frame()
#         # или атрибут current_image
#         player_image = getattr(self.player, 'current_image', self.player.image)
#         self.screen.blit(player_image, self.player.rect)
#
#         pygame.display.flip()
#     def run(self):
#         """Главный игровой цикл"""
#         while self.running:
#             self.handle_events()
#             self.handle_input()
#             self.update()
#             self.render()
#             self.clock.tick(60)
#
#         pygame.quit()
#
#
# class WaveAnimation:
#     def __init__(self, position, frames_folder="res_animation", width=None, height=None):
#         self.frames = self.load_frames(frames_folder, width, height)
#         if not self.frames:
#             raise ValueError("No animation frames found in the specified folder")
#
#         self.current_frame = 0
#         self.animation_speed = 0.2
#         self.frame_counter = 0
#         self.position = position
#         self.rect = self.frames[0].get_rect(center=position)
#
#     def load_frames(self, frames_folder, width, height):
#         """Загрузка кадров анимации"""
#         frames = []
#         try:
#             for i in range(1, 17):
#                 frame_path = os.path.join(frames_folder, f"{i}-4x.png")
#                 frame = pygame.image.load(frame_path).convert_alpha()
#                 if width and height:
#                     frame = pygame.transform.scale(frame, (width, height))
#                 frames.append(frame)
#         except Exception as e:
#             print(f"Error loading animation frames: {e}")
#         return frames
#
#     def update(self):
#         """Обновление анимации"""
#         self.frame_counter += self.animation_speed
#         if self.frame_counter >= 1:
#             self.frame_counter = 0
#             self.current_frame = (self.current_frame + 1) % len(self.frames)
#
#     def draw(self, surface):
#         """Отрисовка текущего кадра"""
#         surface.blit(self.frames[self.current_frame], self.rect)
#
#
# if __name__ == "__main__":
#     game = Game()
#     game.run()
#
# # import pygame
# # from player import *
# # from tiles import *
# # import os
# #
# # pygame.init()
# # W = 1000
# # H = 800
# # i = 1
# # screen = pygame.display.set_mode((W, H))
# # clock = pygame.time.Clock()
# #
# # player = Player()
# # grassmid = GrassMid(150, 800)
# # grassmid_2 = GrassMid(250, 800)
# # grassmid_3 = GrassMid(350, 800)
# # grass856x1112 = Grass(250, 300)
# # grass1056x1012 = Grass(650, 700)
# # grass856x912 = Grass(850, 600)
# # grass656x812 = Grass(650, 500)
# # grass456x712 = Grass(450, 400)
# #
# # grassright = GrassRight(450, 800)
# # grasshillright = GrassHillRight(50, 700)
# #
# # grasshillright2 = GrassHillRight2(50, 800)
# # platforms = [grassmid,
# #     grassmid_2,
# #     grassmid_3,
# #     grass856x1112,
# #     grass856x912,
# #     grass1056x1012,
# #     grass656x812,
# #     grass456x712,
# #     grassright,
# #     grasshillright,
# #     grasshillright2
# # ]
# # # all_sprites = pygame.sprite.Group(player)
# #
# # image = pygame.image.load("res/Free Platform Game Assets/Backgrounds/New Background ( Update 1.7 )/png/2048x1536/Background/NewBackground2048x1536.png")
# # image = pygame.transform.scale(image, (W, H))
# #
# #
# # class WaveAnimation:
# #     def __init__(self, position, frames_folder="res_animation", width=100, height=100):
# #         global i
# #         self.frames = []
# #         frame_files = sorted(os.listdir(frames_folder))
# #
# #         for frame_file in frame_files:
# #             if frame_file.endswith(('.png', '.jpg', '.jpeg')):
# #                 frame_path = f'{frames_folder}\{i}-4x.png'
# #                 i += 1
# #                 if i >= 17:
# #                     i = 1
# #                 frame = pygame.image.load(frame_path).convert_alpha()
# #                 if width is not None and height is not None:
# #                     frame = pygame.transform.scale(frame, (width, height))
# #                 self.frames.append(frame)
# #
# #         if not self.frames:
# #             raise ValueError("No animation frames found in the specified folder")
# #
# #         self.current_frame = 0
# #         self.animation_speed = 0.2
# #         self.frame_counter = 0
# #         self.position = position
# #         self.rect = self.frames[0].get_rect(center=position)
# #
# #     def set_position(self, x, y):
# #         self.position = (x, y)
# #         self.rect.center = (x, y)
# #
# #     def update(self):
# #         self.frame_counter += self.animation_speed
# #         if self.frame_counter >= 1:
# #             self.frame_counter = 0
# #             self.current_frame = (self.current_frame + 1) % len(self.frames)
# #
# #     def draw(self, surface):
# #         surface.blit(self.frames[self.current_frame], self.rect)
# # wave_anim = WaveAnimation((550, 750), width=100, height=100)
# # wave_anim_2 = WaveAnimation((650, 750), width=100, height=100)
# # wave_anim_3 = WaveAnimation((750, 750), width=100, height=100)
# # wave_anim_4 = WaveAnimation((850, 750), width=100, height=100)
# # wave_anim_5 = WaveAnimation((950, 750), width=100, height=100)
# #
# # # 656, 1012
# # try:
# #     wave = WaveAnimation((W // 2, H // 2), "res_animation")
# # except ValueError as e:
# #     print(e)
# #     pygame.quit()
# #     exit()
# #
# # wave_anims = [
# #     WaveAnimation((550, 750)),
# #     WaveAnimation((650, 750)),
# #     WaveAnimation((750, 750)),
# #     WaveAnimation((850, 750)),
# #     WaveAnimation((950, 750))
# # ]
# # player.on_ground = False
# #
# # running = True
# # while running:
# #     # Обработка событий
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
# #
# #     # Управление игроком
# #     keys = pygame.key.get_pressed()
# #
# #     # Горизонтальное движение
# #     player.speed_x = 0
# #     if keys[pygame.K_LEFT]:
# #         player.speed_x = -5
# #     if keys[pygame.K_RIGHT]:
# #         player.speed_x = 5
# #
# #     # Прыжок
# #     if keys[pygame.K_UP] and (player.on_ground or not player.jumping):
# #         player.speed_y = player.jump_power
# #         player.jumping = True
# #         player.on_ground = False
# #
# #     if not player.on_ground:
# #         player.speed_y = min(player.speed_y + player.gravity, player.max_fall_speed)
# #
# #     # Обновление позиции игрока
# #     player.rect.x += player.speed_x
# #     player.rect.y += player.speed_y
# #
# #     # Проверка коллизий с платформами
# #     player.on_ground = False
# #     for platform in platforms:
# #         if 0 <= platform.rect.y <= H:  # Проверяем, находится ли платформа в видимой области
# #             screen.blit(platform.image, platform.rect)
# #         if player.rect.colliderect(platform.rect):
# #             # print(f"Player position: {player.rect.x}, {player.rect.y}")
# #
# #             # Определяем направление столкновения
# #             if player.speed_y > 0:  # Падаем вниз
# #                 player.rect.bottom = platform.rect.top
# #                 player.speed_y = 0
# #                 player.on_ground = True
# #                 player.jumping = False
# #             elif player.speed_y < 0:  # Движемся вверх
# #                 player.rect.top = platform.rect.bottom
# #                 player.speed_y = 0
# #     # if pygame.sprite.collide_mask(player, platform):
# #
# #     # Ограничение игрока в пределах экрана
# #     if player.rect.left < 0:
# #         player.rect.left = 0
# #     if player.rect.right > W:
# #         player.rect.right = W
# #     # if player.rect.top < 0:
# #     #     player.rect.top = 0
# #     if player.rect.bottom > H:
# #         player.jumping = False
# #         player.on_ground = True
# #
# #     # Обновление анимаций
# #     for wave in wave_anims:
# #         wave.update()
# #
# #     # Отрисовка
# #     screen.blit(image, (0, 0))
# #
# #     # Отрисовка платформ
# #     for platform in platforms:
# #         screen.blit(platform.image, platform.rect)
# #
# #     # Отрисовка анимаций
# #     for wave in wave_anims:
# #         wave.draw(screen)
# #
# #     # Отрисовка игрока
# #     screen.blit(player.image, player.rect)
# #
# #     pygame.display.flip()
# #     clock.tick(60)
# #
# # pygame.quit()
