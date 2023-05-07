#导入依赖
from spider import Spider
from data_processor import Data_processor as dp
import streamlit as st

#保存数据
def save_data(data):
    mid = str(data)
    f = open('temp/data.txt', 'w')
    f.writelines(mid)
    f.close()

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



