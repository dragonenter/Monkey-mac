import os
import xlsxwriter
from Base import BaseReport
from datetime import datetime


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def report(info):
    # workbook = xlsxwriter.Workbook('report.xlsx')
    # 获取当前时间
    now = datetime.now()
    # 格式化时间为字符串，例如：'2024-12-16_15-30-00'
    formatted_time = now.strftime('%Y-%m-%d_%H-%M-%S')

    # 创建工作簿，文件名包含当前时间
    workbook = xlsxwriter.Workbook(f'report_{formatted_time}.xlsx')
    bo = BaseReport.OperateReport(workbook)
    bo.monitor(info)
    bo.crash()
    bo.analysis(info)
    bo.close()