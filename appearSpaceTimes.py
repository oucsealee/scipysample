# -*- coding:utf-8 -*-
import pandasReadExcel as pandasReader
import matplotlib.pyplot as plt

def get_appear_matrix(data_frame):
    """
    :param data_frame: C-H列为红球；I列为蓝球；P列为投注总额；R列为奖池金额
    :return: 每行33个元素，其中选中的值为1，未选中的值为0
    """
    list_numbers = []
    for index, row in data_frame.iterrows():
        list_num = [0] * 33
        list_num[row['C'] - 1] = 1
        list_num[row['D'] - 1] = 1
        list_num[row['E'] - 1] = 1
        list_num[row['F'] - 1] = 1
        list_num[row['G'] - 1] = 1
        list_num[row['H'] - 1] = 1

        list_numbers.append(list_num)
    return list_numbers


def get_appear_space_times(list_numbers):
    """
    :param list_numbers: 每行33个元素，其中选中的值为1，未选中的值为0
    :return:
    """
    list_numbers = map(list, zip(*list_numbers))

    list_space = []
    for one_ball in enumerate(list_numbers):
        list_one_space = []
        start_index = 0
        for index, x in enumerate(one_ball[1]):
            if index == 0:
                if x == 0:
                    start_index -= 1
                continue
            if x == 1:
                space = index- start_index- 1
                list_one_space.append(space)
                start_index = index
        list_space.append(list_one_space)
    return list_space


def get_appear_space_frequency(list_one_space):
    """
    :param list_one_space:一个参数出现的间隔数组
    :return:
    """
    dist_space = {}
    for index, space in enumerate(list_one_space):
        if dist_space.has_key(space):
            continue
        dist_space[space] = list_one_space.count(space)
    count = len(list_one_space)
    for key in dist_space:
        dist_space[key] /= count * 1.0
    return dist_space


def main():
    data_frame = pandasReader.read_from_excel()
    list_numbers = get_appear_matrix(data_frame)
    list_space = get_appear_space_times(list_numbers)
    print(list_numbers)
    print(list_space)
    print(len(list_space))
    for one_ball in enumerate(list_space):
        dict_space = get_appear_space_frequency(one_ball[1])
        x = dict_space.keys()
        y = dict_space.values()
        for index, times in enumerate(y):
            y *= 100
        plt.bar(x, y, facecolor='blue')
        plt.show()


if __name__ == '__main__':
    main()

