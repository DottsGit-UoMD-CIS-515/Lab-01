import cv2
import numpy as np
import matplotlib.pyplot as plt

# 2.a Read in an image file (flower.jpg) and store it in a NumPy array x1
x1 = np.array(cv2.imread('images/flower.jpg'))

# 2.b Display x1
plt.imshow(cv2.cvtColor(x1, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.show()

# 2.c Convert the NumPy array x1 to a gray image x2
x2 = np.array(cv2.cvtColor(x1, cv2.COLOR_BGR2GRAY))

# 2.d Display x2
plt.imshow(x2, cmap='gray')
plt.title('Grayscale Image')
plt.show()

# 2.e Rotate x1 clockwise by 90 degrees and save the result in x3
x3 = np.rot90(x1, k=-1)

# 2.f Display x3
plt.imshow(cv2.cvtColor(x3, cv2.COLOR_BGR2RGB))
plt.title('Rotated Image')
plt.show()

# 2.g Scale down x1 to its half size, and save the result in x4
x4 = np.array(cv2.resize(x1, (x1.shape[1]//2, x1.shape[0]//2)))

# 2.h Display x4
plt.imshow(cv2.cvtColor(x4, cv2.COLOR_BGR2RGB))
plt.title('Scaled Down Image')
plt.show()

# 2.i Crop x1 around its centroid such that the cropped window has a half of its original width and height. Save the cropped image as x5.
height, width = x1.shape[:2]
start_row, start_col = int(height * 0.25), int(width * 0.25)
end_row, end_col = int(height * 0.75), int(width * 0.75)
x5 = x1[start_row:end_row, start_col:end_col]

# 2.j Display x5
plt.imshow(cv2.cvtColor(x5, cv2.COLOR_BGR2RGB))
plt.title('Cropped Image')
plt.show()