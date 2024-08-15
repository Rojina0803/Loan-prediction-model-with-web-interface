from flask import Flask, request, render_template
import numpy as np
import pickle 

# Create flask app
app = Flask(__name__)

# To handel input
genders_to_int = {
    'MALE': 1,
    'FEMALE': 0
}

married_to_int = {
    'YES': 1,
    'NO': 0
}

education_to_int = {
    'GRADUATED': 1,
    'NOT GRADUATED': 0
}

dependents_to_int = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3+': 3
}

self_employment_to_int = {
    'YES': 1,
    'NO': 0
}

# Basic route
@app.route("/", methods=["GET", "POST"])
def loan_application():
    if request.method == "GET":
        return render_template(
        "loan_application.html",
    )
    else:
        genders_type = request.form['genders_type']
        marital_status = request.form['marital_status']
        dependents = request.form['dependents']
        education_status = request.form['education_status']
        self_employment = request.form['self_employment']
        applicantIncome = float(request.form['applicantIncome'])
        coapplicantIncome = float(request.form['coapplicantIncome'])
        loan_amnt = float(request.form['loan_amnt'])
        term_d = int(request.form['term_d'])
        credit_history = int(request.form['credit_history'])
        property_area = request.form['property_area']


# Index(['Credit_History', 'LoanAmount_log', 'Gender_Female', 'Gender_Male',
#        'Married_No', 'Married_Yes', 'Dependents_3', 'Dependents_0',
#        'Dependents_1', 'Dependents_2', 'Education_Graduate',
#        'Education_Not Graduate', 'Self_Employed_No', 'Self_Employed_Yes',
#        'Property_Area_Rural', 'Property_Area_Semiurban', 'Property_Area_Urban',
#        'Total_Income', 'Total_Income_log', 'EMI', 'Balance_Income'],
#       dtype='object')

        x = np.ones(21)
        x[0] = 1
        x[1] = loan_amnt
        x[2] = 0
        x[3] = 1
        x[4] = 1
        x[5] = 0
        x[6] = 1
        x[7] = 0
        x[8] = 0
        x[9] = 0
        x[10] = 1
        x[11] = 0
        x[12] = 0
        x[13] = 1
        x[14] = 0
        x[15] = 1
        x[16] = 0
        x[17] = applicantIncome + coapplicantIncome
        x[18] = applicantIncome + coapplicantIncome
        x[19] = loan_amnt / term_d
        x[20] = (applicantIncome + coapplicantIncome) - loan_amnt/term_d
        

        with open('flask/models/logistic_model.pkl', 'rb') as f:
            lrm = pickle.load(f)

        pred = lrm.predict([x])[0]
        
        if pred == 1:
            result = "LOAN APPROVED"
        else:
            result = "LOAN REJECTED"
        return render_template('loan_application.html', res=result)


# # Route with variable
# @app.route("/success/<int:score>", methods=["GET"])
# def success(score):
#     return f"<h1>You Got {score}</h1>"

# # Route with form
# @app.route("/form", methods=["GET", "POST"])
# def form():
#     if request.method == "GET":
#         return render_template("form.html")
#     else:
#         maths = int(request.form["Math"])
#         science = int(request.form["Science"])
#         avg = (maths + science) / 2
#         return render_template("form.html", score=avg)

if __name__ == "__main__":
    app.run(debug=True)