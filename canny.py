import cv2  # 读取是BGR格式
import matplotlib.pyplot as plt
import numpy as np

'''
Canny边缘检测
1）使用高斯滤波器，平滑图像，消除噪音
2）计算图像中每个像素点的梯度强度和方向（用Sobel算子）
3）应用非极大值抑制，消除边缘检测带来的杂散相应
4）应用双阈值检测来确定真实的和潜在的边缘
5）通过抑制孤立的弱边缘最终完成边缘检测
'''