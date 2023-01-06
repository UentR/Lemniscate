import math
from ti_system import *
import ti_rover as rv
from time import *

def lemni():
    precision = 30
    x = 0
    a = distance()
    liste = []

    for i in range(precision):
        y = round((a/math.sqrt(2)) * math.sqrt(math.sqrt(1 + 8 * (x / a) ** 2) - (1 + 2 * (x / a) ** 2)), 5)
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

def distance():
    dev = rv.ranger_measurement()
    rv.to_angle(180)
    arr = rv.ranger_measurement()
    dist = dev + arr

    while arr > dist / 2:
        rv.forward(3)
        arr = rv.ranger_measurement()

    dev = dist - arr

    while dev > dist / 2:
        rv.backwards(2)
        dev = dist - rv.ranger_measurement()

    rv.to_angle(0)

    return int((dist/2) * 6 / 5)

def transDir(liste):
    fin = []

    for i in range(1, math.ceil(len(liste) / 4)):

        x = abs(liste[i][0] - liste[i - 1][0])
        y = abs(liste[i][1] - liste[i - 1][1])

        hyp = math.sqrt(x ** 2 + y ** 2)


        try:
            ang = math.degrees(math.atan(y/x))
        except ZeroDivisionError:
            ang = 270

        if ang < 0:
            ang += 360

        fin.append((hyp, ang))

    pre = fin[0::]
    inv = fin[::-1]

    for i in inv:
        hyp = i[0]
        ang = 270 - (i[1] - 270)
        fin.append((hyp, ang))

    for i in pre:
        hyp = i[0]
        ang = 90 - (i[1] - 90)
        fin.append((hyp, ang))

    for i in inv:
        hyp = i[0]
        ang = i[1]
        fin.append((hyp, ang))
    return fin

def conduite(liste):
    for i in liste:
        rv.to_angle(i[1])
        rv.forward(i[0])


position = lemni()
coordP = transDir(position)

while True:
    conduite(coordP)