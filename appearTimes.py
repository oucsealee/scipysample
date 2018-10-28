# -*- coding:utf-8 -*-
import numpy as np


def get_min_data_row(data_frame):
    list_balls = [0] * 34
    count_row = 0
    min_data_row = 0
    for index, row in data_frame.iterrows():
        list_balls[row['C']] += 1
        list_balls[row['D']] += 1
        list_balls[row['E']] += 1
        list_balls[row['F']] += 1
        list_balls[row['G']] += 1
        list_balls[row['H']] += 1
        count_row += 1
        fall_no_zero = False
        for x in range(1,34):
            if list_balls[x] == 0:
                break
            fall_no_zero = x == 33
        if fall_no_zero:
            min_data_row = max(count_row,min_data_row)
            count_row = 0
    return min_data_row


def get_all_ball_times(data_frame):
    list_balls = [0] * 34
    for index, row in data_frame.iterrows():
        list_balls[row['C']] += 1
        list_balls[row['D']] += 1
        list_balls[row['E']] += 1
        list_balls[row['F']] += 1
        list_balls[row['G']] += 1
        list_balls[row['H']] += 1
    del list_balls[0]
    return list_balls


def draw_appear_times(list_balls, plt_region, last_data):
    list_index = range(0, 34)
    del list_index[0]

    percent_25 = np.percentile(list_balls, 25)
    print ("percent_25=", percent_25)
    middle_val = np.median(list_balls)
    print ('middle=', middle_val)
    percent_75 = np.percentile(list_balls, 75)
    print ('percent_75=', percent_75)
    mean = np.mean(list_balls)
    print('mean=', mean)
    std_cha = np.std(list_balls)
    print('std_cha=', std_cha)
    max_quar = [x for x in list_index if list_balls[x - 1] > percent_75]
    print ('region(percent_75,)=', max_quar)
    min_quar = [x for x in list_index if list_balls[x - 1] < percent_25]
    print ("region(,percent_25)==", min_quar)
    max_cen_quar = [x for x in list_index if list_balls[x - 1] <= percent_75 and list_balls[x-1] >= middle_val]
    print ('region(middle_val,percent_75)=', max_cen_quar)
    min_cen_quar = [x for x in list_index if list_balls[x - 1] >= percent_25 and list_balls[x-1] < middle_val]
    print ('region(percent_25,middle_val)=', min_cen_quar)

    plt_region.hlines(percent_25, 0, 33, colors='g')
    plt_region.hlines(middle_val, 0, 33, colors='g')
    plt_region.hlines(percent_75, 0, 33, colors='g')

    plt_region.scatter(list_index, list_balls)

    list_balls_last = []
    for x in last_data:
        list_balls_last.append(list_balls[x])
    plt_region.scatter(last_data, list_balls_last, color='r')
