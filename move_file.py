import shutil
from os import listdir
from os.path import join
import numpy as np
import os
import write_log as wr

def move(Result_name):
    Imgpath = "upload/"
    testImg = [Imgpath + f for f in listdir(Imgpath)]
    if len(testImg) == 1 :
        imagePath = testImg[0]
        split_file = imagePath.split("/")
        shutil.move( imagePath ,"face-recognition-using-opencv/dataset/" + Result_name.lower()+ "/" + split_file[1])
    # print(imagePath)

def move_if_no(code):
    Imgpath = "upload/"
    testImg = [Imgpath + f for f in listdir(Imgpath)]
    flag, name = wr.read_log(code)
    if len(testImg) == 1 and flag :
        imagePath = testImg[0]
        split_file = imagePath.split("/")
        shutil.move( imagePath ,"face-recognition-using-opencv/dataset/" + name.lower()+ "/" + split_file[1])


def move_if_other():
    Imgpath = "upload/"
    testImg = [Imgpath + f for f in listdir(Imgpath)]
    if len(testImg) == 1 :

        imagePath = testImg[0]
        split_file = imagePath.split("/")
        shutil.move( imagePath ,"face-recognition-using-opencv/other_dataset/" + split_file[1])
