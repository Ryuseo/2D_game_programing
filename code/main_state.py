import random
import json
import os

import game_framework
from pico2d import *
from math import *
import title_state




name = "MainState"

player = None
cdealer = None
mdealer = None
healer = None
map = None
font = None
mob_dog = None
count_pskill = 0
inputw,inputa,inputs,inputd,input_tab,input_pskill,p_atk = False,False,False,False,False, 0, 0


class Map:
    def __init__(self):
        self.image = load_image('map.png')
        self.x, self.y = 480, 320
        self.left, self.bottom = 0,0
    def draw(self):
        self.image.clip_draw(self.left, self.bottom,960, 640, self.x, self.y)
    def update(self):
        pass


class Player:

    global mob_dog, p_atk

    def __init__(self):
        self.x, self.y = 48, 48
        self.vx, self.vy = 0, 0
        self.tx, self.ty = None, None
        self.frame = 0
        self.dir = 0
        self.atk = False
        self.target = None
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
                self.target = mob_dog
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
        global player
        self.frame = (self.frame + 1) % 3
        if self.target == None:
            temp1 = pow(player.x - self.x, 2)
            temp2 = pow(player.y - self.y, 2)
            temp3 = sqrt(temp1 + temp2)
            if temp3 < 100:
                self.target = player
                self.p_agg = 1
        elif self.target == player:
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


class CDealer:
    def __init__(self):
        self.x, self.y = 60, 60
        self.vx, self.vy = 0, 0
        self.tx, self.ty = 0,0
        self.frame = 0
        self.dir = 0
        self.atk = False
        self.atkc = 0
        self.target = None
        self.image = load_image('close_dealer.png')
        self.image_atk = load_image('cdealer_atk1.png')

    def update(self):
        global player, mob_dog
        self.frame = (self.frame + 1) % 3

        if player.target != None:
            self.target = player.target
            self.tx = self.target.x
            self.ty = self.target.y
            self.atc = 0

        if self.target == None:

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
        elif self.target == mob_dog:

            temp1 = pow(mob_dog.x - self.x, 2)
            temp2 = pow(mob_dog.y - self.y, 2)
            temp3 = sqrt(temp1 + temp2)

            if temp3 < 23:
                self.vy = 0
                self.vx = 0
            else:
                temp1 = mob_dog.x - self.x
                temp2 = mob_dog.y - self.y
                self.vx = temp1 / temp3
                self.vy = temp2 / temp3

            if temp3 < 30:
                self.atk = True
                self.tx = self.target.x
                self.ty = self.target.y

        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def draw(self):
        self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)

        if self.atk == True:
            self.image_atk.draw(self.tx,self.ty)
            self.atkc = self.atkc + 1
            if self.atkc == 10:
                self.atkc = 0
                self.atk = False
        else:
            self.atk = False


class MDealer:

    count = 0

    def __init__(self):
        self.x, self.y = 30, 60
        self.vx, self.vy = 0, 0
        self.tx, self.ty = 0,0
        self.frame = 0
        self.dir = 0
        self.atk = False
        self.atkc = 0
        self.atkframe = 0
        self.target = None
        self.image = load_image('magic_dealer.png')
        self.image_atk = load_image('fire.png')

    def update(self):
        global player, mob_dog
        self.frame = (self.frame + 1) % 3
        if player.target != None:
            self.target = player.target
            self.tx = self.target.x
            self.ty = self.target.y
            self.atc = 0

        if self.target == None:

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
        elif self.target == mob_dog:

            temp1 = pow(mob_dog.x - self.x, 2)
            temp2 = pow(mob_dog.y - self.y, 2)
            temp3 = sqrt(temp1 + temp2)

            if temp3 < 23:
                self.vy = 0
                self.vx = 0
            else:
                temp1 = mob_dog.x - self.x
                temp2 = mob_dog.y - self.y
                self.vx = temp1 / temp3
                self.vy = temp2 / temp3

            if temp3 < 100:
                self.atk = True
                self.vx = 0
                self.vy = 0
                self.tx = self.target.x
                self.ty = self.target.y

        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def draw(self):
        self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)

        if self.atk == True:
            self.image_atk.clip_draw(self.atkframe * 32, 0, 32, 32, self.tx, self.ty)

            if MDealer.count < 5:
                MDealer.count = MDealer.count + 1
            elif MDealer.count  ==  5:
                self.atkframe = (self.atkframe + 1) % 5
                MDealer.count = 0
            self.atkc = self.atkc + 1
            if self.atkc == 10:
                self.atkc = 0
                self.atk = False
        else:
            self.atk = False


class Healer:
    def __init__(self):
        self.x, self.y = 30, 60
        self.vx, self.vy = 0, 0
        self.tx, self.ty = 0,0
        self.frame = 0
        self.dir = 0
        self.atk = False
        self.atkc = 0
        self.target = None
        self.image = load_image('healer.png')
        self.image_atk = load_image('heal.png')

    def update(self):
        global player
        self.frame = (self.frame + 1) % 3

        if player.target != None:
            self.target = player
            self.tx = self.target.x
            self.ty = self.target.y
            self.atc = 0

        if self.target == None:

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
        elif self.target == player:

            temp1 = pow(mob_dog.x - self.x, 2)
            temp2 = pow(mob_dog.y - self.y, 2)
            temp3 = sqrt(temp1 + temp2)

            if temp3 < 23:
                self.vy = 0
                self.vx = 0
            else:
                temp1 = mob_dog.x - self.x
                temp2 = mob_dog.y - self.y
                self.vx = temp1 / temp3
                self.vy = temp2 / temp3

            if temp3 < 50:
                #self.atk = True
                self.vx = 0
                self.vy = 0
                self.tx = self.target.x
                self.ty = self.target.y

        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def draw(self):
        self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)

        if self.atk == True:
            self.image_atk.clip_draw(self.frame * 32, 0, 32, 32, self.tx, self.ty)
            self.atkc = self.atkc + 1
            if self.atkc == 10:
                self.atkc = 0
                self.atk = False
        else:
            self.atk = False


def enter():
    global player, map, mob_dog,cdealer,mdealer, healer
    player = Player()
    map = Map()
    mob_dog = Mob_dog()
    cdealer = CDealer()
    mdealer = MDealer()
    healer = Healer()


def exit():
    global boy, grass, cdealer, mdealer, healer
    del(boy)
    del(cdealer)
    del(grass)
    del(mob_dog)
    del(healer)

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
            pass


def update():
    player.update()
    #cdealer.update()
    mdealer.update()
    mob_dog.update()
    healer.update()
    map.update()


def draw():
    clear_canvas()
    map.draw()
    mob_dog.draw()
    cdealer.draw()
    mdealer.draw()
    healer.draw()
    player.draw()
    update_canvas()