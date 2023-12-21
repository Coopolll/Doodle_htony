import pygame as p
import random as r

from Htony_oblachka import *
from Htony_prygalka import *
from Htony_objects import *

oknox = 640
oknoy = 600


class Coin(object):
    def __init__(self, x, y, value, coin_image):
        super().__init__(x, y, 25, 25)
        self.value = value
        self.img = p.image.load(coin_image)
        self.is_collected = False

    def draw(self, dood, okno):
        if not self.is_collected:
            if dood.up and dood.vy > 0 and dood.way > 0:
                self.y += dood.vy
            elif not dood.up and dood.y >= oknoy - dood.height:
                self.y += dood.vy
            if self.y > oknoy:
                self.x = r.randint(0, int(oknox - self.width * 2))
                self.y = r.randint(-300, -int(self.height))
            okno.blit(self.img, (self.x, self.y))

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

    def collect(self):
        self.is_collected = True
