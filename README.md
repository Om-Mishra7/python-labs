# Lab Instructions: Setting Up an OAuth Application Using Flask

## Instructions:

1. **Set Up Your Flask Project:**

- Flask is a minimal Python web framework that allows you to create web applications quickly and easily.

  - Create a new file named `app.py`.
  - Enter the following boilerplate code to create a basic Flask app:

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
        app.run(host="0.0.0.0", port=1337, debug=True)
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
         app.run(host="0.0.0.0", port=1337, debug=True)
     ```

   - Save the file.

   - Run the Flask app:

     ```bash
     python3 app.py
     ```

   - Access the API request route at the provided URL in the browser preview window. You should see a message indicating the success or failure of the API request along with the response.

3. **Create an OAuth App on GitHub:**

   - Create a new GitHub account if you don't already have one by visiting [https://github.com/signup](https://github.com/signup).

   - Log in to your GitHub account.

   - Go to [Developer Settings](https://github.com/settings/apps), by clicking on your profile picture in the top right corner and
     selecting **Settings** from the dropdown menu and then selecting **Developer Settings** from the left sidebar.

   - Click on **OAuth Apps** from the left sidebar, and then click on **New OAuth App**.

   - Enter the following details for your OAuth app:

     - **Application Name:** `CodeDamn OAuth App (Local)`, this is the name of your app and will be displayed to users when they are asked to authorize your app therefore it should be not be misleading.

     - **Homepage URL:** `The url of your browser preview window`, e.g. `https://rope-unit.codedamn.app` this is the url where your app is hosted.

     - **Application Description:** `OAuth App for CodeDamn`, this is the description of your app and will be displayed to users when they are asked to authorize your app therefore it should be not be misleading.

     - **Authorization callback URL:** `The url of your browser preview window` (same as the homepage URL) + `/callback`, e.g. `https://rope-unit.codedamn.app/callback`, this is the url where the user will be redirected after they authorize your app on GitHub.

   - Click on **Register Application**.

   - You will be redirected to the **OAuth Apps** page. Click on the **CodeDamn OAuth App (Local)** app to view the details.

   - Copy the **Client ID** and **Client Secret** and save them in a text file, you will need them later. If you lose them, you can always generate new ones by clicking on **Generate a new client secret**.

   - On top of the app.py file, add the following code to store the client id and client secret in variables:

     ```python
     # Client ID and Client Secret of the OAuth App, please note that these are sensitive credentials and should not be shared with anyone also in a production environment these should be stored in a secure location like environment variables.

     CLIENT_ID = 'YOUR_CLIENT_ID' # This is usually smaller than the client secret
     CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
     REDIRECT_URI = 'YOUR_BROWSER_PREVIEW_URL' + '/callback'
     ```

4. **Create a Route for Authorizing the App:**

   - Open the `app.py` file in the editor.

   - First, we need to import the `redirect` function from the `flask` module:

     ```python
     from flask import Flask, redirect
     ```

   - Create a new route to allow users to authenticate into your app using GitHub:

     ```python

     # Define a route for authorizing the app, this will redirect the user to GitHub to authorize the app and in turn redirect the user back to the callback URL. This route is usually accessed by clicking on a button on the sign in page like "Sign in with GitHub".
     @app.route('/authorize')
     def authorize():
         # URL of the GitHub OAuth Authorize endpoint (https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#1-request-a-users-github-identity), as you can see we are now redirecting the user to GitHub to authorize the app, this is the first step in the OAuth flow where we are sending to get the access token from an authorization server (GitHub in this case).

         # The scope parameter is used to specify the level of access that the app is requesting, in this case we are requesting access to the user's public profile and email address if it is public and is the way the authorization server (GitHub in this case) informs the user of the resources that the app is requesting access to. For more information on scopes, visit https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps.


         authorize_url = f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=user"

          # Redirect the user to the GitHub OAuth Authorize endpoint
          return redirect(authorize_url), 302 # 302 is the status code for redirection
     ```

   - Save the file.

   - Run the Flask app, and access the `/authorize` route at the provided URL in the browser preview window. You should be redirected to GitHub to authorize the app, in case of any error, refer to the error message displayed in the browser the most common error is an invalid client id or redirect uri not matching the one specified in the GitHub OAuth app.

