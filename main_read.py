import numpy as np

from solution import Solution
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("filename", help='default BO')
parser.add_argument("--day")

args = parser.parse_args()

filename = "BO.npy" if args.filename is None else args.filename
day = 5 if args.day is None else int(args.day)

order = np.load(filename)
solution = Solution(order, day=day)
solution.show()

print(solution.evaluate())
print("cp: ", solution.get_total_cp())
print("res: ", solution.get_total_res())