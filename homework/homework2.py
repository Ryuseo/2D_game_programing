from pico2d import *
from math import *


def handle_events(): #2013182002 강태규
    global running
    global x
    global y
    global r
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 599 - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x = x + 10
            elif event.key == SDLK_LEFT:
                x = x - 10
            elif event.key == SDLK_UP:
                y = y + 10
            elif event.key == SDLK_DOWN:
                y = y - 10
            elif event.key == SDLK_a:
                r = r + 10
                #if r > 300:
                #    r = 300
                min(r = r + 10, 300)
            elif event.key == SDLK_d:
                r = r - 10
                #if r < 20:
                #    r = 20
                max(r = r - 10, 20)
            elif event.key == SDLK_ESCAPE:
                running = False


open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x = 400
y = 300
cx = 0
cy = 0
rad = 0
rad2 = 0
r = 100
frame = 0
while (running):
    clear_canvas()

    rad2 = pi * rad
    cx = x + sin(rad2) * r
    cy = y + cos(rad2) * r
    rad = rad + 0.1

    character.clip_draw(frame * 100, 0, 100, 100, cx, cy)

    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    handle_events()

close_canvas()
