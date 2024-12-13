import torch 
from torch import nn 
import torchvision 
# vgg_m1 = torchvision.models.vgg16(weights = True) 
vgg_m2 = torchvision.models.vgg16(weights = False) 
print('ok')