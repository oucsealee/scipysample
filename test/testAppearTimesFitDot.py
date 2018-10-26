#-*- coding:utf-8 -*-
# import pandas as pd
import matplotlib.pyplot as plt
import pandasReadExcel as pandasReader
import numpy as np
import appearTimes as appearTimes
import appearTimesInGroup

def main():
    """
    绘制出现次数和选中的点阵图
    :return:
    """
    data_frame = pandasReader.read_from_excel()
    min_data_row= 5
    step = 5
    list_num_times, list_sel_flags = appearTimesInGroup.get_appear_times_list(data_frame, min_data_row, step)

    x = range(0, 6)
    index_row = 0
    index_col = 0
    for index, list_times in enumerate(list_num_times):
        list_flags = list_sel_flags[index]
        res_fit_count = [0] * 6
        res_unfit_count = [0] * 6
        for i, val in enumerate(list_times):
            if list_flags[i] != 0:
                res_fit_count[val] += 1
            else:
                res_unfit_count[val] -= 1
        plt_c= plt.subplot2grid((4, 10), (index_row, index_col))
        index_col+= 1
        if index_col>= 10:
            index_row += 1
            index_col = 0
        matBar(plt_c, res_fit_count, res_unfit_count, x)
#    matBar(res_fit_count, res_unfit_count, x)
    plt.show()


def matBar(plt, res_fit_count, res_unfit_count, x):
    plt.bar(x, res_fit_count, facecolor='red')
    count = sum(res_fit_count)
    height_font = 8
    for index, item in enumerate(x):
        count_current = (res_fit_count[index] - res_unfit_count[index])
        scale = 0
        if count_current > 0:
            scale = (1.0 * res_fit_count[index]) / count_current
        plt.text(item, res_fit_count[index] + 0.05,
                 '%.3f-%.3f' % (scale, (1.0 * res_fit_count[index]) / count), ha='center', va='bottom',
                 fontsize=height_font)
    plt.bar(x, res_unfit_count, facecolor='blue')
    count_unfit = sum(res_unfit_count) * -1.0
    for index, item in enumerate(x):
        count_current = (res_fit_count[index] - res_unfit_count[index])
        scale = 0
        if count_current > 0:
            scale = (-1.0 * res_unfit_count[index]) / count_current
        plt.text(item, res_unfit_count[index] - 0.05,
                 '%.3f-%.3f' % (scale, (-1.0 * res_unfit_count[index]) / count_unfit), ha='center', va='top',
                 fontsize=height_font)
#    plt.xlim(-1, 6)


if __name__ == '__main__':
    main()