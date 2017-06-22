from flask import Flask, render_template, request

app = Flask(__name__)
file = '/static/example_scout.jpg'
labels = ["Head", "Lungs", "Abdomen", "Pelvis"]

# unlabeled_list = "unlabeled"
# labeling_list = "labeling"
# labeled_list = "labeled"
unlabeled_list = [file]
labeling_list = []
labeled_list = []


def get_file():
    """get file should return a file from the unlabeled dir, move file to """
    file = unlabeled_list.pop()
    labeling_list.append(file)
    return file


@app.route('/', methods=['POST', 'GET'])
def index():
    filename = get_file()
    return render_template('index.html', filename=filename, labels=labels)


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        for index, label in enumerate(labels):
            if label in request.form:
                print(label)
            # print("%s: %s" % (label, request.form['form']))
    return render_template('index.html', filename=file, labels=labels)


if __name__ == '__main__':
    app.run()
