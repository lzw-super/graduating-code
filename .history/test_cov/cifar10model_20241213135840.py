from torch.nn import Conv2d,MaxPool2d,Linear,Sequential ,Flatten
import torch 
from torch import nn 
from torch.utils.tensorboard import SummaryWriter 
class mymodel(nn.Module) :
    def __init__(self):
        super(mymodel,self).__init__() 
        self.model1 = Sequential(
            Conv2d(3,32,5,padding=2),
            MaxPool2d(3) , 
            Conv2d(32,32,5,padding=2),
            MaxPool2d(3),
            Conv2d(32,64,5,padding=2),
            MaxPool2d(3),
            Flatten(),
            Linear(1024,64),
            Linear(64,10)
        )
    def forward(self,x) : 
        x = self.model1(x) 
        return x 
mine = mymodel()
input = torch.ones((64,3,32,32)) 
output = mine(input) 

writer = SummaryWriter('./logs') 
writer.add_graph(mine,input) 
writer.close()

