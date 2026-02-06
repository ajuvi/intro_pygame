from Pantalla import Pantalla
from Nau import Nau
import pygame 
import random
import Globals

def main():
    pantalla=Pantalla()
    nau=Nau(Globals.SCREEN_WIDTH/2,Globals.SCREEN_HEIGHT/2,50,50,(255,0,0))
    

    #bucle principal del joc
    while(pantalla.running):
        if pantalla.running:
            teclat = pantalla.llegir_teclat()   
            logica(teclat,pantalla,nau)
            render(pantalla,nau)

def logica(teclat,pantalla,nau):

    if teclat[pygame.K_q] or teclat[pygame.K_ESCAPE]:
        pantalla.running=False

    if teclat[pygame.K_1]:
        nau.color=(255,0,0)
    if teclat[pygame.K_2]:
        nau.color=(0,0,255)
    if teclat[pygame.K_3]:
        nau.color=(0,255,0)
    if teclat[pygame.K_4]:
        nau.color=(0,0,0)
    if teclat[pygame.K_5]:
        nau.color=(255,255,255)

    if teclat[pygame.K_UP]:
        nau.direccio(0,-1)
    if teclat[pygame.K_DOWN]:
        nau.direccio(0,1);
    if teclat[pygame.K_LEFT]:
        nau.direccio(-1,0);
    if teclat[pygame.K_RIGHT]:
        nau.direccio(1,0);

    nau.update()    

def render(pantalla, avatar):
    pantalla.netejar()
    avatar.pintar(pantalla)
    pantalla.render()

if __name__ == "__main__":
    main()