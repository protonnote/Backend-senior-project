import os

def train_model() :
    os.system("python extract_embeddings.py")
    os.system("python train_model.py")
    os.system("python train_model.py")
    os.system("python train_model.py")
    os.system("python train_model.py")
    os.system("python train_model.py")

def prediction(x) :
    # os.system("python recognize_image.py --image ./test/note/note5.jpg")
    let = os.popen("python ./face-recognition-using-opencv/recognize_image.py --image {}".format(x)).read()
    return let

# print(prediction("note5"))
# print(prediction("note6"))