import cv2
import numpy as np

img = cv2.imread('original.png')
height = img.shape[0]
width = img.shape[1]
norm=np.zeros((height,width,3),np.float32)
norm_rgb=np.zeros((height,width,3),np.uint8)

b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]

sum=b+g+r


norm[:,:,0]=float(b/sum*255)
norm[:,:,1]=float(g/sum*255)
norm[:,:,2]=float(r/sum*255)

norm_rgb=cv2.convertScaleAbs(norm)

cv2.imwrite('norm.png',norm_rgb)