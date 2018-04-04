from threading import Thread
import time

import os

import pandas as pd
from tushare.stock import cons as ct
import lxml.html
from lxml import etree
import re
import time
from pandas.compat import StringIO
from tushare.util import dateu as du
from urllib.request import urlopen, Request


class TimeoutException(Exception):
    pass

#ThreadStop = Thread._Thread__stop#获取私有函数

def timelimited(timeout):
    def decorator(function):
        def decorator2(*args,**kwargs):
            class TimeLimited(Thread):
                def __init__(self,_error= None,):
                    Thread.__init__(self)
                    self._error =  _error

                def run(self):
                    try:
                        self.result = function(*args,**kwargs)
                    except Exception as e:
                        self._error =e

                #def _stop(self):
                    #if self.isAlive():
                        #Thread._stop()

            t = TimeLimited()
            t.setDaemon(True)
            t.start()
            t.join(timeout)


            if isinstance(t._error,TimeoutException):
                #t._stop()
                raise TimeoutException()

            if t.isAlive():
                #t._stop()
                raise TimeoutException()

            if t._error is None:
                return t.result

        return decorator2
    return decorator

@timelimited(2)
def fn_1(secs):
    time.sleep(secs)
    return 'Finished'


def get_report_data(year, quarter):
    """
        获取业绩报表数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
       说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度

    Return
    --------
    DataFrame
        code,代码
        name,名称
        eps,每股收益
        eps_yoy,每股收益同比(%)
        bvps,每股净资产
        roe,净资产收益率(%)
        epcf,每股现金流量(元)
        net_profits,净利润(万元)
        profits_yoy,净利润同比(%)
        distrib,分配方案
        report_date,发布日期
    """
    if ct._check_input(year, quarter) is True:
        ct._write_head()
        df = _get_report_data(year, quarter, 1, pd.DataFrame())
        if df is not None:
            #             df = df.drop_duplicates('code')
            df['code'] = df['code'].map(lambda x: str(x).zfill(6))
        return df


def _get_report_data(year, quarter, pageNo, dataArr,
                     retry_count=3, pause=0.001):
    ct._write_console()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(ct.REPORT_URL%(ct.P_TYPE['http'], ct.DOMAINS['vsf'], ct.PAGES['fd'],
                             year, quarter, pageNo, ct.PAGE_NUM[1]))
            text = urlopen(request, timeout=10).read()
            text = text.decode('GBK')
            text = text.replace('--', '')
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table[@class=\"list_table\"]/tr")
            if ct.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>'%sarr
            df = pd.read_html(sarr)[0]
            df = df.drop(11, axis=1)
            df.columns = ct.REPORT_COLS
            dataArr = dataArr.append(df, ignore_index=True)
            nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
            if len(nextPage)>0:
                pageNo = re.findall(r'\d+', nextPage[0])[0]
                return _get_report_data(year, quarter, pageNo, dataArr)
            else:
                return dataArr
        except Exception as e:
            pass
    raise IOError(ct.NETWORK_URL_ERROR_MSG)

if __name__ == "__main__":
    get_report_data(2014,1)


