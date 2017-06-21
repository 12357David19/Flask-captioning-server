from flask import Flask, render_template, request

app = Flask(__name__)
file = '/static/example_scout.jpg'
labels = ["Head","Lungs","Abdomen","Pelvis"]

def get_file():
	return file

@app.route('/', methods=['POST', 'GET'])
def index():
	filename = get_file()
	return render_template('index.html', filename=filename,labels=labels)

@app.route('/submit', methods=['POST'])
def submit():
	if request.method == "post":
		for index,label in enumerate(labels):
			print("%s: %s"% (label,request.form['form']))
	return render_template('index.html', filename=file,labels=labels)

if __name__ == '__main__':
    app.run()
