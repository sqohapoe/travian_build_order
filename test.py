from solution import Solution
from town2 import  Town
t = Town()

t.deepbuild("bakery")
from greedy import GreedyFinder

gf = GreedyFinder(5)
gf.find()
order = gf.t.get_order()


s = Solution(order, 5, starting_town=t)
print(s.get_town().prod_per_hour)
print(s.evaluate(overbuild_tolerated=True))
