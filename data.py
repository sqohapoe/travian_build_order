from functions import parse_cp, parse_time, make_res_table
import numpy as np

all_buildings = []

time = {}
prerequis = {}
cp = {}
max_level = {}
pop = {}

wood = {}
clay = {}
iron = {}
crop = {}
type_of_village = {"wood": 4, "clay": 4, "iron": 4, "crop": 6}

x = "academy"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [220, 160, 90, 40]))
time[
    x] = "3320 4340 5540 10930 12540 14420 20610 23120 30030 33420 41340 45910 55210 65330 80440 92710 110250 125400 150250 173210"
time[x] = parse_time(time[x])
cp[x] = "5 6 7 8 10 12 14 17 21 25 30 36 43 51 62 74 89 106 128 153"
cp[x] = parse_cp(cp[x])
prerequis[x] = {"main_building": 3, "barracks": 3}
max_level[x] = 20
pop[x] = parse_cp("4 2 2 2 2 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4")

x = "smithy"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [180, 250, 500, 160]))
time[
    x] = "3320 4340 5540 10930 12540 14420 20610 23120 30030 33420 41340 45910 55210 65330 80440 92710 110250 125400 150250 173210"
time[x] = parse_time(time[x])
cp[x] = "2 3 3 4 5 6 7 9 10 12 15 18 21 26 31 37 44 53 64 77"
cp[x] = parse_cp(cp[x])
prerequis[x] = {"main_building": 3, "academy": 1}
max_level[x] = 20
pop[x] = parse_cp("4 2 2 2 2  3 3 3 3 3  3 3 3 3 3  4 4 4 4 4")

x = "main_building"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [70, 40, 60, 20]))
time[
    x] = "4140 4340 5340 10440 11650 13010 14500 20120 21940 23950 30220 32720 35520 42620 50050 53930 62230 71030 80400 90350"
time[x] = parse_time(time[x])
cp[x] = "2 3 3 4 5 6 7 9 10 12 15 18 21 26 31 37 44 53 64 77"
cp[x] = parse_cp(cp[x])
mainbuilding_discount = "100 96 93 90 86 83 80 77 75 72 69 67 64 62 60 58 56 54 52 50"
mainbuilding_discount = parse_cp(mainbuilding_discount)
prerequis[x] = {}
max_level[x] = 20
pop[x] = parse_cp("2 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3")

x = "earth_wall"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [120, 200, 0, 80]))
time[
    x] = "3320 4340 5540 10930 12540 14420 20610 23120 30030 33420 41340 45910 55210 65330 80440 92710 110250 125400 150250 173210"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2 3 4 4 5 6 7 9 11 13 15 18 22 27 32 38"
cp[x] = parse_cp(cp[x])
max_level[x] = 20
pop[x] = parse_cp("0 0 0 0 0 1 1 1 1 1  1 1 1 1 1  2 2 2 2 2")

x = "barracks"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [210, 140, 260, 120]))
time[
    x] = "3320 4340 5540 10930 12540 14420 20610 23120 30030 33420 41340 45910 55210 65330 80440 92710 110250 125400 150250 173210"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2 3 4 4 5 6 7 9 11 13 15 18 22 27 32 38"
cp[x] = parse_cp(cp[x])
prerequis[x] = {"main_building": 3, "rally_point": 1}
max_level[x] = 20
pop[x] = parse_cp("4 2 2 2 2 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4")

x = "heros_mansion"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(lambda x: make_res_table(x, rate=1.33), [220, 160, 90, 40]))
time[
    x] = "3830 4430 5130 5950 10920 12030 13320 14820 20540 22550 24910 31610 34730 42400 50610 55510 65200 75800 91420 104310"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2 3 4 4 5 6 7 9 11 13 15 18 22 27 32 38"
cp[x] = parse_cp(cp[x])
prerequis[x] = {"main_building": 3, "rally_point": 1}
max_level[x] = 20
pop[x] = parse_cp("2 1 1 1 1  2 2 2 2 2  2 2 2 2 2  3 3 3 3 3")

x = "rally_point"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [110, 160, 90, 70]))

time[
    x] = "3320 4340 5540 10930 12540 14420 20610 23120 30030 33420 41340 45910 55210 65330 80440 92710 110250 125400 150550 173210"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2 3 4 4 5 6 7 9 11 13 15 18 22 27 32 38"
