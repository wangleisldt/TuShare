# encoding:utf-8

from 函数目录.function import checkAndCreateDir
from 函数目录.function import file_List_Func
from 函数目录.function import from_filename_get_info
from 函数目录 import profile as pf

import pandas as pd
import numpy as np
import pickle

def 扫描目录_读取_EXECL_对指定的季度数据_转换成_DICT(dir_name,quarter):
    try:
        fileList = file_List_Func(dir_name)
        all_stock_dict = {}
        for filename in fileList:
            stockid1 ,year1, quarter1 = from_filename_get_info(filename)
            if quarter == quarter1:
                key = "%s-%s-%s" % (stockid1 ,year1, quarter1)
                fullfilename = "%s%s" % (dir_name,filename)
                print(fullfilename)
                df = pd.read_excel(fullfilename,usecols=[1,2])

                stock_list = np.array(df)       #通过将df转换成list然后再进行处理

                one_stock_dict = {}
                for element in stock_list:      #对list的每一行进行处理
                    one_stock_dict[element[0]] = element[1]
                all_stock_dict[key] = one_stock_dict
        return all_stock_dict
    except:
        print("文件 %s 有问题。" % (fullfilename))


def 整理某个季度的基本面数据(指标名称,年份,季度):
    #根据参数，扫描目录，将文件转换为字典
    base_dir_name = "%s%s%s" % (pf.GLOBAL_PATH,pf.SEPARATOR,pf.FUNDAMENTAL_DATA)
    dir_name = "%s%s%s%s%s%s"  % ( base_dir_name,pf.SEPARATOR,指标名称,pf.SEPARATOR,年份,pf.SEPARATOR)
    all_stock_dict = 扫描目录_读取_EXECL_对指定的季度数据_转换成_DICT(dir_name, 季度)

    #定义输出的目录和相应的文件名称并保存
    output_filename = "%s-%s%s" % (年份,季度, pf.PklFile)
    output_dir = "%s%s%s%s%s" % (base_dir_name,pf.AfterFinishingData,pf.SEPARATOR,指标名称,pf.SEPARATOR)
    checkAndCreateDir(output_dir)

    full_file_name = "%s%s" % (output_dir,output_filename)

    output = open(full_file_name, 'wb')
    pickle.dump(all_stock_dict, output)
    output.close()

    return full_file_name


if __name__ == '__main__':
    filename = 整理某个季度的基本面数据("财务指标", "2017", "3")

    print(filename)
    pklFile = open(filename, 'rb')
    aaa = pickle.load(pklFile)
    pklFile.close()


    print(aaa['603989-2017-3']['销售毛利率(%)'])
    #print(aaa['603989-2017-3']['销售毛利率(%)'])
    #print(aaa['603989-2017-3']['销售毛利率(%)'])
