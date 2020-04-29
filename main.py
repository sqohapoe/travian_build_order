import os
os.chdir(r"C:\Users\victo\Desktop\BO")
from idiot import IdiotFinder
from greedy import GreedyFinder
from solution import Solution
from exploration import ExploreFinder
import matplotlib.pyplot as plt
import numpy as np

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--explore")
args = parser.parse_args()


DAY=5
MAX_ITER = 20000
MAX_PATIENCE = 2000

# try:
#     order = np.load('BO.npy')
#     start = Solution(list(order), day=DAY)
#     print("continue with given order")
# except FileNotFoundError:
#     gf = GreedyFinder(day=DAY)
#     gf.find()
#     start = Solution(gf.t.get_order(), day=DAY)
#     print("start from greedy")

order = np.load("HIGHCP.npy")
start = Solution(list(order), day=DAY)
print("continue with HIGHCP.npy")

constraints = np.linspace(600, 250, 100)
max_res = np.empty_like(constraints)
for i,lower_bound in enumerate(constraints):
    ef = ExploreFinder(start, method="cid", eval_method='res', lower_bound=lower_bound,
                       max_iter=MAX_ITER, max_patience=MAX_PATIENCE)
    ef.find()
    x1, y1 = ef.max_so_far_history_x, ef.max_so_far_history_y
    y2 = ef.other_history
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('generation')
    ax1.set_ylabel(ef.EVAL_METHOD, color=color)
    ax1.plot(x1, y1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel("cp", color=color)  # we already handled the x-label with ax1

    ax2.plot(x1, y2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    import os
    os.chdir("plotting_and_npy")
    plt.savefig("BOforlowerbound{}.png".format(lower_bound))
    np.save("BOforlowerbound{}.npy".format(lower_bound), ef.argmax_so_far.order)
    os.chdir("..")
    max_res[i] = ef.max_so_far

plt.plot(constraints, max_res)
plt.savefig("max_res vs constraints.png")
