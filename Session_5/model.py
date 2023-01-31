import matplotlib.pyplot as plt

from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR,OneCycleLR
import torch.nn.functional as F

dropout_value = 0.1
num_groups = 2


class Net(nn.Module):
    def __init__(self, norm_type='batch'):
        super(Net, self).__init__()

        self.norm_type = norm_type

        self.conv_block1 = self.conv_block(in_channels=1, out_channels=8, kernel_size=(3, 3), padding=0, bias=False, output_size=26)  # (28, 28, 1) --> (26, 26, 8)
        self.conv_block2 = self.conv_block(in_channels=8, out_channels=16, kernel_size=(3, 3), padding=0, bias=False, output_size=24) # (26, 26, 8) --> (24, 24, 16)

        # TRANSITION BLOCK 1
        self.transitionblock = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=10, kernel_size=(1, 1), padding=0, bias=False)) # (24, 24, 16) --> (24, 24, 10)
        self.pool1 = nn.MaxPool2d(2, 2) # (24, 24, 10) --> (12, 12, 10)

        self.conv_block3 = self.conv_block(in_channels=10, out_channels=8, kernel_size=(3, 3), padding=0, bias=False, output_size=10) # (12, 12, 10) --> (10, 10, 8)
        self.conv_block4 = self.conv_block(in_channels=8, out_channels=8, kernel_size=(3, 3), padding=0, bias=False, output_size=8) # (10, 10, 8) --> (8, 8, 8)
        self.conv_block5 = self.conv_block(in_channels=8, out_channels=8, kernel_size=(3, 3), padding=0, bias=False, output_size=6) # (8, 8, 8) --> (6, 6, 8)
        self.conv_block6 = self.conv_block(in_channels=8, out_channels=8, kernel_size=(3, 3), padding=1, bias=False, output_size=6) # (6, 6, 8) --> (6, 6, 8)
        
        # OUTPUT BLOCK
        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=6)) #  (6, 6, 8) --> (1, 1, 8)

        self.convblockoutput = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=10, kernel_size=(1, 1), padding=0, bias=False)) # (1, 1, 8) --> (1, 1, 10) 

        self.dropout = nn.Dropout(dropout_value)

    def conv_block(self, in_channels, out_channels, kernel_size, padding, bias, output_size=None):
      
      if self.norm_type == 'batch':
        return nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel_size, padding=padding, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(out_channels),
            nn.Dropout(dropout_value)
        ) 
      elif self.norm_type == 'layer':
        return nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel_size, padding=padding, bias=False),
            nn.ReLU(),
            nn.LayerNorm([out_channels, output_size, output_size]),
            nn.Dropout(dropout_value)
        )
      elif self.norm_type == 'group':
        return nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel_size, padding=padding, bias=False),
            nn.ReLU(),
            nn.GroupNorm(num_groups, out_channels),
            nn.Dropout(dropout_value)
        )

    def forward(self, x):
        x = self.conv_block1(x)
        x = self.conv_block2(x)
        x = self.transitionblock(x)
        x = self.pool1(x)

        x = self.conv_block3(x)
        x = self.conv_block4(x)
        x = self.conv_block5(x)
        x = self.conv_block6(x)
       
        x = self.gap(x)        
        x = self.convblockoutput(x)

        x = x.view(-1, 10)
        return F.log_softmax(x, dim=-1)
        
