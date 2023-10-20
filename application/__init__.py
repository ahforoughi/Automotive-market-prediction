from flask import Flask

app = Flask(__name__)

# create api
@app.route('/', methods=['GET', 'POST'])
def predict():
	print("start..")
	return "hello"
