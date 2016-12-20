import random
from math import *
from pico2d import *
import time

class Tanker:
    PIXEL_PER_METER = (32.0 / 2)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
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
        self.hp = 150
        self.mhp = 150
        self.x, self.y = 480.0, 250.0
        self.pos_x, self.pos_y = 480.0, 250.0
        self.view_move_x, self.view_move_y = 0,0
        self.total_frames = 0.0;
        self.frame = 0
        self.cooldown = time.clock()
        self.atk = False
        self.target = None
        self.xdir, self.ydir = 0.0, 0.0
        self.state = self.FRONT_STAND
        if Tanker.image == None:
            Tanker.image = load_image('tanker.png')
        if Tanker.image_atk == None:
            Tanker.image_atk = load_image('tanker_atk1.png')


    def update(self, frame_time):
        if(self.pos_x != self.x and self.pos_y != self.y):
            tempos_x = self.pos_x - self.x
            tempos_y = self.pos_y - self.y
            temp = sqrt(pow(tempos_x, 2) + pow(tempos_y, 2))
            self.xdir = tempos_x / temp
            self.ydir = tempos_y / temp
            if temp < 50 and self.target != None and time.clock() - self.cooldown > 3:
                self.cooldown = time.clock()
                self.atk = True
                self.atking()
        if time.clock() - self.cooldown > 0.5:
            self.atk = False
        distance = Tanker.RUN_SPEED_PPS * frame_time
        self.total_frames += Tanker.FRAMES_PER_ACTION * Tanker.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 3
        self.xdir = self.xdir * distance
        self.ydir = self.ydir * distance
        if self.target != None and sqrt(pow(self.pos_x - self.x, 2) + pow(self.pos_y - self.y, 2)) < 50:
                self.ydir = 0
                self.xdir = 0
        self.x += self.xdir + self.view_move_x
        self.y += self.ydir + self.view_move_y
        if self.target != None:
            self.pos_x = self.target.x
            self.pos_y = self.target.y

        self.pos_x += self.view_move_x
        self.pos_y += self.view_move_y

    def draw(self):
        self.image.clip_draw(self.frame * 32, self.state * 32, 32, 32, self.x, self.y)

    def draw_atk(self):
        if self.atk == True:
            self.image_atk.draw(self.target.x,self.target.y)



    def getpos(self,event):
        self.atk = False
        self.pos_x = event.x
        self.pos_y = 640 - event.y
        self.target = None

    def atking(self):
        self.target.hp -= 5;

class CDealer:
    PIXEL_PER_METER = (32.0 / 2)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    image_atk =None

    BACK_STAND, RIGHT_STAND, LEFT_STAND, FRONT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.hp = 100
        self.mhp = 100
        self.x, self.y = 430.0, 200.0
        self.pos_x, self.pos_y = 430.0, 250.0
        self.view_move_x, self.view_move_y = 0, 0
        self.total_frames = 0.0;
        self.frame = 0
        self.cooldown = time.clock()
        self.atk = False
        self.target = None
        self.xdir, self.ydir = 0.0, 0.0
        self.state = self.FRONT_STAND
        if CDealer.image == None:
            CDealer.image = load_image('close_dealer.png')
        if CDealer.image_atk == None:
            CDealer.image_atk = load_image('cdealer_atk1.png')


    def update(self, frame_time):
        if (self.pos_x != self.x and self.pos_y != self.y):
            tempos_x = self.pos_x - self.x
            tempos_y = self.pos_y - self.y
            temp = sqrt(pow(tempos_x, 2) + pow(tempos_y, 2))
            self.xdir = tempos_x / temp
            self.ydir = tempos_y / temp
            if temp < 50 and self.target != None and time.clock() - self.cooldown > 3:
                self.atk = True
                self.cooldown = time.clock()
                self.atking()
        if time.clock() - self.cooldown > 0.5:
            self.atk = False
        distance = Tanker.RUN_SPEED_PPS * frame_time
        self.total_frames += Tanker.FRAMES_PER_ACTION * Tanker.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 3
        self.xdir = self.xdir * distance
        self.ydir = self.ydir * distance
        if self.target != None and sqrt(pow(self.pos_x - self.x, 2) + pow(self.pos_y - self.y, 2)) < 50:
            self.ydir = 0
            self.xdir = 0
        self.x += self.xdir + self.view_move_x
        self.y += self.ydir + self.view_move_y
        if self.target != None:
            self.pos_x = self.target.x
            self.pos_y = self.target.y

        self.pos_x += self.view_move_x
        self.pos_y += self.view_move_y

    def draw(self):
        self.image.clip_draw(self.frame * 32, self.state * 32, 32, 32, self.x, self.y)

    def draw_atk(self):
        if self.atk == True:
            self.image_atk.draw(self.target.x, self.target.y)

    def getpos(self,event):
        self.pos_x = event.x
        self.pos_y = 640 - event.y
        self.target = None
        self.atk = False

    def atking(self):
        self.target.hp -= 10;

