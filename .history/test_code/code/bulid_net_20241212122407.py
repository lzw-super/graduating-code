# from torch.utils.tensorboard import SummaryWriter
# # 创建编辑器，保存日志，指令保存路径log_dir
# writer = SummaryWriter(log_dir="./logs") 
# # 指定保存位置
# # y = 2 * x
# for i in range(100):
    
# # 添加标题，x轴，y轴
    
# # tag: 标题名， scalar_value: y轴， global_step: x轴
#     writer.add_scalar(tag="y=3x",scalar_value=3*i,global_step=i)
#     # writer.add_scalar('training loss',train_total_loss,epoch) 
#     writer.add_image()
# # 关闭
# writer.close()

from  torchvision import datasets, transforms  
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader
trans = transforms.Compose([
    transforms.ToTensor()
])
train_data = datasets.CIFAR10(root='./cifardata',train=True,transform= trans,download=True)
test_data = datasets.CIFAR10(root='./cifardata',train=False,transform= trans,download=True)

data_load = DataLoader(dataset = train_data,batch_size=36,shuffle=True,num_workers=0,drop_last=False) 

writer = SummaryWriter(log_dir="./cifarcompare") 
for epoch in range(2) : 
    count = 0
    for data in data_load :
        writer.add_images(tag='epoch = {} cifardata'.format(epoch),img_tensor=data,global_step=count,)
        count = count +1

writer.close()


