import random

from pico2d import *

class Target:

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 0, 0
        self.select = None
        if Target.image == None:
            Target.image = load_image('target.png')

    def draw(self):
        if self.x != 0:
            self.image.draw(self.x, self.y)

    def update(self):
        if self.select != None:
            self.x = self.select.x;
            self.y = self.select.y + 32;

    def input(self,event, person):
        if person.x + 16 > event.x:
            if person.x - 16 < event.x:
                if person.y + 16 > 640 - event.y:
                    if person.y - 16 < 640 - event.y:
                        self.select = person

    def input_td(self,event, mob):
        if mob.x + 16 > event.x:
            if mob.x - 16 < event.x:
                if mob.y + 16 > 640 - event.y:
                    if mob.y - 16 < 640 - event.y:
                        self.select.target = mob
                        self.select.px = mob.x
                        self.select.py = mob.y

    def input_h(self,event, person):
        if person.x + 16 > event.x:
            if person.x - 16 < event.x:
                if person.y + 16 > 640 - event.y:
                    if person.y - 16 < 640 - event.y:
                        self.select.target = person
                        self.select.px = person.x
                        self.select.py = person.y









