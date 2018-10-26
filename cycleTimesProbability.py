#-*- coding:utf-8 -*-
"""
    计算一个选定周期内的出现次数的经验概率（即所有已知期数中当前周期内出现次数的统计值）
"""
import pandasReadExcel as pandasReader
import appearTimesInGroup


def cycle_times_probability(list_num_times, list_sel_flags, cycle):
    """
    :param list_num_times:每个球周期范围内出现的次数
           list_sel_flags:与list_num_times一一对应，表示当前出现次数条件下下次选中还是没有选中
    :return:返回出现次数的条件概率
    """
    list_times_probability = [[0] * cycle for i in range(33)]
    for index, list_times in enumerate(list_num_times):
        list_flags = list_sel_flags[index]
        res_fit_count = [0] * (cycle + 1)
        res_unfit_count = [0] * (cycle+ 1)
        for i, val in enumerate(list_times):
            if list_flags[i] != 0:
                res_fit_count[val] += 1
            else:
                res_unfit_count[val] += 1

        for i in range(cycle):
            count_current = (res_fit_count[i] + res_unfit_count[i])
            scale = 0
            if count_current > 0:
                scale = (1.0 * res_fit_count[i]) / count_current
            list_times_probability[index][i] = scale

    return list_times_probability


def cycle_times_probability_fit(list_num_times, list_sel_flags, cycle):
    """
    :param list_num_times:每个球周期范围内出现的次数
    :param list_sel_flags:与list_num_times一一对应，表示当前出现次数条件下下次选中还是没有选中
    :param cycle:周期长短
    :return:返回选中条件下出现次数的条件概率
    """
    list_times_probability = [[0] * cycle for i in range(33)]
    for index, list_times in enumerate(list_num_times):
        list_flags = list_sel_flags[index]
        res_fit_count = [0] * (cycle+1)
        for i, val in enumerate(list_times):
            if list_flags[i] != 0:
                res_fit_count[val] += 1

        count = sum(res_fit_count)
        for i in range(cycle):
            scale = (1.0 * res_fit_count[i]) / count
            list_times_probability[index][i] = scale

    return list_times_probability


def cycle_times_probability_unfit(list_num_times, list_sel_flags, cycle):
    """
    :param list_num_times:每个球周期范围内出现的次数
    :param list_sel_flags:与list_num_times一一对应，表示当前出现次数条件下下次选中还是没有选中
    :param cycle:周期长短
    :return:返回未选中条件下出现次数的条件概率
    """
    list_unfit_probability = [[0] * cycle for i in range(33)]
    for index, list_times in enumerate(list_num_times):
        list_flags = list_sel_flags[index]
        res_unfit_count = [0] * (cycle + 1)
        for i, val in enumerate(list_times):
            if list_flags[i] == 0:
                res_unfit_count[val] += 1

        count = sum(res_unfit_count)
        for i in range(cycle):
            scale = (1.0 * res_unfit_count[i]) / count
            list_unfit_probability[index][i] = scale

    return list_unfit_probability


def main():
    data_frame = pandasReader.read_from_excel()
    min_data_row = 5
    step = 5
    list_num_times, list_sel_flags = appearTimesInGroup.get_appear_times_list(data_frame, min_data_row, step)

    list_probability = cycle_times_probability(list_num_times, list_sel_flags, min_data_row)
    print list_probability

    list_probability_fit = cycle_times_probability_fit(list_num_times, list_sel_flags, min_data_row)
    print list_probability_fit

    list_probability_unfit = cycle_times_probability_unfit(list_num_times, list_sel_flags, min_data_row)
    print list_probability_unfit


if __name__ == '__main__':
    main()