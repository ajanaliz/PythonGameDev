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
        self.velX = 0
        self.velY = 5
        self.jumping, self.go_down = False, False
        self.max_jump = 275

    def motion(self, SCREENWIDTH, SCREENHEIGHT):
        self.rect.x += self.velX
        self.__jump(SCREENHEIGHT)

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x + self.width > SCREENWIDTH:
            self.rect.x = SCREENWIDTH - self.width
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y + self.height > SCREENHEIGHT:
            self.jumping = False
            self.go_down = False
            self.rect.y = SCREENHEIGHT - self.height

    def __jump(self, SCREENHEIGHT):
        if self.jumping:
            if self.rect.y < self.max_jump:
                self.go_down = True
            if self.go_down:
                self.rect.y += self.velY
            else:
                self.rect.y -= self.velY
