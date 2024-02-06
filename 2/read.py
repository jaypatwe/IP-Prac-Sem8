import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread(r"C:\Users\jayda\OneDrive\Desktop\IP Practical\2\sample.jpg", cv2.IMREAD_GRAYSCALE)

# Display the original image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")

# Display the histogram of the original image
plt.subplot(2, 2, 2)
plt.hist(image.flatten(), 256, [0, 256], color='r')
plt.title("Histogram - Original Image")

# Equalize the histogram
equalized_image = cv2.equalizeHist(image)

# Display the equalized image
plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap="gray")
plt.title("Equalized Image")

# Display the histogram of the equalized image
plt.subplot(2, 2, 4)
plt.hist(equalized_image.flatten(), 256, [0, 256], color='r')
plt.title("Histogram - Equalized Image")

# Show the plots
plt.show()
