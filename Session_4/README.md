# Tuning CNN Models

1. **Skeleton** - Reduced the number of parameters using Convolution Blocks with less number of output channels (removed 64, 128, 256 and 512 for every layer) and removed bias
2. **Max-Pooling** - Transition Block (max pooling followed by 1x1) after 5x5 receptive field added in network.
3. **Batch-Normalization** - Added after every convolution layer except the last one to normalize the values being passed between convolution layers
4. **Capacity** - With very less paramters ~4k parameters, even with all the right concepts in place model couldnt learn. Increased capacity a bit to increase the accuracy.
5. **Global Average pooling** - GAP followed by fully connected layer (1x1 is applied on 1d data) used just before prediction to give the network a little flexibility with the input image size.
6. **Augmentation** - Image augmentation technique like image rotation, color jitter and affine transformation are used
7. **Regularization** - Adding drop out, helped reduced the gap between training and test loss.
8. **Learning Rate** - Used OneCycleLR Learning Rate to tune the model