cp[x] = parse_cp(cp[x])
prerequis[x] = {}
max_level[x] = 20
pop[x] = parse_cp("1 1 1 1 1  1 1 1 1 1   2 2 2 2 2  2 2 2 2 2 ")

x = "tournament_square"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [1750, 2250, 1530, 240]))
time[
    x] = "3320 4340 5540 10930 12540 14420 20610 23120 30030 33420 41340 45910 55210 65330 80440 92710 110250 125400 150550 173210"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2 3 4 4 5 6 7 9 11 13 15 18 22 27 32 38"
cp[x] = parse_cp(cp[x])
prerequis[x] = {"rally_point": 15}
max_level[x] = 20
pop[x] = parse_cp("1 1 1 1 1  1 1 1 1 1   2 2 2 2 2  2 2 2 2 2 ")

x = "stable"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [260, 140, 220, 100]))
time[
    x] = "3640 4730 10010 11450 13140 15120 21410 24040 31120 34700 42820 51620 61150 71620 83110 95800 113840 133530 155100 182810"
time[x] = parse_time(time[x])
cp[x] = "2 3 3 4 5 6 7 9 10 12 15 18 21 26 31 37 44 53 64 77"
cp[x] = parse_cp(cp[x])
prerequis[x] = {"smithy": 3, "academy": 5}
max_level[x] = 20
pop[x] = parse_cp("5 3 3 3 3  3 3 3 3 3  4 4 4 4 4  4 4 4 4 4")

x = "workshop"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [460, 510, 600, 320]))
time[
    x] = "5000 10300 11800 13530 15550 21920 24640 31720 35510 43740 52710 62430 73100 84800 101740 120130 140200 162140 190350 221150"
time[x] = parse_time(time[x])
cp[x] = "4 4 5 6 7 9 11 13 15 19 22 27 32 39 46 55 67 80 96 115"
cp[x] = parse_cp(cp[x])
prerequis[x] = {"main_building": 5, "academy": 10}
max_level[x] = 20
pop[x] = parse_cp("3 2 2 2 2  2 2 2 2 2  3 3 3 3 3  3 3 3 3 3")

x = "granary"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [80, 100, 70, 20]))
time[
    x] = "2640 3600 4640 5910 11340 13020 14950 21230 23840 30900 34410 42510 51230 60730 71120 82520 95110 113050 132620 154020"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2 3 4 4 5 6 7 9 11 13 15 18 22 27 32 38"
cp[x] = parse_cp(cp[x])
max_level[x] = 20
pop[x] = parse_cp("1 1 1 1 1  1 1 1 1 1  2 2 2 2 2  2 2 2 2 2")

x = "warehouse"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [130, 60, 90, 40]))
time[
    x] = "3320 4340 5540 10930 12540 14420 20610 23120 30030 33420 41340 45910 55210 65330 80440 92710 110250 125400 150250 173210"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2 3 4 4 5 6 7 9 11 13 15 18 22 27 32 38"
cp[x] = parse_cp(cp[x])
max_level[x] = 20
pop[x] = parse_cp("1 1 1 1 1  1 1 1 1 1  2 2 2 2 2  2 2 2 2 2 ")

x = "marketplace"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [80, 70, 120, 70]))
time[
    x] = "3000 3950 5110 10420 11940 13720 15800 22150 24930 32140 35900 44210 53220 63030 73800 85620 102700 121220 141430 163620"
time[x] = parse_time(time[x])
cp[x] = "4 4 5 6 7 9 11 13 15 19 22 27 32 39 46 55 67 80 96 115"
cp[x] = parse_cp(cp[x])
max_level[x] = 20
pop[x] = parse_cp("4 2 2 2 2 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 ")
prerequis[x] = {"main_building": 3, "warehouse": 1, "granary": 1}

x = "town_hall"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [1250, 1110, 1260, 600]))
time[
    x] = "32820 40640 45110 54240 64230 75200 91230 104550 123410 143950 170540 195450 231100 265830 312230 362840 422350 491550 571340 662810"
time[x] = parse_time(time[x])
cp[x] = "6 7 9 10 12 15 18 21 26 31 37 45 53 64 77 92 111 133 160 192"
cp[x] = parse_cp(cp[x])
max_level[x] = 20
pop[x] = parse_cp("4 2 2 2 2 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 ")
prerequis[x] = {"main_building": 10, "academy": 10}

