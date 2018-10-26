#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import pandasReadExcel as pandasReader
import numpy as np
import appearTimesInGroup


data_frame = pandasReader.read_from_excel()
min_data_row= 10
step = 10

def main():
    list_num_times_freq = appearTimesInGroup.get_appear_times_frequency_list(data_frame, min_data_row, step)
    # count = appearTimesInGroup.get_count_groups(data_frame, min_data_row)
    # col_count = appearTimesInGroup.get_column_count(count, step)
    # row = 0
    # col = 0
    # list_index = range(0, min_data_row+1)
    #
    # for x in list_num_times_freq:
    #     plot_w = plt.subplot2grid((4, 10), (row, col))
    #     plot_w.bar(list_index, x, facecolor ='green')
    #     plot_w.set_title(row* 10+ col+1)
    #     col = col+ 1
    #     if col>= 10:
    #         row= row+ 1
    #         col = 0
    # plt.show()

    data_frame_tail = data_frame.tail(step)
    list_num_times, list_sel_flags = appearTimesInGroup.get_appear_times_list(data_frame_tail, min_data_row, step)
    list_freq = [0.0]*33
    for ball_i, x in enumerate(list_num_times):
        list_freq[ball_i] = list_num_times_freq[ball_i][x[0]+ 1]/ float(1000)
    temp=[]
    Inf = 0
    for i in range(3):
        temp.append(list_freq.index(max(list_freq)))
        list_freq[list_freq.index(max(list_freq))]=Inf
    print (temp)

if __name__ == '__main__':
    main()