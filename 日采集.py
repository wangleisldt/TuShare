# encoding:utf-8

import 基本面数据.股票列表获取 as gplist

import 交易数据.实时交易数据 as rt

import 基本面数据.基本面数据获取 as jbmget

if __name__ == '__main__':
    #获取股票清单
    gplist.getStockList()

    #获取股票实时行情
    rt.getRealtimeQuotesDataToExecl()
