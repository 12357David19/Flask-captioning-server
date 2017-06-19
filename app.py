from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	file = '/home/justin/Documents/Flask-captioning-server/smiley.gif'
	return render_template('index.html', filename=file)

if __name__ == '__main__':
    app.run()
