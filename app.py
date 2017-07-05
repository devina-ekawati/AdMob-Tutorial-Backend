from flask import Flask, jsonify
from pprint import pprint
import json

with open('data.json') as data_file:    
    result = json.load(data_file)

app = Flask(__name__)

@app.route('/get-ads', methods=['GET'])
def get_ads():
	return jsonify(result)

@app.route('/get-ad/<activity>', methods=['GET'])
def get_ad(activity):
	ad = [item for item in result["data"] if item['activity'] == activity]
	return jsonify({'data': ad})
	
print result["data"]

if __name__ == '__main__':
    app.run()