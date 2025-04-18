from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests
import os

app = Flask(__name__, 
    static_folder='static',
    template_folder='templates'
)

# Set secret key for flash messages
app.secret_key = os.urandom(24)

# Get your EspoCRM API config from environment variables or set manually
ESPOCRM_API_KEY = os.getenv("ESPOCRM_API_KEY", "42c7dd457cf25a3486072b4bd9a68c39")
ESPOCRM_API_URL = os.getenv("ESPOCRM_API_URL", "http://localhost/espo/api/v1/Lead")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    # Check if there's a success message in the session
    success_message = session.pop('success_message', None)
    return render_template('contact.html', success_message=success_message)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Collect form data from your static HTML form
        form_data = {
            "firstName": request.form.get('name'),        # maps HTML "name" to EspoCRM "firstName"
            "mobile": request.form.get('phone'),          # maps HTML "phone"
            "emailAddress": request.form.get('email'),    # maps HTML "email"
            "description": request.form.get('message')    # maps HTML "message"
        }

        # Validate required fields
        if not all([form_data['firstName'], form_data['mobile'], form_data['emailAddress']]):
            flash('Please fill in all required fields', 'error')
            return redirect(url_for('contact'))

        # Prepare headers for EspoCRM API
        headers = {
            'X-Api-Key': ESPOCRM_API_KEY,
            'Content-Type': 'application/json'
        }

        # Make the API request
        response = requests.post(ESPOCRM_API_URL, json=form_data, headers=headers)
        response.raise_for_status()
        
        # Store success message in session
        session['success_message'] = 'Thank you for your message! We will get back to you soon.'
        
        # Redirect to contact page with success message
        return redirect(url_for('contact'))

    except requests.exceptions.RequestException as e:
        print(f"Failed to submit lead: {e}")
        flash('There was an error submitting your message. Please try again later.', 'error')
        return redirect(url_for('contact'))
    except Exception as e:
        print(f"Unexpected error: {e}")
        flash('An unexpected error occurred. Please try again later.', 'error')
        return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
