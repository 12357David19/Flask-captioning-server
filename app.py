from flask import Flask, render_template, request
import json
import os
import dicom
import csv
import numpy as np
from cv2 import imwrite
app = Flask(__name__)
hosted_dir = os.path.abspath("static") + '/'
labels = ["head", "lung", "abdomen", "pelvis"] # user-facing labels
data_location = "C:\Users\\212581462\Documents\Scout-data/"

def get_dir_list(path):
    l = os.listdir(path)
    output = []
    for dcm in l:
        output.append(data_location + dcm)
    return output

unlabeled_list = get_dir_list(data_location)
labeling_list = []
fn = ['filename', 'is_head', 'is_lung', 'is_abdomen', 'is_pelvis'] #server/csv side labels
with open('labeled.csv', 'wb') as f:
    writer = csv.DictWriter(f, fieldnames=fn)
    writer.writeheader()


def get_file():
    """get file should return a file from the unlabeled dir, move file to """
    try:
        file = unlabeled_list.pop()
    except IndexError as e:
        return "empty list"
    #taking dicom file and creating a png and displaying it
    if ".dcm" in os.path.basename(file):
        d = dicom.read_file(file)
        d_array = d.pixel_array
        filename =os.path.basename(file.replace(".dcm", ".png"))
        png_name = os.path.join(hosted_dir + filename)
        imwrite(png_name, d_array)
        file = png_name

    labeling_list.append(file)
    return file


def get_file_data(json):
    png_file = json['filename']
    file_name = os.path.basename(json['filename'])
    dcm_path = data_location + file_name.replace(".png",".dcm")
    json['filename'] = dcm_path
    with open('labeled.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fn)
        writer.writerow(json)
    labeling_list.remove(png_file)
    os.remove(png_file)


@app.route('/', methods=['GET'])
def index():
    filename = get_file()
    if filename == "empty list":
        return render_template('empty.html')
    return render_template('index.html', filename=filename, labels=labels)


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        data = json.loads(request.data)
        get_file_data(data)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
