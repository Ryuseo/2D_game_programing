from pico2d import *

import game_framework


from player import Tanker,CDealer,MDealer,Healer # import Boy class from boy.py
from mob import Dog
from map import Map
from target import Target



name = "mainstate"

tankers = None
cdealers = None
mdealers = None
healers = None
map = None
target = None
dog = None
font = None


def create_world():
    global tankers,cdealers,mdealers,healers,map,dog,target

    tankers = [Tanker() for i in range(1)]
    cdealers = [CDealer() for i in range(1)]
    mdealers = [MDealer() for i in range(1)]
    healers = [Healer() for i in range(1)]
    map = Map()
    target = Target()
    dog = [Dog(i) for i in range(11)]


def destroy_world():
    global tankers,cdealers,mdealers,healers,map,dog,target

    del(tankers)
    del(cdealers)
    del(mdealers)
    del(healers)
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


def mob_dead():
    global dog
    for dogy in dog:
        if dogy.hp < 1:
            for tanker in tankers:
                if tanker.target == dogy:
                    tanker.target = None
                    tanker.atk = False
                    tanker.pos_x = tanker.x
                    tanker.pos_y = tanker.y
            for cdealer in cdealers:
                if cdealer.target == dogy:
                    cdealer.target = None
                    cdealer.atk = False
                    cdealer.pos_x = cdealer.x
                    cdealer.pos_y = cdealer.y
            for mdealer in mdealers:
                if mdealer.target == dogy:
                    mdealer.target = None
                    mdealer.atk = False
                    mdealer.pos_x = mdealer.x
                    mdealer.pos_y = mdealer.y
            dog.remove(dogy)

def player_dead():
    global dog
    for tanker in tankers:
        if tanker.hp < 1:
            for dogy in dog:
                if  dogy.target == tanker:
                    dogy.target = None
                    dogy.atk = False
                    dogy.pos_x = dogy.x
                    dogy.pos_y = dogy.y
            for healer in healers:
                if healer.target == tanker:
                    healer.target = None
                    healer.atk = False
                    healer.pos_x = healer.x
                    healer.pos_y = healer.ydogy
            tankers.remove(tanker)
            target.x, target.y = 0, 0  # 선택대상의 좌표
            target.select = None  # 선택 대상
    for cdealer in cdealers:
        if cdealer.hp < 1:
            for dogy in dog:
                if  dogy.target == cdealer:
                    dogy.target = None
                    dogy.atk = False
                    dogy.pos_x = dogy.x
                    dogy.pos_y = dogy.y
            for healer in healers:
                if healer.target == tanker:
                    healer.target = None
                    healer.atk = False
                    healer.pos_x = healer.x
                    healer.pos_y = healer.ydogy
            cdealers.remove(cdealer)
            target.x, target.y = 0, 0  # 선택대상의 좌표
            target.select = None  # 선택 대상
    for mdealer in mdealers:
        if mdealer.hp < 1:
            for dogy in dog:
                if  dogy.target == mdealer:
                    dogy.target = None
                    dogy.atk = False
                    dogy.pos_x = dogy.x
                    dogy.pos_y = dogy.y
            for healer in healers:
                if healer.target == tanker:
                    healer.target = None
                    healer.atk = False
                    healer.pos_x = healer.x
                    healer.pos_y = healer.ydogy
            mdealers.remove(mdealer)
            target.x, target.y = 0, 0  # 선택대상의 좌표
            target.select = None  # 선택 대상
    for healer in healers:
        if healer.hp < 1:
            for dogy in dog:
                if  dogy.target == healer:
                    dogy.target = None
                    dogy.atk = False
                    dogy.pos_x = dogy.x
                    dogy.pos_y = dogy.y
            healers.remove(healer)
            target.x, target.y = 0, 0  # 선택대상의 좌표
            target.select = None  # 선택 대상

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_w or event.key == SDLK_a or event.key == SDLK_s or event.key == SDLK_d:
                map.keydown(event,frame_time,tankers,cdealers,mdealers,healers,dog)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w or event.key == SDLK_a or event.key == SDLK_s or event.key == SDLK_d:
                map.keyup(event,tankers,cdealers,mdealers,healers,dog)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                for tanker in tankers:target.input(event,tanker)
                for cdealer in cdealers:target.input(event, cdealer)
                for mdealer in mdealers:target.input(event, mdealer)
                for healer in healers:target.input(event, healer)
            elif event.button == SDL_BUTTON_RIGHT:
                for tanker in tankers:
                    if target.select == tanker:
                        tanker.getpos(event)
                        for dogy in dog:
                            target.input_td(event, dogy)
                for cdealer in cdealers:
                    if target.select == cdealer:
                        cdealer.getpos(event)
                        for dogy in dog:
                            target.input_td(event, dogy)
                for mdealer in mdealers:
                    if target.select == mdealer:
                        mdealer.getpos(event)
                        for dogy in dog:
                            target.input_td(event, dogy)
                for healer in healers:
                    if target.select == healer:
                        healer.getpos(event)
                        for tanker in tankers:
                            target.input_h(event, tanker)
                        for cdealer in cdealers:
                            target.input_h(event, cdealer)
                        for mdealer in mdealers:
                            target.input_h(event, mdealer)
                        for healer in healers:
                            target.input_h(event, healer)

