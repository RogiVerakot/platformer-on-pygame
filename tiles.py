import pygame
a = 100

class Tails(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, [a, a])
        self.rect = self.image.get_rect()

class GrassMid(Tails):
    def __init__(self, x, y):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassMid.png')
        self.rect = self.image.get_rect(midbottom=(x, y))

class GrassHillRight2(Tails):
    def __init__(self, x, y):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassHillRight2.png')
        self.rect = self.image.get_rect(midbottom=(x, y))

class GrassRight(Tails):
    def __init__(self, x, y):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassRight.png')
        self.rect = self.image.get_rect(midbottom=(x, y))

class GrassHillRight(Tails):
    def __init__(self, x, y):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/GrassHillRight.png')
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.slope_p1 = (self.rect.left, self.rect.top)
        self.slope_p2 = (self.rect.left, self.rect.bottom)
        self.slope_p3 = (self.rect.right, self.rect.bottom)
        self.slope_k = (self.slope_p3[1] - self.slope_p1[1]) / (self.slope_p3[0] - self.slope_p1[0])
        self.slope_b = self.slope_p1[1] - self.slope_k * self.slope_p1[0]
        self.slope = (self.slope_p3[1] - self.slope_p1[1]) / (self.slope_p3[0] - self.slope_p1[0])
        self.y_intercept = self.slope_p1[1] - self.slope * self.slope_p1[0]
        self.is_slope = True

class Grass(Tails):
    def __init__(self, x, y):
        super().__init__(image_path='res/Free Platform Game Assets/Tiles/2D Tiles ( Update 1.9 )/Spring/512x512/Grass.png')
        self.rect = self.image.get_rect(midbottom=(x, y))