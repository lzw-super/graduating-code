import torch 
from torch import nn 
import torchvision 
vgg_m2 = torchvision.models.vgg16(weights = False)   

# 保存模型
torch.save(vgg_m2,'../vgg_1.pth') 
#保存模型参数
torch.save(vgg_m2.state_dict(),'../vgg_2.pth')     # 模型后缀为.pth  


m1 = torch.load('../vgg_1.pth')

vgg_m3 = torchvision.models.vgg16(weights = False)   
vgg_m3.load_state_dict(torch.load('../vgg_2.pth'))



