from torchvision import transforms  
import cv2   
from PIL import Image
from torch.utils.tensorboard import SummaryWriter 
writer = SummaryWriter(log_dir="./logs")  
img_data = Image.open(r'E:\graduating design\test_code\dataset1\train\ants\0013035.jpg') 
# print(img_data.size)
img_tensor = transforms.ToTensor() 
tensor_data = img_tensor(img_data)
writer.add_image('init img' , tensor_data , 0)

trans = transforms.Compose([
    transforms.Resize((256,256)) , 
    transforms.ToTensor() , 
    transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
]) 
img_trans = trans(img_data) 
writer.add_image('resize and norm data' , img_trans , 0) 

trans2 = transforms.Compose([
    transforms.RandomCrop((500,1000)) , 
    transforms.ToTensor() , 
])  
for i in range(10) : 
    crop_wh_img = trans2(img_data) 
    writer.add_image('crop_wh_img',crop_wh_img,i)
writer.close() 

