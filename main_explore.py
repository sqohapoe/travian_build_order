import numpy as np

from functions import double_plot
from greedy import GreedyFinder
from exploration import ExploreFinder
from idiot import IdiotFinder
from solution import Solution


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--day", help='default 5 days')
parser.add_argument("--max_iter", help='default 5000')
parser.add_argument("--max_patience", help='default 5000')
parser.add_argument("--loadname", help='default BO')
parser.add_argument("--savename", help='default BO')
parser.add_argument("--show", help='default False')
parser.add_argument("--method", help="choose among sid, cid, scid or a single one. Default scid")
parser.add_argument("--eval_method", help="choose from cp or res. Default cp")
parser.add_argument("--lower_bound")
parser.add_argument("--greedy", help='start from greedy or idiot. True for greedy')
parser.add_argument("--plot")
parser.add_argument("--starting_town")
args = parser.parse_args()


DAY=5 if args.day is None else int(args.day)
MAX_ITER = 5000 if args.max_iter  is None else int(args.max_iter)
MAX_PATIENCE = 5000 if args.max_patience  is None else int(args.max_patience)
loadname = "BO" if args.loadname  is None else args.loadname
savename = "BO" if args.savename  is None else args.savename
METHOD = "scid" if args.method is None else args.method
EVAL_METHOD = "cp" if args.eval_method is None else args.eval_method
CONSTRAINT_METHOD = "cp" if EVAL_METHOD == "res" else "res"
LOWER_BOUND = 0 if args.lower_bound is None else int(args.lower_bound)
greedy = args.greedy in ["true", "True"] if args.greedy is not None else False


try:
    order = np.load('{}.npy'.format(loadname))
    start = Solution(list(order), day=DAY)
    print("continue with given order")
except FileNotFoundError:
    if greedy:
        gf = GreedyFinder(day=DAY)
        gf.find()
        start = Solution(gf.t.get_order(), day=DAY)
        print("start from greedy")

    else:
        if_ = IdiotFinder(day=DAY)
        if_.find()
        start = Solution(if_.t.get_order(), day=DAY)
        print("start from idiot")

if args.starting_town is not None:
    try:
        order = np.load(args.starting_town)
        starting_town = Solution(order, float('Inf')).get_town()
    except FileNotFoundError:
        starting_town = None
else:
    starting_town = None

histx = []
histy = []

ef = ExploreFinder(start, method=METHOD, max_iter=MAX_ITER,
                   eval_method=EVAL_METHOD, lower_bound=LOWER_BOUND, starting_town=starting_town)
ef.find()

if args.plot:
    x1, y1 = ef.max_so_far_history_x, ef.max_so_far_history_y
    y2 = ef.other_history
    double_plot(x1, y1, y2)

np.save(savename, ef.argmax_so_far.order)

if args.show:
    ef.argmax_so_far.show()


