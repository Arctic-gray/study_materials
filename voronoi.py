from PIL import Image # PIL (Python Imaging Library)
import random
import math

# Исходные данные:
# ширина и высота изображения
width = 400
height = 400
#height = 143
# координаты исходных точек
#cells = [(11, 24), (46, 87), (55, 91), (105, 50), (150, 98), (193, 100), (200, 50), (250, 87), (310, 70), (350, 93)]
#cells = [(145, 110), (90, 200), (150, 295), (200, 200), (255, 105), (310, 200), (255, 290)]
cells = [(60, 100), (215, 10), (365, 100), (215, 190), (55, 280), (210, 370), (360, 280)]


freq = 20000000
power = 44
antenna_gain = 17
pl_const = 28.0 + 20 * math.log10(freq)

image = Image.new("RGB", (width, height))
imgx, imgy = image.size

num_cells = len(cells)

nx = [] # Координата Х точек из массива cells
ny = [] # Координата У точек из массива cells
# Значения R,G,B помещаем в отдельные массивы. Цвет генерируем случайным образом
nr = []
ng = []
nb = []

for i in range(num_cells):
    nx.append(cells[i][0])
    ny.append(cells[i][1])
    nr.append(random.randrange(256))
    ng.append(random.randrange(256))
    nb.append(random.randrange(256))

for y in range(imgy):
    for x in range(imgx):
        dmin = 50 * math.hypot(imgx - 1, imgy - 1) #math.hypot(X, Y) - вычисляет гипотенузу треугольника с катетами X и Y (math.sqrt(x * x + y * y))
        power_max  = power + antenna_gain - (pl_const + 22.0 * math.log10(dmin))
        j = -1
        for i in range(num_cells):
            d = 50 * math.hypot(nx[i] - x, ny[i] - y)
            if d == 0:
                continue
            pw = power + antenna_gain - (pl_const + 22.0 * math.log10(d))
            if pw > power_max:
                power_max = pw
                j = i
        # в точку с координатами (x,y) помещаем цветную точку цветом (nr[j], ng[j], nb[j])
        image.putpixel((x, y), (nr[j], ng[j], nb[j]))

for i in range(len(cells)):
    # в каждом полигоне рисуем белую точку
    image.putpixel((cells[i][0], cells[i][1]), (255, 255, 255))
    image.putpixel((cells[i][0] + 1, cells[i][1]), (255, 255, 255))
    image.putpixel((cells[i][0], cells[i][1] + 1), (255, 255, 255))
    image.putpixel((cells[i][0] + 1, cells[i][1] + 1), (255, 255, 255))
    image.putpixel((cells[i][0] - 1, cells[i][1]), (255, 255, 255))
    image.putpixel((cells[i][0], cells[i][1] - 1), (255, 255, 255))

image.save("VoronogoDiagram.png", "PNG")
