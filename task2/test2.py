import sympy as sym
import re

with open('coordinates.txt', 'r') as s:
    for sand in s:
        center = re.findall(r'center: .*?]', sand)
        center = re.findall(r'[\d+]', center[0])
        for index in range(len(center)):
            center[index] = int(center[index])
        radius = re.findall(r'radius: [0-9.-]+', sand)
        radius = re.findall(r'[\d+.]', radius[0])
        radius = ''.join(radius)
        radius = float(radius)
        line = (re.findall(r'line: {.+?}', sand))
        line = (re.findall(r'[0-9.+-]+', line[0]))

        lambd = sym.Symbol('lambd')
        sphere = center

        radius = radius

        line1 = [float(line[0]), float(line[1]), float(line[2])]
        line2 = [float(line[3]), float(line[4]), float(line[5])]

        a = sym.solveset((line1[0] + (line2[0] - line1[0]) * lambd - sphere[0]) ** 2 + (
                line1[1] + (line2[1] - line1[1]) * lambd - sphere[1]) ** 2 + (
                                 line1[2] + (line2[2] - line1[2]) * lambd - sphere[2]) ** 2 - radius ** 2)

        for i in a:
            PointX = (line1[0] + (line2[0] - line1[0]) * i)
            PointY = (line1[1] + (line2[1] - line1[1]) * i)
            PointZ = (line1[2] + (line2[2] - line1[2]) * i)
            if "I" in (str(PointX) and str(PointY) and str(PointZ)):
                print('Коллизий не найдено')
                break
            else:
                print(round(float(PointX), 3), " ", round(float(PointY), 3), " ", round(float(PointZ), 3))
        print()