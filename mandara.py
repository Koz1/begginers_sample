import matplotlib.pyplot as plt
import math 

n = 36 # ピンの本数
kaku = 360 / n
x = []
y = []

# 素数のリスト
pnum = [13, 7, 5, 3, 17]

# 素数番目のピンに糸をかける
plt.figure(figsize=(8, 8))
for p in pnum:
    for i in range(n+1):
        th = math.radians(kaku*i*p)
        x.append(100 * math.cos(th))
        y.append(100 * math.sin(th))

    plt.plot(x, y)

    x.clear()
    y.clear()
plt.savefig("figure1.png")
plt.show()
