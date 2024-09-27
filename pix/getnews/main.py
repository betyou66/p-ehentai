from datetime import datetime
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset,DataLoader
from matplotlib import pyplot as plt
import numpy as np
import math
import base64
from PIL import Image

sentences = [
    # 中文和英语的单词个数不要求相同
    # enc_input                dec_input           dec_output
    ['我 有 一 个 好 朋 友 P', 'S I have a good friend .', 'I have a good friend . E'],
    ['我 有 零 个 女 朋 友 P', 'S I have zero girl friend .', 'I have zero girl friend . E'],
    ['我 有 一 个 男 朋 友 P', 'S I have a boy friend .', 'I have a boy friend . E']
]
src_vocab = {'P': 0, '我': 1, '有': 2, '一': 3,
             '个': 4, '好': 5, '朋': 6, '友': 7, '零': 8, '女': 9, '男': 10}
d_k = d_v = 64
n_layers = 6
n_heads = 8


'''
1,定义具有一些可学习参数(或权重)的神经网络。
2,迭代输入数据集。
3,通过网络处理输入。
4,计算损失(输出距离正确多远)。
5,将渐变传播回网络参数。
6,通常使用下面给出的简单更新来更新网络的权重。
词库，向量，张量，输出层，隐藏层，输出层，线性层，激活函数，损失函数，优化器，编码层，编码块，解码层，解码块，编码器，解码器，Transformer
训练集
语言词库
语言句子长度

'''
d_model = 512
d_ff = 2048
device = "cuda:0"
src_len = 8  # （源句子的长度）enc_input max sequence length
tgt_len = 7  # dec_input(=dec_output) max sequence length
dropout = 0.1
'''
编码器
有6个块
inputs
输入一维向量
inputs_embeds
输入词嵌入
position_embeds
输入位置嵌入
self_attention
自己的注意力
注意力接受到一个X
X * WQ = Q
X * WK = K
X * WV = V
W*是线性变阵
公式
Attention(Q,K,V) = softmax(QK^T/sqrt(d_k))V
T是转置运算，转置是一种线性代数中的操作用于交换矩阵的行和列，通过QK^T转置确保QK内部维度相同从而可以相乘
Q是查询向量，K是键向量，V是值向量
d_k是键向量和查询向量的维度
softmax是一种归一化函数，用于计算注意力权重
sqrt(d_k)获得这个维度的平方根
公式得到softmax后和V相乘得到值为Z
Z1 = softmax * V
multihead_attention
多头注意力
输入X -> self_attention -> z1
得到多个z*后会将z*拼接在一起传入一个线性层 输出一个Z
add&norm
公式
layerNorm(X + mutihead_attention(X))
layernorm(X + Feed forward(x))
X是输入
mutihead_attention(X)是多头注意力
Feed forward(x)是前馈神经网络
layerNorm是一种归一化函数，用于归一化输入
X + mutihead_attention(X)是将输入和输出拼接在一起
feed forward
是一个两层的线性层
第一层使用非线性激活函数
第二层使用线性层
第二层不使用激活函数
上面的步骤进行完就可以构造成了一个encoder block
encoder block接受一个输入X(n*d)输出一个O(n*d)通过6个形成一个encoder
第一个块输入的是单词向量矩阵
从下一个块开始每一层的输入是前一层的输出
最后一个块是编码信息矩阵C
'''
'''
解码器
有6个块
解码层有两个多头注意力
第一个多头注意力采用了掩码操作
第二个没有
通过输入X获得Q,K,V
通过Q,K,V获得QK^T/sqrt(d_k)
然后使用mask矩阵每个单词之后的信息
QK^T/sqrt(d_k)按位相乘mask矩阵得到maskQK^T/sqrt(d_k)和V相乘得到输出Z
Z1只包含单词1的信息
第二个多头注意力
里面的自注意力的K,V不是使用上一个解码块的输出，而是使用编码块的编码信息矩阵C计算
根据C计算出K,V根据上一个解码块的输出计算Q，如果是第一个解码块则使用输入X计算Q
解码块最后的部分使用softmax计算注意力权重
softmax(QK^T/sqrt(d_k))V
'''
class Encoder(nn.Module):
    def __init__(self):
        super(Encoder, self).__init__()


class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout=0.1, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)#在训练期间，使用伯努利分布中的样本以概率随机将输入张量的某些元素归零。

        pe = torch.zeros(max_len, d_model,device=device)#创建一个深度为max_len，宽度为d_model的张量
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)#创建一个大小为一维的张量从0到，max_len类型为浮点数，unsqueeze增加指定位置1的维度
        div_term = torch.exp(torch.arange(#exp返回一个元素指数的新张量，创建一个0到d_model的张量步长为2的浮点数然后乘以负数字的自然对数除以d_model
            0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)#数组切片用法取维度的序列0和序列2的元素 = 张量乘以张量的正弦 使用了三角函数获取正弦对边除以斜边
        #
        pe[:, 1::2] = torch.cos(position * div_term)#数组切片用法取维度的序列1和序列2的元素 = 张量乘以张量的余弦 使用三角函数获取余弦领边除以斜边
        #
        pe = pe.unsqueeze(0).transpose(0, 1)#增加指定位置0的维度，将张量转置，序列0和序列1的元素维度交换 transpose(0,1)交换矩阵0和1的维度 将行和列互换元素变化输入的矩阵和输出的矩阵内存共享两者一起改变
        self.register_buffer('pe', pe)#定义一组参数将张量注册到模型buffers()中



    def forward(self, x):
        """
        x: [seq_len, batch_size, d_model]
        """
        x = x + self.pe[:x.size(0), :]#输入张量矩阵加切片用法张量维度的x.size(0)的元素如果是1则+张量矩阵的第一行
        return self.dropout(x)#随机将输入张量的某些元素归零。


#线性回归
#x = torch.randn(50) 
def img(d):
    im = base64.b64decode(d)
    im = np.frombuffer(im, np.uint8)
    print(im)
    
img(open("C:\dow\stable-diffusion-webui\一些小脚本\pix\server\_Phase04_001.jpg",'rb').read())
op = Image.open("C:\dow\stable-diffusion-webui\一些小脚本\pix\server\_Phase04_001.jpg")
print(op)
sw = np.array(op)
print(sw)
print(sw.shape)
print(sw.size)
#图像是三维的
#sw.shape[0]是图像的高度
#sw.shape[1]是图像的宽度
#sw.shape[2]是图像的通道数
#sw.size是图像的大小
#sw.dtype是图像的类型
#sw.ndim是图像的维度
#sw.itemsize是图像的字节数
#3d模型是4维的
'''
k近邻算法
kNN算法是一种非监督学习算法，用于寻找样本数据中最相似的样本数据，kNN算法的思想是：如果一个样本与其他样本的距离都很近，那么这个样本与其他样本的类别也很可能是近似的。
kNN算法的优点是简单，易于实现，计算代价也很低，缺点是对异常值不敏感，对数据稀疏性要求较高。
'''