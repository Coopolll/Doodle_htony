import pygame as p
import random as r

from Htony_monstriki import *
from Htony_prygalka import *
from Htony_objects import *
from Htony_monetki import *

oknox = 640
oknoy = 600


class Blocks(object):
    def __init__(self, img, width, height, starter, blocks):
        super().__init__(0, 0, width / 2, height)
        self.time = 5
        self.all_blocks = blocks
        if (starter == False):
            self.generate_random_position()
        elif (starter == True):  # starter создает первый блок в самом начале под дудлом
            self.x = (oknox - self.width) / 2
            self.y = oknoy - self.height
        self.img = p.image.load(img)
        if (img == 'oblachko2.png'):  # вид блока -1 это нормальный 1 это ломающийся
            self.broke = 1
        else:
            self.broke = -1

    def generate_random_position(self):
        self.x = r.randint(0, int(oknox - self.width * 2))
        self.y = r.randint(0, int(oknoy - self.height))
        while self.collides_with_other_blocks():
            self.x = r.randint(0, int(oknox - self.width * 2))
            self.y = r.randint(0, int(oknoy - self.height))

    def collides_with_other_blocks(self):
        for block in self.all_blocks:
            if (block != self and
                    self.x < block.x + block.width and
                    self.x + self.width > block.x and
                    self.y < block.y + block.height and
                    self.y + self.height > block.y):
                return True
        return False

    def draw(self, dood):
        if (((dood.up == True) and (dood.vy > 0) and (dood.way > 0) and (self.broke != 0)) or (
                (dood.up == False) and (dood.y >= oknoy - dood.height))):
            self.y += dood.vy
        elif (self.broke == 0):
            self.img = p.image.load('oblachko3.png')  # анимация ломания блока 1
            self.y += 5
            if self.time == 0:
                self.y = oknox + 100
            else:
                self.time -= 1
        if (self.y > oknoy):  # переносим блок ушедший вниз наверх и восстанавливаем сломанный блок
            if (self.broke == 0):
                self.img = p.image.load('oblachko2.png')
                self.broke = 1
                self.time = 5
            self.x = r.randint(0, int(oknox - self.width * 2))
            self.y = r.randint(-300, -int(self.height))
