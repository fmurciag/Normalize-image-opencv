import cv2
import numpy as np

# Load an image
imgName='pargo.jpg'
img = cv2.imread(imgName)

#get the image size for matrix creation
height = img.shape[0]
width = img.shape[1]
norm=np.zeros((height,width,3),np.float32)
norm_rgb=np.zeros((height,width,3),np.uint8)

#get the channels
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]

#sum the channels
sum=b+g+r

#aply the equation (chanel/sum*255)
norm[:,:,0]=b/sum*255
norm[:,:,1]=g/sum*255
norm[:,:,2]=r/sum*255

#convert to uint8
norm_rgb=cv2.convertScaleAbs(norm)

#save the image
cv2.imwrite('norm_'+imgName,norm_rgb)