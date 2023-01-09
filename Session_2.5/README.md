
### Problem Statement:

Write a neural network that can take 2 inputs:
* an image from MNIST dataset and
* a random number between 0 and 9

and gives two outputs:
* the "number" that was represented by the MNIST image, and
* the "sum" of this number with the random number that was generated and sent as the input to the network

<p align="center"><img src="https://user-images.githubusercontent.com/42609155/118740404-6aee2180-b869-11eb-9a42-d72efbc4f132.png" width="600"></p>

Network can be written with fully connected layers and convolution layers. 


## Data Preparation:

The MNIST dataset is used as one of the input to the model, it contains 70,000 images of handwritten digits: 60,000 for training and 10,000 for testing. The images are grayscale, 28x28 pixels

Custom dataset is created using MNIST dataset and generates data in below format: 

|Mnist Image|Mnist Label|One hot encoded Random Number|Sum of random number and Mnist Number| 
|----|-----|------|-----|

A random integer, sum of MNIST label and the random integer along with MNIST Image and its label. 

## Model

<p align="center"><img src="https://github.com/gkdivya/EVA/blob/7b9feda284e2b2eb7342e1652f7efb5e95206e09/3_PyTorchNeuralNetwork/assets/MNIST_RandomAddition.png" width="800"></p>

* Using convolution blocks, MNIST image features are extracted 
* One hot encoded random number is concatenated with the MNIST image features, are further passed to fully connected layers to predict the sum
* MNIST features are flatten and passed to a softmax function directly to predict the MNIST number

      Network(
        (conv1): Conv2d(1, 32, kernel_size=(3, 3), stride=(1, 1))
        (conv2): Conv2d(32, 64, kernel_size=(3, 3), stride=(1, 1))
        (conv3): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1))
        (conv4): Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1))
        (conv5): Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1))
        (conv6): Conv2d(512, 1024, kernel_size=(3, 3), stride=(1, 1))
        (fc1): Linear(in_features=50176, out_features=120, bias=True)
        (fc2): Linear(in_features=120, out_features=60, bias=True)
        (fc3): Linear(in_features=10, out_features=120, bias=True)
        (fc4): Linear(in_features=120, out_features=60, bias=True)
        (out1): Linear(in_features=60, out_features=10, bias=True)
        (out2): Linear(in_features=60, out_features=19, bias=True)
        (dropout): Dropout(p=0.2, inplace=False)
      )

## Number of parameters
Model has 12,326,465 trainable parameters.


## Loss Function
Because both the MNIST classification and the sum(0-18) are multi class classification problem, we have used Negative Log-Likelihood Loss Function for each of the outputs and averaged the loss:

 Loss = (Mnist NLL Loss + Addition NLL Loss)/2

In NLL, the model is punished for making the correct prediction with smaller probabilities and encouraged for making the prediction with higher probabilities. The logarithm does the punishment. NLL does not only care about the prediction being correct but also about the model being certain about the prediction with a high score. 

The Pytorch NLL Loss is expressed as: log(x,y) = -log(y)
x represents the actual value and y the predicted value.


## Training Log

      Epoch 1 : 
      epoch: 1 , loss mnist : 4836.4594547423185, loss sum : 0.0
      Val set: Average loss: 0.138, MNIST Accuracy:95.62, Sum_Accuracy:1.2

      Epoch 2 : 
      epoch: 2 , loss mnist : 829.8254803930613, loss sum : 0.0
      Val set: Average loss: 0.106, MNIST Accuracy:96.96, Sum_Accuracy:1.18

      Epoch 3 : 
      epoch: 3 , loss mnist : 559.0599792947141, loss sum : 0.0
      Val set: Average loss: 0.023, MNIST Accuracy:98.12, Sum_Accuracy:1.3

      Epoch 4 : 
      epoch: 4 , loss mnist : 426.3578369369934, loss sum : 0.0
      Val set: Average loss: 0.018, MNIST Accuracy:98.16, Sum_Accuracy:1.14

      Epoch 5 : 
      epoch: 5 , loss mnist : 343.4942731789979, loss sum : 0.0
      Val set: Average loss: 0.014, MNIST Accuracy:98.58, Sum_Accuracy:1.0

      Epoch 6 : 
      epoch: 6 , loss mnist : 281.4830155648451, loss sum : 0.0
      Val set: Average loss: 0.001, MNIST Accuracy:98.84, Sum_Accuracy:1.12

      Epoch 7 : 
      epoch: 7 , loss mnist : 240.01546333435635, loss sum : 0.0
      Val set: Average loss: 0.001, MNIST Accuracy:98.8, Sum_Accuracy:1.1

      Epoch 8 : 
      epoch: 8 , loss mnist : 206.07607260052555, loss sum : 0.0
      Val set: Average loss: 0.001, MNIST Accuracy:98.82, Sum_Accuracy:1.0

      Epoch 9 : 
      epoch: 9 , loss mnist : 176.6826218062921, loss sum : 0.0
      Val set: Average loss: 0.001, MNIST Accuracy:99.14, Sum_Accuracy:1.16

      Epoch 10 : 
      epoch: 10 , loss mnist : 149.8762259758117, loss sum : 0.0
      Val set: Average loss: 0.000, MNIST Accuracy:99.1, Sum_Accuracy:1.06


<p align="center"><img src="https://user-images.githubusercontent.com/42609155/119095568-10eb8880-ba30-11eb-910d-f766d3a1d237.png" width="500"></p>

## Test Loss

      Test set: Average loss: 0.072, MNist Accuracy:99.27, Sum_Accuracy:99.24
      
## Inference

<p align="center">
    <img src="https://user-images.githubusercontent.com/42609155/119095810-60ca4f80-ba30-11eb-974f-e123a9e02fb3.png" width="200">
    <img src="https://user-images.githubusercontent.com/42609155/119095818-645dd680-ba30-11eb-980d-8fe1618ff0be.png" width="200">
    <img src="https://user-images.githubusercontent.com/42609155/119095826-66279a00-ba30-11eb-8720-495a8134885b.png" width="200">
    <img src="https://user-images.githubusercontent.com/42609155/119100042-2adb9a00-ba35-11eb-96a9-b3ef330a6954.png" width="200">
</p>