5. **Create a Route for Handling the Callback:**

   - Open the `app.py` file in the editor.

   - First, we need to import the `request` object from the `flask` module:

     ```python
     from flask import Flask, redirect, request # The request object is used to access the query parameters in the callback URL
     ```

   - Create a new route to handle the callback from GitHub:

     ```python
     # Define a route for handling the callback from GitHub, this is the route that the user will be redirected to after they authorize the app on GitHub, and is the second step in the OAuth flow where we are getting the access token from the authorization server (GitHub in this case).
     @app.route('/callback')
     def callback():
         # The code parameter is used to specify the authorization code that the authorization server (GitHub in this case) will send to the callback URL after the user authorizes the app. This code is used to get the access token from the authorization server (GitHub in this case) in the next step of the OAuth flow. For more information on the code parameter, visit https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#2-users-are-redirected-back-to-your-site-by-github.

         CODE = request.args.get('code')

         if CODE is None:
          # If the code parameter is not present in the callback URL, the user has denied the authorization request or there was some other error during the authorization process.
             return 'Oops! The OAuth flow has failed. Please try again.'

          # URL of the GitHub OAuth Access Token endpoint (https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#3-use-the-authorization-code-to-get-an-access-token), as you can see we are now sending a POST request to GitHub to get the access token from the authorization server (GitHub in this case), this is the third step in the OAuth flow where we are getting the access token from the authorization server (GitHub in this case) using the authorization code that we received in the callback URL in the previous step.


          access_token_url = f"https://github.com/login/oauth/access_token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&code={CODE}"

          # Make a POST request to the GitHub OAuth Access Token endpoint to get the access token

          response = requests.post(access_token_url)

          # Check if the request was successful (status code 200)

          if response.status_code == 200:
            access_token = response.json()['access_token'] # Extract the access token from the response which is in JSON format
          else:
            return f'Error getting access token. Status Code: {response.status_code}'

          # URL of the GitHub API endpoint (https://docs.github.com/en/rest/reference/users#get-the-authenticated-user), as you can see we are now sending a GET request to GitHub to get the authenticated user's details using the access token that we received in the previous step, this is the fourth step in the OAuth flow where we are using the access token to access the protected resources on the resource server (GitHub in this case). There is no refresh token in the GitHub OAuth flow, as we just need to get the user's details and not access any other protected resources on the resource server (GitHub in this case).

          api_url = 'https://api.github.com/user'

          # Make a GET request to the GitHub API endpoint to get the authenticated user's details

          # Note: We are sending the access token in the Authorization header using the Bearer authentication scheme (https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#bearer_authentication), this is the standard way of sending access tokens in HTTP requests.

          response = requests.get(api_url, headers={'Authorization': f'token {access_token}'})

          # Check if the request was successful (status code 200)

          if response.status_code == 200:
            user_data = response.json() # Extract the user data from the response which is in JSON format
          else:
            return f'Error getting user data. Status Code: {response.status_code}'

          # Return the user's data

          return user_data
     ```

   - Save the file.

   - Run the Flask app, and access the `/authorize` route at the provided URL in the browser preview window. You should be redirected to GitHub to authorize the app and then redirected back to the callback URL where you should see the user's data displayed in the browser.

This is the basic flow of the OAuth 2.0 protocol, in production apps the user data is matched with the data in the database and the user is authenticated into the app and a session is created for the user to persist the user's data across requests, but that is beyond the scope of this lab.

**Additional Notes:**

- Ensure that the external API (`https://ather.api.projectrexa.dedyn.io`) is accessible and responds to GET requests.
- Use the `requests` library to make HTTP requests to external APIs.
- Use the `redirect` function to redirect the user to another route.
- Use the `request` object to access the query parameters in the callback URL.
- Use the `json()` method to extract the JSON data from the response.
- Use the `headers` parameter to send the access token in the Authorization header using the Bearer authentication scheme.

- **Note:** The condition `if __name__ == "__main__":` is used to check whether the Python script is being run directly or imported as a module. If the script is the main program, the app will be run; if it is imported as a module, the app will not run. This allows the script to be reusable as a module in other applications.

- **Note:** The `redirect` function is used to redirect the user to another route. The `request` object is used to access the query parameters in the callback URL. The `json()` method is used to extract the JSON data from the response. The `headers` parameter is used to send the access token in the Authorization header using the Bearer authentication scheme.
