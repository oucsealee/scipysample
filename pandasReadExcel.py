# -*- coding:utf-8 -*-
import pandas as pd


def read_from_excel():
    data_frame = pd.read_excel('D:\Source\scipysample\ssq.xls')
    data_frame.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T',
                          'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD']
    data_frame.drop(
        columns=['A', 'B', 'J', 'K', 'L', 'M', 'N', 'O', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC',
                 'AD'], inplace=True)
    return data_frame


def get_last_data(data_frame):
    last_data_frame = data_frame.tail(1)
    for index, row in last_data_frame.iterrows():
        last_data = [row['C'], row['D'], row['E'], row['F'], row['G'], row['H']]
        break
    return last_data

