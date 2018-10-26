#-*- coding:utf-8 -*-
# import pandas as pd
import matplotlib.pyplot as plt
import pandasReadExcel as pandasReader
import numpy as np
import appearTimes as appearTimes
import appearTimesInGroup


def main():
    data_frame = pandasReader.read_from_excel()
    #min_data_row = appearTimes.get_min_data_row(data_frame)
    min_data_row= 5
    step = 5
    list_num_times = appearTimesInGroup.get_appear_frequency_list(data_frame, min_data_row, step)
    print (list_num_times)
    count = appearTimesInGroup.get_count_groups(data_frame, min_data_row)
    col_count = appearTimesInGroup.get_column_count(count, step)
    list_index = range(0, col_count)
    row = 0
    col = 0
    min_fre = 100
    max_fre = 0
    for x in list_num_times:
        for item in x:
            min_fre = min(min_fre, item)
            max_fre = max(max_fre, item)
    for x in list_num_times:
        plot_w = plt.subplot2grid((1, 1), (0, 0))
        std_cha = np.std(x)
        middle_val = np.mean(x)
        percent_25 = middle_val- std_cha
        percent_75 = middle_val+ std_cha
        plot_w.set_ylim(min_fre, max_fre)
        plot_w.plot(list_index, x, color='green')
        plot_w.set_title(row* 10+ col+1)
        plot_w.hlines(percent_25, 1, len(list_index), colors='r')
        plot_w.hlines(middle_val, 1, len(list_index), colors='r')
        plot_w.hlines(percent_75, 1, len(list_index), colors='r')
        plt.show()
        col = col+ 1
        if col>= 10:
            row= row+ 1
            col = 0
    #plt.show()

if __name__ == '__main__':
    main()