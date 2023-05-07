#导入依赖
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#导入字体，用于表格显示中文
font = FontProperties(fname="font/SimHei.ttf", size=14)

#网页显示
def show_sale(data,name):
    END = len(data)
    #定义开始期号和结束期号的滑杆
    start = st.sidebar.slider('开始期号', 0, END - 1, int(END / 100) + 1)
    end = st.sidebar.slider('结束期号', 0, END - 1, int(END / 100) + 1)
    if start != end:
        x = []
        y = []
        for line in data[start:end+1]:
                x.append(line["issue_num"])
                y.append(line["sale"])
        x = np.array(x)
        y = np.array(y)
        #画出柱状图
        plt.bar(x,y)
        plt.title(name+'的销售额（'+str(data[start]["issue_num"])+"期--"+str(data[end]["issue_num"])+"期）",fontproperties=font)
        plt.xlabel('期号',fontproperties=font)
        plt.ylabel('销售额',fontproperties=font)
        #显示图形
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.xlim(min(x) - 1, max(x) + 1) #修改x轴始末值
        st.pyplot()

#读取数据
data_text=open('temp/data.txt','r')

#数据格式转化
data=''
for line in data_text.readlines():
    data+=line
data=eval(data)
dict={'qxc': '七星彩', 'sd': '3D', 'dlt': '大乐透', 'qlc': '七乐彩', 'ssq': '双色球', 'plw': '排列五', 'ps': '排列三'}

#调用网页展示
show_sale(data,dict[data[0]])