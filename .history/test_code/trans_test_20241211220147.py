from torchvision import transforms  
import cv2 
img_data = cv2.imread(r'E:\graduating design\test_code\dataset1\train\ants\0013035.jpg')
img_tensor = transforms.ToTensor() 
tensor_data = img_tensor(img_data)

trans = transforms.Compose([
    transforms.Resize((256,256)) , 
    transforms.ToTensor() , 
    transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
]) 
img_trans = trans(img_data)
