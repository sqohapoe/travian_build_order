from functions import OverBuildException
from greedy import GreedyFinder
from town2 import Town


class Solution:

    def __init__(self, order, day, starting_town=None, ok_even_not_buildable=False):
        if starting_town is not None:
            self.starting_town = starting_town.__copy__()
            self.starting_town.forget_history()
        else:
            self.starting_town = Town()
        self.order = order
        self.DAY = day
        self.OK_EVEN_NOT_BUILDABLE = ok_even_not_buildable

    def __copy__(self, new_order=None):
        if new_order is None:
            new_order = self.order
        clone = Solution(new_order, self.DAY)
        clone.OK_EVEN_NOT_BUILDABLE = self.OK_EVEN_NOT_BUILDABLE
        starting_town = self.starting_town.__copy__()
        return clone

    def order_is_buildable(self, overbuild_tolerated=False):
        t = self.starting_town.__copy__()
        for building_name in self.order:
            if t.is_buildable(building_name, overbuild_tolerated=overbuild_tolerated):
                t.build(building_name, overbuild_tolerated=overbuild_tolerated)
            else:
                return False
            if t.total_time > self.DAY * 86400:
                return True
        return True

    def is_admissible(self, constraint_method="cp", lower_bound=0, overbuild_tolerated=False):
        # return True
        try:
            if not self.order_is_buildable(overbuild_tolerated=overbuild_tolerated):
                return False
        except OverBuildException:
            return True
        if constraint_method == "cp":
            return self.get_total_cp() > lower_bound
        elif constraint_method == 'res':
            return self.get_total_res() > lower_bound
        else:
            print("what")
            return True

    def get_town(self, timed=False) -> Town:
        t = self.starting_town.__copy__()
        for building_name in self.order:
            t.deepbuild(building_name)
            if timed:
                if t.total_time > self.DAY * 86400:
                    break
        return t

    def cut_the_queue(self):
        t = self.get_town(timed=True)
        return self.__copy__(new_order=t.get_order())

    def evaluate(self, eval_method="cp", lower_bound=0, duration_day=None, overbuild_tolerated=False):
        if duration_day is None:
            duration_day = self.DAY
        constraint_method = "cp" if eval_method == "res" else "res"
        if not self.OK_EVEN_NOT_BUILDABLE and not self.is_admissible(constraint_method=constraint_method,
                                                                     lower_bound=lower_bound,
                                                                     overbuild_tolerated=overbuild_tolerated):
            return 0
        if eval_method == "res":
            return self.get_total_res(duration_day=duration_day)
        else:
            return self.get_total_cp(duration_day=duration_day)

    def get_total_cp(self, duration_day=None):
        if duration_day is None:
            duration_day = self.DAY
        t = self.starting_town.__copy__()
        for building_name in self.order:
            try:
                time_to_build = t.time_if_build(building_name)
            except IndexError:
                time_to_build = 0
            if t.total_time + time_to_build < duration_day * 86400:
                t.deepbuild(building_name)
            else:
                break
        if self.OK_EVEN_NOT_BUILDABLE:
            self.order = t.get_order()
        return (t.total_cp + (duration_day * 86400 - t.total_time) * t.cp_per_day) / 86400

    def get_total_res(self, duration_day=None):
        if duration_day is None:
            duration_day = self.DAY
        t = self.starting_town.__copy__()
        for building_name in self.order:
            try:
                time_to_build = t.time_if_build(building_name)
            except IndexError:
                time_to_build = 0
            if t.total_time + time_to_build < duration_day * 86400:
                t.deepbuild(building_name)
            else:
                break
        if self.OK_EVEN_NOT_BUILDABLE:
            self.order = t.get_order()
        return (t.total_res_got + (duration_day * 86400 - t.total_time) * t.prod_per_hour).sum() / 3600

    def continue_with_greedy(self, daysleft):
        """Suppose that the solution given is admissible, finish with greedy."""
        t = self.get_town()
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
        t = self.__copy__(new_order=self.order[0:a]).get_town()
        building_name = choice(all_buildings) if building_name is None else building_name
        level = choice(range(get_max_level(building_name))) + 1 if level is None else level
        # print(a, building_name, level)
        t.deepbuild_to_level(building_name, level)
        return self.__copy__(new_order=t.get_order() + self.order[a:])

    def inserg(self, a=None):
        n = len(self.order)
        from random import randint
        if a is None:
            a = randint(0, n - 1)
        t = self.__copy__(self.order[:a]).get_town()
        gf = GreedyFinder(self.DAY, t)
        building_name = gf.find_next_to_build()
        new_order = self.order.copy()
        new_order.insert(a, building_name)
        return self.__copy__(new_order=new_order)

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
        # return Solution(new_order, self.DAY)
        return self.__copy__(new_order=new_order)

    def drop(self, a=None):
        from random import randint
        n = len(self.order)
        if a is None:
            a = randint(0, n - 1)
        new_order = self.order.copy()
        building_name = new_order.pop(a)
        # print("dropped ", a, building_name)
        return self.__copy__(new_order=new_order)

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
        return self.__copy__(new_order=new_order)

    def get_neighbor(self, method=None, p=None):
        if p is None:
            p = [10, 1, 1]
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

    def show(self, onebyone=False, show_building_details=False):
        t = Town()
        for i, building_name in enumerate(self.order):
            level = t.get_current_level(building_name)
            try:
                print("{}th: {} -> {} : {}".format(i, level, level + 1, building_name), end=', ')
                print("cp += {}, {} min".format(t.cp_if_build(building_name),
                                                t.time_if_build(building_name) // 60))
                # print("------------------------------------------------------------------------------------")
                t.build(building_name)
                t.show() if show_building_details else None
            except IndexError:
                print("{} tasked again but max".format(building_name))
            if onebyone:
                import os
                os.system("pause")
