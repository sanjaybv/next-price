import json
import sqlite3
from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/realtime')
def realtime():
    return render_template('realtime.html')

@app.route('/historical')
def historical():
    return render_template('historical.html')

@app.route('/<symbol>')
def stock(symbol=None):
    return render_template('stock.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    name = {1: 'foo', 2: 'bar', 3: 'baz'}
    return render_template('hello.html', name=name)

@app.route('/plot/')
@app.route('/plot/<name>')
def plot(name=None):
	conn = sqlite3.connect('data/stocks.db')
	cursor = conn.cursor()

	cursor.execute('SELECT * FROM historical LIMIT 50')
	rows = cursor.fetchall()

	cleaned = []
	ctr = 1

	for row in rows:
	    # print row[4], row[5]
	    temp = {}
	    temp["closePrice"]  = row[4]
	    temp["date"] = row[5]
	    cleaned.append(temp)
	    ctr += 1

	# for row in cleaned:
	    # print row

	conn.close()

	# fp = open('templates/data.json', 'wb')
	# json.dump(cleaned, fp, indent = 3)
	return render_template('plot.html', name = cleaned)

@app.route('/lineplot2/')
@app.route('/lineplot2/<name>')
def lineplot2(name=None):
	conn = sqlite3.connect('data/stocks.db')
	cursor = conn.cursor()

	cursor.execute('SELECT * FROM historical LIMIT 50')
	rows = cursor.fetchall()

	cleaned = []
	ctr = 1

	for row in rows:
	    # print row[4], row[5]
	    temp = {}
	    temp["closePrice"]  = row[4]
	    temp["date"] = row[5]
	    cleaned.append(temp)
	    ctr += 1

	conn.close()

	# data = [
 #    {"year" : "2005", "closePrice": 770000},
 #    {"year" : "2006", "closePrice": 670000},
 #    {"year" : "2007", "closePrice": 570000},
 #    {"year" : "2008", "closePrice": 770000},
 #    {"year" : "2009", "closePrice": 870000}
	# ]
	# data = [
 #    {"year" : "2005-10-10", "value": 870},
 #    {"year" : "2006-11-11", "value": 770},
 #    {"year" : "2010-12-12", "value": 570},
 #    {"year" : "2012-09-09", "value": 740},
 #    {"year" : "2015-08-08", "value": 780}
	# ]
	# return render_template('lineplot2.html', name = data)
	return render_template('lineplot2.html', name = cleaned)

@app.route('/googleChart')
@app.route('/googleChart/<name>')
def googleChart(name=None):
	conn = sqlite3.connect('data/stocks.db')
	cursor = conn.cursor()

	cursor.execute('SELECT * FROM historical LIMIT 50')
	rows = cursor.fetchall()

	cleaned = []
	ctr = 1

	for row in rows:
	    temp = []
	    temp.append(row[5])
	    temp.append(row[4])
	    cleaned.append(temp)
	    ctr += 1

	conn.close()
	
	return render_template('googleChart.html', name = cleaned)

def main():
    app.run()

if __name__ == '__main__':
    main()
