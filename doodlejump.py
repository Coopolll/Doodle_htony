import pygame as p
import random as r
from Htony_monstriki import *
from Htony_oblachka import *
from Htony_prygalka import *
from Htony_monetki import *

p.init()
oknox = 640
oknoy = 600
okno = p.display.set_mode((oknox, oknoy))
back = p.image.load('bck.jpg')
f1 = p.font.Font('shrift.ttf', 50)
f2 = p.font.Font('shrift.ttf', 25)  # шрифты и окно

blocks = []  # список блоков
for i in range(27):
    blocks.append(Blocks('oblachko.png', 65, 19, False, blocks))
for i in range(2):
    blocks.append(Blocks('oblachko2.png', 65, 19, False, blocks))
blocks.append(Blocks('oblachko.png', 65, 19, True, blocks))

monst = []  # список монстров
for i in range(1):
    monst.append(Monster(100, 40, 'monstric1.png', 'monstric2.png', 'monstric3.png', 'monstric4.png'))

dood = Doodle('doodle_right.png', 'doodle_left.png', 46, 45)

play = True
level_plitki = 1000
level_monster = 1500
level_time = 2000
timedelay = 14
imp = [level_plitki, level_monster, level_time, timedelay]

coin_count = 0  # Счетчик монеток
current_coin = None

melodies = [
    p.mixer.Sound('e8bb96b602ce7d7.mp3'),
    p.mixer.Sound('164b99c10472d02.mp3'),
    p.mixer.Sound('ce8e6287c767e45.mp3'),
    p.mixer.Sound('we-wish-you-a-merry-christmas-synthified-music-bed-179198.mp3')
]

monster_music_playing = False

main_music = r.choice(melodies)
main_channel = p.mixer.Channel(0)
main_channel.set_volume(0.5)

monster_music = p.mixer.Sound('ryik-lva-korotkiy-zvuk-30857.mp3')
monster_channel = p.mixer.Channel(1)  # Канал для музыки монстра
monster_channel.set_volume(0.4)

monetki_music = p.mixer.Sound('podbrasyivanie-monetyi.mp3')
monetki_channel = p.mixer.Channel(2)
monetki_channel.set_volume(0.3)

die_music = p.mixer.Sound('c73057a4c775b92.mp3')
die_channel = p.mixer.Channel(3)
die_channel.set_volume(1.0)

is_monster_visible = False

while play:
    current_time = p.time.get_ticks()
    for event in p.event.get():
        if event.type == p.QUIT:
            play = False
        if event.type == p.KEYDOWN and event.key == 32 and dood.up == False:
            # создание новой игры
            dood.first = False
            level_plitki, level_monster, level_time, timedelay = imp[0], imp[1], imp[2], imp[3]
            dood.go = 0
            dood.way = 0
            coin_count = 0
            dood.up = True
            dood.vy = 8
            dood.x = (oknox - dood.width) / 2
            dood.y = oknoy - dood.height
            blocks.clear()
            if dood.game_start == False:
                main_music = r.choice(melodies)
                main_channel = p.mixer.Channel(0)
                main_channel.set_volume(0.5)
                main_channel.play(main_music)
                dood.game_start = True
            for i in range(27):
                blocks.append(Blocks('oblachko.png', 65, 19, False, blocks))
            for i in range(2):
                blocks.append(Blocks('oblachko2.png', 65, 19, False, blocks))
            blocks.append(Blocks('oblachko.png', 65, 19, True, blocks))
            monst.clear()
            for i in range(1):
                monst.append(Monster(120, 40, 'monstric1.png', 'monstric2.png', 'monstric3.png', 'monstric4.png'))

    mx, my = p.mouse.get_pos()
    okno.blit(back, (0, 0))
    okno.blit(back, (0, 512))
    okno.blit(back, (320, 0))
    okno.blit(back, (320, 512))

    for i in range(len(blocks)):
        blocks[i].draw(dood)
        okno.blit(blocks[i].img, (blocks[i].x, blocks[i].y))

    if dood.go >= level_plitki:
        level_plitki += 1000
        for i in range(len(blocks)):
            if blocks[i].broke == -1:
                blocks[i].img = p.image.load('oblachko2.png')  # каждые 1000 меняем 1 зеленую плитку на ораньжевую
                blocks[i].broke = 1
                break
    if dood.go >= level_monster:
        level_monster += 1500
        monst.append(Monster(120, 40, 'monstric1.png', 'monstric2.png', 'monstric3.png', 'monstric4.png'))

    if dood.go >= level_time:
        level_time += 2000
        if timedelay >= 7:
            timedelay -= 1  # ускорение игры каждые 2000

    dood.draw(mx, my, blocks, current_coin, coin_count)
    okno.blit(dood.itogimg, (dood.x, dood.y))

    for i in range(len(monst)):
        monst[i].draw(dood, monst, die_channel, die_music)
        okno.blit(monst[i].itogimg, (monst[i].x, monst[i].y))

    has_visible_monster = any(monster.is_visible for monster in monst)

    if has_visible_monster != is_monster_visible and dood.game_start == True:
        is_monster_visible = has_visible_monster
        if is_monster_visible:
            monster_channel.play(monster_music)
        else:
            monster_channel.stop()

    text1 = f1.render(dood.text1, False, (0, 0, 0))
    text2 = f1.render(dood.text2, False, (0, 0, 0))
    text3 = f2.render(str(max(0, int(dood.go))), False, (0, 0, 0))
    text4 = f2.render(str(int(coin_count)), False, (0, 0, 0))
    text5 = f1.render(dood.text3, False, (0, 0, 0))
    okno.blit(text1, (200, 120))
    okno.blit(text2, (55, 250))
    okno.blit(text3, (0, 0))
    okno.blit(text4, (600, 0))
    okno.blit(text5, (50, 380))
    okno.blit(p.image.load('monetka.png'), (565, 0))

    if current_coin is None or current_coin.is_collected or current_coin.y > oknoy:
        current_coin = Coin(r.randint(0, oknox - 20), 0, 1, 'monetka.png')

    current_coin.draw(dood, okno)

    # Проверяем столкновение и собираем монетку, если необходимо
    if not current_coin.is_collected and dood.collides_with(current_coin):
        coin_count += current_coin.value
        current_coin.collect()
        monetki_channel.play(monetki_music)

    p.display.update()
    p.time.delay(timedelay)
