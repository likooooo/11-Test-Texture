'''
Description: 
Version: 1.0
Autor: like
Date: 2022-06-08 09:31:06
LastEditors: like
LastEditTime: 2022-06-08 17:10:52
'''
# import numpy as np
# import cv2 as cv
# import matplotlib.pyplot as plt
# # 1 读取图像
# img = cv.imread('1.png',0)
# cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # 2 显示图像
# # 2.1 利用opencv展示图像
# cv.imshow('image',img)
# cv.waitKey(0)
# # 2.2 在matplotplotlib中展示图像
# plt.imshow(img[:,:,::-1])
# plt.title('匹配结果'), plt.xticks([]), plt.yticks([])
# plt.show()
# k = cv.waitKey(0)
# # 3 保存图像
# cv.imwrite('messigray.png',img)

import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
def FindAngle(img):
    centerx = img.shape[1]/2
    centery = img.shape[0]/2
    for deg in range(0, 180):
        rad = math.pi * deg / 180
        # for col in range()
def fft(img):
    imgFloat32 = np.float32(img)  # 将图像转换成 float32
    dft = cv2.dft(imgFloat32, flags=cv2.DFT_COMPLEX_OUTPUT)  # 傅里叶变换
    dftShift = np.fft.fftshift(dft)  # 将低频分量移动到频域图像的中心
    
    # 幅度谱
    # ampSpe = np.sqrt(np.power(dft[:,:,0], 2) + np.power(dftShift[:,:,1], 2))
    dftAmp = cv2.magnitude(dft[:,:,0], dft[:,:,1])  # 幅度谱，未中心化
    dftShiftAmp = cv2.magnitude(dftShift[:,:,0], dftShift[:,:,1])  # 幅度谱，中心化
    dftAmpLog = np.log(1 + dftShiftAmp)  # 幅度谱对数变换，以便于显示
    # 相位谱
    phase = np.arctan2(dftShift[:,:,1], dftShift[:,:,0])  # 计算相位角(弧度制)
    dftPhi = phase / np.pi*180  # 将相位角转换为 [-180, 180]
    
    print("dftMag max={}, min={}".format(dftAmp.max(), dftAmp.min()))
    print("dftPhi max={}, min={}".format(dftPhi.max(), dftPhi.min()))
    print("dftAmpLog max={}, min={}".format(dftAmpLog.max(), dftAmpLog.min()))
    
    # cv2.idft 实现图像的逆傅里叶变换
    invShift = np.fft.ifftshift(dftShift)  # 将低频逆转换回图像四角
    imgIdft = cv2.idft(invShift)  # 逆傅里叶变换
    imgRebuild = cv2.magnitude(imgIdft[:,:,0], imgIdft[:,:,1])  # 重建图像
    
    plt.figure(figsize=(9, 6))
    plt.subplot(231), plt.title("Original image"), plt.axis('off')
    plt.imshow(img, cmap='gray')
    plt.subplot(232), plt.title("DFT Phase"), plt.axis('off')
    plt.imshow(dftPhi, cmap='gray')
    plt.subplot(233), plt.title("Rebuild image with IDFT"), plt.axis('off')
    plt.imshow(imgRebuild, cmap='gray')
    plt.subplot(234), plt.title("DFT amplitude spectrum"), plt.axis('off')
    plt.imshow(dftAmp, cmap='gray')
    plt.subplot(235), plt.title("DFT-shift amplitude"), plt.axis('off')
    plt.imshow(dftShiftAmp, cmap='gray')
    plt.subplot(236), plt.title("Log-trans of DFT amp"), plt.axis('off')
    plt.imshow(dftAmpLog, cmap='gray')
    plt.tight_layout()
    plt.show()

def GetContour(index):
    # Read the original image
    img = cv2.imread(("%d.png") % (index)) 
    # Display original image
    cv2.imshow('Original', img)
    # cv2.waitKey(0)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fft(img_gray)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

    # Sobel Edge Detection
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
    # Display Sobel Edge Detection Images
    # cv2.imshow('Sobel X', sobelx)
    # cv2.waitKey(0)
    # cv2.imshow('Sobel Y', sobely)
    # cv2.waitKey(0)
    # cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
    # cv2.waitKey(0)

    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
    # Display Canny Edge Detection Image
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)

    # cv2.destroyAllWindows()

for i in range(1, 21):
    GetContour(i)