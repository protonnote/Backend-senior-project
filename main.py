# from crypt import methods
import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
import recognize_image as predict
import move_file as mv
import threading
import time
import datetime
import extract_train_model as train_model

def auto_train():
	print("start")
	day_counter = 1
	while True:
		print(f"Day : {day_counter}, Time : {datetime.datetime.now()}")
		train_model.run_embedding()
		train_model.run_train()
		day_counter += 1
		time.sleep(86400)


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello():
  q = request.args.get('q')
#   print(q)
  return { "message": "Check Check" }, 201



@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

		# call Predict <----
		resp = predict.Prediction()
		resp.status_code = 201
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400

	return resp

@app.route('/confirm', methods=['POST'])
def confirm():
	if request.json['status'] == "YES":
		print("YES case.")
		name = request.json['name']
		mv.move(name)
		resp = jsonify({'message' : 'Done'})
		resp.status_code = 201
	elif request.json['status'] == "NO":
		print("NO case.")
		code = request.json['code']
		if check_pin := mv.move_if_no(int(code)):
			resp = jsonify({'message' : 1})
		else:
			resp = jsonify({'message' : 0})
		resp.status_code = 201
	elif request.json['status'] == "IDLE":
		print("IDLE case.")
		mv.move_if_other()
		resp = jsonify({'message' : 'Done IDLE case'})
		resp.status_code = 201
	else: 
		resp = jsonify({'message' : 'Fail'})
		resp.status_code = 400

	return resp


@app.route('/train')
def train():
	print("Train case")
	q = request.args.get('q')
	train_model.run_embedding()
	train_model.run_train()
	return { "message": "train success" }, 201


if __name__ == "__main__" :
	threading.Thread(target=auto_train, daemon=True).start()
	app.run(host="0.0.0.0",port=5000,debug=True)