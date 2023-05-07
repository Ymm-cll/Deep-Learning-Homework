#导入依赖
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.pyplot import MultipleLocator

#导入字体，用于表格显示中文
font = FontProperties(fname="font/SimHei.ttf", size=14)

#网页显示
def show_p(data,name):
    #用于计数
    count_6={}
    count_7={}
    total_6=0
    total_7=0
    END=len(data)
    start = st.sidebar.slider('开始期号', 0, END-1, int(END/100)+1)
    end = st.sidebar.slider('结束期号',0,END-1, int(END/100)+1)
    if start != end:
        for line in data[start:end+1]:
            for num in line["number"][:-1]:
                if num not in count_6.keys():
                    count_6[num]=0
                count_6[num]+=1
                total_6+=1
            last=line["number"][-1]
            if last not in count_7:
                count_7[last]=0
            count_7[last] += 1
            total_7 += 1

        # 前六位数字
        x = []
        y = []
        #计数转化为概率
        for num in count_6.keys():
            x.append(num)
            y.append(count_6[num]/total_6)
        x = np.array(x)
        y = np.array(y)
        #画出柱状图
        plt.bar(x, y)
        plt.title(name + '的前六位各数字概率（' + str(data[start]["issue_num"]) + "期--" + str(data[end]["issue_num"]) + "期）",
                  fontproperties=font)
        plt.xlabel('数字', fontproperties=font)
        plt.ylabel('概率', fontproperties=font)
        ax = plt.gca()
        # ax为两条坐标轴的实例
        ax.xaxis.set_major_locator(MultipleLocator(1))
        plt.xlim(min(x)-0.5, max(x)+0.5)
        # 显示图形
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        #第七位数字
        x = []
        y = []
        # 计数转化为概率
        for num in count_7.keys():
            x.append(num)
            y.append(count_7[num] / total_7)
        x = np.array(x)
        y = np.array(y)
        plt.bar(x, y)
        plt.title(name + '的第七位各数字概率（' + str(data[start]["issue_num"]) + "期--" + str(data[end]["issue_num"]) + "期）",
                  fontproperties=font)
        plt.xlabel('数字', fontproperties=font)
        plt.ylabel('概率', fontproperties=font)
        ax = plt.gca()
        # ax为两条坐标轴的实例
        ax.xaxis.set_major_locator(MultipleLocator(1))
        plt.xlim(min(x) - 0.5, max(x) + 0.5)
        # 显示图形
        st.set_option('deprecation.showPyplotGlobalUse', False)
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
show_p(data,dict[data[0]])