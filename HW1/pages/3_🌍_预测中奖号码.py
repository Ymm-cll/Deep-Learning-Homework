import streamlit as st
import torch
import torch.nn as nn
input_size = 1  # 输入特征大小
hidden_size = 128  # 隐藏状态大小
output_size = 1  # 输出大小
seq_length = 7  # 输入序列长度
num_epochs = 100

class GRULotto(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(GRULotto, self).__init__()
        self.hidden_size = hidden_size
        self.gru = nn.GRU(input_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)
    def forward(self, input):
        _, hidden = self.gru(input)
        output = self.fc(hidden)
        return output

num = st.number_input('请输入所要预测中奖号码的期号',step=1)

model = GRULotto(input_size, hidden_size, output_size)
model._load_to_state_dict("model/model")
model.eval()
# 示例测试数据
test_data = torch.randn(10, seq_length, input_size)
# 进行预测
with torch.no_grad():
    predictions = model(test_data)
# 打印预测结果
print('Predictions:')
for i in range(predictions.shape[0]):
    print(predictions[i].item())