from flask import Flask, request, render_template
import joblib
import numpy as np
import os
from flask import Flask


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "models/main.pkl")
# to get your model: joblib.dump(model, "model.pkl")

model = joblib.load(model_path)

app = Flask(
    'IndigoWaitingTime',
    template_folder=os.path.join(BASE_DIR, 'templates')
)

# app = Flask('IndigoWaitingTime')

@app.route('/debug')
def debug():
    return str(os.listdir('templates'))

@app.route('/', methods=['GET'])
def greet():
	# return app.send_static_file('CheckWaitingTime.html')
	return render_template('CheckWaitingTime.html')

@app.route('/show_waiting_time',methods=['POST'])
def show_waiting_time():
	data = dict(request.form)
	# This list needs to be in the same order as 
	# the features when the model was initially trained
	featureList = ['day_of_week', 'time_of_day',
                   'patient_age', 'patient_gender',
				   'num_doctors', 'num_receptionists',
				   'temperature', 'rainfall',
				   'pct_prior_vacant_slots',
				   'prior_emergency',
				   'avg_doctor_experience',
				   'pct_switch', 'avg_age_prior',
				   'avg_gender_prior']
	X = [data[f] for f in featureList]
	X = [float(x) for x in X]

	# Convert percentage values to proportions
	idx = featureList.index('pct_prior_vacant_slots')
	X[idx] = X[idx] / 100
	idx = featureList.index('pct_switch')
	X[idx] = X[idx] / 100

	Xnp = np.array(X).reshape(1,-1)
	# model = joblib.load({folder and model name})
	prediction = model.predict(Xnp)
	
	return render_template('WaitingTime.html', waittime=round(prediction[0]))
	

if __name__ == '__main__':
    app.run(debug=True)