import sympy as sym

lambd = sym.Symbol('lambd')
sphere = [0, 0, 0]
radius = 10.67
line1 = [1, 0.5, 15]
line2 = [43, -14.6, 0.04]

a = sym.solveset((line1[0] + (line2[0] - line1[0]) * lambd - sphere[0]) ** 2 + (
            line1[1] + (line2[1] - line1[1]) * lambd - sphere[1]) ** 2 + (
            line1[2] + (line2[2] - line1[2]) * lambd - sphere[2]) ** 2 - radius ** 2)

for i in a:
    PointX = (line1[0] + (line2[0] - line1[0]) * i)
    PointY = (line1[1] + (line2[1] - line1[1]) * i)
    PointZ = (line1[2] + (line2[2] - line1[2]) * i)
    print(PointX, " ", PointY, " ", PointZ)
