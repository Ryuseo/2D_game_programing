import random

from pico2d import *

class Map:
    image = None
    end_image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 480, 1600
        self.vx, self.vy = 0,0
        self.state = self.RIGHT_STAND
        self.wall_x1 = 240
        self.wall_x2 = 336
        self.wall_x3 = 624
        self.wall_x4 = 720
        self.wall_y1 = 16
        self.wall_y2 = 1424
        self.wall_y3 = 1712
        self.wall_y4 = 2928
        self.wall_y5 = 3152

        if Map.image == None:
            Map.image = load_image('map.png')
        if Map.end_image == None:
            Map.end_image = load_image('END.png')


    def draw(self):
        self.image.draw(self.x,self.y)
    def draw_end(self):
        self.end_image.draw(480,320)
    def update(self):
        self.x = self.x + self.vx;
        self.y = self.y + self.vy;
        self.wall_x1 = self.wall_x1 + self.vx;
        self.wall_x2 = self.wall_x2 + self.vx;
        self.wall_x3 = self.wall_x3 + self.vx;
        self.wall_x4 = self.wall_x4 + self.vx;
        self.wall_y1 = self.wall_y1 + self.vy;
        self.wall_y2 = self.wall_y2 + self.vy;
        self.wall_y3 = self.wall_y3 + self.vy;
        self.wall_y4 = self.wall_y4 + self.vy;
        self.wall_y5 = self.wall_y5 + self.vy;
    def keydown(self,event,frame_time,tankers,cdealers,mdealers,healers,dog):
        if event.key == SDLK_w:
            self.vy = - 1
            for tanker in tankers:  tanker.view_move_y = -1
            for cdealer in cdealers:cdealer.view_move_y = -1
            for mdealer in mdealers:mdealer.view_move_y = -1
            for healer in healers:  healer.view_move_y = -1
            for dogy in dog:
                dogy.vy = -1
        elif event.key == SDLK_s:
            self.vy = 1
            for tanker in tankers:  tanker.view_move_y = 1
            for cdealer in cdealers:cdealer.view_move_y = 1
            for mdealer in mdealers:mdealer.view_move_y = 1
            for healer in healers:  healer.view_move_y = 1
            for dogy in dog:
                dogy.vy = 1
        elif event.key == SDLK_a:
            self.vx = 1
            for tanker in tankers:  tanker.view_move_x = 1
            for cdealer in cdealers:cdealer.view_move_x = 1
            for mdealer in mdealers:mdealer.view_move_x = 1
            for healer in healers:  healer.view_move_x = 1
            for dogy in dog:
                dogy.vx = 1
        elif event.key == SDLK_d:
            self.vx = -1
            for tanker in tankers:  tanker.view_move_x = -1
            for cdealer in cdealers:cdealer.view_move_x = -1
            for mdealer in mdealers:mdealer.view_move_x = -1
            for healer in healers:  healer.view_move_x = -1
            for dogy in dog:
                dogy.vx = -1
    def keyup(self,event,tankers,cdealers,mdealers,healers,dog):
        if event.key == SDLK_w or event.key == SDLK_s:
            self.vy = 0
            for tanker in tankers:  tanker.view_move_y = 0
            for cdealer in cdealers:cdealer.view_move_y = 0
            for mdealer in mdealers:mdealer.view_move_y = 0
            for healer in healers:  healer.view_move_y = 0
            for dogy in dog:
                dogy.vy = 0
        elif event.key == SDLK_a or event.key == SDLK_d:
            self.vx = 0
            for tanker in tankers:  tanker.view_move_x = 0
            for cdealer in cdealers:cdealer.view_move_x = 0
            for mdealer in mdealers:mdealer.view_move_x = 0
            for healer in healers:  healer.view_move_x = 0
            for dogy in dog:
                dogy.vx = 0

    def collide_unit(a, b):
        if a.x + 16 > b.x - 16:
            if a.x - 16 < b.x + 16:
                if a.y + 16 > b.y - 16:
                    if a.y - 16 < b.y + 16:
                        a.x -= (a.xdir)
                        a.y -= (a.ydir)

    def collide_map(self,a):
        if a.x < self.wall_x1:
            a.x -= (a.xdir)
            a.y -= (a.ydir)
        elif a.x > self.wall_x4:
            a.x -= (a.xdir)
            a.y -= (a.ydir)
        elif a.y > self.wall_y5:
            a.x -= (a.xdir)
            a.y -= (a.ydir)
        elif a.y < self.wall_y1:
            a.x -= (a.xdir)
            a.y -= (a.ydir)
        elif a.y < self.wall_y2:
            if a.x < self.wall_x2:
                a.x -= (a.xdir)
                a.y -= (a.ydir)
            elif a.x > self.wall_x3:
                a.x -= (a.xdir)
                a.y -= (a.ydir)
        elif a.y > self.wall_y3 and a.y < self.wall_y4:
            if a.x < self.wall_x2:
                a.x -= (a.xdir)
                a.y -= (a.ydir)
            elif a.x > self.wall_x3:
                a.x -= (a.xdir)
                a.y -= (a.ydir)
