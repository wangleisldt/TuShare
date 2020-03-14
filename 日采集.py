# encoding:utf-8

import 基本面数据.股票列表获取 as gplist

import 交易数据.实时交易数据 as rt

import 基本面数据.基本面数据获取 as jbmget

from  数据采集.沪深港通持股.沪深港通持股 import 沪深港通持股

#from 数据采集.上市公司调研情况.上市公司调研情况_对外接口 import

if __name__ == '__main__':
    #获取股票清单
    gplist.getStockList()

    #获取股票实时行情
    #rt.getRealtimeQuotesDataToExecl()

    #获取沪深港通持股
    a = 沪深港通持股()
    a.根据全量股票进行获取()
    a.步骤一()
    #a.步骤二()
    #a.步骤三()
