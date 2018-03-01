import sys, pygame
pygame.init()

size = width, height = 1024, 768
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

tank = pygame.image.load("tank.png")
tankrect = tank.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed = [0, -2]
            if event.key == pygame.K_s:
                speed = [0, 2]

    tankrect = tankrect.move(speed)
    #if tankrect.left < 0 or tankrect.right > width:
    #    speed[0] = -speed[0]
    #if tankrect.top < 0 or tankrect.bottom > height:
    #    speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(tank, tankrect)
    pygame.display.flip()
