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


raw_root_path='../recordData_process_annotation'
raw_root_list=os.listdir(raw_root_path)

for raw_root_element in raw_root_list:

    rgb_path=os.path.join(raw_root_path,raw_root_element,'rgb')
    depth_path=os.path.join(raw_root_path,raw_root_element,'depth')
    depth_rgb_path = os.path.join(raw_root_path, raw_root_element, 'rgb_depth')
    annotation_path = os.path.join(raw_root_path, raw_root_element, 'annotation')
    print(annotation_path)
    # annotation_list = os.listdir(annotation_path)
    rgb_list = os.listdir(rgb_path)
    depth_list = os.listdir(depth_path)
    depth_rgb_list = os.listdir(depth_rgb_path)

    for element in rgb_list:
        filename_jpg = annotation_path + '/' + element.rstrip('jpg') + 'xml'
        print(filename_jpg)
        if not os.path.exists(filename_jpg):
            print('no xml:', element)
            os.remove(rgb_path + '/' + element)

    for element in depth_list:
        filename_jpg = annotation_path + '/' + element.rstrip('jpg') + 'xml'
        print(filename_jpg)
        if not os.path.exists(filename_jpg):
            print('no xml:', element)
            os.remove(depth_path + '/' + element)

    for element in depth_rgb_list:
        filename_jpg = annotation_path + '/' + element.rstrip('jpg') + 'xml'
        if not os.path.exists(filename_jpg):
            print('no xml:', element)
            os.remove(depth_rgb_path + '/' + element)


