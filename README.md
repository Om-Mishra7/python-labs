# Lab Instructions: Flask Routes and API Requests

**Objective:** Create Flask routes and make a GET request to an external API using the codedamn labs editor.

## Instructions:

1. **Set Up Your Flask Project:**

   - Create a new file named `app.py`.
   - Enter the following code to set up a basic Flask app:

     ```python
     from flask import Flask

     # Create a Flask web application
     app = Flask(__name__)

     # Define a route for the home page
     @app.route('/')
     def home():
         return 'Hello, CodeDamn!'
     ```

   - Save the file.

   - Run the Flask app:

     ```bash
     flask run
     ```

   - Access the app at the provided URL in the output. You should see the message "Hello, CodeDamn!" displayed in your browser.

2. **Create a Route for API Request:**

   - Open the `app.py` file in the editor.
   - Modify the code to include a new route for making a GET request to an external API:

     ```python
     from flask import Flask
     import requests

     # Create a Flask web application
     app = Flask(__name__)

     # Define a route for the home page
     @app.route('/')
     def home():
         return 'Hello, CodeDamn!'

     # Define a route for making a GET request to an external API
     @app.route('/api_request')
     def api_request():
         # URL of the external API
         api_url = 'https://ather.api.projectrexa.dedyn.io'

         # Make a GET request to the API using the requests library
         response = requests.get(api_url)

         # Check if the request was successful (status code 200)
         if response.status_code == 200:
             return f'Successful API request! Response: {response.text}'
         else:
             return f'Error making API request. Status Code: {response.status_code}'
     ```

   - Save the file.

   - Run the Flask app:

     ```bash
     flask run
     ```

   - Access the API request route at the provided URL in the output (e.g., http://127.0.0.1:5000/api_request). You should see a message indicating the success or failure of the API request along with the response.

3. **Additional Notes:**

   - Ensure that the external API (`https://ather.api.projectrexa.dedyn.io`) is accessible and responds to GET requests.
   - Use the `requests` library to make HTTP requests to external APIs.
