import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill("blue")
        self.rect = self.image.get_rect(midbottom=(100, 500))
        self.speed_x = 0



    def update(self):
        self.speed_x = 0
        self.velocity = 0
        self.gravity = 1
        self.velocity += self.gravity
        self.rect.y += self.velocity
    def jump(self):
        self.velocity = -5

