from flask import Flask, render_template, request

app = Flask(__name__)
file = '/static/example_scout.jpg'
labels = ["Head","Lungs","Abdomen","Pelvis"]
# @app.route('/')
@app.route('/', methods=['POST'])
def index():
	if method = "post":
		for index,label in enumerate(labels):
			print("%s: %s"% (label,request.form[label]))
	return render_template('index.html', filename=file,labels=labels)

def submit():

	return render_template('index.html', filename=file,labels=labels)

if __name__ == '__main__':
    app.run()
