# MNIST
The project objective is to be able to recognise all well spaced numbers from a well lit and framed image of a page, with 90%+ total accuracy.


## Part 1: Finding possible numbers in an image
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

### Method 2: Centre of mass
