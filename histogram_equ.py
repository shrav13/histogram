import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('histoequal2.jpg',0)
width=img.shape[0]
height=img.shape[1]
tp=width*height

final_img=np.zeros((width,height),dtype=np.int)     # Histogram of Original Image
hist,bins = np.histogram([img],256,[0,256])
plt.hist(img.flatten(),256,[0,256], color = 'g')
plt.xlim([0,256])
plt.show()
n=256


print 'Size : ' , width ,' X', height
freq=np.zeros((n),dtype=np.int)
cum=np.zeros((n),dtype=np.float)
hist=np.zeros((n),dtype=np.float)
mult=np.zeros((n),dtype=np.int)
div=np.zeros((n),dtype=np.float)

for i in range(n):
	freq[i]=0
	
for i in range(width):
	for j in range(height):
		freq[img[i,j]]=freq[img[i,j]]+1
		
cum[0]=freq[0]	
for i in range(1,n-1):
	cum[i]=cum[i-1]+freq[i]
	

for i in range(n):
	div[i]=cum[i]/float(tp)
	mult[i]=div[i]*255
	
for i in range(width):
	for j in range(height):
		final_img[i,j]=int(mult[img[i,j]])
	
cv2.imwrite('18.png',final_img)
hist1,bins = np.histogram([final_img],256,[0,256])      # Histogram of Final Image
plt.hist(final_img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.show()

res=np.hstack((img,final_img))
cv2.imwrite('result.png',res)
