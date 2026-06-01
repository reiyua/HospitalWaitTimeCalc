from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask('IndigoWaitingTime')

@app.route('/', methods=['GET'])
def greet():
	return app.send_static_file('CheckWaitingTime.html')

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
	model = joblib.load({folder and model name})
	prediction = model.predict(Xnp)
	
	return render_template('WaitingTime.html', waittime=prediction[0])
	