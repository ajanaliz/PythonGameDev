import pygame, sys, gamedev.classes

pygame.init()
WIDTH, HEIGHT = 640, 360
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
wizimage = pygame.image.load("res\pictures\Wizard.png")


running = True
clock = pygame.time.Clock()
FPS = 60
totalFrames = 0
variable = 0

bug = gamedev.classes.Bug(0,50,174,294, "res\pictures\Wizard.png")

while running:
    # PROCESSES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # PROCESSES
    # LOGIC
    bug.motion()
    # LOGIC
    # RENDER
    screen.fill((180, variable, (variable * 2) % 255))
    gamedev.classes.GameObject.allSprites.draw(screen)

    pygame.display.flip()
    # RENDER

    clock.tick(FPS)

print("its done")
