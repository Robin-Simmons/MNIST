# MNIST
I'm trying to bring a trained MNIST network into "the real world". That involves building a network, training it, and then finding a way to get raw image data to look like MNIST data.
## Part 1: "Solving" MNIST
The smart way to solve MNIST is by using tensorflow. However this project isn't about simplicity, so I wrote it in numpy, using tensorflow only to download and extract the images.

### No Hidden Layers
My first attempt used sigmoid functions on every layer, with 2 hidden layers, and a quadratic cost function. I did this as these are all functions that seemed "simple" to differentiate and use. However even with multiple different layer sizes tested, an accuracy of more than 30% was not achieved. So I moved to softmax and cross entropy, which I had been avoiding. This worked instantly, was actually much easier, and even with no hidden layers accuracy of 80% was possible. Compared to an identical tensorflow network, the training of the network was much slower, approximately 10 times, and accuracy was lower. The tensorflow network achieved a best of 92%. Evaluation of the network was similar, tensorflow marginally beating when hundreds of images were evaluated. 

### TODO Boosting the Accuracy
Convolution seems like a good route. However finding the discrepancy between my network and the tensorflow one is most important aims. 

## Part 2: Finding possible numbers in an image
While a neural net could be trained to find regions in an image likely to be numbers before passing them off to a categoriser, this would require a huge set of training data of many images and huge amounts of training. Instead, it is much simpler to use image processing and cluster analysis. 
### Method 1: Scipy ndimage.label
Processing is done to increase the contrast and turn the RGB image into a binary one. Then scipy's ndimage.label assigns labels to objects that are made of overlapping matrices of the form

[[0,1,0],

 [1,1,1],
 
 [0,1,0]].
 
The labels are then passed to ndimage.find_objects which returns x and y slices that frame the object. The slices are converted to arrays and then given some padding space on all sides (assuming the parent image is large enough), to better fit the MNIST image style. The arrays are used to slice the image into a collection of subimages, all containing possibile number candiadates. It is simple to test the effectiveness of the scripy by asking it to draw boundries around every sub image. 

![Semi-sucessful number recognition](https://i.postimg.cc/SsJBwTj1/numbers-Found.png)
While all numbers were recognised, 3 were sliced too small. 

![Semi-sucessful number recognition 2](https://i.postimg.cc/902BGz3P/image.png)
Same problem as above.

![image.png](https://i.postimg.cc/gk8nC4Z0/image.png)=
Same image as above, but showing the method with overlapping subimages allowed and the displayed image being the binary mask rather than the raw image. 

Finding the bounding union of these subsets would get the desired results.
