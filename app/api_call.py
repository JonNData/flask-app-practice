# query multiple ticker
from urllib import request
import json
from flask import render_template

def api_call(symbol):
    """ Construct a url for specified symbol """
    url = request.urlopen(f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=30min&apikey=80SZHZ4OO2DV39L8")
    data = url.read()
    new_data = json.loads(data.decode('utf-8'))
    response_body = new_data['Time Series (30min)']
    return response_body