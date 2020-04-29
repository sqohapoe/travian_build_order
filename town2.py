from data import all_buildings, nb_all_buildings, get_cp, get_max_level, get_pop, get_prerequis, get_time, get_res
from data import production_of_level, type_of_village, capacity_of_level
from data import mainbuilding_discount
import numpy as np

from functions import OverBuildException


class Town:

    def __init__(self):
        """a class that integrates the information of the town"""
        self.buildings = {"main_building":1}
        self.pop = 2
        self.total_time = 0
        self.total_cp = 0
        self.total_res_spent = np.zeros((4,), dtype=np.int32)
        self.total_res_got = np.zeros((4,), dtype=np.float64)
        self.cp_per_day = 2
        self.history = []
        self.prod_per_hour = np.zeros((4,), dtype=np.int32)
        self.warehouse_capacity = 800
        self.granary_capacity = 800
        self.update_production()
        self.update_capacity()

        # self.cp_per_sec_hist = []

    def __copy__(self):
        t = Town()
        t.buildings = self.buildings.copy()
        t.pop = self.pop
        t.total_res_spent = self.total_res_spent.copy()
        t.total_res_got = self.total_res_got.copy()
        t.cp_per_day = self.cp_per_day
        t.prod_per_hour = self.prod_per_hour.copy()
        t.warehouse_capacity = self.warehouse_capacity
        t.granary_capacity = self.granary_capacity
        t.update_production()
        t.update_capacity()


        t.total_time = self.total_time
        t.total_cp = self.total_cp
        t.history = self.history
        return t

    def forget_history(self):
        self.total_time = 0
        self.total_cp = 0
        self.history = []

    def show(self):
        print(self.buildings)
        print("production per hour", self.prod_per_hour)
        # print("total pop", self.total_pop)
        # print("total time", self.total_time)
        # print("total cp", self.total_cp)
        print("total res spend", self.total_res_spent)
        print("total res got ", self.total_res_got)
        print("cp per day", self.cp_per_day)

    def get_order(self):
        order = []
        for info_dict in self.history:
            order.append((info_dict["building_name"]))
        return order

    def update_production(self):
        def update_this_one(num, res, names_of_bonus_building):
            somme = 0
            for w in range(type_of_village[res]):
                level_res = self.get_current_level("{} {}th".format(res, w + 1))
                level_bonus = 0
                for building_name in names_of_bonus_building:
                    level_bonus += self.get_current_level(building_name)
                somme += production_of_level[level_res] * (1 + level_bonus * 0.05)
            self.prod_per_hour[num] = somme
        update_this_one(0, 'wood', ['sawmill'])
        update_this_one(1, 'clay', ['brickyard'])
        update_this_one(2, 'iron', ['the_iron_foundry'])
        update_this_one(3, 'crop', ['grain_mill', 'bakery'])

    def update_capacity(self):
        lvl = self.get_current_level("warehouse")
        self.warehouse_capacity =  capacity_of_level[lvl]
        lvl = self.get_current_level("granary")
        self.granary_capacity =  capacity_of_level[lvl]



    def get_current_level(self, building_name):
        if building_name not in self.buildings.keys():
            return 0
        else:
            return self.buildings[building_name]

    def build(self, building_name, overbuild_tolerated=False): #building name can be "crop 1th"
        if building_name not in all_buildings:
            # print("this building doesn't exist")
            return None
        # print("{} sucessfully built/upgraded".format(building_name))
        level = self.get_current_level(building_name)
        if overbuild_tolerated and level >= get_max_level(building_name):
            return None
        self.pop += get_pop(building_name, level + 1)
        self.total_time += self.time_if_build(building_name)
        self.total_cp += self.time_if_build(building_name)*self.cp_per_day # when building, the cp are not yet updated
        self.total_res_got += self.prod_per_hour * self.time_if_build(building_name) / 3600
        self.total_res_spent += get_res(building_name, level+1)
        self.cp_per_day += self.cp_if_build(building_name)
        # self.cp_per_sec_hist.append(self.cp_if_build(building_name)/self.time_if_build(building_name))
        self.buildings[building_name] = level+1
        if building_name[:4] in ["crop", "grai", "bake"]:
            self.update_production()
        self.history.append({"building_name":building_name,"level_updated": level+1, "finished_at":self.total_time,
                             "cp_updated":self.cp_per_day})
        if building_name in ["warehouse", "granary"]:
            self.update_capacity()


    def deepbuild(self, building_name):  # building name can be "crop 1th"
        level = self.get_current_level(building_name)
        if level == get_max_level(building_name):
            return None
        return self.deepbuild_to_level(building_name, level + 1)

    def build_crop(self):
        argmin = None
        min = 100
        for w in range(1, 7):
            cropname = "crop {}th".format(w)
            if self.get_current_level(cropname) < min:
                min = self.get_current_level(cropname)
                argmin = w
        if min != 10:
            self.build("crop {}th".format(argmin))
        # else:
        #     print("cannot build crop anymore")


    def deepbuild_to_level(self, building_name, level):
        if not self.is_satisfying_level(building_name):
            return None
        if not self.is_satisfying_building_space():
            return None
        if building_name in self.buildings or self.is_satisfying_prerequis(building_name):
            current_level = self.get_current_level(building_name)
            if level <= current_level:
                return None
            if not self.is_satisfying_pop(building_name):
                self.build_crop()
            elif not self.is_satisfying_warehouse_capacity(building_name):
                warehouse_level = self.get_current_level("warehouse")
                if warehouse_level == 20:
                    return None
                self.deepbuild_to_level("warehouse", warehouse_level+1)
            elif not self.is_satisfying_granary_capacity(building_name):
                granary_level = self.get_current_level("granary")
                if granary_level == 20:
                    return None
                self.deepbuild_to_level("granary", granary_level+1)
            else:
                self.build(building_name)
            self.deepbuild_to_level(building_name, level)
        else:
            for req_building, req_level in get_prerequis(building_name).items():
                self.deepbuild_to_level(req_building, req_level)
            self.deepbuild_to_level(building_name, level)

    def cp_if_build(self, building_name):
        level = self.get_current_level(building_name)
        if level == 0:
            return get_cp(building_name, 1)
        else:
            return get_cp(building_name, level+1)- get_cp(building_name, level)

    def time_if_build(self, building_name):
        level = self.get_current_level(building_name)
        discount = mainbuilding_discount[self.buildings["main_building"]-1]
        return get_time(building_name, level+1)*discount/100


    def is_satisfying_pop(self, building_name):
        level = self.get_current_level(building_name)
        free_crop = self.prod_per_hour[3] - self.pop
        crop_needed = get_pop(building_name, level+1)
        if free_crop > crop_needed+1:
            return True
        else:
            # print("you can't build {} cuz pop non satisfied. You only got {} free crop but need {} pop".format(building_name, free_crop, crop_needed))
            return False

    def is_satisfying_warehouse_capacity(self, building_name):
        level = self.get_current_level(building_name)
        res_needed = get_res(building_name, level+1)
        return res_needed[0:3].max() <= self.warehouse_capacity

    def is_satisfying_granary_capacity(self, building_name):
        level = self.get_current_level(building_name)
        res_needed = get_res(building_name, level+1)
        return  res_needed[3] <= self.granary_capacity

    def is_satisfying_prerequis(self, building_name):
        if building_name in self.buildings.keys():
            return True
        prerequis_dict = get_prerequis(building_name) #prerequis = {"main_building":3, "rally_point":1} for ex
        for requested_building_name, requested_level in prerequis_dict.items():
            if requested_building_name not in self.buildings.keys():
                # print("you can't build {}, cuz {} not built yet".format(building_name, requested_building_name))
                return False
            if self.buildings[requested_building_name] < requested_level:
                # print("you can't build {}, cuz {} not built to level {} yet".format(
                # building_name, requested_building_name, requested_level))
                return False
        return True


    def is_satisfying_building_space(self):
        count = 0
        for building_name in self.buildings:
            if building_name[:4] not in ["wood", "clay", "iron", "crop"]:
                count+=1
        if count >= 21:
            # print("no space anymore")
            return False
        else:
            return True

    def is_satisfying_level(self, building_name):
        level = self.get_current_level(building_name)
        max = get_max_level(building_name)
        if level < max:
            return True
        else:
            # print("{} achieved max level {}, you can't build it".format(building_name, max))
            return False

    def is_buildable(self, building_name, overbuild_tolerated=False):
        if not self.is_satisfying_level(building_name):
            if overbuild_tolerated:
                raise OverBuildException
            else:
                return False
        if not self.is_satisfying_warehouse_capacity(building_name):
            return False
        elif not self.is_satisfying_granary_capacity(building_name):
            return False
        if building_name not in self.buildings.keys():
            if building_name[:4] not in ["wood", "clay", "iron", "crop"]:
                return self.is_satisfying_prerequis(building_name) and \
                       self.is_satisfying_pop(building_name) and \
                       self.is_satisfying_building_space()
            else:
                return self.is_satisfying_pop(building_name)
        else:
            return self.is_satisfying_pop(building_name)

    def find_all_buildables(self):
        result = []
        for building_name in all_buildings:
            if self.is_buildable(building_name):
                result.append(building_name)
        return result


