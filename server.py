from flask import Flask, jsonify
import db
# Create the application instance
app = Flask(__name__)


# Create a URL route in our application for "/"
@app.route('/popularity/<symbol>')
def home(symbol):
    """
    This functions takes the symbol as parameter, 
    finds the stock datapoints in MongoDB and return them.

    :return:
    """
    result = db.findStockBySymbol(symbol)
    return jsonify(result)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)

    
    