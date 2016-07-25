import pygame


class GameObject(pygame.sprite.Sprite):
    allSprites = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):
        pygame.sprite.Sprite.__init__(self)
        GameObject.allSprites.add(self)
        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height


class Bug(GameObject):
    objectList = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):
        GameObject.__init__(self, x, y, width, height, image_string)
        Bug.objectList.add(self)
        self.velX = 3
        self.velY = 0

    def motion(self):
            self.rect.x += self.velX
            self.rect.y += self.velY

