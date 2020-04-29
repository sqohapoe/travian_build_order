import numpy as np
from town2 import Town
from data import all_buildings, nb_all_buildings

class IdiotFinder():
    def __init__(self, day, t=Town()):
        self.DAY = day
        self.t = t

    def find(self)-> None:
        while self.exist_buildable() and self.t.total_time < self.DAY*86400:
            building_name = self.find_next_to_build()
            self.t.build(building_name)




    def exist_buildable(self):
        if self.t.find_all_buildables() != []:
            return True
        else:
            return False


    def find_next_to_build(self) -> str:
        buildables = self.t.find_all_buildables()
        from random import choice
        return choice(buildables)

