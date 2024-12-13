import torchvision  
from torch import nn 
from torch.nn import Conv2d 
from torch.utils.data import DataLoader
data = torchvision.datasets.CIFAR10(r'E:\graduating design\cifardata\cifar-10-batches-py',False,torchvision.transforms.ToTensor(),download=False) 
data_l = DataLoader(data,batch_size=64) 

class mycov(nn.Module) : 
    def __init__(self) :
        super(mycov,self).__init__() 
        self.conv1 = Conv2d(3,6,3,1,padding=0) 
    def forword(self,x) : 
        x = self.conv1(x) 

mine = mycov()
print(mine)