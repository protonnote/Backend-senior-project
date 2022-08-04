import os

def train_model() :
    os.system("python face-recognition-using-opencv/extract_embeddings.py")
    os.system("python face-recognition-using-opencv/train_model.py")
    # os.system("python face-recognition-using-opencv/train_model.py")
    # os.system("python face-recognition-using-opencv/train_model.py")
    # os.system("python train_model.py")
    # os.system("python train_model.py")

