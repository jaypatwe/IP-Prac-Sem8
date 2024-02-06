import cv2
import numpy as np
import matplotlib.pyplot as plt

def contrast_stretching(image):
    min_intensity = np.min(image)
    max_intensity = np.max(image)
    stretched_image = 255 * (image - min_intensity) / (max_intensity - min_intensity)
    return stretched_image.astype(np.uint8)

def intensity_level_slicing(image, lower_threshold, upper_threshold):
    sliced_image = np.copy(image)
    sliced_image[(image >= lower_threshold) & (image <= upper_threshold)] = 255
    sliced_image[(image < lower_threshold) | (image > upper_threshold)] = 0
    return sliced_image.astype(np.uint8)

# Read the image
image = cv2.imread(r"C:\Users\jayda\OneDrive\Desktop\IP Practical\3\sample.jpg", cv2.IMREAD_GRAYSCALE)

# Perform contrast stretching
stretched_image = contrast_stretching(image)

# Perform intensity level slicing
lower_threshold = 100
upper_threshold = 200
sliced_image = intensity_level_slicing(image, lower_threshold, upper_threshold)

# Display the original image
plt.subplot(2, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")

# Display the histogram of the original image
plt.subplot(2, 3, 2)
plt.hist(image.flatten(), 256, [0, 256], color='r')
plt.title("Histogram - Original Image")

# Display the contrast-stretched image
plt.subplot(2, 3, 4)
plt.imshow(stretched_image, cmap="gray")
plt.title("Contrast Stretched Image")

# Display the histogram of the stretched image
plt.subplot(2, 3, 5)
plt.hist(stretched_image.flatten(), 256, [0, 256], color='r')
plt.title("Histogram - Stretched Image")

# Display the intensity level sliced image
plt.subplot(2, 3, 6)
plt.imshow(sliced_image, cmap="gray")
plt.title("Intensity Level Sliced Image")

# Show the plots
plt.show()
