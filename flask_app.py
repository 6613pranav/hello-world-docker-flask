from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This will work on your machine too :)</h1>"


if __name__ == '__main__':
    # we are binding the flask app to run on port 5000 & The application will run on all hosts (localhost & local machine network)
    app.run(debug=True, host = '0.0.0.0', port = 5000)

# Command to run  flask App "flask --app flask_app run -h 0.0.0.0"