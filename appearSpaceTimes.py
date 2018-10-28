# -*- coding:utf-8 -*-
import pandasReadExcel as pandasReader


def get_appear_space_times(data_frame):
    """
    :param data_frame: C-H列为红球；I列为蓝球；P列为投注总额；R列为奖池金额
    :return:
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
        print(list_num)
    list_numbers = map(list, zip(*list_numbers))

    return list_numbers


def main():
    data_frame = pandasReader.read_from_excel()
    list_numbers = get_appear_space_times(data_frame)
    print(list_numbers)
    print(len(list_numbers))


if __name__ == '__main__':
    main()

