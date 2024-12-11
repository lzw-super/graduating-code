from torchvision import transforms  
import cv2 
img_data = cv2.imread(r'E:\graduating design\test_code\dataset1\train\ants\0013035.jpg')
img_tans = transforms.ToTensor() 
# tensor_data = img_tans(img_data)