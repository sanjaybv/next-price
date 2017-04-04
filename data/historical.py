from yahoo_finance import Share
from pprint import pprint

import sqlite3

stock_symbols = ['GOOGL', 'YHOO', 'MSFT', 'AMZN', 'TWTR', \
        'FB', 'CSCO', 'BAC', 'AAPL', 'AMD']

def main():

    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    insert_query = \
        'INSERT INTO historical VALUES ("{0}", {1}, {2}, {3}, {4}, "{5}", "{6}")'

    for symbol in stock_symbols:
        print 'getting data for', symbol
        stock = Share(symbol)
        data = stock.get_historical('2014-01-01', '2016-01-01')
        
        path = 'data/hist_' + symbol + '.csv'
        for day_data in data:
            cursor.execute(insert_query.format(
                symbol,
                day_data['Open'],
                day_data['High'],
                day_data['Low'],
                day_data['Close'],
                day_data['Date'],
                day_data['Volume']))

        conn.commit()

if __name__ == '__main__':
    main()