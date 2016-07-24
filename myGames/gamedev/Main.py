import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640, 360), 0, 32)

color1 = (22, 122, 211)
color2 = (0, 44, 166)
color3 = (34, 55, 245)

running = True
clock = pygame.time.Clock()
FPS = 24
totalFrames = 0
variable = 0
while running:
    # PROCESSES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # PROCESSES
    # LOGIC
    variable += 5
    if variable > 255:
        variable %= 255
    totalFrames += 1
    # LOGIC
    # RENDER
    screen.fill((180, variable, (variable * 2) % 255))
    pygame.draw.line(screen, color2, (0, 0), (640, 360), 5)
    pygame.draw.rect(screen, color3, (40, 40, 300, 45))
    pygame.draw.circle(screen, color1, (500, 85), 40, 25)

    pygame.display.flip()
    # RENDER

    clock.tick(FPS)

print("its done")
