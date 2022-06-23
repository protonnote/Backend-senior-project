import shutil
from os import listdir
from os.path import join
import numpy as np
import os


def move(Result_name):
    Imgpath = "upload/"
    testImg = [Imgpath + f for f in listdir(Imgpath)]
    if len(testImg) == 1 :
        imagePath = testImg[0]
        split_file = imagePath.split("/")
        shutil.move( imagePath ,"face-recognition-using-opencv/dataset/" + Result_name.lower()+ "/" + split_file[1])
    # print(imagePath)

def move_if_no():
    Imgpath = "upload/"
    testImg = [Imgpath + f for f in listdir(Imgpath)]
    if len(testImg) == 1 :
        imagePath = testImg[0]
        split_file = imagePath.split("/")
        shutil.move( imagePath ,"face-recognition-using-opencv/other_dataset/" + split_file[1])
