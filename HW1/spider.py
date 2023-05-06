# 导入selenium和其他需要的库
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# 创建一个webdriver对象，使用Chrome浏览器
driver = webdriver.Chrome()

# 访问目标网址
driver.get("http://datachart.500.com/qxc/history/history.shtml")
#time.sleep(10)
driver.switch_to.frame("chart")

wait=WebDriverWait(driver,10) #显式等待：指定等待某个标签加载完毕
wait.until(EC.presence_of_element_located((By.CLASS_NAME,'chart')))
start=driver.find_element_by_id("start")
start.clear()
start.send_keys(start_number)
end=driver.find_element_by_id("end")
end.clear()
end.send_keys(end_number)
button = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/div/div/div/div[1]/div/table/tbody/tr/td[2]/img')  # 找到id为su的节点（百度一下）
button.click()
time.sleep(random.randint(0,2))
chart=driver.find_element_by_class_name("chart")
print(chart.text)
time.sleep(random.randint(0,2))
driver.close()
driver.quit()