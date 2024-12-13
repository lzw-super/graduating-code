from torch.nn import Conv2d,MaxPool2d,Linear,Sequential ,Flatten
import torch 
from torch import nn  
import torchvision 
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter 
# 读数据 
data = torchvision.datasets.CIFAR10(root = r'E:\dataset',train = False,
transform = torchvision.transforms.ToTensor(),download=True) 
data_l = DataLoader(data,batch_size=64) 

# 建立模型
class mymodel(nn.Module) :
    def __init__(self):
        super(mymodel,self).__init__() 
        self.model1 = Sequential(
            Conv2d(3,32,5,padding=2),
            MaxPool2d(2) , 
            Conv2d(32,32,5,padding=2),
            MaxPool2d(2),
            Conv2d(32,64,5,padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024,64),
            Linear(64,10)
        )
    def forward(self,x) : 
        x = self.model1(x) 
        return x 
mine = mymodel()
# input = torch.ones((64,3,32,32)) 
# output = mine(input) 
# print(output.shape)  

# 加入loss and opitm 
optim =  torch.optim.SGD(mine.parameters(),0.01,)
loss_f = nn.CrossEntropyLoss()
for epoch in range(10) : 
    loss = 0.0
    for data in data_l :
        imgs , target = data  
        output = mine(imgs)
        optim.zero_grad()   # 每个batch_size 归零梯度 
        l = loss_f(output,target) 
        l.backward()     # 反向传播  根据损失函数来计算每个参数的梯度（让loss下降最快）
        optim.step()     # 优化器进行参数优化   
        loss = loss + l 
    print('epoch = {}, loss = {}'.format(epoch+1, loss))



# writer = SummaryWriter('./logs') 
# writer.add_graph(mine,input) 
# writer.close()