x = "embassy"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [180, 130, 150, 80]))
time[
    x] = "3320 4340 5540 10930 12540 14420 20610 23120 30030 33420 41340 45910 55210 65330 80440 92710 110250 125400 150250 173210"
time[x] = parse_time(time[x])
cp[x] = "5 6 7 8 10 12 14 17 21 25 30 36 43 51 62 74 89 106 128 153"
cp[x] = parse_cp(cp[x])
max_level[x] = 20
pop[x] = parse_cp("3 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3")

x = "residence"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(make_res_table, [580, 460, 350, 180]))
time[
    x] = "3320 4340 5540 10930 12540 14420 20610 23120 30030 33420 41340 45910 55210 65330 80440 92710 110250 125400 150250 173210"
time[x] = parse_time(time[x])
cp[x] = "2 3 3 4 5 6 7 9 10 12 15 18 21 26 31 37 44 53 64 77"
cp[x] = parse_cp(cp[x])
max_level[x] = 20
pop[x] = parse_cp("1 1 1 1 1  1 1 1 1 1  2 2 2 2 2  2 2 2 2 2")

x = "cranny"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(lambda x: make_res_table(x, maxlvl=10), [40, 50, 30, 10]))
time[x] = "500 1050 1730 2520 3420 4450 5700 11110 12740 14640"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2 3 4 4 5 6"
cp[x] = parse_cp(cp[x])
max_level[x] = 10
pop[x] = parse_cp("0 0 0 0 0 1 1 1 1 1")

for i in range(19):
    x = "cranny {}th".format(i + 1)
    all_buildings.append(x)
    time[x] = "500 1050 1730 2520 3420 4450 5700 11110 12740 14640"
    [wood[x], clay[x], iron[x], crop[x]] = list(map(lambda x: make_res_table(x, maxlvl=10), [40, 50, 30, 10]))
    time[x] = parse_time(time[x])
    cp[x] = "1 1 2 2 2 3 4 4 5 6"
    cp[x] = parse_cp(cp[x])
    max_level[x] = 10
    prerequis[x] = {"cranny": 10}
    if i > 0:
        prerequis[x]["cranny {}th".format(i)] = 1
    pop[x] = parse_cp("0 0 0 0 0 1 1 1 1 1")

for i in range(type_of_village["wood"]):
    x = "wood {}th".format(i + 1)
    all_buildings.append(x)
    [wood[x], clay[x], iron[x], crop[x]] = list(
        map(lambda x: make_res_table(x, rate=1.67, maxlvl=10), [40, 100, 50, 60]))
    time[x] = "420 1020 1950 3500 5920 13810 24020 41950 65910 111400"
    time[x] = parse_time(time[x])
    cp[x] = "1 1 2 2 2 3 4 4 5 6"
    cp[x] = parse_cp(cp[x])
    max_level[x] = 10
    pop[x] = parse_cp("2 1 1 1 1 2 2 2 2 2")

for i in range(type_of_village["clay"]):
    x = "clay {}th".format(i + 1)
    all_buildings.append(x)
    [wood[x], clay[x], iron[x], crop[x]] = list(
        map(lambda x: make_res_table(x, rate=1.67, maxlvl=10), [80, 40, 80, 50]))
    time[x] = "340 910 1800 3210 5450 13110 22910 40200 63030 102810"
    time[x] = parse_time(time[x])
    cp[x] = "1 1 2 2 2 3 4 4 5 6"
    cp[x] = parse_cp(cp[x])
    max_level[x] = 10
    pop[x] = parse_cp("2 1 1 1 1 2 2 2 2 2")

for i in range(type_of_village["iron"]):
    x = "iron {}th".format(i + 1)
    all_buildings.append(x)
    [wood[x], clay[x], iron[x], crop[x]] = list(
        map(lambda x: make_res_table(x, rate=1.67, maxlvl=10), [100, 80, 30, 60]))
    time[x] = "730 1520 2750 4800 12000 21120 33330 54450 91510 145140"
    time[x] = parse_time(time[x])
    cp[x] = "1 1 2 2 2 3 4 4 5 6"
    cp[x] = parse_cp(cp[x])
    max_level[x] = 10
    pop[x] = parse_cp("3 2 2 2 2 2 2 2 2 2")

