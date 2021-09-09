import cv2
from matplotlib import pyplot as plt
import function as fun

img = cv2.imread('img2.jpeg')
img1 = cv2.imread('img4.jpeg')
img2 = cv2.imread('img5.jpeg')

prob1 = 0.05

noisy_img = fun.sp_noise(img, prob1)
noisy_img1 = fun.sp_noise(img1, prob1)
noisy_img2 = fun.sp_noise(img2, prob1)

median = fun.reduce_noise(noisy_img, prob1)
median1 = fun.reduce_noise(noisy_img1, prob1)
median2 = fun.reduce_noise(noisy_img2, prob1)

result = fun.colorShapes(median)
result1 = fun.colorShapes(median1)
result2 = fun.colorShapes(median2)

plt.subplot(131)
plt.title('input')
plt.imshow(img[:, :, ::-1])
plt.xticks([])
plt.yticks([])

plt.subplot(132)
plt.title('input')
plt.imshow(noisy_img)
plt.xticks([])
plt.yticks([])

plt.subplot(133)
plt.title('filltered result')
plt.imshow(result)
plt.xticks([])
plt.yticks([])

plt.show()

plt.subplot(131)
plt.title('input')
plt.imshow(img1[:, :, ::-1])
plt.xticks([])
plt.yticks([])

plt.subplot(132)
plt.title('input')
plt.imshow(noisy_img1)
plt.xticks([])
plt.yticks([])

plt.subplot(133)
plt.title('filltered result')
plt.imshow(result1)
plt.xticks([])
plt.yticks([])

plt.show()

plt.subplot(131)
plt.title('input')
plt.imshow(img2[:, :, ::-1])
plt.xticks([])
plt.yticks([])

plt.subplot(132)
plt.title('input')
plt.imshow(noisy_img2)
plt.xticks([])
plt.yticks([])

plt.subplot(133)
plt.title('filltered result')
plt.imshow(result2)
plt.xticks([])
plt.yticks([])

plt.show()





