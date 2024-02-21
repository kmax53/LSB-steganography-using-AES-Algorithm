import cv2
import matplotlib.pyplot as plt

# Load the original and stegano images
original_image = cv2.imread('c.png')
stegano_image = cv2.imread('c1.png')

# Split the images into their respective channels
original_channels = cv2.split(original_image)
stegano_channels = cv2.split(stegano_image)

# Define the colors for the channels
colors = ('b', 'g', 'r')

# Plot the histograms for the original image
plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.title('Original Image Histogram')
plt.xlabel('Pixel Values')
plt.ylabel('Number of Pixels')

for i, channel in enumerate(original_channels):
    hist = cv2.calcHist([channel], [0], None, [128], [0, 128])
    plt.plot(hist, color=colors[i], label=f'Channel {i}')
    plt.xlim([0, 128])

plt.legend()

# Plot the histograms for the stegano image
plt.subplot(122)
plt.title('Stegano Image Histogram')
plt.xlabel('Pixel Values')
plt.ylabel('Number of Pixels')

for i, channel in enumerate(stegano_channels):
    hist = cv2.calcHist([channel], [0], None, [128], [0, 128])
    plt.plot(hist, color=colors[i], label=f'Channel {i}')
    plt.xlim([0, 128])

plt.legend()
plt.show()