for i in range(type_of_village["crop"]):
    x = "crop {}th".format(i + 1)
    all_buildings.append(x)
    [wood[x], clay[x], iron[x], crop[x]] = list(
        map(lambda x: make_res_table(x, rate=1.67, maxlvl=10), [70, 90, 70, 20]))
    time[x] = "230 720 1500 2730 4710 11850 20940 33040 54030 90800"
    time[x] = parse_time(time[x])
    cp[x] = "1 1 2 2 2 3 4 4 5 6"
    cp[x] = parse_cp(cp[x])
    max_level[x] = 10
    pop[x] = parse_cp("0 0 0 0 0 1 1 1 1 1")

x = "sawmill"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(lambda x: make_res_table(x, maxlvl=5, rate=1.8), [520, 380, 290, 90]))
time[x] = "5000 13500 24230 42350 65540"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2"
cp[x] = parse_cp(cp[x])
max_level[x] = 5
pop[x] = parse_cp("4 2 2 2 2")
prerequis[x] = {'wood 1th': 10, 'main_building': 5}

x = "brickyard"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(lambda x: make_res_table(x, maxlvl=5, rate=1.8), [440, 480, 320, 50]))
time[x] = "4720 13100 23630 41450 64210"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2"
cp[x] = parse_cp(cp[x])
max_level[x] = 5
pop[x] = parse_cp("3 2 2 2 2")
prerequis[x] = {'clay 1th': 10, 'main_building': 5}

x = "the_iron_foundry"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(lambda x: make_res_table(x, maxlvl=5, rate=1.8), [200, 450, 510, 120]))
time[x] = "10800 20200 32300 52400 82650"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2"
cp[x] = parse_cp(cp[x])
max_level[x] = 5
pop[x] = parse_cp("6 3 3 3 3")
prerequis[x] = {'iron 1th': 10, 'main_building': 5}

x = "grain_mill"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(lambda x: make_res_table(x, maxlvl=5, rate=1.8), [500,440,380,1240]))
time[x] = "3040 10600 15900 31830 51750"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2"
cp[x] = parse_cp(cp[x])
max_level[x] = 5
pop[x] = parse_cp("3 2 2 2 2")
prerequis[x] = {'crop 1th':5}

x = "bakery"
all_buildings.append(x)
[wood[x], clay[x], iron[x], crop[x]] = list(map(lambda x: make_res_table(x, maxlvl=5, rate=1.8), [1200,1480,870,1600]))
time[x] = "10120 15200 30800 50200 75300"
time[x] = parse_time(time[x])
cp[x] = "1 1 2 2 2"
cp[x] = parse_cp(cp[x])
max_level[x] = 5
pop[x] = parse_cp("4 2 2 2 2")
prerequis[x] = {'crop 1th': 10, 'main_building': 5, "grain_mill":5}

production_of_level = [3, 7, 13, 21, 31, 46, 70, 98, 140, 203, 280]
production_increase_of_level = [5, 10, 15, 20, 25]
capacity_of_level = [800, 1200, 1700, 2300, 3100, 4000, 5000, 6300, 7800, 9600, 11800, 14400, 17600, 21400, 25900,
                     31300, 37900, 45700, 55100, 66400, 80000]


def get_cp(building_name, level):
    return cp[building_name][level - 1]


def get_time(building_name, level):
    return time[building_name][level - 1]


def get_res(building_name, level):
    l = []
    for res in [wood, clay, iron, crop]:
        l.append(res[building_name][level - 1])
    return np.array(l)


def get_prerequis(building_name):
    try:
        return prerequis[building_name]
    except KeyError:
        return {}


def is_atom(building_name):
    try:
        return prerequis[building_name] == {}
    except KeyError:
        return True


def combine_prerequis(prerequis1, prerequis2):
    prerequis3 = prerequis2
    for k, _ in prerequis1.items():
        if k in prerequis2.keys():
            prerequis3[k] = max(prerequis1[k], prerequis2[k])
        else:
            prerequis3[k] = prerequis1[k]
    return prerequis3


def get_prerequis_of_atom(building_name):
    to_be_checked = list(get_prerequis(building_name).keys())
    result = get_prerequis(building_name)
    while to_be_checked != []:
        building_being_checked = to_be_checked.pop()
        for req_building, req_level in get_prerequis(building_being_checked).items():
            if not is_atom(req_building):
                to_be_checked.append(req_building)
            result = combine_prerequis(result, {req_building: req_level})
    return result


def get_pop(building_name, level):
    return pop[building_name][level - 1]


def get_max_level(building_name):
    return max_level[building_name]


nb_all_buildings = len(all_buildings)
