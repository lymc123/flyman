import unittest
from  selenium import  webdriver
from HTMLTestRunner import HTMLTestRunner

import os,sys,time

class unitone(unittest.TestCase):
    def setUp(self)  :
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')


    def test_a(self):
        self.driver.find_element_by_id('kw').send_keys('苹果')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        title=self.driver.title
        self.assertEqual(title,"苹果_百度搜索")


    def test_b(self):
        self.driver.find_element_by_id('kw').send_keys('小米')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        title=self.driver.title
        self.assertEqual(title,"小米_百度搜索")

    def tearDown(self) :
        time.sleep(3)
        self.driver.quit()

if __name__=='__main__':
    # current_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # suite=unittest.TestSuite()
    # suite.addTest(unitone("test_a"))
    # suite.addTest(unitone("test_b"))
    # # report_path= "./SoftTestReport_" + current_time  + '.html'
    #
    #
    # fp =open('./ResultReport.html','wb')
    # runner =HTMLTestRunner(stream=fp,title='测试报告', description='用例执行情况')
    # runner.run(suite)
    # fp.close()
    unittest.main()

