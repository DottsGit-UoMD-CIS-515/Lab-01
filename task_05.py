import PIL
from PIL import Image
import matplotlib.pyplot as plt

# 5.a Use PIL.Image.open to open the image file: flower.jpg and store it in an image object y1
y1 = Image.open('images/flower.jpg')

# 5.b Display y1
plt.imshow(y1)
plt.title('Original Image (y1)')
plt.show()

# 5.c Rotate y1 by 25 degree with expand = 1 and save the result as another image object y2
y2 = y1.rotate(25, expand=1)

# 5.d Display the width and height of y2
width, height = y2.size
print(f"Width of y2: {width}, Height of y2: {height}")

plt.imshow(y2)
plt.title(f"Rotated Image (y2): Width: {width}, Height: {height}")
plt.show()

# 5.e Let left, top, right, bottom = 4, height/5, width/2, 3*height/5
left, top, right, bottom = 4, height//5, width//2, 3*height//5

# 5.f use (left, top, right, bottom) to crop y1 and save the result as an image object y3
y3 = y1.crop((left, top, right, bottom))

# 5.g Display y3
plt.imshow(y3)
plt.title('Cropped Image (y3)')
plt.show()

# 5.h let newsize = (128, 128)
newsize = (128, 128)

# 5.i use newsize to resize y1 to y4
y4 = y1.resize(newsize)

# 5.j save y4 as an image file: resized_image.png
y4.save('resized_image.png')

# Display y4 to confirm the resize
plt.imshow(y4)
plt.title('Resized Image (y4)')
plt.show()