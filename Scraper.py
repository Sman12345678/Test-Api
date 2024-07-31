from flask import Flask, jsonify, request
from scraper import scrape_website

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('https://Copilot.microsoft.com')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    data = scrape_website(url)
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run(debug=True)
