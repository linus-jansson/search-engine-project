
import sys
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def API_test():
    output = {
        'test': 3
    }

    return jsonify(output)


@app.route('/api/getURLMatches')
def getSearchResults():
    pass

@app.route('/api/saveURL')
def saveURL():
    pass

@app.route('/api/testScraperURL')
def testPageScraper():
    pass

if __name__ == '__main__':
    shouldRunDebug = "debug" in sys.argv
    app.run(debug=shouldRunDebug)