import cv2
import numpy as np

img = cv2.imread('original.png')

#setting the array result
resultimage = np.zeros((800, 800))

#normalizing exposeing the image
normalizedimage = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

cv2.imwrite('normalize.png', normalizedimage)


cv2.waitKey(0)
cv2.destroyAllWindows()