"""
`基础知识 <intro.html>`_ ||
`快速入门 <quickstart_tutorial.html>`_ ||
`张量 <tensorqs_tutorial.html>`_ ||
`数据集与数据加载器 <data_tutorial.html>`_ ||
`Transforms <transforms_tutorial.html>`_ ||
**构建神经网络** ||
`自动微分 <autogradqs_tutorial.html>`_ ||
`优化模型参数 <optimization_tutorial.html>`_ ||
`保存和加载模型 <saveloadrun_tutorial.html>`_

构建神经网络
========================

神经网络由执行数据操作的 层/模块 组成。`torch.nn <https://pytorch.org/docs/stable/nn.html>`_ 命名空间提供了构建你自己的神经网络所需的所有构建块。
PyTorch 中的每个模块都是 `nn.Module <https://pytorch.org/docs/stable/generated/torch.nn.Module.html>`_ 的子类。
神经网络本身就是一个由其他模块（层）组成的模块。这种嵌套结构允许轻松构建和管理复杂的架构。

在接下来的部分中，我们将构建一个神经网络，用于对 FashionMNIST 数据集中的图像进行分类。

"""

import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


#############################################
# 获取训练设备
# -----------------------
# 我们希望能够在硬件加速器（如 GPU 或 MPS）上训练我们的模型（如果可用）。
# 让我们检查一下 `torch.cuda <https://pytorch.org/docs/stable/notes/cuda.html>`_
# 或 `torch.backends.mps <https://pytorch.org/docs/stable/notes/mps.html>`_ 是否可用，否则我们使用 CPU。

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)
print(f"Using {device} device")

##############################################
# 定义类
# -------------------------
# 我们通过继承 ``nn.Module`` 来定义我们的神经网络，并在 ``__init__`` 方法中初始化神经网络层。
# 每个 ``nn.Module`` 子类都在 ``forward`` 方法中实现对输入数据的操作。


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

##############################################
# 我们创建一个 ``NeuralNetwork`` 的实例，并将其移动到 ``device`` 上，然后打印其结构。


model = NeuralNetwork().to(device)
print(model)


##############################################
# 要使用模型，我们将输入数据传递给它。这将执行模型的 ``forward`` 方法，
# 以及一些`后台操作 <https://github.com/pytorch/pytorch/blob/270111b7b611d174967ed204776985cefca9c144/torch/nn/modules/module.py#L866>`_。
# 不要直接调用 ``model.forward()``！
#
# 将输入传递给模型会返回一个二维张量，其中 dim=0 对应每个类别的 10 个原始预测值的输出，dim=1 对应每个输出的各个值。我们通过将其传递给 `nn.Softmax` 模块的实例来获得预测概率。

X = torch.rand(1, 28, 28, device=device)
logits = model(X)
pred_probab = nn.Softmax(dim=1)(logits)
y_pred = pred_probab.argmax(1)
print(f"Predicted class: {y_pred}")


######################################################################
# --------------
#


##############################################
# 模型层
# -------------------------
#
# 让我们分解一下 FashionMNIST 模型中的各层。为了解释它，我们将取一个包含 3 张 28x28 尺寸图像的小批量样本，
# 并观察它在通过网络时发生了什么。

input_image = torch.rand(3, 28, 28)
print(input_image.size())

##################################################
# nn.Flatten
# ^^^^^^^^^^^^^^^^^^^^^^
# 我们初始化 `nn.Flatten <https://pytorch.org/docs/stable/generated/torch.nn.Flatten.html>`_ 层，
# 将每个二维 28x28 图像转换为包含 784 个像素值的连续数组（保留小批量维度（dim=0））。

flatten = nn.Flatten()
flat_image = flatten(input_image)
print(flat_image.size())

##############################################
# nn.Linear
# ^^^^^^^^^^^^^^^^^^^^^^
# `线性层 <https://pytorch.org/docs/stable/generated/torch.nn.Linear.html>`_ 是一个模块，
# 它使用存储的权重(weights)和偏置(biases)对输入应用线性变换。
#
layer1 = nn.Linear(in_features=28*28, out_features=20)
hidden1 = layer1(flat_image)
print(hidden1.size())


#################################################
# nn.ReLU
# ^^^^^^^^^^^^^^^^^^^^^^
# 非线性激活函数创建了模型输入和输出之间的复杂映射。它们在线性变换之后应用，以引入*非线性*，
# 帮助神经网络学习各种现象。
#
# 在这个模型中，我们在线性层之间使用 `nn.ReLU <https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html>`，
# 但还有其他激活函数可以在你的模型中引入非线性。

print(f"Before ReLU: {hidden1}\n\n")
hidden1 = nn.ReLU()(hidden1)
print(f"After ReLU: {hidden1}")


#################################################
# nn.Sequential
# ^^^^^^^^^^^^^^^^^^^^^^
# `nn.Sequential <https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html>`_
# 是一个有序的模块容器。数据按照定义的顺序依次通过所有模块。您可以使用序列容器来快速组合一个网络，
# 例如 ``seq_modules``。

seq_modules = nn.Sequential(
    flatten,
    layer1,
    nn.ReLU(),
    nn.Linear(20, 10)
)
input_image = torch.rand(3, 28, 28)
logits = seq_modules(input_image)

################################################################
# nn.Softmax
# ^^^^^^^^^^^^^^^^^^^^^^
# 神经网络的最后一个线性层返回的是 [logits（对数几率）](https://en.wikipedia.org/wiki/Logit)
# - 在 [-\infty, \infty] 范围内的原始值 - 这些值会被传递到
# `nn.Softmax https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html>`_ 模块。
# 对数几率被缩放到值为 [0, 1] 的范围，表示模型对每个类别的预测概率。``dim`` 参数指示值必须在其沿着的维度上求和为 1。

softmax = nn.Softmax(dim=1)
pred_probab = softmax(logits)


#################################################
# 模型参数
# -------------------------
# 神经网络内部的许多层都是*参数化*的，即在训练过程中会优化的相关权重和偏置。
# 通过子类化 ``nn.Module``，可以自动跟踪模型对象内定义的所有字段，并使用模型的 ``parameters()``
# 或 ``named_parameters()`` 方法访问所有参数。
#
# 在这个示例中，我们遍历每个参数，并打印其大小以及值的预览。


print(f"Model structure: {model}\n\n")

for name, param in model.named_parameters():
    print(f"Layer: {name} | Size: {param.size()} | Values : {param[:2]} \n")

######################################################################
# --------------
#

#################################################################
# 延伸阅读
# -----------------
# - `torch.nn API <https://pytorch.org/docs/stable/nn.html>`_
