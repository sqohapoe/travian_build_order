import numpy as np
from solution import Solution
from idiot import IdiotFinder


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--filename")
parser.add_argument("--day", help='default 5 days')
parser.add_argument("--show")
parser.add_argument("--save")
args = parser.parse_args()

filename = "idiot" if args.filename is None else args.filename

day = 5 if args.day is None else args.day
ifd = IdiotFinder(day=day)

ifd.find()
sol = ifd.t.get_order()

if args.save is None or args.save == True:
    np.save('idiot', sol)

if args.show:
    Solution(sol, day=day).show()





