from os import listdir
from os.path import join
from unittest import result
import cv2
import os
import numpy as np
# from tensorflow.keras.models import load_model
import json
from flask import jsonify
import datetime
import shutil
import call_com

# model = load_model('test_model.h5')
# width = 128

Rsult = []
Fname = []

def Prediction():
    testpath = 'C:/Users/hpccmu/Documents/face-backend/upload/'
    testImg = [testpath+f for f in listdir(testpath)]
    rimg = []
    # print(testImg)
    imagePath = testImg[-1]
    # for imagePath in (testImg):
    print(imagePath.split("/")[6])
    print(testImg)
    # if imagePath.split('.')[0] != "":
    # #     emp = []
    # #     img = cv2.imread(imagePath , cv2.COLOR_BGR2RGB)
    # #     img = cv2.resize(img ,(width,width))
    # #     rimg = np.array(img)
    # #     rimg = rimg.astype('float32')
    # #     rimg /= 255
    # #     rimg = np.reshape(rimg ,(1,128,128,3))
    # #     predict = model.predict(rimg)
    # #     percent = np.round((predict*100),2)
    # #     p_f = percent.flatten()
    # #     pp = p_f.tolist()
    # #     label = ['Note','Prayut']
    # #     name = imagePath.split('/')
    # #     pre_result = []
    # #     [ emp.append([label[i],pp[i]]) for i in range(len(label))]
    # #     emp_sort = sorted(emp,key=lambda l:l[1],reverse=True)
    # #     print(len(emp_sort))
    # #     for i in range(len(emp)) :
    # #         if i == 4 : break
    # #         else :
    # #             if emp_sort[i][1] >= 80 :
    # #                 pre_result.append(emp_sort[i])
    # #                 # result = label[np.argmax(predict)]
    # #                 # P_result = str(result)+" "+ str(pp[np.argmax(predict)])
    # #             else :
    # #                pre_result.append(["Unknow",0]) 
    # #     ct = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # #     tuple_list = {"File name":name[1],
    # #                 "Predict result": pre_result ,
    # #                 "Time":str(ct)}
    # # #move img to dir 
    # # Rsult.append(pre_result)
    # # filename = testImg[0].split("/")
    # # # Rsult.append(label[np.argmax(predict)])
    # # Fname.append(filename)
    reback = call_com.prediction(imagePath)
    return jsonify(reback)

def getOtherValue():
    return Fname[-1], Rsult[-1]




