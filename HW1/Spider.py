# 导入selenium和其他需要的库
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class spider():
    def __init__(self,lottery_name,start_num=-1,end_num=-1):
        #参数传递
        self.lottery_name=lottery_name
        self.start_num=start_num
        self.end_num=end_num
        self.data=[]
        self.spider_1_list=["qxc","sd","pls","plw"]
    def visit(self):
        if self.lottery_name in self.spider_1_list:
            self.spider_1()
        else:
            self.spider_2()
    def spider_1(self):
        # 创建一个webdriver对象，使用Chrome浏览器
        driver = webdriver.Chrome()
        # 访问目标网址
        url1="http://datachart.500.com/"
        url2="/history/history.shtml"
        driver.get(url1+self.lottery_name+url2)
        #跳转到名为“chart”的frame
        driver.switch_to.frame("chart")
        # 显式等待
        wait=WebDriverWait(driver,10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,'chart')))
        #定位开始和结束的input框,并设置期号
        if self.start_num != -1:
            start=driver.find_element_by_id("start")
            start.clear()
            start.send_keys(self.start_num)
        if self.end_num != -1:
            end=driver.find_element_by_id("end")
            end.clear()
            end.send_keys(self.end_num)
        #定位搜索按钮节点，并click
        if self.start_num != -1 or self.end_num !=-1:
            button = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/div/div/div/div[1]/div/table/tbody/tr/td[2]/img')
            button.click()
            time.sleep(random.randint(0,2))
        #定位id=“chart”的节点
        chart=driver.find_element_by_class_name("chart")
        time.sleep(random.randint(0,2))
        #参数传递
        self.data=chart.text
        #关闭浏览器
        driver.close()
        driver.quit()
    def spider_2(self):
        # 创建一个webdriver对象，使用Chrome浏览器
        driver = webdriver.Chrome()
        # 访问目标网址
        url1="http://datachart.500.com/"
        url2="/history/history.shtml"
        driver.get(url1+self.lottery_name+url2)
        # 显式等待
        wait=WebDriverWait(driver,10)
        wait.until(EC.presence_of_element_located((By.ID,'datachart')))
        #定位开始和结束的input框,并设置期号
        if self.start_num != -1:
            start=driver.find_element_by_id("start")
            start.clear()
            start.send_keys(self.start_num)
        if self.end_num != -1:
            end=driver.find_element_by_id("end")
            end.clear()
            end.send_keys(self.end_num)
        #定位搜索按钮节点，并click
        if self.start_num != -1 or self.end_num !=-1:
            button = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/div/div/div/div[1]/div/table/tbody/tr/td[2]/img')
            button.click()
            time.sleep(random.randint(0,2))
        #定位id=“chart”的节点
        chart=driver.find_element_by_id("datachart")
        time.sleep(random.randint(0,2))
        #参数传递
        self.data=chart.text
        #关闭浏览器
        driver.close()
        driver.quit()
    def get_data(self):
        return self.data