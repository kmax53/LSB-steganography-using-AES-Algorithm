#import necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

#using opencv to read an image
#BGR Image
image = cv2.imread("87705.jpg")

#seperating colour channels
B = image[:,:,0] #blue layer
G = image[:,:,1] #green layer
R = image[:,:,2] #red layer

#calculating histograms for each channel
B_histo = cv2.calcHist([image],[0], None, [256], [0,256])
G_histo = cv2.calcHist([image],[1], None, [256], [0,256])
R_histo = cv2.calcHist([image],[2], None, [256], [0,256])

#visualizing histograms
plt.subplot(2, 2, 1)
plt.plot(B_histo, 'b')
plt.title('Blue Channel Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.subplot(2, 2, 2)
plt.plot(G_histo, 'g')
plt.title('Green Channel Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.subplot(2, 2, 3)
plt.plot(R_histo, 'r')
plt.title('Red Channel Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

#visualizing image
cv2.namedWindow("BGR Image", cv2.WINDOW_NORMAL);
cv2.imshow("BGR Image",image);
cv2.waitKey(0) & 0xFF 
cv2.destroyAllWindows()