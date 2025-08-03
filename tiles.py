import pygame
a = 100

class Tails(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)

class GrassCliffMid(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.rect = self.image.get_rect(midbottom=(356, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassCliffMid_2(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.rect = self.image.get_rect(midbottom=(456, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassCliffMid_3(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.rect = self.image.get_rect(midbottom=(556, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassCliffMid_4(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.rect = self.image.get_rect(midbottom=(656, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassCliffMid_5(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.rect = self.image.get_rect(midbottom=(756, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassCliffMid_6(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
        self.rect = self.image.get_rect(midbottom=(856, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassCliffLeft(Tails):
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffLeft.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffLeft.png')
        self.rect = self.image.get_rect(midbottom=(256, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassCliffRight(Tails):
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffRight.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffRight.png')
        self.rect = self.image.get_rect(midbottom=(656, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])