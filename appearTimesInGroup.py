# -*- coding:utf-8 -*-
import appearTimes as appearTimes
import numpy as np


def get_count_groups(data_frame, count_group_items):
    count_data_frame = data_frame.iloc[:, 0].size
    count = count_data_frame - count_group_items + 1
    return count


def get_column_count(count, step):
    if step == 1:
        return count
    col_count = divmod(count, step)
    num_col = col_count[0]
    if col_count[1] > 0:
        num_col += 1
    return num_col


def get_appear_times_list(data_frame, count_group_items, step):
    count = get_count_groups(data_frame, count_group_items)
    col_count = get_column_count(count, step)
    list_num_times = [[0] * col_count for i in range(33)]
    list_sel_flags = [[0] * col_count for i in range(33)]
    col_index = 0
    for index in range(0, count, step):
        data_frame_latest_30 = data_frame[index: (index + count_group_items)]
        if (index + count_group_items) >= data_frame.iloc[:, 0].size:
            break
        data_latest = data_frame.iloc[index + count_group_items]
        list_latest_all = data_latest.tolist()
        list_latest = list_latest_all[0:6]
        list_balls = appearTimes.get_all_ball_times(data_frame_latest_30)
        for i in range(0, len(list_balls)):
            list_num_times[i][col_index] = list_balls[i]
            if (i+1) in list_latest:
                list_sel_flags[i][col_index] = 1
        col_index = col_index+ 1
    return list_num_times, list_sel_flags


def get_appear_frequency_list(data_frame, count_group_items, step):
    list_num_times, list_sel_flags = get_appear_times_list(data_frame, count_group_items, step)
    for x in list_num_times:
        for index, frequency in enumerate(x):
            fre = frequency / float(count_group_items)
            x[index] = int(np.around(fre*100))
    return list_num_times


def get_appear_times_column_list(data_frame, count_group_items, step):
    list_num_times, list_sel_flags = get_appear_times_list(data_frame, count_group_items, step)
    list_times_col = [[0] * (count_group_items+1) for i in range(33)]
    for ball_i, x in enumerate(list_times_col):
        for index, frequency in enumerate(list_num_times[ball_i]):
            x[frequency] += 1
    return list_times_col


def get_appear_times_frequency_list(data_frame, count_group_items, step):
    list_num_times = get_appear_times_column_list(data_frame, count_group_items, step)
    for x in list_num_times:
        count_times = sum(x)
        for index, frequency in enumerate(x):
            fre = frequency / float(count_times)
            x[index] = int(np.around(fre*1000))
    return list_num_times
