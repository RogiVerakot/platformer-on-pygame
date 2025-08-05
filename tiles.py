import pygame
a = 100

class Tails(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)

class GrassMid(Tails):
    def __init__(self, position, position_2):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.rect = self.image.get_rect(midbottom=(position, position_2))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassHillRight2(Tails):
    def __init__(self, position, position_2):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassHillRight2.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassHillRight2.png')
        self.rect = self.image.get_rect(midbottom=(position, position_2))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassRight(Tails):
    def __init__(self, position, position_2):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassRight.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassRight.png')
        self.rect = self.image.get_rect(midbottom=(position, position_2))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassHillRight(Tails):
    def __init__(self, position, position_2):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassHillRight.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassHillRight.png')
        self.rect = self.image.get_rect(midbottom=(position, position_2))
        self.image = pygame.transform.scale(self.image, [a, a])

class Grass(Tails):
    def __init__(self, position, position_2):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/Grass.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/Grass.png')
        self.rect = self.image.get_rect(midbottom=(position, position_2))
        self.image = pygame.transform.scale(self.image, [a, a])
