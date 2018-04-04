import os
import pickle
import pathlib

from 函数目录 import profile as pf

#################################################
#   判断目录是否存在，如果不存在创建该目录
#################################################
def checkAndCreateDir(dirName):
    if os.path.exists(dirName):
        pass
    else:
        os.makedirs(dirName)
        print("\n创建目录：",dirName)

#################################################
#   从pkl文件读取数据到字典dict
#################################################
def getPklDataToDict(filename):
    pklFile = open( filename , 'rb')
    returnDict = pickle.load(pklFile)
    pklFile.close()
    return returnDict

#################################################
#   检测文件是否存在
#################################################
def check_file_exist(dirname,filename):
    checkAndCreateDir(dirname)
    path = pathlib.Path("%s%s%s" % (dirname,pf.SEPARATOR,filename))
    return path.is_file()


#################################################
#   保存文件
#################################################
def save_file_dataframe_to_execl(dirname,filename,df):
    if check_file_exist(dirname, filename):
        print("文件存在！")
    else:
        full_filename = dirname + pf.SEPARATOR +filename
        df.to_excel(full_filename)
        print("%s  保存文件成功。" % (full_filename))


#################################################
#   扫描目录，返回文件名称List
#################################################
def file_List_Func(Path):
    fileList = []
    for file in os.listdir(Path):
        file_path = os.path.join(Path, file)
        if os.path.isdir(file_path):
            pass
        else:
            fileList.append(file)
    return fileList
