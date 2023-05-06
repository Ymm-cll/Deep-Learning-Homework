import re

class Data_processor():
    def __init__(self,lottery_name,data_raw):
        self.lottery_name=lottery_name
        self.data_raw=data_raw
        self.lotterys=[]
        #issue_num,number,sale,date
        #索引字典：期号，中奖号码开始，中奖号码结束，销售额，时间
        self.dict={"qxc":[0,1,7,9,10]}
    def str2int(self):
        data = self.data_raw.replace(",", "").split("\n")
        data_new = []
        for line in data:
            line_new = []
            for ele in line.split(" "):
                if re.match(r"\d+", ele) and '-' not in ele:
                    ele = int(ele)
                line_new.append(ele)
            data_new.append(line_new)
        return data_new
    def extract(self,data_new):
        for line in data_new[2:]:
            lottery={}
            lottery["issue_num"]=line[self.dict[self.lottery_name][0]]
            lottery["number"]=line[self.dict[self.lottery_name][1]:self.dict[self.lottery_name][2]+1]
            lottery["sale"]=line[self.dict[self.lottery_name][3]]
            lottery["date"] = line[self.dict[self.lottery_name][4]]
            self.lotterys.append(lottery)
    def process(self):
        self.extract(self.str2int())
        return self.lotterys