class MDealer:
    PIXEL_PER_METER = (32.0 / 2)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
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
        self.hp = 80
        self.mhp = 80
        self.x, self.y = 530.0, 200.0
        self.pos_x, self.pos_y = 530.0, 200.0
        self.view_move_x, self.view_move_y = 0, 0
        self.total_frames = 0.0;
        self.frame = 0
        self.cooldown = time.clock()
        self.atk = False
        self.target = None
        self.xdir, self.ydir = 0.0, 0.0
        self.state = self.FRONT_STAND
        if MDealer.image == None:
            MDealer.image = load_image('magic_dealer.png')
        if MDealer.image_atk == None:
            MDealer.image_atk = load_image('fire.png')


    def update(self, frame_time):
        if(self.pos_x != self.x and self.pos_y != self.y):
            tempos_x = self.pos_x - self.x
            tempos_y = self.pos_y - self.y
            temp = sqrt(pow(tempos_x, 2) + pow(tempos_y, 2))
            self.xdir = tempos_x / temp
            self.ydir = tempos_y / temp
            if temp < 200 and self.target != None and time.clock() - self.cooldown > 3:
                self.atk = True
                self.cooldown = time.clock()
                self.atking()
        if time.clock() - self.cooldown > 0.5:
            self.atk = False
        distance = MDealer.RUN_SPEED_PPS * frame_time
        self.total_frames += MDealer.FRAMES_PER_ACTION * MDealer.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 3
        self.xdir = self.xdir * distance
        self.ydir = self.ydir * distance
        if self.target != None and sqrt(pow(self.pos_x - self.x, 2) + pow(self.pos_y - self.y, 2)) < 200:
            self.ydir = 0
            self.xdir = 0
        self.x += self.xdir + self.view_move_x
        self.y += self.ydir + self.view_move_y
        if self.target != None:
            self.pos_x = self.target.x
            self.pos_y = self.target.y
        self.pos_x += self.view_move_x
        self.pos_y += self.view_move_y

    def draw(self):
        self.image.clip_draw(self.frame * 32, self.state * 32, 32, 32, self.x, self.y)

    def draw_atk(self):
        if self.atk == True:
            self.image_atk.draw(self.target.x, self.target.y)

    def getpos(self,event):
        self.pos_x = event.x
        self.pos_y = 640 - event.y
        self.target = None
        self.atk = False

    def atking(self):
        self.target.hp -= 10;

class Healer:
    PIXEL_PER_METER = (32.0 / 2)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
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
        self.hp = 80
        self.mhp = 80
        self.x, self.y = 480.0, 200.0
        self.pos_x, self.pos_y = 480.0, 200.0
        self.view_move_x, self.view_move_y = 0, 0
        self.total_frames = 0.0;
        self.frame = 0
        self.cooldown = time.clock()
        self.atk = False
        self.target = None
        self.xdir, self.ydir = 0.0, 0.0
        self.state = self.FRONT_STAND
        if Healer.image == None:
            Healer.image = load_image('healer.png')
        if Healer.image_atk == None:
            Healer.image_atk = load_image('heal.png')


    def update(self, frame_time):
        if(self.pos_x != self.x and self.pos_y != self.y):
            tempos_x = self.pos_x - self.x
            tempos_y = self.pos_y - self.y
            temp = sqrt(pow(tempos_x, 2) + pow(tempos_y, 2))
            self.xdir = tempos_x / temp
            self.ydir = tempos_y / temp
        if sqrt(pow(self.pos_x - self.x, 2) + pow(self.pos_y - self.y, 2)) < 200 and self.target != None and time.clock() - self.cooldown > 3:
            self.atk = True
            self.cooldown = time.clock()
            self.atking()
        if time.clock() - self.cooldown > 0.5:
            self.atk = False
        distance = Healer.RUN_SPEED_PPS * frame_time
        self.total_frames += Healer.FRAMES_PER_ACTION * Healer.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 3
        self.xdir = self.xdir * distance
        self.ydir = self.ydir * distance
        if self.target != None and sqrt(pow(self.pos_x - self.x, 2) + pow(self.pos_y - self.y, 2)) < 200:
                self.ydir = 0
                self.xdir = 0
        self.x += self.xdir + self.view_move_x
        self.y += self.ydir + self.view_move_y
        if self.target != None:
            self.pos_x = self.target.x
            self.pos_y = self.target.y
        self.pos_x += self.view_move_x
        self.pos_y += self.view_move_y

    def draw(self):
        self.image.clip_draw(self.frame * 32, self.state * 32, 32, 32, self.x, self.y)

    def draw_atk(self):
        if self.atk == True:
            self.image_atk.clip_draw( self.frame * 32, 0, 32, 32, self.target.x, self.target.y)

    def getpos(self,event):
        self.pos_x = event.x
        self.pos_y = 640 - event.y
        self.target = None
        self.atk = False

    def atking(self):
        self.target.hp += 10
        if self.target.mhp < self.target.hp:
             self.target.hp = self.target.mhp
