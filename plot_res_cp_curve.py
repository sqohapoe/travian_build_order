import os
os.chdir(r"C:\Users\victo\Desktop\BO\plotting_and_npy")
l = os.listdir()
m = []
for ele in l:
    if ele[-3:] == "npy":
        m.append(ele)



import numpy as np
from solution import Solution
from exploration import ExploreFinder
res = []
cp = []
for ele in m:
    order = np.load(r"C:\Users\victo\Desktop\BO\plotting_and_npy\{}".format(ele), allow_pickle=True)
    # print(order)
    sol = Solution(list(order), day=5)
    res.append(sol.evaluate(eval_method="res"))
    cp.append(int(ele[15:18]))

for i in range(len(res)-1, -1, -1):
    res[i] = max(res[i:])
import matplotlib.pyplot as plt
plt.plot(cp, res)
plt.xlabel('cp lowerbound constraint')
plt.ylabel('max res calculated')
plt.show()

