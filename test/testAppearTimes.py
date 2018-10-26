#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import pandasReadExcel as pandasReader
import numpy as np
import appearTimes

def main():
    data_frame = pandasReader.read_from_excel()
    min_data_row = appearTimes.get_min_data_row(data_frame)
    print ('MinDataRow=', min_data_row)

    last_data = pandasReader.get_last_data(data_frame)
    count = 20
    plat_whole = plt.subplot2grid((1, count+ 1), (0, 0))
    list_ball_all = appearTimes.get_all_ball_times(data_frame)
    appearTimes.draw_appear_times(list_ball_all, plat_whole, last_data)

    start_row = data_frame.size- min_data_row- count
    for index in range(start_row, data_frame.size- min_data_row):
        data_frame_latest_all = data_frame.tail(data_frame.size- index)
        data_frame_latest_30 = data_frame_latest_all.head(min_data_row)
        # print (data_frame_latest_30)
        list_balls = appearTimes.get_all_ball_times(data_frame_latest_30)
        plat_latest_30 = plt.subplot2grid((1,count+ 1),(0,index- start_row+ 1))
        appearTimes.draw_appear_times(list_balls, plat_latest_30, last_data)
    #
    # plat_inner_10 = plt.subplot2grid((1,5),(0,2))
    # data_frame_latest_30_10 = data_frame_latest_30.head(10)
    # QuartileAnalysis(data_frame_latest_30_10, plat_inner_10,last_data)
    # plat_inner_30 = plt.subplot2grid((1,5),(0,3))
    # data_frame_latest_30_30 = data_frame_latest_30.tail(10)
    # QuartileAnalysis(data_frame_latest_30_30, plat_inner_30,last_data)
    # plat_inner_20 = plt.subplot2grid((1,5),(0,4))
    # data_frame_latest_30_20_whole = data_frame_latest_30.tail(20)
    # data_frame_latest_30_20 = data_frame_latest_30_20_whole.head(10)
    # QuartileAnalysis(data_frame_latest_30_20, plat_inner_20,last_data)
    plt.show()

if __name__ == '__main__':
    main()