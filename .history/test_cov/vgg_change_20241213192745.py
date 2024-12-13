import torch 
from torch import nn 
import torchvision 
# vgg_m1 = torchvision.models.vgg16(weights = True) 
vgg_m2 = torchvision.models.vgg16(weights = False) 
print('ok')
vgg_m2.classifier.add_module(nn.modules.Linear(1000,10)) 
print(vgg_m2)
vgg_m2.classifier[3] = nn.modules.AvgPool2d((3,3))
print(vgg_m2)