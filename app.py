from flask import Flask, jsonify, request, render_template as suleiman
from scraper import scrape_website  

""""
We can decide to add website at the root of the API
"""


app = Flask(__name__)

@app.route('/')
def suleiman_home():
    return suleiman('home.html')
           
@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url') 
    if not url:
        return jsonify({'error': 'url is required'}), 400  
    data = scrape_website(url)  
    return jsonify({'data': data})  

if __name__ == '__main__':
    app.run(debug=True)  # Run😑
