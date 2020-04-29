import numpy as np
from town2 import Town
from data import all_buildings, nb_all_buildings


class GreedyFinder():
    def __init__(self, day, t=Town()):
        self.day = day
        self.t = t

    def exist_buildable(self):
        if self.t.find_all_buildables() != []:
            return True
        else:
            return False

    def find_next_to_build(self, verbose=False) -> str:
        buildables = self.t.find_all_buildables()
        # return buildables[0]
        cppersec = np.empty(len(buildables))
        for i, building_name in enumerate(buildables):
            cppersec[i] = self.t.cp_if_build(building_name)/self.t.time_if_build(building_name)
        if verbose:
            building_name = buildables[cppersec.argmax()]
            # print("among {} buildables".format(self.t.find_all_buildables()))
            print("upgrade {} from level {} to level {}".format(building_name, self.t.get_current_level(building_name), 1+self.t.get_current_level(building_name)))
            print("cp increase by {}, within {} minutes".format(self.t.cp_if_build(building_name), self.t.time_if_build(building_name)//60))
            print("------------------------------------------------------------------------------------")
        return buildables[cppersec.argmax()]


    def find(self, verbose=False)-> None:
        while self.exist_buildable() and self.t.total_time < self.day*86400:
            building_name = self.find_next_to_build(verbose)
            self.t.build(building_name)



    # def find(self):
    #     current_order = []
    #     to_be_decided = np.array([1]*total_number, dtype=np.int8) # a list of True and False
    #     while to_be_decided.any():
    #         cp_per_sec_allowed = self._get_cp_per_sec_allowed(current_order, to_be_decided)
    #         next_step_found = cp_per_sec_allowed.argmax()
    #         current_order.append(next_step_found)
    #         to_be_decided[next_step_found] = 0
    #         building_name = stringspace[next_step_found]
    #         self._update_timespace(building_name, mainbuilding_discount = mainbuilding_discount)
    #         # print(building_name, end=' ')
    #         # print(cp_per_sec_allowed[next_step_found])
    #     return Solution(current_order)
    #
    # def find2(self):
    #     current_order = []
    #     t = Town()
    #     while t.find_all_buildables_general(to_string=False).__len__()>0:
    #         buildables = t.find_all_buildables_general(to_string=False)
    #         theircp = [cpspace[id] for id in buildables]
    #         theirtime = [timespace[id] for id in buildables]
    #         theircp_per_time = np.array([cpspace[i]/timespace[i] for i in buildables])
    #         choice = theircp_per_time.argmax()
    #         # choice = buildables[0]
    #         t.build_general_from_id(choice)
    #         current_order.append(choice)
    #     return Solution(current_order)

    # def _update_timespace(self, building_name, mainbuilding_discount):
    #     if building_name[:10] == "main_building"[:10]:
    #         level = building_name[-2:]
    #         level = int(level)
    #         percentage = mainbuilding_discount[level - 1]
    #         for k, _ in timespace.items():
    #             timespace[k] = beforetimespace[k] * percentage / 100
    #
    # def _get_cp_per_sec_allowed(self, current_order, to_be_decided):
    #     cp_per_sec = np.array([cpspace[i] / timespace[i] for i in range(total_number)])
    #     possible_next_steps = Solution(current_order).find_possible_next_steps()  # 1 if can be built, 0 otherwise
    #     cp_per_sec_allowed = to_be_decided * cp_per_sec * possible_next_steps  # only consider those satisfying
    #     return cp_per_sec_allowed