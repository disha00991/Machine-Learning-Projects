import numpy as np
from matplotlib import pyplot as plt

from TreeClassifier import question_4, question_5
from LinearModels import question_9, question_10
from NeuralNetwork import prediction_loss, prediction_grad

stuff=np.load("../report_src/data.npz")
X_trn = stuff["X_trn"]
y_trn = stuff["y_trn"]
X_tst = stuff["X_tst"]

def show(x):
    img = x.reshape((3,32,32)).transpose(1,2,0)
    plt.imshow(img)
    plt.axis('off')
    plt.draw()
    plt.pause(10)

####Q:4 Train 6 different classification trees on the image data, with each of the following maximum depths
####{1,3,6,9,12,14}
####use 5-fold cross validation
# question_4(X_trn, y_trn, X_tst)

####Q:5 Use best depth in above question to predict results for test data and uplaod to kaggle
####best depth above is 6
# question_5(X_trn, y_trn, X_tst)

###Q:9 For both hinge loss and logistic loss, train linear models with ridge regularization
###train the model and estimate the mean out of sample loss/error using 5-fold cross-validation
###l = {.0001,.001,1,10,100}
# question_9(X_trn, y_trn, X_tst)

#### Q:10 Choose the training loss and \lambda that you think will perform best
#### Make predictions for the test data
####best lambda above: , best training loss estimator: 
# question_10(X_trn, y_trn, X_tst)

#### Q:11 Write a function to evaluate the neural network and loss
###prediction_loss(x,y,W,V,b,c) function in NeuralNetwork.py

#### Q:12 Write a function to evaluate the gradient of the neural network
###prediction_grad(x,y,W,V,b,c) function in NeuralNetwork.py

# #### Q:13 Compute gradient wrt W,v,b,c using q:12
# x = np.array([1, 2])
# y=1
# W=np.array([[0.5,-1], [-0.5, 1], [1, 0.5]])
# V=np.array([[-1,-1, 1], [1, 1, 1]])
# b=np.array([0, 0, 0])
# c=np.array([0, 0])
# dLdW, dLdV, dLdb, dLdc = prediction_grad(x,y,W,V,b,c)
# print(f"dLdW, dLdV, dLdb, dLdc: {dLdW}, {dLdV}, {dLdb}, {dLdc}")

#### Q:14 Write a function to evaluate the same gradient as in Question 12 using the autograd toolbox
#### Make predictions for the test data
####best lambda above: , best training loss estimator: 
# question_14()




