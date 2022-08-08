# from crypt import methods
import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
import recognize_image as predict
import move_file as mv
import call_com as cc

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

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
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp

@app.route('/confirm', methods=['POST'])
def confirm():
	if request.json['status'] == "YES" :
		name = request.json['name']
		mv.move(name)
	elif request.json['status'] == "NO" :
		mv.move_if_no(request.json['code']) #to be fix
	elif request.json['status'] == "IDLE" :
		mv.move_if_other()
	else : 
		resp = jsonify({'message' : 'Fail'})
		resp.status_code = 400
		return resp
	resp = jsonify({'message' : 'Done'})
	resp.status_code = 201
	return resp

@app.route('/train')
def train():
	q = request.args.get('q')
	cc.train_model()
	return { "message": "train success" }, 201


if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=5000)