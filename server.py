from flask import Flask

# Create the application instance
app = Flask(__name__)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:
    """
    return "Hello"

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)