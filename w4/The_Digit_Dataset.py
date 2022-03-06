# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

from sklearn import datasets

import matplotlib.pyplot as plt # matplotlib for visualize this data

# Load the digits dataset
digits = datasets.load_digits()
print(len(digits.images))
# Display the last digit
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[5], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()

# This algorithm try to generate the most similar image using the data set.

#Source:https://scikit-learn.org/stable/auto_examples/datasets/plot_digits_last_image.html#sphx-glr-auto-examples-datasets-plot-digits-last-image-py