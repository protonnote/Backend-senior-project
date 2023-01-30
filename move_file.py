import shutil
from os import listdir
from os.path import join
import numpy as np
import os
import write_log as wr

def move(Result_name):
    Imgpath = "upload/"
    testImg = [Imgpath + f for f in listdir(Imgpath)]
    if len(testImg) == 1:
        imagePath = testImg[0]
        split_file = imagePath.split("/")
        shutil.move(
            imagePath,
            f"face-recognition-using-opencv/dataset/{Result_name.lower()}/{split_file[1]}",
        )
        print("Move complete.")
    else: print("Upload is empty.!!")

def move_if_no(code : int):
    Imgpath = "upload/"
    testImg = [Imgpath + f for f in listdir(Imgpath)]
    flag, name = wr.read_log(code)
    print("validate:",flag,name)
    r_flags = False
    if len(testImg) == 1 and flag == 1:
        print(f"code {code} correct.!!")
        imagePath = testImg[0]
        split_file = imagePath.split("/")
        shutil.move(
            imagePath,
            f"face-recognition-using-opencv/dataset/{name.lower()}/{split_file[1]}",
        )
        r_flags = True
    else: 
        print(f"code {code} incorrect.!!")
        imagePath = testImg[0]
        split_file = imagePath.split("/")
        shutil.move(
            imagePath,
            f"face-recognition-using-opencv/other_dataset/{split_file[1]}",
        )
        r_flags = False
    print("Move complete.")
    return r_flags


def move_if_other():
    Imgpath = "upload/"
    testImg = [Imgpath + f for f in listdir(Imgpath)]
    if len(testImg) == 1:
        print("Nothing")
        imagePath = testImg[0]
        split_file = imagePath.split("/")
        shutil.move(
            imagePath,
            f"face-recognition-using-opencv/other_dataset/{split_file[1]}",
        )
        print("Move complete.")
    else: print("Upload is empty.!!")
