import pygame
a = 100

class Tails(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)

class GrassMid(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.rect = self.image.get_rect(midbottom=(356, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassMid_2(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.rect = self.image.get_rect(midbottom=(456, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassMid_3(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.rect = self.image.get_rect(midbottom=(556, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassMid_4(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.rect = self.image.get_rect(midbottom=(656, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassMid_5(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.rect = self.image.get_rect(midbottom=(756, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassMid_6(Tails):
    # def __init__(self):
    #     super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid.png')
    #     # self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassCliffMid')
    #     self.image = pygame.transform.scale(self.image, [a, a])
    #     self.rect = self.image.get_rect(midbottom=(50, 0))
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.rect = self.image.get_rect(midbottom=(856, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassHillRight2(Tails):
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassHillRight2.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassHillRight2.png')
        self.rect = self.image.get_rect(midbottom=(256, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassRight(Tails):
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassRight.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassRight.png')
        self.rect = self.image.get_rect(midbottom=(656, 1012))
        self.image = pygame.transform.scale(self.image, [a, a])

class GrassHillRight(Tails):
    def __init__(self):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassHillRight.png')
        self.image = pygame.image.load('res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassHillRight.png')
        self.rect = self.image.get_rect(midbottom=(256, 912))
        self.image = pygame.transform.scale(self.image, [a, a])