from torchvision import transforms  
import cv2  
from torch.utils.tensorboard import SummaryWriter 
writer = SummaryWriter(log_dir="./logs")  
img_data = cv2.imread(r'E:\graduating design\test_code\dataset1\train\ants\0013035.jpg') 
print(img_data.size)
img_tensor = transforms.ToTensor() 
tensor_data = img_tensor(img_data)
writer.add_image('init img' , tensor_data , 0)

trans = transforms.Compose([
    transforms.Resize((256,256)) , 
    transforms.ToTensor() , 
    transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
]) 
img_trans = trans(tensor_data) 
writer.add_image('resize and norm data' , img_trans , 0)
writer.close() 

