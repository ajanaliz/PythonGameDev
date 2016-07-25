import pygame, sys

def process(bug):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        bug.velX = 5
    elif keys[pygame.K_a]:
        bug.velX = -5
    else:
        bug.velX = 0
    if keys[pygame.K_w]:
        bug.jumping = True
