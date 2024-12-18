from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__,template_folder="../templates")

# MongoDB setup
client = MongoClient("")
db = client['database_1']
collection = db['policy_1']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Signup')
def Signup():
    return render_template('Sign up.html')

@app.route('/login')
def Login():
    return render_template('login.html')

@app.route('/login_up', methods=['POST'])
def login_up():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        form_data = {
                "email": email,
                "password": password,}
        collection.insert_one(form_data)
        return "Form submitted successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/sign_up', methods=['POST'])
def sign_up():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        form_data = {
                "name": name,
                "email": email,
                "phone_number": phone_number,}
        collection.insert_one(form_data)
        return "Form submitted successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        insurance_type = request.form.get('choice')
        coverage = request.form.get('coverage')
        start_date = request.form.get('Start_date')
        end_date = request.form.get('End_date')

        # Check if any field is missing


        # Save to MongoDB
        form_data = {
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "insurance_type": insurance_type,
            "coverage": coverage,
            "start_date": start_date,
            "end_date": end_date
        }
        collection.insert_one(form_data)
        return "Form submitted successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
