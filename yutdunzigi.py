import pygame
import PygamePrint as pp
import random
sum = 0
mvcnt = 0
running = True
pp.blit_center(pp.anykey_image, pp.find_coord((0, 200)))
pygame.display.update()
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            x = random.randint(0, 1)
            image = pp.yut_0_image
            if (x == 1):
                image = pp.yut_1_image
                mvcnt += 1
            pp.blit_center(image, pp.find_coord(pp.yut_loc[sum]))
            pygame.display.update()
            sum += 1


        if sum == 4:
            pygame.time.delay(500)
            if mvcnt == 1:
                pp.blit_center(pp.do_image, pp.find_coord((0, 0)))
                pygame.display.update()
            elif mvcnt == 2:
                pp.blit_center(pp.gae_image, pp.find_coord((0, 0)))
                pygame.display.update()
            elif mvcnt == 3:
                pp.blit_center(pp.girl_image, pp.find_coord((0, 0)))
                pygame.display.update()
            elif mvcnt == 4:
                pp.blit_center(pp.yut_image, pp.find_coord((0, 0)))
                pygame.display.update()
            else:
                pp.blit_center(pp.mo_image, pp.find_coord((0, 0)))
                pygame.display.update()
                mvcnt = 5

            running = False
            pygame.time.delay(700)
            break

