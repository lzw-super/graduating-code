import torch 
from PIL import Image 
from torch.utils.data import Dataset  
import os 
class mydata(Dataset) :
    def __init__(self,root_path) :
        self.root_path = root_path 
        self.img_path = os.path.join(root_path,'img') 
        self.label_path = os.path.join(root_path,'label') 
        self.data_path = os.listdir(self.img_path)
    def __getitem__(self, index) :
        self.img = self.data_path[index]
        self.data =  Image.open(os.path.join(self.img_path,self.img)) 
        self.name = self.img.split('.jpg')[0]
        with open (os.path.join(self.label_path,'{}.txt'.format(self.name))) as f :
            self.label = f.read()
        return self.data , self.label

    def __len__(self) : 
        return len(self.data_path)  



root_path  = r'E:\毕业设计\test_code\dataset2\train'  
data = mydata(root_path) 
img , label = data[136] 
img.show() 
print(label) 
print(len(data))
# feature1 = 'ants'
# feature2 = 'bees'
# ants_dataset = mydata(root_path,feature1) 
# bees_dataset = mydata(root_path,feature2)
# data = ants_dataset + bees_dataset

# img , label = ants_dataset[0] 
# img.show() 
# print(label) 

# img1 , label1 = data[124] 
# img1.show() 
# print(label1) 