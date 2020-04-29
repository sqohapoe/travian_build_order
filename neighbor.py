
class Neighbor():
    def __init__(self, sol):
        self.sol = sol
    def continue_with_greedy(self, daysleft):
        """Suppose that the solution given is admissible, finish with greedy."""
        t = self.sol.get_town()
        gf = GreedyFinder(daysleft, t)
        gf.find()
        self.order = gf.t.get_order()

    def prioritize(self, priority_building, level=1):
        t = self.get_town()
        t.deepbuild_to_level(priority_building, level)

    def insert(self, a=None, building_name=None, level=None):
        n = len(self.order)
        from random import randint, choice
        from data import all_buildings, get_max_level
        a = randint(0, n - 1) if a is None else a
        t = Solution(self.order[0:a], day=self.day).get_town()
        building_name = choice(all_buildings) if building_name is None else building_name
        level = choice(range(get_max_level(building_name))) + 1 if level is None else level
        # print(a, building_name, level)
        t.deepbuild_to_level(building_name, level)
        return Solution(t.get_order() + self.order[a:], day=self.day)

    def inserg(self, a=None):
        n = len(self.order)
        from random import randint
        if a is None:
            a = randint(0, n - 1)
        t = Solution(self.order[:a]).get_town()
        gf = GreedyFinder(self.day, t)
        building_name = gf.find_next_to_build()
        new_order = self.order.copy()
        new_order.insert(a, building_name)
        return Solution(new_order, self.day)

    def circular(self, a=None, b=None):
        # print(self.order)
        if a is None or b is None:
            from random import randint
            n = self.order.__len__()
            a, b = randint(0, n - 1), randint(0, n - 1)
        from numpy.random import geometric
        h = geometric(0.5)  # h>=1
        # print("{} to {} all go to {}".format(b, b+h, a))
        new_order = self.order.copy()
        buildings = new_order[b:b + h]
        new_order = new_order[:b] + new_order[b + h:]
        new_order = new_order[:a] + buildings + new_order[a:]
        # print(new_order)
        return Solution(new_order, self.day)

    def drop(self, a=None):
        from random import randint
        n = len(self.order)
        if a is None:
            a = randint(0, n - 1)
        new_order = self.order.copy()
        building_name = new_order.pop(a)
        # print("dropped ", a, building_name)
        return Solution(new_order, day=self.day)

    def new_prioritize(self, priority_building, level=1):
        t = self.get_town()
        order_before = t.get_order().copy()
        t.deepbuild_to_level(priority_building, level)
        self.order = t.get_order()
        order_after = t.get_order().copy()
        return order_before, order_after

    def swap(self, a=None, b=None):
        n = len(self.order)
        from random import randint
        if b is None:
            if a is None:
                a, b = randint(0, n - 1), randint(0, n - 1)
            else:
                a, b = a, randint(0, n - 1)
        if a > b:
            a, b = b, a
        new_order = self.order.copy()
        A, B = new_order[a], new_order[b]
        new_order[a], new_order[b] = B, A
        return Solution(new_order, day=self.day)

    def get_neighbor(self, method=None, p=None):
        if p is None:
            p = [1, 1, 1]
        from numpy.random import choice
        from numpy import array
        p = array(p)
        if method == "sid":
            decide = choice(["swap", "insert", "drop"], p=p / p.sum())
        # elif method == "sidig":
        #     decide = choice(["swap", "insert", "inserg", "drop"], p=p/p.sum())
        elif method == "cid":
            decide = choice(["circular", "insert", "drop"], p=p / p.sum())
        elif method == "scid":
            p = [2, 10, 1, 2]
            p = array(p)
            decide = choice(["swap", "circular", "insert", "drop"], p=p / p.sum())
        else:
            decide = method
        neighbor = getattr(self, decide)()
        return neighbor, decide
