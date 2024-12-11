import torch 
from PIL import Image 
from torch.utils.data import Dataset  
import os 
class mydata(Dataset) :
    def __init__(self,root_path,feature) :
        self.root_path = root_path 
        self.feature = feature
        self.data_path = os.path.join(root_path,feature) 
        self.feature_path = os.listdir(self.data_path)
    def __getitem__(self, index) :
        self.img_path = self.feature_path[index] 
        self.data =  Image.open(os.path.join(self.data_path,self.img_path)) 
        return self.data , self.feature

    def __len__(self) : 
        return len(self.feature_path)  

root_path  = r'E:\毕业设计\test_code\dataset1\train' 
feature1 = 'ants'
feature2 = 'bees'
ants_dataset = mydata(root_path,feature1) 
bees_dataset = mydata(root_path,feature2)
data = ants_dataset + bees_dataset

img , label = ants_dataset[0] 
img.show() 
print(label) 

img1 , label1 = data[124] 
img1.show() 
print(label1) 