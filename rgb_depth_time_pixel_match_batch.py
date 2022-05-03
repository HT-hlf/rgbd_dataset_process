# coding:utf-8
# @Author     : HT
# @Time       : 2022/3/4 15:05
# @File       : rgb_depth_match.py
# @Software   : PyCharm
import os
import cv2
import numpy as np

def creat_dir(out_dir):
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)


raw_root_path='../recordData'
process_root_path='../recordData_process'
raw_root_list=os.listdir(raw_root_path)
fps = 30
imgInfo = (1064, 1550)
size = (imgInfo[1], imgInfo[0])  # 获取图片宽高度信息
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_path = os.path.join(process_root_path, 'video')
creat_dir(video_path)
# video_name_depth_sum= video_path+'/'+'sum.mp4'
# videoWrite_1 = cv2.VideoWriter(video_name_depth_sum, fourcc, fps, size)  # 根据图片的大小，创建写入对象 （文件名，支持的编码器，5帧，视频大小（图片大小））

count=0
inter=18
for raw_root_element in raw_root_list:
    fps = 300
    imgInfo = (1064, 1550)
    size = (imgInfo[1], imgInfo[0])  # 获取图片宽高度信息
    # fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_path = os.path.join(process_root_path, raw_root_element, 'video')
    creat_dir(video_path)
    video_name_depth= video_path+'/'+raw_root_element+'.mp4'
    # videoWrite = cv2.VideoWriter(video_name_depth, fourcc, fps, size)  # 根据图片的大小，创建写入对象 （文件名，支持的编码器，5帧，视频大小（图片大小））

    rgb_path=os.path.join(raw_root_path,raw_root_element,'rgb')
    depth_path=os.path.join(raw_root_path,raw_root_element,'depth')
    process_rgb_path = os.path.join(process_root_path, raw_root_element, 'rgb')
    creat_dir(process_rgb_path)
    process_annotation_path = os.path.join(process_root_path, raw_root_element, 'annotation')
    creat_dir(process_annotation_path)
    process_depth_path = os.path.join(process_root_path, raw_root_element, 'depth')
    creat_dir(process_depth_path)
    process_depth_rgb_path = os.path.join(process_root_path, raw_root_element, 'rgb_depth')
    creat_dir(process_depth_rgb_path)
    # rgb_path='RGBD_m_6/rgb'
    # depth_path='RGBD_m_6/depth'
    # rgb_path='../RGBD_bk_7/rgb'
    # depth_path='../RGBD_bk_7/depth'
    rgb_list=os.listdir(rgb_path)
    depth_list=os.listdir(depth_path)
    constant_num=0.579746
    constant_pixel_bottom=8
    constant_pixel_left=5
    constant_rgb_depth_left=90
    constant_rgb_depth_right=90
    # constant_num=0.46743
    # constant_num=100
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
    # count=True
    for i,f in enumerate(rgb_list):
        f_path = rgb_path + '/' + f
        process_rgb_path_jpg=process_rgb_path+ '/' + raw_root_element+'_'+str(i)+'.jpg'
        process_depth_path_jpg = process_depth_path + '/' + raw_root_element+'_'+ str(i) + '.jpg'
        process_depth_rgb_path_jpg = process_depth_rgb_path + '/' + raw_root_element+'_'+ str(i) + '.jpg'
        image=cv2.imread(f_path)
        image = image[constant_pixel_bottom:540, constant_rgb_depth_left:960-constant_pixel_left-constant_rgb_depth_right]
        # cv2.imwrite(process_rgb_path_jpg,image)
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
        image_depth_gray=image_depth=image_depth[0:540-constant_pixel_bottom,constant_pixel_left+constant_rgb_depth_left:960-constant_rgb_depth_right]
        # cv2.imshow('img_depth', image_depth)
        image_depth_one_chan=image_depth[:,:,0]
        # print(image_depth_one_chan.shape)
        # cv2.imshow('img_depth_one_chan', image_depth_one_chan)
        # cv2.imwrite(process_depth_path_jpg, image_depth_one_chan)
        # print(image_depth.shape)
        image_depth=cv2.applyColorMap(image_depth,2)
        # cv2.imshow('img_depth', image_depth)
        img_rgb_depth=cv2.add(image,image_depth)
        # cv2.imwrite(process_depth_rgb_path_jpg, img_rgb_depth)
        img2_1 = np.hstack((image, image_depth_gray))
        img2_2 = np.hstack((image_depth, img_rgb_depth))
        img4 =np.vstack((img2_1 , img2_2))
        # if count%inter==0:
        #     videoWrite_1.write(img4)  # 将图片写入所创建的视频对象
        # count+=1
        # videoWrite.write(img4)  # 将图片写入所创建的视频对象
        print(img_rgb_depth.shape)
        # cv2.imshow('img2', img4)
        # cv2.waitKey(1)
        # cv2.imshow('img_rgb_depth', img_rgb_depth)
        # cv2.waitKey(1)
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