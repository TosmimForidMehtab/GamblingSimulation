import random
import matplotlib.pyplot as plt

acocunt = 0
x = []
y = []

for i in range(365):
    x.append(i+1)

    bet = random.randint(1, 10)
    luckyDraw = random.randint(1, 10)

    if bet == luckyDraw:
        acocunt += 900-100
    else:
        acocunt -= 100
    y.append(acocunt)
plt.plot(x, y)
plt.show()
