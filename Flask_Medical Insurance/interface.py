from flask import Flask,jsonify,request,render_template
from project_app.utils import MedicalInsurance

import config

app = Flask(__name__)

@app.route("/")   # Home API
def hello_flask():
    return render_template('home.html')
    

@app.route("/Form")
def Form():
    return render_template("index.html")

@app.route("/Predict", methods = ['POST', 'GET'])
def get_insurance_charges(): 

    if request.method == 'POST':
        form_data = request.form

        a1 = int(form_data["Age"])
        b1 = str(form_data["Sex"])
        c1 = int(form_data["bmi"])
        d1 = int(form_data["children"])
        e1 = str(form_data["smoker"])
        f1 = str(form_data["region"])

        print(a1,b1,c1,d1,e1,f1)
        
        obj = MedicalInsurance(a1,b1,c1,d1,e1,f1)
        y = obj.get_predict_charges()
        y = float(y)

        return render_template("index.html", result = y)

    else:
        return 'Something Wrong'  




    
    # age  = 19
    # sex  = 'male'
    # bmi  = 20 
    # children = 2
    # smoker = 'yes'
    ## region = 'southwest'

    # med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    # charges = med_ins.get_predict_charges()

    # return jsonify({"Return" : f"Predicted medical isurance charges are :{charges}"})



if __name__ == "__main__":
   app.run(host = "0.0.0.0",port = 5055,debug = True) # server start