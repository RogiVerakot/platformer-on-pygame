import pygame
import os
from player import Player
from tiles import GrassMid, Grass, GrassRight, GrassHillRight, GrassHillRight2
from wave_animation import WaveAnimation
import platforms
# lkzxc

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

wave_animations = [
    WaveAnimation((x, 750), width=100, height=100)
    for x in range(550, 951, 100)
]

def handle_events():
    global running
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
    # Получаем направление движения от игрока
    move_direction = player.update()

    # Двигаем все платформы в противоположную сторону
    if move_direction != 0:
        if platforms.level == 0:
            for platform in platforms.platforms:
                platform.rect.x += move_direction * 5  # 5 - скорость движения
        elif platforms.level == 1:
            for platform in platforms.platforms_2:
                platform.rect.x += move_direction * 5  # 5 - скорость движения

        # Двигаем анимации волн тоже
        for wave in wave_animations:
            wave.rect.x += move_direction * 5

    if platforms.level == 0:
        if move_direction != 0:
            for door in platforms.doors:
                door.rect.x += move_direction * 5  # 5 - скорость движения

    # Проверка коллизий (остаётся без изменений)
    # player.on_ground = False
    # for platform in platforms.platforms:
    #     if player.rect.colliderect(platform.rect):
    #         handle_collision(platform)
    #
    # for door in platforms.doors:
    #     if player.rect.colliderect(door.rect):
    #         platforms.level += 1

    # Границы экрана (теперь проверяем, чтобы игрок не уходил за пределы)
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
    # # Удерживаем игрока в пределах экрана по горизонтали
    # if player.rect.left < 50:  # Левая граница
    #     player.rect.left = 50
    # elif player.rect.right > WIDTH - 50:  # Правая граница
    #     player.rect.right = WIDTH - 50
    #
    # Нижняя граница (если игрок падает вниз)
    if player.rect.bottom > HEIGHT:
        player.rect.bottom = HEIGHT
        player.velocity = 0
        player.on_ground = True

def render():
    screen.blit(background, (0, 0))

    if platforms.level == 0:
        for platform in platforms.platforms:
            if 0 <= platform.rect.y <= HEIGHT:
                screen.blit(platform.image, platform.rect)

    elif platforms.level == 1:
        for platform in platforms.platforms_2:
            if 0 <= platform.rect.y <= HEIGHT:
                screen.blit(platform.image, platform.rect)

    if platforms.level == 0:
        for door in platforms.doors:
            if 0 <= door.rect.y <= HEIGHT:
                screen.blit(door.image, door.rect)

    for wave in wave_animations:
        wave.draw(screen)

    screen.blit(player.image, player.rect)
    pygame.display.flip()

def main():

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