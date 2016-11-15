import random
import time
from math import  *

from pico2d import *

class Dog:
    PIXEL_PER_METER = (32.0 / 2)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 22.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    image_atk = None

    BACK_STAND, RIGHT_STAND, LEFT_STAND, FRONT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.hp = 100
        self.x, self.y = 500.0, 500.0
        self.px, self.py = 500.0, 500.0
        self.vx, self.vy = 0, 0
        self.total_frames = 0.0;
        self.target = None
        self.frame = 0
        self.cooldown = time.clock()
        self.atk = False
        self.xdir, self.ydir = 0.0, 0.0
        self.state = self.FRONT_STAND
        if Dog.image == None:
            Dog.image = load_image('dog.png')
        if Dog.image_atk == None:
            Dog.image_atk = load_image('tanker_atk1.png')


    def update(self, frame_time,tanker,cdealer,mdealer,healer):
        if (self.px != self.x and self.py != self.y):
            tempx = self.px - self.x
            tempy = self.py - self.y
            temp = sqrt(pow(tempx, 2) + pow(tempy, 2))
            self.xdir = tempx / temp
            self.ydir = tempy / temp
            if temp < 50 and self.target != None and time.clock() - self.cooldown > 3:
                self.atk = True
                self.cooldown = time.clock()
        if time.clock() - self.cooldown > 0.5:
            self.atk = False
        distance = Dog.RUN_SPEED_PPS * frame_time
        self.total_frames += Dog.FRAMES_PER_ACTION * Dog.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 3
        self.xdir = self.xdir * distance
        self.ydir = self.ydir * distance
        if self.target != None and sqrt(pow(self.px - self.x, 2) + pow(self.py - self.y, 2)) < 50:
                self.ydir = 0
                self.xdir = 0
        self.x += self.xdir + self.vx
        self.y += self.ydir + self.vy
        if self.target != None:
            self.px = self.target.x
            self.py = self.target.y


        self.px += self.vx
        self.py += self.vy
        if self.target == None:
            self.serch(tanker,cdealer,mdealer,healer)

    def draw(self):
        self.image.clip_draw(self.frame * 32, self.state * 32, 32, 32, self.x, self.y)

    def draw_atk(self):
        if self.atk == True:
            self.image_atk.draw(self.target.x,self.target.y)
            self.atking()

    def getpos(self,event):
        self.px = event.x
        self.py = 640 - event.y

    def serch(self,tanker,cdealer,mdealer,healer):
        tempx = tanker.x - self.x
        tempy = tanker.y - self.y
        temp = sqrt(pow(tempx, 2) + pow(tempy, 2))
        if temp < 200:
            self.target = tanker
        tempx = cdealer.x - self.x
        tempy = cdealer.y - self.y
        temp = sqrt(pow(tempx, 2) + pow(tempy, 2))
        if temp < 200:
            self.target = cdealer
        tempx = mdealer.x - self.x
        tempy = mdealer.y - self.y
        temp = sqrt(pow(tempx, 2) + pow(tempy, 2))
        if temp < 200:
            self.target = mdealer
        tempx = healer.x - self.x
        tempy = healer.y - self.y
        temp = sqrt(pow(tempx, 2) + pow(tempy, 2))
        if temp < 200:
            self.target = healer

    def atking(self):
        self.target.hp -= 10