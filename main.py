import pygame
import os
from player import Player
from tiles import GrassMid, Grass, GrassRight, GrassHillRight, GrassHillRight2
from wave_animation import WaveAnimation


def main():
    # Инициализация Pygame
    pygame.init()
    WIDTH, HEIGHT = 1000, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Platformer Game")
    clock = pygame.time.Clock()
    running = True

    # Загрузка ресурсов
    bg_image = pygame.image.load(
        "res/Free Platform Game Assets/Backgrounds/New Background ( Update 1.7 )/2048x1536/Background/NewBackground2048x1536.png")
    background = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

    # Инициализация игровых объектов
    player = Player(frames_folder_run="res_animation_run", height=73)

    platforms = [
        GrassMid(150, 800),
        GrassMid(250, 800),
        GrassMid(350, 800),
        Grass(250, 300),
        Grass(650, 700),
        Grass(850, 600),
        GrassHillRight(700, 400),
        GrassMid(650, 400),
        GrassRight(450, 800),
        GrassHillRight(0, 700),
        GrassHillRight2(50, 800)
    ]

    wave_animations = [
        WaveAnimation((x, 750), width=100, height=100)
        for x in range(550, 951, 100)
    ]

    def handle_events():
        nonlocal running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if player.on_ground:
                        player.jump()
                        player.on_ground = False

    def handle_input():
        keys = pygame.key.get_pressed()
        player.speed_x = 0
        # Обработка ввода (если требуется)
        if keys[pygame.K_LEFT]:
            player.speed_x = -5
        elif keys[pygame.K_RIGHT]:
            player.speed_x = 5
        else:
            player.speed_x = 0

    def update():
        player.update()

        # Проверка коллизий с платформами
        player.on_ground = False
        for platform in platforms:
            if player.rect.colliderect(platform.rect):
                handle_collision(platform)

        # Границы экрана
        handle_screen_bounds()

        # Обновление анимаций волн
        for wave in wave_animations:
            wave.update()

    def handle_collision(platform):
        if hasattr(platform, 'is_slope') and platform.is_slope:
            return handle_slope_collision(platform)
        return handle_standard_collision(platform)

    def handle_standard_collision(platform):
        dx = min(player.rect.right - platform.rect.left,
                 platform.rect.right - player.rect.left)
        dy = min(player.rect.bottom - platform.rect.top,
                 platform.rect.bottom - player.rect.top)

        if dx < dy:
            if player.rect.centerx < platform.rect.centerx:
                player.rect.right = platform.rect.left
            else:
                player.rect.left = platform.rect.right
            player.speed_x = 0
        else:
            if player.velocity > 0:
                player.rect.bottom = platform.rect.top
                player.velocity = 0
                player.on_ground = True
            else:
                player.rect.top = platform.rect.bottom
                player.velocity = 0
        return True

    def handle_slope_collision(platform):
        if not (platform.rect.left <= player.rect.centerx <= platform.rect.right):
            return False

        # if isinstance(platform, GrassHillRight):
        #     relative_x = player.rect.centerx - platform.rect.left
        #     slope_ratio = relative_x / platform.rect.width
        #     slope_y = platform.rect.bottom - int(slope_ratio * platform.rect.height)
        #
        #     if player.rect.bottom > slope_y:
        #         if player.velocity >= 0:
        #             player.rect.bottom = slope_y
        #             player.velocity = 0
        #             player.on_ground = True
        #             player.on_slope = True
        #             if player.speed_x > 0:
        #                 player.rect.y -= 1
        #             return True
        #         else:
        #             player.rect.top = platform.rect.bottom
        #             player.velocity = 0

        elif isinstance(platform, (GrassHillRight, GrassHillRight2)):
            relative_x = platform.rect.right - player.rect.centerx  # Инвертируем расчет
            slope_ratio = relative_x / platform.rect.width
            slope_y = platform.rect.bottom - int(slope_ratio * platform.rect.height)

            if player.rect.bottom > slope_y:
                if player.velocity >= 0:
                    player.rect.bottom = slope_y
                    player.velocity = 0
                    player.on_ground = True
                    player.on_slope = True
                    if player.speed_x < 0:  # Игрок движется влево
                        player.rect.y -= 1
                    return True
                else:
                    player.rect.top = platform.rect.bottom
                    player.velocity = 0
        return False

    def handle_screen_bounds():
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.right > WIDTH:
            player.rect.right = WIDTH
        if player.rect.bottom > HEIGHT:
            player.rect.bottom = HEIGHT
            player.velocity = 0
            player.on_ground = True

    def render():
        screen.blit(background, (0, 0))

        for platform in platforms:
            if 0 <= platform.rect.y <= HEIGHT:
                screen.blit(platform.image, platform.rect)

        for wave in wave_animations:
            wave.draw(screen)

        screen.blit(player.image, player.rect)
        pygame.display.flip()

    # Главный игровой цикл
    while running:
        handle_events()
        handle_input()
        update()
        render()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()