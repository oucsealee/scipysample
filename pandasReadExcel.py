# -*- coding:utf-8 -*-
import pandas as pd


def read_from_excel():
    """
    :return: data_frame: C-H为红球；I为蓝球；P为投注总额；R为奖池金额
    """
    data_frame = pd.read_excel('D:\Source\scipysample\ssq.xls')
    data_frame.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T',
                          'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD']
    data_frame.drop(
        columns=['A', 'B', 'J', 'K', 'L', 'M', 'N', 'O', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC',
                 'AD'], inplace=True)
    return data_frame


def get_last_red_data(data_frame):
    last_data_frame = data_frame.tail(1)
    for index, row in last_data_frame.iterrows():
        last_data = [row['C'], row['D'], row['E'], row['F'], row['G'], row['H']]
        break
    return last_data


def main():
    data_frame = read_from_excel()
    print (data_frame)
    last_data = get_last_red_data(data_frame)
    print (last_data)


if __name__ == '__main__':
    main()
