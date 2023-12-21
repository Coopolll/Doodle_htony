import pygame as p
import random as r

from Htony_monstriki import *
from Htony_oblachka import *
from Htony_monetki import *

p.init()
f1 = p.font.Font('shrift.ttf', 50)

oknox = 640
oknoy = 600


class Doodle(object):  # гг, сам дудл который следует за мышкой
    def __init__(self, imgright, imgleft, width, height):
        # super().__init__(0, 0, 0, 0)
        self.width = width
        self.height = height
        self.first = True
        self.x = (oknox - self.width) / 2
        self.y = oknoy - self.height
        self.centerx = self.x + self.width / 2
        self.centery = self.y + self.height / 2
        self.imgright = p.image.load(imgright)
        self.imgleft = p.image.load(imgleft)
        self.itogimg = self.imgleft
        self.max = 250  # уровень отсекающий вертикальное движение выше планки
        self.way = 0  # на сколько движется экран
        self.vx = 0
        self.vy = 9
        self.ay = -0.15
        self.up = False  # смерть
        self.text1 = ''
        self.text2 = ''
        self.text3 = ''
        self.go = 0  # колво очков
        self.game_start = False

    def draw(self, mx, my, blocks, coins, coin_count):
        self.centerx = self.x + self.width / 2
        self.centery = self.y + self.height / 2
        self.vx = (mx - self.centerx) / 10
        if (self.vx > 0):
            self.itogimg = self.imgright
        elif (self.vx < 0):
            self.itogimg = self.imgleft
        self.x += self.vx
        if (self.up == True):
            self.text1 = ''
            self.text2 = ''
            self.text3 = ''
            self.vy += self.ay
            self.y -= self.vy
            if (self.go <= self.max):
                self.go += self.vy
            elif ((self.up == True) and (self.vy > 0) and (self.way > 0)):
                self.go += self.vy
            if (self.y <= self.max):
                self.y = self.max
                self.way += self.vy
            if (self.vy <= 0):
                self.way = 0
                for i in range(len(blocks)):
                    if ((blocks[i].x + 13 <= self.x + self.width) and (
                            blocks[i].x + 13 + blocks[i].width >= self.x) and (
                            blocks[i].y <= self.y + self.height) and (
                            blocks[i].y >= self.y + self.height + self.vy)):  # удар о блоки
                        self.vy = 9
                        if (blocks[i].broke > 0):
                            blocks[i].broke -= 1
            if (self.y + self.height >= oknoy):
                self.up = False
                self.way = 0
        elif (self.up == False):  # анимация падения
            if self.first:
                self.text1 = 'Начать игру!'
                self.text2 = '           Нажми пробел!'
            else:
                self.vy = -5
                if (self.y < oknoy - self.height):
                    self.y -= self.vy
                    self.way = 0
                elif (self.y >= oknoy - self.height):
                    self.y = oknoy - self.height
                    self.way -= self.vy
                    if (self.way >= oknoy + 100):
                        self.vy = 0
                        self.text1 = 'Ты проиграл!'
                        self.text2 = 'Очков: ' + str(max(0, int(self.go))) + '         ' + 'Монеток:' + str(
                            int(coin_count))
                        self.text3 = 'Нажми пробел, чтобы продолжить'
                        p.mixer.music.stop()
                        self.game_start = False

    def collides_with(self, other_object):
        dood_left = self.x
        dood_right = self.x + self.width
        dood_top = self.y
        dood_bottom = self.y + self.height

        other_left = other_object.x
        other_right = other_object.x + other_object.width
        other_top = other_object.y
        other_bottom = other_object.y + other_object.height

        if (dood_right >= other_left and
                dood_left <= other_right and
                dood_bottom >= other_top and
                dood_top <= other_bottom):
            return True
        else:
            return False
