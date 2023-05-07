from spider import Spider
from data_processor import Data_processor as dp
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.pyplot import MultipleLocator

font = FontProperties(fname="font/SimHei.ttf", size=14)

def show_sale(data,name):
    x = []
    y = []
    for line in data[1:]:
            x.append(line["issue_num"])
            y.append(line["sale"])
    x = np.array(x)
    y = np.array(y)
    # 绘图
    plt.bar(x,y)
    plt.title(name+'的销售额（'+str(data[-1]["issue_num"])+"期--"+str(data[1]["issue_num"])+"期）",fontproperties=font)
    plt.xlabel('期号',fontproperties=font)
    plt.ylabel('销售额',fontproperties=font)
    # 显示图形
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.xlim(min(x) - 1, max(x) + 1)
    st.pyplot()

data_text=open('temp/data.txt','r')
data=''
for line in data_text.readlines():
    data+=line
data=eval(data)
dict={'qxc': '七星彩', 'sd': '3D', 'dlt': '大乐透', 'qlc': '七乐彩', 'ssq': '双色球', 'plw': '排列五', 'ps': '排列三'}
show_sale(data,dict[data[0]])