def update(frame_time):
    map.update()
    for tanker in tankers:
        tanker.update(frame_time)
    for cdealer in cdealers:
        cdealer.update(frame_time)
    for mdealer in mdealers:
        mdealer.update(frame_time)
    for healer in healers:
        healer.update(frame_time)
    for dogy in dog:
        dogy.update(frame_time,tankers,cdealers,mdealers,healers)
    target.update()
    for tanker in tankers:
        for cdealer in cdealers:
            collide_unit(tanker, cdealer)
        for mdealer in mdealers:
            collide_unit(tanker, mdealer)
        for healer in healers:
            collide_unit(tanker, healer)
        for dogy in dog:
            collide_unit(tanker, dogy)

    for cdealer in cdealers:
        for tanker in tankers:
            collide_unit(cdealer, tanker)
        for mdealer in mdealers:
            collide_unit(cdealer, mdealer)
        for healer in healers:
            collide_unit(cdealer, healer)
        for dogy in dog:
            collide_unit(cdealer, dogy)

    for mdealer in mdealers:
        for cdealer in cdealers:
            collide_unit(mdealer, cdealer)
        for tanker in tankers:
            collide_unit(mdealer, tanker)
        for healer in healers:
            collide_unit(mdealer, healer)
        for dogy in dog:
            collide_unit(mdealer, dogy)

    for healer in healers:
        for cdealer in cdealers:
            collide_unit(healer, cdealer)
        for mdealer in mdealers:
            collide_unit(healer, mdealer)
        for tanker in tankers:
            collide_unit(healer, tanker)
        for dogy in dog:
            collide_unit(healer, dogy)

    for dogy in dog:
        for cdealer in cdealers:
            collide_unit(dogy, cdealer)
        for mdealer in mdealers:
            collide_unit(dogy, mdealer)
        for healer in healers:
            collide_unit(dogy, healer)
        for tanker in tankers:
            collide_unit(dogy, tanker)
        for doggy in dog:
            if doggy != dogy:
                collide_unit(doggy, dogy)

    for tanker in tankers:
        map.collide_map(tanker)
    for cdealer in cdealers:
        map.collide_map(cdealer)
    for mdealer in mdealers:
        map.collide_map(mdealer)
    for healer in healers:
        map.collide_map(healer)
    for dogy in dog:
        map.collide_map(dogy)
    mob_dead()
    player_dead()

def draw(frame_time):
    clear_canvas()

    if len(dog) == 0:
        map.draw_end()
    elif len(tankers) == 0 and len(cdealers) == 0 and len(mdealers) == 0 and len(healers) == 0:
        map.draw_end()
    else:
        map.draw()
        for tanker in tankers:
            tanker.draw()
        for cdealer in cdealers:
            cdealer.draw()
        for mdealer in mdealers:
            mdealer.draw()
        for healer in healers:
            healer.draw()
        for dogy in dog:
            dogy.draw()

        for tanker in tankers:tanker.draw_atk()
        for cdealer in cdealers:cdealer.draw_atk()
        for mdealer in mdealers:mdealer.draw_atk()
        for healer in healers:healer.draw_atk()
        for dogy in dog:
            dogy.draw_atk()

        target.draw()

    update_canvas()