from solution import Solution


class ExploreFinder():

    def __init__(self, start, max_iter=5000, max_patience=5000, method=None,
                 elitism=True, p=None, eval_method='cp', lower_bound=0, starting_town=None):
        self.MAX_ITER = max_iter
        self.MAX_PATIENCE = max_patience
        self.METHOD = method
        self.ELITISM = elitism
        self.P = p
        self.EVAL_METHOD = eval_method
        self.LOWER_BOUND = lower_bound

        self.collections = [start]
        self.argmax_so_far = start
        self.max_so_far = start.evaluate(eval_method=eval_method, lower_bound=lower_bound)
        self.max_so_far_history_x = [0]
        self.max_so_far_history_y = [self.max_so_far]
        if eval_method == "cp":
            self.other_history = [start.get_total_res()]
        else:
            self.other_history = [start.get_total_cp()]

    def choose_from_collections(self):
        if self.ELITISM:
            return self.argmax_so_far
        from random import choice
        solution = choice(self.collections)
        return solution

    def get_neighbor(self):
        solution = self.choose_from_collections()
        neighbor = solution.get_neighbor(method=self.METHOD, p=self.P)
        return neighbor

    def find(self):
        counter = 0
        # stat = {"swap":0, "drop":0, "insert":0, "inserg":0}
        for gene in range(self.MAX_ITER):
            if counter > self.MAX_PATIENCE:
                return None
            solution = self.choose_from_collections()
            new_solution, decide = solution.get_neighbor(method=self.METHOD)
            value = new_solution.evaluate(eval_method=self.EVAL_METHOD, lower_bound = self.LOWER_BOUND)
            print(value)
            if value >= self.max_so_far:
                if value == self.max_so_far:
                    if new_solution.order.__len__() < self.argmax_so_far.order.__len__() :
                        self.argmax_so_far = new_solution
                    continue
                else:
                    # print(new_solution.order.__len__())
                    self.max_so_far = value
                    self.argmax_so_far = new_solution
                counter = 0
                if True or value - self.max_so_far_history_y[-1] > 0.5:
                    print("improved solution found at generation {} of value {} by {}"
                          .format(gene, self.max_so_far, decide))
                    self.max_so_far_history_x.append(gene)
                    self.max_so_far_history_y.append(value)
                # stat[decide]+=1
                # print(stat)
                if self.EVAL_METHOD == 'cp':
                    self.other_history.append(new_solution.get_total_res())
                else:
                    self.other_history.append(new_solution.get_total_cp())
            else:
                counter+=1

            if self.ELITISM:
                self.collections = [self.argmax_so_far]
            else:
                self.collections.append(new_solution)
        # print(stat)

    def get_order(self):
        return self.argmax_so_far
