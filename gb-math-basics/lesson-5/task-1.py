import numpy as np

for i in range(0, 5):
    val = np.random.randint(0, 36)
    print(val)
    if val == 0:
        print("zero")
    elif val % 2 == 0:
        print("red")
    else:
        print("black")
