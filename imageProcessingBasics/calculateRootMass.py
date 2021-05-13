"""
 * Python program to determine root mass, as a ratio of pixels in the
 * root system to the number of pixels in the entire image.
 *
 * usage: python RootMass.py <filename> <sigma>
"""

import sys
import numpy as np
import skimage.io
import skimage.filters

# Get file name and sigma from the command line
fileName = sys.argv[1]
sigma = float(sys.argv[2])

# Read the original image, converting to grayscale
image = skimage.io.imread(fname=fileName, as_gray=True)

# Apply blur to image
blur = skimage.filters.gaussian(image, sigma=sigma)

# Apply binary threshold to remove labels and size markers
blur[blur > 0.95] = 0

# Use Otsu's method of adaptive thresholding to define mask
# then apply
binary = blur > skimage.filters.threshold_otsu(blur)

### Save mask in case want to examine
# Find index of the dot before the file extension
iDot = fileName.rindex('.')

# Add "_mask" after original file name before the extension
binaryFileName = fileName[:iDot] + "_binary" + fileName[iDot:]

# Save the mask using skimage.img_as_ubyte() to convert from binary
# to grayscale, which is needed if want to save as png
skimage.io.imsave(fname=binaryFileName, arr=skimage.img_as_ubyte(binary))
###

### Determine the root mass ratio
# Count the number of nonzero pixels in image
rootPixels = np.count_nonzero(binary)

# Determine the width and height of the image
w = binary.shape[1]
h = binary.shape[0]

# Calculate the density of white pixels
density = float(rootPixels)/(w*h)

# Output in csv format
print(fileName, density, sep=",")
###
