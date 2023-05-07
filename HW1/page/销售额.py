from spider import Spider
from data_processor import Data_processor as dp
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
from matplotlib.pyplot import MultipleLocator

font = FontProperties(fname="../font/SimHei.ttf", size=14)

def save_data(data):
    mid = str(data)
    f = open('temp/data.txt', 'w')
    f.writelines(mid)
    f.close()
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
    st.pyplot()

data=open('../temp')