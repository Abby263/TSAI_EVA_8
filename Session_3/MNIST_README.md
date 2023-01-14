## Experiments

Batch Size = 128 <br>
Epochs = 20


### Model Architecture

----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 8, 26, 26]              80
              ReLU-2            [-1, 8, 26, 26]               0
       BatchNorm2d-3            [-1, 8, 26, 26]              16
           Dropout-4            [-1, 8, 26, 26]               0
            Conv2d-5           [-1, 16, 24, 24]           1,168
              ReLU-6           [-1, 16, 24, 24]               0
       BatchNorm2d-7           [-1, 16, 24, 24]              32
           Dropout-8           [-1, 16, 24, 24]               0
            Conv2d-9           [-1, 32, 22, 22]           4,640
             ReLU-10           [-1, 32, 22, 22]               0
      BatchNorm2d-11           [-1, 32, 22, 22]              64
          Dropout-12           [-1, 32, 22, 22]               0
           Conv2d-13            [-1, 8, 22, 22]             264
             ReLU-14            [-1, 8, 22, 22]               0
      BatchNorm2d-15            [-1, 8, 22, 22]              16
          Dropout-16            [-1, 8, 22, 22]               0
           Conv2d-17           [-1, 16, 20, 20]           1,168
             ReLU-18           [-1, 16, 20, 20]               0
      BatchNorm2d-19           [-1, 16, 20, 20]              32
          Dropout-20           [-1, 16, 20, 20]               0
           Conv2d-21           [-1, 32, 18, 18]           4,640
             ReLU-22           [-1, 32, 18, 18]               0
      BatchNorm2d-23           [-1, 32, 18, 18]              64
          Dropout-24           [-1, 32, 18, 18]               0
        MaxPool2d-25             [-1, 32, 9, 9]               0
           Conv2d-26              [-1, 8, 9, 9]             264
             ReLU-27              [-1, 8, 9, 9]               0
      BatchNorm2d-28              [-1, 8, 9, 9]              16
          Dropout-29              [-1, 8, 9, 9]               0
           Conv2d-30             [-1, 16, 7, 7]           1,168
             ReLU-31             [-1, 16, 7, 7]               0
      BatchNorm2d-32             [-1, 16, 7, 7]              32
          Dropout-33             [-1, 16, 7, 7]               0
           Conv2d-34             [-1, 32, 5, 5]           4,640
           Linear-35                   [-1, 10]           8,010
================================================================
Total params: 26,314
Trainable params: 26,314
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 1.62
Params size (MB): 0.10
Estimated Total Size (MB): 1.72

### Training Log

    Epoch : 1
loss=0.027234604582190514 batch_id=468: 100%|██████████| 469/469 [00:18<00:00, 25.17it/s]
Test set: Average loss: 0.0768, Accuracy: 9756/10000 (97.56%)

Epoch : 2
loss=0.034358128905296326 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.09it/s]
Test set: Average loss: 0.0623, Accuracy: 9799/10000 (97.99%)

Epoch : 3
loss=0.0718812346458435 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.12it/s]
Test set: Average loss: 0.0503, Accuracy: 9818/10000 (98.18%)

Epoch : 4
loss=0.05470559000968933 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 29.51it/s]
Test set: Average loss: 0.0647, Accuracy: 9791/10000 (97.91%)

Epoch : 5
loss=0.05947612598538399 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 29.00it/s]
Test set: Average loss: 0.0506, Accuracy: 9827/10000 (98.27%)

Epoch : 6
loss=0.0058059245347976685 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 29.76it/s]
Test set: Average loss: 0.0506, Accuracy: 9830/10000 (98.30%)

Epoch : 7
loss=0.04500335454940796 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 29.98it/s]
Test set: Average loss: 0.0492, Accuracy: 9833/10000 (98.33%)

Epoch : 8
loss=0.02988850511610508 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 28.43it/s]
Test set: Average loss: 0.0516, Accuracy: 9837/10000 (98.37%)

Epoch : 9
loss=0.04712998494505882 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.04it/s]
Test set: Average loss: 0.0521, Accuracy: 9839/10000 (98.39%)

Epoch : 10
loss=0.05651883780956268 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.14it/s]
Test set: Average loss: 0.0466, Accuracy: 9845/10000 (98.45%)

Epoch : 11
loss=0.05493533983826637 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 29.96it/s]
Test set: Average loss: 0.0416, Accuracy: 9866/10000 (98.66%)

Epoch : 12
loss=0.01331122312694788 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.19it/s]
Test set: Average loss: 0.0428, Accuracy: 9862/10000 (98.62%)

Epoch : 13
loss=0.015752285718917847 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 29.84it/s]
Test set: Average loss: 0.0431, Accuracy: 9855/10000 (98.55%)

Epoch : 14
loss=0.006339320447295904 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.19it/s]
Test set: Average loss: 0.0388, Accuracy: 9881/10000 (98.81%)

Epoch : 15
loss=0.01386841107159853 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 29.30it/s]
Test set: Average loss: 0.0474, Accuracy: 9864/10000 (98.64%)

Epoch : 16
loss=0.012428586371243 batch_id=468: 100%|██████████| 469/469 [00:16<00:00, 29.28it/s]
Test set: Average loss: 0.0501, Accuracy: 9848/10000 (98.48%)

Epoch : 17
loss=0.046596262603998184 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 29.74it/s]
Test set: Average loss: 0.0365, Accuracy: 9878/10000 (98.78%)

Epoch : 18
loss=0.007671449799090624 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.18it/s]
Test set: Average loss: 0.0442, Accuracy: 9856/10000 (98.56%)

Epoch : 19
loss=0.047103866934776306 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.02it/s]
Test set: Average loss: 0.0382, Accuracy: 9883/10000 (98.83%)

