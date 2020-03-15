from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import time

def softmax(x):
    soft_x = np.exp(x)/(np.sum(np.exp(x)))
    return soft_x
# Read data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

rate = 0.005
numSteps = 10000
batch_size = 100
inputDataBatch, labelsDataBatch = mnist.train.next_batch(batch_size)
testImages = mnist.test.images
testLabels = mnist.test.labels
#create network
weights = np.random.random([10,28**2]).astype(dtype = np.float32)
bias = np.zeros(10).astype(dtype = np.float32)

for j in range(numSteps):
    avgCost = 0
    
    for i in range(batch_size):
        inputData = inputDataBatch[i]
        label = labelsDataBatch[i]
        #forward prop
        output = softmax(np.matmul(weights,inputData)+bias)
        costFunction = np.sum(np.log(output)*label)
        #backward prop
        dCost = output-label
        dWeight = np.outer(dCost,inputData)
        weights = weights - dWeight*rate
        bias = bias - rate*dCost
    
    if j%100 == 0:
        numCorrect = 0
        for k in range(100):
            inputData = testImages[k+j]
            label = testLabels[k+j]
            prediction = softmax(np.matmul(weights,inputData)+bias)
            if np.argmax(prediction) == np.argmax(label):
                numCorrect += 1
        print("Percent correct: {} %".format(numCorrect))
