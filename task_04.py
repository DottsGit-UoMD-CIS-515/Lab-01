import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('images\Yellow_trafic_sign.png') # The incorrect spelling took me a while to figure out

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range of yellow color in HSV
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# Create a mask
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Bitwise-AND mask and original image
result = cv2.bitwise_and(image, image, mask=mask)

# Display the original image, mask, and result
plt.figure(figsize=(15,5))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(132)
plt.imshow(mask, cmap='gray')
plt.title('Mask')

plt.subplot(133)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title('Segmentation Result')

plt.show()