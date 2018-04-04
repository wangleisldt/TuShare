import xlrd

from 函数目录 import profile as pf, date


def getPriceFromExecl(StockId,YearMonth,Type=pf.Hfq,PriceCount = 3):
    try:
        # 打开文件，读取每一行，每一列
        dirBase = pf.GLOBAL_PATH + pf.SEPARATOR + pf.TransactionData + pf.SEPARATOR + pf.HistoryData + pf.SEPARATOR
        filename = dirBase + Type + pf.SEPARATOR + YearMonth[0:4] + pf.SEPARATOR +StockId + pf.Execl
        workbook = xlrd.open_workbook(filename)
        sheet = workbook.sheet_by_index(0)
        rows = sheet.nrows
        price = 0
        count = PriceCount
        for i in range(rows):
            if i != 0:
                row = sheet.row_values(i)
                if str(row[1][0:4])+str(row[1][5:7]) == YearMonth:
                    if count > 0:
                        count = count -1
                        price = round(price + round(row[3], 2), 2)
        if count == 0 :
            return round(price/PriceCount,2)
        else:
            return 0
    except:
        return 0


#################################################
# 计算股票获利百分比
#################################################
def calculateStockPriceDifference(StockId,FromYearMonth,LengthMonth,Type=pf.Hfq,PriceCount=3):
    toYearMonth = date.getYearMonthFromMonthLength(FromYearMonth, LengthMonth)
    priceBegin = getPriceFromExecl(StockId, FromYearMonth, Type=Type, PriceCount = PriceCount)
    priceEnd = getPriceFromExecl(StockId, toYearMonth, Type=Type, PriceCount=PriceCount)
    #返回增长率
    if priceBegin!=0 and priceEnd !=0:
        return True,round((priceEnd-priceBegin)/priceBegin*100 , 5),FromYearMonth,toYearMonth
    else:
        return False,0,FromYearMonth,toYearMonth

if __name__ == '__main__':
    b = calculateStockPriceDifference("600900", "201408",36)
    print(b)