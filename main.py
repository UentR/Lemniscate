import math
from PIL import Image, ImageDraw
import pygame
from time import *

def represente(liste):
    X = 1100
    im = Image.new('RGB', (X, X), color="white")
    draw = ImageDraw.Draw(im)
    for i in liste:
        i = tuple([o + X/2 for o in i])
        draw.point((i[0], i[1]), fill="red")
    im.save('Representation.png', 'PNG')
    im.show()

def lemni():
    precision = 100
    x = 0
    a = 500
    liste = []
    for i in range(precision):
        y = round((a/math.sqrt(2)) * math.sqrt(math.sqrt(1 + 8 * (x / a) ** 2) - (1 + 2 * (x / a) ** 2)), 3)
        liste.append((x, y))
        x = round(x + (a/precision), 5)
    pre = liste[0::]
    inv = liste[::-1]
    for i in inv:
        x = i[0]
        y = - 1 * i[1]
        liste.append((x, y))
    for i in pre:
        x = -1 * i[0]
        y = i[1]
        liste.append((x, y))
    for i in inv:
        x = -1 * i[0]
        y = - 1 * i[1]
        liste.append((x, y))
    return liste

def transDir(liste):
    fin = []
    for i in range(1, int(len(liste) / 4) + 1):
        x = -1 * liste[i][0] + liste[i - 1][0]
        y = -1 * liste[i][1] + liste[i - 1][1]
        try:
            ang = math.degrees(math.atan(y/x))
        except ZeroDivisionError:
            ang = 270
        hyp = math.sqrt(x ** 2 + y ** 2)
        if ang < 0:
            ang += 360
        fin.append((hyp, ang))
    pre = fin[0::]
    inv = fin[::-1]
    for i in inv:
        x = i[0]
        y = 270 - (i[1] - 270)
        fin.append((x, y))
    for i in pre:
        x = i[0]
        y = 90 - (i[1] - 90)
        fin.append((x, y))
    for i in inv:
        x = i[0]
        y = i[1]
        fin.append((x, y))
    return fin

def posR(ecran, x, y, dir):
    ecran.fill((255, 255, 255))
    x = transform(x, y)[0] - 20
    y = transform(x, y)[1]
    rover = pygame.image.load('Sprite/rover.png')
    rover = pygame.transform.scale(rover, (40, 23))
    rover = pygame.transform.rotate(rover, dir)
    ecran.blit(rover, (x, y))
    pygame.display.update()

def transform(x, y):
    x = 500 + x
    y = 500 - y
    return x, y

def somme(liste):
    moy = 0
    for i in liste:
        moy += i[0]
    return moy

represente(lemni())

liste = lemni()
fin = transDir(liste)

moy = somme(fin)
a = 5000*5.24412
print(moy, a)

print(a/moy)

ecran = pygame.display.set_mode([1000, 1000], pygame.RESIZABLE)
for j in range(5):
    for i in range(len(liste)):
        posR(ecran, liste[i][0], liste[i][1], fin[i][1])

