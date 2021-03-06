import os

from pygame import Rect,mask,key,font,display,event,mouse,image,mixer
from pygame.locals import *

import sys

scr = display.get_surface()
scrrect = scr.get_rect()

from .background import Background

font.init()

maindir = os.path.dirname(os.path.dirname(__file__))
police = font.Font(os.path.join(maindir, 'Roboto.ttf'), 50)
#police.set_bold(1)

class NewGame(object):
    """The new game label"""

    def update(self):
        self.text = police.render("New Game", 1, (200,200,200))
        self.textpos = self.text.get_rect(center=scrrect.center)

    def render(self):
        scr.blit(self.text, self.textpos)

    def click(self,pos):
        mouse_rect = Rect(pos, (0,0))
        return self.textpos.colliderect(mouse_rect)

    def mouse_over(self,pos):
        mouse_rect = Rect(pos, (0,0))
        #return self.textpos.colliderect(mouse_rect)

        if self.textpos.colliderect(mouse_rect):
            self.text = police.render("Press [Enter] to start", 1, (255,0,0))
            #self.render()
        else:
            self.text = police.render("Press [Enter] to start", 1, (200,200,200))


#newgame = NewGame()

class Menu(object):
    """This is the main menu class"""

    def run(self):
        #mixer.init()
        #mixer.music.load('sound/ACDC.mp3')
        #mixer.music.play(-1)

        new = NewGame()
        new.update()
        display.set_caption("Menu")
        going = True

        while going:
            ev = event.poll()

            if ev.type == QUIT:
                sys.exit()
            if ev.type == KEYDOWN and ev.key == K_SPACE:
                going = False
            if ev.type == MOUSEBUTTONDOWN:
                if new.click(mouse.get_pos()):
                    print("hello world")
                    going = False

            new.mouse_over(mouse.get_pos())
            #print "Mouse at : ", mouse.get_pos(), "and rect is : ", new.textpos

            Background.render()

            new.render()

            display.flip()


