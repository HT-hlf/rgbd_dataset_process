# coding:utf-8
# @Author     : HT
# @Time       : 2022/3/4 15:05
# @File       : rgb_depth_match.py
# @Software   : PyCharm
import os
import cv2
import numpy as np
import shutil
import random

# TRAIN_RATIO = 85
TRAIN_RATIO = 110
def creat_dir(out_dir):
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)


path_list=['../recordData_process_annotation','../recordData_process_annotation_daytime_aug_bright_1','../recordData_process_annotation_night_but_light_bright_1']
dist_root_path='../recordData_process_annotation_sum_new'
for path in path_list:
    raw_root_path = path
    # dist_root_path='../recordData_process_annotation_sum'
    raw_root_list=os.listdir(raw_root_path)

    for raw_root_element in raw_root_list:

        rgb_path=os.path.join(raw_root_path,raw_root_element,'rgb')
        depth_path=os.path.join(raw_root_path,raw_root_element,'depth')
        depth_rgb_path = os.path.join(raw_root_path, raw_root_element, 'rgb_depth')
        annotation_path = os.path.join(raw_root_path, raw_root_element, 'annotation')

        annotations_train_path = os.path.join(dist_root_path, 'Annotations_train')
        annotations_val_path = os.path.join(dist_root_path, 'Annotations_val')
        images_train_path = os.path.join(dist_root_path, 'JPEGImages_train')
        images_val_path = os.path.join(dist_root_path, 'JPEGImages_val')
        depth_train_path = os.path.join(dist_root_path, 'depth_train')
        depth_val_path = os.path.join(dist_root_path, 'depth_val')
        depth_rgb_train_path = os.path.join(dist_root_path, 'depth_rgb_train')
        depth_rgb_val_path = os.path.join(dist_root_path, 'depth_rgb_val')
        creat_dir(annotations_train_path)
        creat_dir(annotations_val_path)
        creat_dir(images_train_path)
        creat_dir(images_val_path)
        creat_dir(depth_train_path)
        creat_dir(depth_val_path)
        creat_dir(depth_rgb_train_path)
        creat_dir(depth_rgb_val_path)
        # print(annotation_path)
        # annotation_list = os.listdir(annotation_path)
        rgb_list = os.listdir(rgb_path)
        depth_list = os.listdir(depth_path)
        depth_rgb_list = os.listdir(depth_rgb_path)

        for element in rgb_list:
            prob = random.randint(1, 100)
            filename_rgb = rgb_path + '/' + element
            filename_annotation = annotation_path + '/' + element.rstrip('jpg') + 'xml'
            filename_depth = depth_path + '/' + element
            filename_depth_rgb = depth_rgb_path + '/' + element
            if (prob < TRAIN_RATIO):
                dist_rgb = images_train_path + '/' + element
                dist_annotation = annotations_train_path + '/' + element.rstrip('jpg')+'xml'
                dist_depth = depth_train_path + '/' + element
                dist_depth_rgb = depth_rgb_train_path + '/' + element
            else:
                dist_rgb = images_val_path + '/' + element
                dist_annotation = annotations_val_path + '/' + element.rstrip('jpg') + 'xml'
                dist_depth = depth_val_path + '/' + element
                dist_depth_rgb = depth_rgb_val_path + '/' + element

            shutil.copy(filename_rgb,dist_rgb)
            shutil.copy(filename_annotation, dist_annotation)
            shutil.copy(filename_depth, dist_depth)
            shutil.copy(filename_depth_rgb, dist_depth_rgb)

