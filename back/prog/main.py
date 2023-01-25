
import sys
from flask import Flask, jsonify, request

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

@app.route('/api/getURLData')
def testPageScraper(url=None):
    import scraper
    import _parser as parser
    # get url from body from request
    url = request.args.get('q')
    if url is None:
        return jsonify({'error': 'No URL provided'}), 400
    print(url)

    url_list = url.split(',')
    output_data = []
    for url, data in scraper.scrapeURLS(url_list, 60, 20):
        new_page = parser.Page(url, data)
        output_data.append(new_page.pageObject)

    return jsonify(output_data), 200

if __name__ == '__main__':
    shouldRunDebug = "debug" in sys.argv
    app.run(debug=shouldRunDebug)