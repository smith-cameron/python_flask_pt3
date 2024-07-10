from flask_app import app  # Import the Flask app instance from the flask_app package
from flask import render_template, redirect, request, session

# Route for the homepage
@app.route('/')
def index():
  # Log the incoming form data (though this route is a GET request and it is empty for now)
  print(f"GET Route: {request.form}")  
  # Uncomment line 39 if 'name' is set in the session. If it is not it will trigger a key error
  # print(f"GET Route(session): {session['name']}")  
  return render_template('index.html')  # Render the index.html template

# Route to handle form submission (POST request)
@app.route('/users/create', methods=['POST'])
def users_create():
    print(f"POST Route: {request.form}")  # Log the incoming form data for debugging
    print(request.form['email'])  # Log the email input received in the form
    # Store form data in session variables for persistence across requests
    session['some_key'] = request.form
    session['email'] = request.form['email']
    session['name'] = request.form['name']
    session['birthday'] = request.form['user_birthday']
    session['age'] = request.form['age']
    session['password'] = request.form['user_password']
    return redirect('/')  # Redirect to the homepage after processing the form data

# Route to clear session data
@app.route('/clear_session')
def clear_session():
    session.clear()  # Clear all session variables
    # session.pop('desired_key_to_pop')  # Syntax to remove specific session variables
    # session.pop('email')  # Example of popping a specific session variable
    return redirect('/')  # Redirect to the homepage after clearing session
