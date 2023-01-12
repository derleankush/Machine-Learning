from flask import Flask, jsonify, render_template, request
from project_app.utils import CollegePlacement

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route("/Form")
def Form():
    return render_template("index.html")
    


@app.route("/Mod", methods = ['POST', 'GET'])
def CollegePlace():
    if request.method == 'POST':
        form_data = request.form

        a1 = int(form_data["Age"])
        b1 = int(form_data["Internship"])
        c1 = int(form_data["CGPA"])
        d1 = int(form_data["HistoryOfBacklogs"])
        e1 = str(form_data["Stream"])

        print(a1,b1,c1,d1,e1)
        
        obj = CollegePlacement(a1,b1,c1,d1,e1)
        y = obj.get_predict()
        
        if y == 1:
            return render_template("index.html", result = "Congratulaions ..You Can Placed....!!")
        else:
            return render_template("index.html", result = "You Can Not Placed")

    else:
        return 'Something Wrong'    

app.run(host = "0.0.0.0",port = 5055,debug = False)
