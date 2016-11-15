import random

from pico2d import *

class Map:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 480, 1600
        self.vx, self.vy = 0,0
        self.state = self.RIGHT_STAND
        if Map.image == None:
            Map.image = load_image('map.png')


    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        self.x = self.x + self.vx;
        self.y = self.y + self.vy;
    def keydown(self,event,frame_time,tanker,cdealer,mdealer,healer,dog):
        if event.key == SDLK_w:
            self.vy = - 1
            tanker.vy = -1
            cdealer.vy = -1
            mdealer.vy = -1
            healer.vy = -1
            dog.vy = -1
        elif event.key == SDLK_s:
            self.vy = 1
            tanker.vy = 1
            cdealer.vy = 1
            mdealer.vy = 1
            healer.vy = 1
            dog.vy = 1
        elif event.key == SDLK_a:
            self.vx = 1
            tanker.vx = 1
            cdealer.vx = 1
            mdealer.vx = 1
            healer.vx = 1
            dog.vx = 1
        elif event.key == SDLK_d:
            self.vx = -1
            tanker.vx = -1
            cdealer.vx = -1
            mdealer.vx = -1
            healer.vx = -1
            dog.vx = -1
    def keyup(self,event,tanker,cdealer,mdealer,healer,dog):
        if event.key == SDLK_w or event.key == SDLK_s:
            self.vy = 0
            tanker.vy = 0
            cdealer.vy = 0
            mdealer.vy = 0
            healer.vy = 0
            dog.vy = 0
        elif event.key == SDLK_a or event.key == SDLK_d:
            self.vx = 0
            tanker.vx = 0
            cdealer.vx = 0
            mdealer.vx = 0
            healer.vx = 0
            dog.vx = 0