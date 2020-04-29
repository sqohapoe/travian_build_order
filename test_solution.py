import argparse
import numpy as np
from solution import Solution
parser = argparse.ArgumentParser()

parser.add_argument('--swap')
parser.add_argument('--filename')
parser.add_argument('--day')
parser.add_argument("--show")
args = parser.parse_args()


filename = "BO.npy" if args.filename is None else args.filename
day = 5 if args.day is None else args.day
order = np.load(filename)
sol = Solution(order, day=day)
print(sol.evaluate())
if args.show:
    sol.show()
if not args.swap is None:
    a, b = args.swap.split()
    a, b = int(a), int(b)
    sol = sol.swap(a, b)
    print("changed")
    print(sol.evaluate())
    if args.show:
        sol.show()