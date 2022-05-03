# coding:utf-8
# @Author     : HT
# @Time       : 2022/3/4 15:05
# @File       : rgb_depth_match.py
# @Software   : PyCharm
import os
import cv2

rgb_path='../recordData/RGBD_bk_7/rgb'
depth_path='../recordData/RGBD_bk_7/depth'
# rgb_path='RGBD_m_6/rgb'
# depth_path='RGBD_m_6/depth'
# rgb_path='../RGBD_bk_5/rgb'
# depth_path='../RGBD_bk_5/depth'
rgb_list=os.listdir(rgb_path)
depth_list=os.listdir(depth_path)
constant_num=0.579746
# constant_num=0.46743
# constant_num=100
fps = 30
imgInfo = (540,960)
size = (imgInfo[1],imgInfo[0])  #获取图片宽高度信息
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
videoWrite = cv2.VideoWriter('bk_7.mp4',fourcc,fps,size)# 根据图片的大小，创建写入对象 （文件名，支持的编码器，5帧，视频大小（图片大小））

def find_depth(f,list):
    depth_num=float(f.rstrip('.png'))+constant_num
    min_list=100
    match_depth='None'
    for f_depth in list:
        min_num=abs(float(f_depth.rstrip('.png'))-depth_num)
        if min_num<min_list:
            match_depth=f_depth
            min_list=min_num
    return match_depth
def find_depth_index(f,list):
    depth_num=float(f.rstrip('.png'))+constant_num
    min_list=100
    match_depth_index=0
    for i ,f_depth in enumerate(list):
        min_num=abs(float(f_depth.rstrip('.png'))-depth_num)
        if min_num<min_list:
            match_depth_index=i
            min_list=min_num
    return match_depth_index

for i,f in enumerate(rgb_list):
    f_path = rgb_path + '/' + f
    image=cv2.imread(f_path)
    # cv2.imshow('img',image)
    # cv2.waitKey(0)
    constant_num1=40
    if (i+constant_num1)<=len(depth_list) and (i-constant_num1)>=0:
        match_depth=find_depth(f, depth_list[i-constant_num1:i+constant_num1])
    elif (i+constant_num1)<=len(depth_list):
        match_depth=find_depth(f, depth_list[0:i + constant_num1])
    elif (i-constant_num1)>=0:
        match_depth=find_depth(f, depth_list[i-constant_num1:])
    else:
        print('error')
    f_depth_path = depth_path + '/' + match_depth
    image_depth = cv2.imread(f_depth_path)
    image_depth=cv2.applyColorMap(image_depth,2)
    # cv2.imshow('img_depth', image_depth)
    img_rgb_depth=cv2.add(image,image_depth)
    # cv2.imshow('img_rgb_depth', img_rgb_depth)
    # cv2.waitKey(0)
    videoWrite.write(img_rgb_depth)  # 将图片写入所创建的视频对象
    print('rgb:{},depth:{}'.format(f,match_depth))

# match_depth_index=0
# for i,f in enumerate(rgb_list):
#     f_path = rgb_path + '/' + f
#     image=cv2.imread(f_path)
#     cv2.imshow('img',image)
#     # cv2.waitKey(0)
#     constant_num1=40
#     if i==0:
#         match_depth_index=find_depth_index(f, depth_list[0:i + constant_num1])
#     f_depth_path = depth_path + '/' + depth_list[match_depth_index+i]
#     image_depth = cv2.imread(f_depth_path)
#     image_depth=cv2.applyColorMap(image_depth,2)
#     cv2.imshow('img_depth', image_depth)
#     img_rgb_depth=cv2.add(image,image_depth)
#     cv2.imshow('img_rgb_depth', img_rgb_depth)
#     cv2.waitKey(0)
#     print('rgb:{},depth:{}'.format(f,match_depth_index))