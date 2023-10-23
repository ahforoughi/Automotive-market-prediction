from flask import Flask
import joblib
import pandas as pd


app = Flask(__name__)

model_path = "D:\car-market\Automotive-market-prediction\model_with_encoder.joblib"
loaded_pipeline = joblib.load(model_path)


# create api
@app.route('/', methods=['GET', 'POST'])
def predict():
	print("start...")
	new_data_dict = {
		'buying': 'low',
		'maint': 'low',
		'doors': '4',
		'persons': '4',
		'lugage': 'med',
		'safety': 'high'
	}
	new_data = pd.DataFrame(new_data_dict, index=[0])
	predictions = loaded_pipeline.predict(new_data)
	# return json format data
	Jsonpredictions = {"predictions": predictions.tolist()}
	return Jsonpredictions


