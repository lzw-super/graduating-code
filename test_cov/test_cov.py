import torchvision  
from torch import nn 
from torch.nn import Conv2d 
from torch.utils.data import DataLoader  
import torch

from torch.utils.tensorboard import SummaryWriter
data = torchvision.datasets.CIFAR10(root = r'E:\graduating design\cifardata',train = False,
transform = torchvision.transforms.ToTensor(),download=False) 
data_l = DataLoader(data,batch_size=64) 

class mycov(nn.Module) : 
    def __init__(self) :
        super(mycov,self).__init__() 
        self.conv1 = Conv2d(3,6,3,1,padding=0) 
    def forward(self,x) : 
        x = self.conv1(x) 
        return x

mine = mycov()
print(mine) 
writer = SummaryWriter('./logs') 
step = 0
for d in data_l :
    imgs = d[0] 
    output = mine(imgs) 
    # print(imgs.shape) 
    # print(output.shape) 
    writer.add_images('input',imgs,step) 
    output = torch.reshape(output,(-1,3,30,30))

    writer.add_images('output',output,step) 
    step = step+1 
writer.close()
