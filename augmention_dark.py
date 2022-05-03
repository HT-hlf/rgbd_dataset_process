# coding:utf-8
# @Author     : HT
# @Time       : 2022/3/11 9:55
# @File       : augmention_dark.py
# @Software   : PyCharm
from PIL import Image
from PIL import ImageEnhance
import os
import cv2
import numpy as np
import random

def creat_dir(out_dir):
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

def brightnessEnhancement(root_path,img_name):#亮度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_bri = ImageEnhance.Brightness(image)
    brightness = random.randint(2,8)/100
    # brightness = random.randint(9, 25) / 100
    image_brightened = enh_bri.enhance(brightness)
    return image_brightened,brightness

def rename(depth_path,name,houzui=False):
    if houzui:
        old_filename = depth_path + '/' + name.rstrip('jpg') + 'xml'
        new_filename = depth_path + '/bright_1_' + name.rstrip('jpg')+'xml'
    else:
        old_filename = depth_path + '/' + name
        new_filename = depth_path + '/bright_1_' + name
    os.rename(old_filename, new_filename)
# G:\lab_collect_dataset\recordData_process_annotation_daytime
raw_root_path='../recordData_process_annotation_night_but_light_bright_1'
raw_root_list=os.listdir(raw_root_path)


for raw_root_element in raw_root_list:
    imageDir = os.path.join(raw_root_path,raw_root_element,'rgb') # 要改变的图片的路径文件夹
    saveDir = os.path.join(raw_root_path,raw_root_element,'bright_1')  # 要保存的图片的路径文件夹
    creat_dir(saveDir)
    depth_path = os.path.join(raw_root_path, raw_root_element, 'depth')
    # creat_dir(depth_path)
    depth_rgb_path = os.path.join(raw_root_path, raw_root_element, 'rgb_depth')
    # creat_dir(depth_rgb_path)
    annotation_path = os.path.join(raw_root_path, raw_root_element, 'annotation')
    # creat_dir(annotation_path)
    for name in os.listdir(imageDir):
        saveImage,brightness = brightnessEnhancement(imageDir,name)    #()前函数改成功能对应的函数名，即可使用
        saveName = "bright_1_" + name  # 保存的文件名
        saveImage.save(os.path.join(saveDir,saveName))

        rename(depth_path, name)
        rename(depth_rgb_path, name)
        rename(annotation_path, name,True)


    # i = i + 1