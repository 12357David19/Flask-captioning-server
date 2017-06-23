from flask import Flask, render_template, request
import json
import csv
app = Flask(__name__)
input_list = 'to_be_labeled.csv'
labels = ["head", "lung", "abdomen", "pelvis"]

# unlabeled_list = "unlabeled"
# labeling_list = "labeling"
# labeled_list = "labeled"
unlabeled_list = []
with open(input_list, 'r') as f:
    for line in f:
        unlabeled_list.append(line.replace('\n', ''))
labeling_list = []
fn = ['filename', 'is_head', 'is_lung', 'is_abdomen', 'is_pelvis']
with open('labeled.csv', 'wb') as f:
    writer = csv.DictWriter(f, fieldnames=fn)
    writer.writeheader()


def get_file():
    """get file should return a file from the unlabeled dir, move file to """
    try:
        file = unlabeled_list.pop()
    except IndexError as e:
        return "empty list"
    labeling_list.append(file)
    with open('labeling.txt', 'a') as f:
        f.write(file + '\n')
    # if file ==
    return file


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
        with open('labeled.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=fn)
            writer.writerow(data)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
