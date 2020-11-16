import sympy as sym

lambd = sym.Symbol('lambd')
sphere = [0, 0, 0]
radius = 10
line1 = [20, 0, 60]
line2 = [20, 0, -60]

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
