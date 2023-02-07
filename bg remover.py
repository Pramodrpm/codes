import cv2
import numpy as np

# Load the image
img = cv2.imread("image.png")

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define range of background color in HSV
lower_bg = np.array([0, 0, 0])
upper_bg = np.array([179, 255, 30])

# Threshold the HSV image to get only background colors
mask = cv2.inRange(hsv, lower_bg, upper_bg)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img, img, mask=mask)

# Save result
cv2.imwrite("result.jpg", res)