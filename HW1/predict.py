import torch
import torch.nn as nn

#定义超参数
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

model = GRULotto(input_size, hidden_size, output_size)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 示例训练数据
train_data = torch.randn(100, seq_length, input_size)
# 示例目标数据
target_data = torch.randn(100, output_size)

for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    # 前向传播
    output = model(train_data)
    # 计算损失
    loss = criterion(output, target_data)
    # 反向传播和优化
    loss.backward()
    optimizer.step()




