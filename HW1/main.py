import re
from spider import Spider
from data_processor import Data_processor as dp

lottery=Spider("qxc")
processor=dp(lottery.get_name(),lottery.visit())
data=processor.process()
