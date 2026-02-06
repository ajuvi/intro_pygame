#pip install pygame

import pygame
import datetime
from time import sleep
import Globals

class Pantalla:

    def __init__(self):

        #self.FLAGS=pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
        self.FLAGS= pygame.HWSURFACE | pygame.DOUBLEBUF   

        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Globals.SCREEN_WIDTH,Globals.SCREEN_HEIGHT), self.FLAGS)

    def netejar(self):
        self.screen.fill(Globals.BACKGROUND_COLOR)            

    def pintar_rectangle(self, x, y, width, height, color):
        if color==None:
            color=Globals.DEFAULT_COLOR
        pygame.draw.rect(self.screen, color, (x, y, width, height))

    def llegir_teclat(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
             
        return pygame.key.get_pressed()

    def render(self):
        pygame.display.flip()
        self.clock.tick(Globals.FPS)
