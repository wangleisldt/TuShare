import os

from 函数目录.function import file_List_Func

from 函数目录.function import 获取文件名前缀与后缀

from pdfminer.converter import PDFPageAggregator
#from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.layout import *

import re
import pandas as pd


def pdf文件处理(dirname,filename):
    #try:
        文件带全路径 = dirname + filename

        print(文件带全路径)

        fp = open(文件带全路径, 'rb')  # rb以二进制读模式打开本地pdf文件
        # request = Request(url=_path, headers={'User-Agent': random.choice(user_agent)})  # 随机从user_agent列表中抽取一个元素
        # fp = urlopen(request) #打开在线PDF文档

        # 用文件对象来创建一个pdf文档分析器
        praser_pdf = PDFParser(fp)

        # 创建一个PDF文档
        doc = PDFDocument()

        # 连接分析器 与文档对象
        praser_pdf.set_document(doc)
        doc.set_parser(praser_pdf)

        # 提供初始化密码doc.initialize("123456")
        # 如果没有密码 就创建一个空的字符串
        doc.initialize()

        # 检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            pass
            # raise PDFTextExtractionNotAllowed
        else:
            # 创建PDf资源管理器 来管理共享资源
            rsrcmgr = PDFResourceManager()

            # 创建一个PDF参数分析器
            laparams = LAParams()

            # 创建聚合器
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)

            # 创建一个PDF页面解释器对象
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            # 循环遍历列表，每次处理一页的内容
            # doc.get_pages() 获取page列表
            for page in doc.get_pages():
                # 使用页面解释器来读取
                interpreter.process_page(page)

                # 使用聚合器获取内容
                layout = device.get_result()

                # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
                for x in layout:
                    # 判断是否含有get_text()方法，图片之类的就没有

                        if isinstance(x, LTFigure):  # figure对象
                            print("bbb")
                            #x._objs[0]
                        elif isinstance(x, LTTextBoxHorizontal):  # 获取文本内容LTTextBox
                            results = x.get_text()
                            print(results)
                        else:
                            print(type(x))
                            print("aaa")


                            #if hasattr(out,"get_text"):
                        #print(out.get_text)
    #except:


if __name__ == '__main__':
    pdf文件处理("C:\\temp\\", "aaa.pdf")
