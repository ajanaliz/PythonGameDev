import pygame, sys, gamedev.classes, gamedev.process

pygame.init()
WIDTH, HEIGHT = 1024, 764
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
wizimage = pygame.image.load("res\pictures\Wizard.png")


running = True
clock = pygame.time.Clock()
FPS = 60
totalFrames = 0

bug = gamedev.classes.Bug(0,HEIGHT - 294,174,294, "res\pictures\Wizard.png")

while running:
    # PROCESSES
    gamedev.process.process(bug)
    # PROCESSES
    # LOGIC
    bug.motion(WIDTH,HEIGHT)
    # LOGIC
    # RENDER

    gamedev.classes.GameObject.allSprites.draw(screen)

    pygame.display.flip()
    # RENDER

    clock.tick(FPS)

print("its done")
