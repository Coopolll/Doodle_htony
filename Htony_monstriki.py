import pygame as p
import random as r

from Htony_oblachka import *
from Htony_prygalka import *
from Htony_objects import *
from Htony_monetki import *

oknox = 640
oknoy = 600


class Monster(object):
    def __init__(self, width, height, img1, img2, img3, img4):
        super().__init__(r.randint(int(width), int(oknox - 2 * width)), r.randint(-3000, -2000), width, height)
        self.img1 = p.image.load(img1)
        self.img2 = p.image.load(img2)
        self.img3 = p.image.load(img3)
        self.img4 = p.image.load(img4)
        self.itogimg = self.img1
        self.chet = 0
        self.vx = 3
        self.is_visible = False

    def draw(self, dood, monst, die_channel, die_music):
        self.x += self.vx
        self.chet += 1
        if (self.chet == 3):
            self.itogimg = self.img1
        elif (self.chet == 6):
            self.itogimg = self.img2
        elif (self.chet == 9):
            self.itogimg = self.img3
        elif (self.chet == 12):
            self.itogimg = self.img4  # анимация пархания
            self.chet = 0
        if ((self.x + self.width >= oknox) or (self.x <= 0)):
            self.vx = -self.vx
        if (((dood.up == True) and (dood.vy > 0) and (dood.way > 0)) or (
                (dood.up == False) and (dood.y >= oknoy - dood.height))):
            self.y += dood.vy
        if (self.y >= oknoy):
            self.y = r.randint(-2000, -1000)
        for i in range(len(monst)):  # проверка на столкновение с мобом
            if ((dood.x + dood.width > self.x) and (dood.x < self.x + self.width) and (
                    dood.y < self.y + self.height) and (dood.y + dood.width > self.y)):
                dood.up = False
                die_channel.play(die_music)
        if self.y > 0 and self.y < oknoy:
            self.is_visible = True
        else:
            self.is_visible = False
