import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640,360),0,32)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()


print("its done")