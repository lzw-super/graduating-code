import os 
import shutil
file_path = r'E:\毕业设计\test_code\dataset2\val'  
# os.mkdir(file_path + 'img') 
# os.mkdir(file_path + 'label')
dir1 = 'bees_img'  
label1 = dir1.split('_')[0]
dir2 = 'ants_img'  
label2 = dir2.split('_')[0] 
def write_label(file_path,dir,label) :
    path_dir = os.listdir(os.path.join(file_path,dir)) 
    for p in path_dir :
        shutil.copy(os.path.join(os.path.join(file_path,dir),p),os.path.join(file_path,'img'))
        name = p.split('.jpg')[0] 
        with open(os.path.join(file_path,'label',"{}.txt".format(name)),'w') as f :
            f.write(label)
write_label(file_path,dir1,label1) 
write_label(file_path,dir2,label2)







