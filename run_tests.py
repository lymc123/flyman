import unittest
from HTMLTestRunner import HTMLTestRunner
import os,sys,time


test_dir='./test_case'
suits=unittest.defaultTestLoader.discover(test_dir,pattern='Unitone.py')

if __name__ == '__main__':
    current_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    report_path= "./test_report/ResultReport_" + current_time  + '.html'
    fp =open(report_path,'wb')
    runner =HTMLTestRunner(stream=fp,title='测试报告', description='百度搜索，chrome80浏览器')
    runner.run(suits,rerun=0, save_last_run=False)
    fp.close()