
import sys
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/search', methods=['POST'])
def search():
    # Match the search term to the database
    # Handle Results
    # If results older than 30 days; re-scrape url?
    pass

@app.route('/api/URL/')
def testGetPage():
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

@app.route('/api/URL/save', methods=['POST'])
def savePage():
    # Get URL/s from body of request
    # Parse URL/s
    # Save to database
    pass

@app.route('/api/URL/delete', methods=['DELETE'])
def removePage():
    # Get URL/s from body of request
    # Delete from database
    pass

if __name__ == '__main__':
    shouldRunDebug = "debug" in sys.argv
    app.run(debug=shouldRunDebug)