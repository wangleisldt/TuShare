# encoding:utf-8
import sys

GLOBAL_PATH = 'C:\量化'
SEPARATOR = "\\"
Execl = ".xlsx"
PklFile = ".pkl"


#基本面数据相关目录常量
FUNDAMENTAL_DATA = "基本面数据"

PerformanceReport = "业绩报告（主表）"
ProfitAbility = "盈利能力"
OperationCapacity = "营运能力"
GrowthAbility = "成长能力"
DebtPayingAbility = "偿债能力"
CashFlow = "现金流量"

FinancialIndex = '财务指标'
BalanceSheet = '资产负债表'
CashFlowSheet = '现金流量表'
CompanyProfitStatement = '公司利润表'

#股票列表目录、文件常量
StockList = "股票列表"
StockListFilename = "stocklist"

#交易数据目录常量
TransactionData = "交易数据"

HistoryData = "历史行情"
RehabilitationOfHistoricalData = "复权数据"
Qfq = "qfq"
Hfq = "hfq"


RealtimeQuotesData = "实时行情"
StockRealtimeQuotesDataFilename = "StockRealtimeQuotes"


###################################################################

P_TYPE = {'http': 'http://', 'ftp': 'ftp://'}

#http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/000001/ctrl/2017/displaytype/4.phtml
财务指标_URL = '%smoney.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/%s/ctrl/%s/displaytype/%s.phtml'
#http://money.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet/stockid/000952/ctrl/2016/displaytype/4.phtml
资产负债表_URL = '%smoney.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet/stockid/%s/ctrl/%s/displaytype/%s.phtml'
#http://money.finance.sina.com.cn/corp/go.php/vFD_CashFlow/stockid/000952/ctrl/2016/displaytype/4.phtml
现金流量表_URL = '%smoney.finance.sina.com.cn/corp/go.php/vFD_CashFlow/stockid/%s/ctrl/%s/displaytype/%s.phtml'
#http://money.finance.sina.com.cn/corp/go.php/vFD_ProfitStatement/stockid/000001/ctrl/2016/displaytype/4.phtml
公司利润表_URL = '%smoney.finance.sina.com.cn/corp/go.php/vFD_ProfitStatement/stockid/%s/ctrl/%s/displaytype/%s.phtml'

DATA_GETTING_TIPS = '[Getting data:]'
DATA_GETTING_FLAG = '#'

def _write_head():
    sys.stdout.write(DATA_GETTING_TIPS)
    sys.stdout.flush()

def _write_console():
    sys.stdout.write(DATA_GETTING_FLAG)
    sys.stdout.flush()

def _write_msg(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()



DATE_CHK_MSG = '年度输入错误：请输入1989年以后的年份数字，格式：YYYY'
DATE_CHK_Q_MSG = '季度输入错误：请输入1、2、3或4数字'

def _check_input(year, quarter):
    if isinstance(year, str) or year < 1989 :
        raise TypeError(DATE_CHK_MSG)
    elif quarter is None or isinstance(quarter, str) or quarter not in [1, 2, 3, 4]:
        raise TypeError(DATE_CHK_Q_MSG)
    else:
        return True

End_OF_SEASON_DAY = {1: '-03-31', 2: '-06-30', 3: '-09-30', 4: '-12-31'}



