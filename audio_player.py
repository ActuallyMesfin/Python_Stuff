import time
import random


i = 1
while True:
    x = random.randint(0,5)
    y = str(random.randrange(3, 5))
    mbs = f"{y} +  MB/S : "
    i = i * x
    print(mbs, end="")
    print('|'*i, end="")
    time.sleep(1)
    if i == 20:
        break