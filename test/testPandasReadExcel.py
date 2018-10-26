#-*- coding:utf-8 -*-
import pandas as pd
import pandasReadExcel

def main():
    data_frame = pandasReadExcel.read_from_excel()
    print(data_frame)
    last_data = pandasReadExcel.get_last_data(data_frame)
    print (last_data)

if __name__ == '__main__':
    main()