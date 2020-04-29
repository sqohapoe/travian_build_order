def nearswap(self):
    n = len(self.order)
    from random import randint
    a = randint(1, n - 1)
    new_order = self.order.copy()
    new_order[0], new_order[1] = new_order[1], new_order[0]
    return Solution(new_order, day=self.day)


def weak_insert(self):
    n = len(self.order)
    from random import randint, choice
    from data import all_buildings, get_max_level
    a = randint(0, n - 1)
    t = Solution(self.order[0:a], day=self.day).get_town()
    building_name = choice(all_buildings)
    # level = choice(range(get_max_level(building_name))) + 1
    # print(a, building_name, level)
    # t.deepbuild_to_level(building_name, level)
    t.deepbuild(building_name)
    return Solution(t.get_order() + self.order[a:], day=self.day)


def priorcon(self):
    """prioritize something and continue"""
    n = len(self.order)
    from random import randint
    a, b = randint(0, n - 1), randint(0, n - 1)
    if a > b:
        a, b = b, a
    s = Solution(self.order[:a], day=self.day)
    building_name = self.order[b]
    level = Solution(self.order[:b]).get_town().get_current_level(building_name)
    order_before, order_after = s.new_prioritize(building_name, level)

    order_copy = self.order.copy()
    order_copy.pop(b)
    to_be_finished = order_copy[a:]
    but_they_are_built = order_after[len(order_before):]
    for building_name in but_they_are_built:
        try:
            to_be_finished.remove(building_name)
        except ValueError:
            None
    new_order = order_copy[:a] + order_after[len(order_before):] + to_be_finished
    return Solution(new_order, day=self.day)


def prior(self):
    n = len(self.order)
    from random import randint
    a, b = randint(0, n - 1), randint(0, n - 1)
    if a > b:
        a, b = b, a
    s = Solution(self.order[:a], day=self.day)
    building_name = self.order[b]
    level = Solution(self.order[:b]).get_town().get_current_level(building_name)
    s.prioritize(building_name, level)
    s.continue_with_greedy(self.day)
    return s