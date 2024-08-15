Project Structure

app.py: The main Flask application file.
templates/loan_application.html: The HTML template for the loan application form.
models/logistic_model.pkl: The serialized logistic regression model.
static/: Directory for static files like CSS and JavaScript .
requirements.txt: List of dependencies.


Technology Stack
Backend: Flask (Python)
Frontend: HTML/CSS (Jinja2 templating)
Model: Logistic Regression (scikit-learn)
Storage: Pickle for model serialization



Key Features
User Input: Collects user data such as gender, marital status, dependents, education level, employment status, income, loan amount, and property area.
Model Prediction: Utilizes a logistic regression model to predict the loan approval status.
Real-Time Feedback: Provides instant feedback to users on their loan application status.



How It Works
The user fills out the loan application form with their personal and financial details.
Upon submission, the input data is processed and transformed into a feature vector suitable for the model.
The logistic regression model predicts the outcome based on the provided inputs.
The result (Loan Approved or Loan Rejected) is displayed on the web page.
