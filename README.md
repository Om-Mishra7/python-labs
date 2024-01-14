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

     # Check if the script is being run directly
     if __name__ == "__main__":
         # Run the Flask app on port 1337
         app.run(host="0.0.0.0", port=1337)
     ```

   - Save the file.

   - Install Flask and Requests using the following commands:

     ```bash
     pip install Flask
     pip install requests
     ```

   - Run the Flask app:

     ```bash
     python3 app.py
     ```

   - Access the app at the provided URL in the browser preview window. You should see the message "Hello, CodeDamn!" displayed in your browser. A browser preview will appear on the side.

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

     # Check if the script is being run directly
     if __name__ == "__main__":
         # Run the Flask app on port 1337
         app.run(host="0.0.0.0", port=1337)
     ```

   - Save the file.

   - Run the Flask app:

     ```bash
     python3 app.py
     ```

   - Access the API request route at the provided URL in the browser preview window. You should see a message indicating the success or failure of the API request along with the response.

3. **Additional Notes:**

   - Ensure that the external API (`https://ather.api.projectrexa.dedyn.io`) is accessible and responds to GET requests.
   - Use the `requests` library to make HTTP requests to external APIs.

   - **Note:** The condition `if __name__ == "__main__":` is used to check whether the Python script is being run directly or imported as a module. If the script is the main program, the app will be run; if it is imported as a module, the app will not run. This allows the script to be reusable as a module in other applications.
