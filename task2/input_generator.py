import random

for i in range(10):
    def rN():
        return round(random.uniform(100, -100), 2)

    with open('coordinates.txt', 'a') as me:
        me.writelines(
        F"{{sphere: {{center: [{rN()}, {rN()}, {rN()}], radius: {rN()}}}, line: {{[{rN()}, {rN()}, {rN()}], [{rN()}, {rN()}, {rN()}]}}}} \n")


