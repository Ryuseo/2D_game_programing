import random
import json
import os

import game_framework
from pico2d import *
from math import *
import title_state




name = "MainState"

player = None
map = None
font = None
mob_dog = None
count_pskill = 0
inputw,inputa,inputs,inputd,input_tab,input_pskill,p_atk = False,False,False,False,False, 0, 0


class Map:
    def __init__(self):
        self.image = load_image('map.png')
        self.x, self.y = 32, 32
    def draw(self):
        self.image.clip_draw(0, 0,960, 640, 480, 320)



class Player:

    global mob_dog, p_atk

    def __init__(self):
        self.x, self.y = 48, 48
        self.vx, self.vy = 0, 0
        self.tx, self.ty = None, None
        self.frame = 0
        self.dir = 0
        self.jop = 0
        self.atk = False
        self.image = load_image('tanker.png')
        self.image_t = load_image('target.png')
        self.image_atk = load_image('tanker_atk1.png')

    def update(self):
        global inputw,inputa,inputs,inputd,input_tab,input_pskill
        self.frame = (self.frame + 1) % 3

        temp1 = pow(self.x - mob_dog.x, 2)
        temp2 = pow(self.y - mob_dog.y, 2)
        temp3 = sqrt(temp1 + temp2)

        if inputw == True:
            self.vy = 1
            self.dir = 0
        elif inputs == True:
            self.vy = -1
            self.dir = 3
        else:
            self.vy = 0

        if inputd == True:
            self.vx = 1
            self.dir = 1
        elif inputa == True:
            self.vx = -1
            self.dir = 2
        else:
            self.vx = 0

        if input_tab == True:
            if temp3 < 200:
                self.tx = mob_dog.x
                self.ty = mob_dog.y + 32

        if input_pskill == 1:
            if temp3 < 28:
                self.atk = True
                input_pskill = 0

        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def draw(self):
        global count_pskill, input_pskill
        delay(0.01)
        self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)
        if self.tx != None:
            self.image_t.draw(self.tx,self.ty)

        if self.atk == True:
            self.image_atk.draw(self.tx,self.ty - 32)
            count_pskill = count_pskill + 1
            if count_pskill == 10:
                count_pskill = 0
                self.atk = False
        else:
            self.atk = False



class Mob_dog:
    image = None
    global player

    Player, CDealer, MDealer, NPC = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 300, 300
        self.vx, self.vy = 0, 0
        self.frame, self.dir = 0, 0
        self.target = None
        self.p_agg ,self.cd_agg ,self.md_agg ,self.npc_agg = 0, 0, 0, 0
        if Mob_dog.image == None:
           Mob_dog.image = load_image('dog.png')

    def update(self):
        self.frame = (self.frame + 1) % 3
        if self.target == None:
            temp1 = pow(player.x - self.x, 2)
            temp2 = pow(player.y - self.y, 2)
            temp3 = sqrt(temp1 + temp2)
            if temp3 < 100:
                self.target = Player
                self.p_agg = 1
        elif self.target == Player:
            temp1 = pow(player.x - self.x, 2)
            temp2 = pow(player.y - self.y, 2)
            temp3 = sqrt(temp1 + temp2)
            if temp3 < 23:
                self.vy = 0
                self.vx = 0
            else:
                temp1 = player.x - self.x
                temp2 = player.y - self.y
                self.vx = temp1 / temp3
                self.vy = temp2 / temp3

        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def draw(self):
        delay(0.01)
        self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)


def enter():
    global player, map, mob_dog
    player = Player()
    map = Map()
    mob_dog = Mob_dog()


def exit():
    global boy, grass
    del(boy)
    del(grass)
    del(mob_dog)

def pause():
    pass


def resume():
    pass


def handle_events():
    global inputw, inputa, inputs, inputd, input_tab,input_pskill

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_w:
                inputw = True
            elif event.key == SDLK_a:
                inputa = True
            elif event.key == SDLK_s:
                inputs = True
            elif event.key == SDLK_d:
                inputd = True
            elif event.key == SDLK_TAB:
                input_tab = True
            elif event.key == SDLK_1:
                input_pskill = 1

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:
               inputw = False
            elif event.key == SDLK_a:
               inputa = False
            elif event.key == SDLK_s:
               inputs = False
            elif event.key == SDLK_d:
               inputd = False


def update():
    player.update()
    mob_dog.update()


def draw():
    clear_canvas()
    map.draw()
    mob_dog.draw()
    player.draw()
    update_canvas()