import pygame


class Gomb():
    def __init__(self,x,y,kep):
        self.kep=kep
        self.negyzet=self.kep.get_rect()
        self.negyzet.topleft=(x,y)
        self.kattint=False

    def rajz(self,ablak):
        action=False
        #egerhelye

        hely=pygame.mouse.get_pos()

        #gombra rakattintottak e
        if self.negyzet.collidepoint(hely):
            #[0] a balklikk
            if pygame.mouse.get_pressed()[0]==1 and self.kattint==False:
                self.kattint=True
                action=True

        if pygame.mouse.get_pressed()[0]==0:
            self.kattint=False


        ablak.blit(self.kep,(self.negyzet.x,self.negyzet.y))

        return action