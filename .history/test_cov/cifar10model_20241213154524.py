from torch.nn import Conv2d,MaxPool2d,Linear,Sequential ,Flatten
import torch 
from torch import nn  
import torchvision 
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter 
# 读数据 
data = torchvision.datasets.CIFAR10(root = r'E:\graduating design\cifardata',train = False,
transform = torchvision.transforms.ToTensor(),download=False) 
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
        optim.zero_grad()   # 每个batch 归零梯度 
        output = mine(imgs)
        l = loss_f(output,target) 
        l.backward() 
        optim.step()
        loss = loss + l 
    print('{epoch = {},loss = {}}'.format(epoch,loss)) 



# writer = SummaryWriter('./logs') 
# writer.add_graph(mine,input) 
# writer.close()


