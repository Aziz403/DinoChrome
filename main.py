from Model import *
import sys

pygame.init()
gm = Game(WIDTH, HEIGHT)

def Events():
    global gm
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and not gm.Start and not gm.Over:
                gm.Start = True
                gm.Pause = False
            elif event.key == K_SPACE and gm.Start and not gm.Over:
                gm.Dino.IsJump = True
                Dino.FirstJump = True
            elif event.key == K_p and not gm.Over:
                gm.Start = False
                gm.Pause = True
            elif event.key == K_r:
                gm = None
                gm = Game(WIDTH, HEIGHT)


def Main():
    while True:
        Events()
        gm.Draw()
        gm.Update()
        pygame.display.update()


Main()
sys.exit()


