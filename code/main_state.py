from pico2d import *

import game_framework


from player import Tanker,CDealer,MDealer,Healer # import Boy class from boy.py
from mob import Dog
from map import Map
from target import Target



name = "mainstate"

tanker = None
cdealer = None
mdealer = None
healer = None
map = None
target = None
mob_dog = None
font = None


def create_world():
    global tanker,cdealer,mdealer,healer,map,dog,target

    tanker = Tanker()
    cdealer = CDealer()
    mdealer = MDealer()
    healer = Healer()
    map = Map()
    target = Target()
    dog = Dog()


def destroy_world():
    global tanker,cdealer,mdealer,healer,map,dog,target

    del(tanker)
    del(cdealer)
    del(mdealer)
    del(healer)
    del(map)
    del(dog)
    del(target)

def enter():
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass

def collide_unit(a, b):

    if a.x + 16 > b.x - 16:
        if a.x - 16 < b.x + 16:
            if a.y + 16 > b.y - 16:
                if a.y - 16 < b.y + 16:
                    a.x -= (a.xdir)
                    a.y -= (a.ydir)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_w or event.key == SDLK_a or event.key == SDLK_s or event.key == SDLK_d:
                map.keydown(event,frame_time,tanker,cdealer,mdealer,healer,dog)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w or event.key == SDLK_a or event.key == SDLK_s or event.key == SDLK_d:
                map.keyup(event,tanker,cdealer,mdealer,healer,dog)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                target.input(event,tanker)
                target.input(event, cdealer)
                target.input(event, mdealer)
                target.input(event, healer)
            elif event.button == SDL_BUTTON_RIGHT:
                if target.select == tanker:
                    tanker.getpos(event)
                    target.input_td(event, dog)
                if target.select == cdealer:
                    cdealer.getpos(event)
                    target.input_td(event, dog)
                if target.select == mdealer:
                    mdealer.getpos(event)
                    target.input_td(event, dog)
                if target.select == healer:
                    healer.getpos(event)
                    target.input_h(event, tanker)
                    target.input_h(event, cdealer)
                    target.input_h(event, mdealer)

def update(frame_time):
    map.update()
    tanker.update(frame_time)
    cdealer.update(frame_time)
    mdealer.update(frame_time)
    healer.update(frame_time)
    dog.update(frame_time,tanker,cdealer,mdealer,healer)
    target.update()
    collide_unit(tanker, cdealer)
    collide_unit(tanker, mdealer)
    collide_unit(tanker, healer)
    collide_unit(tanker, dog)

    collide_unit(cdealer, tanker)
    collide_unit(cdealer, mdealer)
    collide_unit(cdealer, healer)
    collide_unit(cdealer, dog)

    collide_unit(mdealer, cdealer)
    collide_unit(mdealer, tanker)
    collide_unit(mdealer, healer)
    collide_unit(mdealer, dog)

    collide_unit(healer, cdealer)
    collide_unit(healer, mdealer)
    collide_unit(healer, tanker)
    collide_unit(healer, dog)

    collide_unit(dog, cdealer)
    collide_unit(dog, mdealer)
    collide_unit(dog, healer)
    collide_unit(dog, tanker)

def draw(frame_time):
    clear_canvas()

    map.draw()
    tanker.draw()
    cdealer.draw()
    mdealer.draw()
    healer.draw()
    dog.draw()
    target.draw()

    update_canvas()