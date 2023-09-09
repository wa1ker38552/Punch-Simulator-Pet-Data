import pyautogui as dev
import time

GLOBALX, GLOBALY = dev.size()
KEYCODE = {
    '170 255 127': 'UNCOMMON',
    '85 170 255': 'RARE',
    '170 85 255': 'MYTHIC',
    '255 255 127': 'LEGENDARY',
    '193 0 3': 'SECRET'
}

def get_position():
    while True:
        x, y = dev.position()
        print(x, y)
        time.sleep(1)

stats = {'UNCOMMON': 0, 'RARE': 0, 'MYTHIC': 0, 'LEGENDARY': 0, 'SECRET': 0}
eggs = 0
while True:
    r, g, b = dev.pixel(round(GLOBALX/2), round(GLOBALY/2))
    if r+g+b < 100:
        eggs += 1
        time.sleep(1.9)
        r, g, b = dev.pixel(1215, 1225)
        if f'{r} {g} {b}' in KEYCODE:
            stats[KEYCODE[f"{r} {g} {b}"]] += 1
            total = sum([stats[i] for i in stats])
            u = stats["UNCOMMON"]
            r = stats["RARE"]
            m = stats["MYTHIC"]
            l = stats["LEGENDARY"]
            s = stats["SECRET"]
            print(f'EGG HATCHED: {round(u/total*100)}/{round(r/total*100)}/{round(m/total*100)}/{round(l/total*100)}/{round(s/total*100)} || {u}/{r}/{m}/{l}/{s} || {total}')
        else:
            print(r, g, b)
