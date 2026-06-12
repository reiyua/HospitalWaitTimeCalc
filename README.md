# Hospital Wait Time Calculator

Machine learning model + web app to predict hospital wait times for a fictional hospital based on fictional data.

---

## Live Demo of Web App

Azure:  
https://rayyan-h-tafe-nsw-indigo-hospital-wait-time-calculator.azurewebsites.net/

Fly.io (Mirror):  
https://rayyan-h-tafe-nsw-indigo-hospital-wait-time-calculator.fly.dev/

---

## About

HospitalWaitTimeCalc

Predicts how long a patient will wait based on appointment details.

---

## Model

- Regression model  (XGBoost)
- Output: Wait time (minutes)  

Inputs:
- Day  
- Time  
- Age  
- Gender  
- Doctor  

---

## Tech

- Python  
- scikit-learn
- XGBoost
- JobLib  
- Pandas / NumPy  
- Flask

---

## Run Notebook in MyBinder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/reiyua/HospitalWaitTimeCalc/HEAD?urlpath=%2Fdoc%2Ftree%2FHospitalWaitTimeCalc.ipynb)


## Run Notebook in Google Colab

https://colab.research.google.com/github/reiyua/ICTAII501/blob/main/your_notebook.ipynb


---

## Run Web App

```bash
git clone https://github.com/reiyua/HospitalWaitTimeCalc
cd ICTAII501
pip install -r requirements.txt
python app.py




