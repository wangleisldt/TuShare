from 函数目录.function import file_List_Func

def 读取_EXECL_转换成_DATAFRAME():
    fileList = file_List_Func("C://量化//基本面数据//财务指标//2017//")
    for e in fileList:
        print(e)

if __name__ == '__main__':
    读取_EXECL_转换成_DATAFRAME()
