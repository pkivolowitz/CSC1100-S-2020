import csv
import numpy as np
import yfinance as yf

from sys import argv
from matplotlib import pyplot as plt

def FitAPolynomial(xaxis, yaxis, degree, style, label):
	coef = np.polyfit(xaxis, yaxis, degree)
	poly1d_fn = np.poly1d(coef)
	plt.plot(xaxis, poly1d_fn(xaxis), style, linewidth=2, label=label)

def MovingAverage(items, window_size):
	window= np.ones(int(window_size))/float(window_size)
	return np.convolve(items, window, 'same')

def main(symbol):
	try:
		equity = yf.Ticker(symbol)
		data = equity.history(period='3mo')
		data = data.to_csv()
		lines = data.split('\n')
		reader = csv.reader(lines)
		next(reader)
		closing_price = []
		for row in reader:
			if len(row) > 4:
				closing_price.append(float(row[4]))

		xaxis = list(range(len(closing_price)))
		plt.figure(figsize=(12,8))
		plt.plot(xaxis, closing_price, ':k')
		plt.plot(xaxis, closing_price, 'bo', label='Closing Price', markersize=4)

		FitAPolynomial(xaxis, closing_price, 1, '--r', 'Linear')
		FitAPolynomial(xaxis, closing_price, 3, '--g', 'Quadratic')
		FitAPolynomial(xaxis, closing_price, 4, '--b', 'Cubic')

		days = 5
		ma = MovingAverage(closing_price, days)
		xaxis = xaxis[days:]
		xaxis = xaxis[0: -days]
		ma = ma[days:]
		ma = ma[0: -days]
		plt.plot(xaxis, ma, 'm', linewidth=3, label=str(days) + ' DMA')

		plt.legend()
		plt.title(symbol)
		plt.show()


	except TypeError as ex:
		print(ex.args[0])

if __name__ == "__main__":
	symbol = 'MSFT'
	if len(argv) > 1:
		symbol = argv[1]
	main(symbol)

