import numpy as np
from PIL import Image
from numpy import asarray
from matplotlib import pyplot

image=Image.open("imgs/3264.jpg")
data=asarray(image)
print("data array size:",data.shape)
print(data[1:10,1:10,1])

image2=Image.formarray(data[:,:,1])
print(image2.mode)
print(image2.size)
image2.save("outP1.jpg")
pyplot.imshow(image2)
pyplot.show()