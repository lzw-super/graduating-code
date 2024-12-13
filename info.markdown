## AI领域论文 
- baseline（基准模型，往往来源于顶刊） + 模块（来源不明）    


## 查论文 
- letpub、 知网、 web of science、 ccf、 

## pytorch 用法 
### 数据 
- dataset （加载数据及其标签）  dataloader（传入数据到模型 batch ） 
- Conv2d卷积层的参数 输入输出channels就照着模型图写入即可 而padding、stride、dialation（没说明一般默认为1）则需要用公式来算  [pytorch文档](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html#torch.nn.Conv2d)   
- 选择合适的损失函数，以及合适的优化函数用以反向传播来更新模型参数（常见有梯度下降） 
- 


## python info 
- dir() 打开工具箱找工具  and help() 看工具箱的使用说明 
- 当dir后只有__name__ 则表明这个就是一个小工具了，而不是更小的工具箱 
- help 中工具或工具箱不需要带括号 带括号表示执行函数（工具）  
- 延注意多看官方文档以及输入输出要求   ，看函数需要什么样的参数，默认的不修改即可 ，非默认则需带入值 
- 卷积是为了计算减少图像的大小（融合特征）而池化更多是为了提取特征（从而舍去部分小特征）  padding层就是对输入的周围进行填充数据
- 全连接层即torch中的linear层，相当于将channel变化从 in --> out  
- 
  
## tensorboard 用法
### Tensorboard常用的四个功能 ：
- graphs： 保存网络结构图；
- scalars： 精确度，学习率，损失曲线；
- histograms： 训练权重分布；
- images： 展示图像信息。 

