# python recognize.py  --image path/to/image.jpg

# import libraries
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
import copyreg
from flask import jsonify
from os import listdir
from os.path import join
from datetime import datetime
import write_log as wr

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="input image path")
# args = vars(ap.parse_args())

# load our serialized face detector from disk
# print("Loading Face Detector...")
protoPath = "face-recognition-using-opencv/face_detection_model/deploy.prototxt"
modelPath = "face-recognition-using-opencv/face_detection_model/res10_300x300_ssd_iter_140000.caffemodel"
detector = cv2.dnn.readNetFromCaffe(protoPath,modelPath )

# load our serialized face embedding model from disk
# print("Loading Face Recognizer...")
embedder = cv2.dnn.readNetFromTorch('face-recognition-using-opencv/openface_nn4.small2.v1.t7')

# load the actual face recognition model along with the label encoder
recognizer = pickle.loads(open('face-recognition-using-opencv/output/recognizer', "rb").read())
le = pickle.loads(open('face-recognition-using-opencv/output/le.pickle', "rb").read())

def Prediction():
	Imgpath = "upload/"
	testImg = [Imgpath + f for f in listdir(Imgpath)]
	if len(testImg) < 1 :
		return jsonify({'messege':'empty filse'})
	else :
		imagePath = testImg[0]
		# load the image, resize it to have a width of 600 pixels (while maintaining the aspect ratio), and then grab the image dimensions
		image = cv2.imread(imagePath)
		# image = cv2.imread("upload/image_1_10_56_24.png")
		image = imutils.resize(image, width=600)
		(h, w) = image.shape[:2]

		# construct a blob from the image
		imageBlob = cv2.dnn.blobFromImage(
			cv2.resize(image, (300, 300)), 1.0, (300, 300),
			(104.0, 177.0, 123.0), swapRB=False, crop=False)

		# apply OpenCV's deep learning-based face detector to localize faces in the input image
		detector.setInput(imageBlob)
		detections = detector.forward()

		# loop over the detections
		for i in range(0, detections.shape[2]):

			# extract the confidence (i.e., probability) associated with the prediction
			confidence = detections[0, 0, i, 2]

			# filter out weak detections
			if confidence > 0.5:
				# compute the (x, y)-coordinates of the bounding box for the face
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")

				# extract the face ROI
				face = image[startY:endY, startX:endX]
				(fH, fW) = face.shape[:2]

				# ensure the face width and height are sufficiently large
				if fW < 20 or fH < 20:
					continue

				# construct a blob for the face ROI, then pass the blob through our face embedding model to obtain the 128-d quantification of the face
				faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96),
					(0, 0, 0), swapRB=True, crop=False)
				embedder.setInput(faceBlob)
				vec = embedder.forward()

				# perform classification to recognize the face
				preds = recognizer.predict_proba(vec)[0]
				j = np.argmax(preds)
				proba = preds[j]
				# name = le.classes_[j]

				re_obj = {'filename':'','Name':[],'Percent':[],'Time':''}

				for i in range(len(le.classes_)) :
					re_obj['Name'].append(le.classes_[i]) 
					re_obj['Percent'].append(round(preds[i] * 100,2)) 
					# text = "{}: {:.2f}%".format(le.classes_[i], preds[i] * 100)
					# print(text)
				# print(le.classes_)
				fname = imagePath.split('/')
				re_obj['filename'] = fname[1]
				re_obj['Time'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
				print(re_obj)
				# sort_orders = dict(sorted(re_obj.items(), key=lambda x: x[1], reverse=True))
				# print(re_obj)
		flag = wr.save_log(re_obj)
		if flag :
			return jsonify(re_obj)
		# return re_obj

			# draw the bounding box of the face along with the associated probability
			# y = startY - 10 if startY - 10 > 10 else startY + 10
			# cv2.rectangle(image, (startX, startY), (endX, endY),
			# 	(0, 0, 255), 2)
			# cv2.putText(image, text, (startX, y),
			# 	cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

	# show the output image
	# cv2.imshow("Image", image)
	# cv2.waitKey(0)


# print(Prediction())