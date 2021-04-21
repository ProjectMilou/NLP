from flask import Flask, jsonify
import db
import twitter
import nlp
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
    
    #result = db.findStockBySymbol(symbol)
    
    test = twitter.searchRecentTweets("Apple")
    nlpPreparedText = twitter.prepareTweetsForNLP(test)
    tokens = nlp.getFrequencyFromTweets(nlpPreparedText)
    return jsonify(tokens)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)

    
    