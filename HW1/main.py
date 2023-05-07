from spider import Spider
from data_processor import Data_processor as dp
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
from matplotlib.pyplot import MultipleLocator

font = FontProperties(fname="font/SimHei.ttf", size=14)
def show_p(data,name):
    count_6={}
    count_7={}
    total_6=0
    total_7=0
    END=len(data)
    start = st.sidebar.slider('开始期号', 0, END, int(END/100)+1)
    end = st.sidebar.slider('结束期号',0,END, int(END/100)+1)
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

    x = []
    y = []
    for num in count_6.keys():
        x.append(num)
        y.append(count_6[num]/total_6)
    x = np.array(x)
    y = np.array(y)
    plt.bar(x, y)
    plt.title(name + '的前六位各数字概率（' + str(data[-1]["issue_num"]) + "期--" + str(data[1]["issue_num"]) + "期）",
              fontproperties=font)
    plt.xlabel('数字', fontproperties=font)
    plt.ylabel('概率', fontproperties=font)
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(MultipleLocator(1))
    plt.xlim(min(x)-0.5, max(x)+0.5)
    # 显示图形
    st.set_option('deprecation.showPyplotGlobalUse', False)
    if st.button('开始/更新'):
        st.pyplot()

    x = []
    y = []
    for num in count_7.keys():
        x.append(num)
        y.append(count_7[num] / total_7)
    x = np.array(x)
    y = np.array(y)
    plt.bar(x, y)
    plt.title(name + '的第七位各数字概率（' + str(data[-1]["issue_num"]) + "期--" + str(data[1]["issue_num"]) + "期）",
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


#网页显示
st.markdown("# 彩票数据分析")
st.markdown("***")
st.markdown("### 请选择彩票种类：")
option = st.radio(
        '支持以下七种彩票（默认为空）',
        ('空','七星彩', '排列三', '排列五','大乐透','双色球','七乐彩','3D'))
start = st.number_input('输入开始期号（若为0，则默认为近30期 ; 若为1，则从最早一期开始）',step=1)
end = st.number_input('输入结束期号（若为0，则默认为最近一期）',step=1)
button=st.button('开始分析')
#爬虫和数据清洗
dict={"七星彩":"qxc","3D":"sd","大乐透":"dlt","七乐彩":"qlc","双色球":"ssq","排列五":"plw","排列三":"ps"}
if option != '空' and button:
        lottery=Spider(dict[option],start,end)
        processor=dp(lottery.get_name(),lottery.visit())
        data=processor.process()
        save_data(data)
        show_sale(data,option)
        show_p(data,option)



