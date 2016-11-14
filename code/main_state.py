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
frame_time = None
current_time = 0.0

class Map:

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.image = load_image('map.png')
        self.x, self.y = 480, 320
        self.vx,self.vy = 0,0;
        self.left, self.bottom = 0,0
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        self.x = self.x + self.vx;
        self.y = self.y + self.vy;
    def keydown(self,event):
        distance = Map.RUN_SPEED_PPS * frame_time
        if event == SDLK_w:
            self.vy = - 1
        elif event == SDLK_s:
            self.vy = 1
        elif event == SDLK_a:
            self.vx = 1
        elif event == SDLK_d:
            self.vx = -1
    def keyup(self,event):
        if event == SDLK_w or event == SDLK_s:
            self.vy = 0
        elif event == SDLK_a or event == SDLK_d:
            self.vx = 0


class Player:

    PIXEL_PER_METER = (32.0 / 2)  # 32 pixel 200 cm
    RUN_SPEED_KMPH = 4.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):

        self.image = load_image('tanker.png')
        self.image_t = load_image('target.png')
        self.image_atk = load_image('tanker_atk1.png')

    def update(self):
        pass
    def draw(self):
        pass

class Mob_dog:
    image = None

    PIXEL_PER_METER = (32.0 / 2)  # 32 pixel 200 cm
    RUN_SPEED_KMPH = 4.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        if Mob_dog.image == None:
           Mob_dog.image = load_image('dog.png')

    def update(self):
       pass

    def draw(self):
        pass


class CDealer:

    PIXEL_PER_METER = (32.0 / 2)  # 32 pixel 200 cm
    RUN_SPEED_KMPH = 4.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.image = load_image('close_dealer.png')
        self.image_atk = load_image('cdealer_atk1.png')

    def update(self):
       pass

    def draw(self):
        pass


class MDealer:

    PIXEL_PER_METER = (32.0 / 2)  # 32 pixel 200 cm
    RUN_SPEED_KMPH = 4.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.image = load_image('magic_dealer.png')
        self.image_atk = load_image('fire.png')

    def update(self):
        pass

    def draw(self):
        pass


class Healer:

    PIXEL_PER_METER = (32.0 / 2)  # 32 pixel 200 cm
    RUN_SPEED_KMPH = 4.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.image = load_image('healer.png')
        self.image_atk = load_image('heal.png')

    def update(self):
        pass
    def draw(self):
        pass

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global player, map, mob_dog,cdealer,mdealer, healer, frame_time
    player = Player()
    map = Map()
    mob_dog = Mob_dog()
    cdealer = CDealer()
    mdealer = MDealer()
    healer = Healer()
    frame_time = get_frame_time()


def exit():
    global boy, grass, cdealer, mdealer, healer, player
    del(boy)
    del(cdealer)
    del(grass)
    del(mob_dog)
    del(healer)
    del(player)

def pause():
    pass


def resume():
    pass


def handle_events(frame_time):

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_w or event.key == SDLK_a or event.key == SDLK_s or event.key == SDLK_d:
                map.keydown(event.key)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w or event.key == SDLK_a or event.key == SDLK_s or event.key == SDLK_d:
                map.keyup(event.key)



def update():
    player.update()
    cdealer.update()
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