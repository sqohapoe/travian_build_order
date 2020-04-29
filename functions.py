def string_to_intlist(string):
    l = string.split()
    m = [int(i) for i in l]
    return m

def int_to_time(int):
    sec = int%100
    min = (int//100)%100
    hour = (int//10000)
    return sec+60*min+3600*hour

def parse_res(building):
    wood = string_to_intlist(building[0])
    clay = string_to_intlist(building[1])
    iron = string_to_intlist(building[2])
    crop = string_to_intlist(building[3])
    assert len(wood) == len(clay) == len(iron) == len(crop)
    return [[wood[i], clay[i], iron[i], crop[i]] for i in range(len(wood))]

def parse_time(building):
    int_list = string_to_intlist(building)
    return [int_to_time(i) for i in int_list]

def parse_cp(building):
    return string_to_intlist(building)


def make_res_table(initial, maxlvl=20, rate=1.28):
    l = [initial]
    for i in range(maxlvl-1):
        l.append(l[-1] * rate)
    for i, ele in enumerate(l):
        l[i] = int(ele/5+0.5)*5
    return l

def double_plot(x1, y1, y2, eval_method="res"):

    import matplotlib.pyplot as plt
    constraint_method = "cp" if eval_method == "res" else "res"
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('generation')
    ax1.set_ylabel(eval_method, color=color)
    ax1.plot(x1, y1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:blue'
    ax2.set_ylabel(constraint_method, color=color)  # we already handled the x-label with ax1
    ax2.plot(x1, y2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()


class OverBuildException(Exception):
    pass

# def add_building_name_general(string_from_id, building_general, max_level):
#     for i in range(max_level):
#         building_name_general = building_general + " level " + str(i + 1)
#         string_from_id[len(string_from_id)] = building_name_general
#
#
# def building2string(building_name, level):
#     return building_name+ " level {}".format(level)
#
# def string2building(name):
#     [building_name, the_word_level, level_str] = name.split()
#     return building_name, int(level_str)
#
# def res2string(res_type, which_one, level):
#     return res_type + " {}th level {}".format(which_one+1, level)
#
# def string2res(name):
#     [res_type, which_one_str, the_word_level, level_str] = name.split()
#     return res_type, int(which_one_str[0])-1, int(level_str)
#
#
# def building2id(namespace, building_name, level):  # dict = {building:level...}
#     for id_namespace, building_name_namespace in namespace.items():
#         if building_name_namespace == building2string(building_name, level):
#             return id_namespace
#
# def res2id(namespace, res_type, which_one, level):
#     for id_namespace, building_name_namespace in namespace.items():
#         if building_name_namespace == res_type+" {}th level {}".format(which_one+1, level):
#             return id_namespace
#
#
# def is_res_id(namespace, id):
#     return is_res_string(namespace[id])
#
# def is_res_string(building_name):
#     return building_name[:4] in ["wood", "clay", "iron", "crop"]
#
# def id2building(namespace, id):
#     return string2building(namespace[id])
#
# def id2res(namespace, id):
#     "return the res_type, which_one, and level"
#     return string2res(namespace[id])
