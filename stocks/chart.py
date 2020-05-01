import csv
import yfinance as yf 
from matplotlib import pyplot as plt 

def main(symbol):
	equity = yf.Ticker(symbol)
	data = equity.history(period='max')
	data = data.to_csv()
	lines = data.split('\n')
	reader = csv.reader(lines)
	next(reader)
	closing_price = []
	for row in reader:
		if len(row) > 4:
			closing_price.append(float(row[4]))

	xaxis = list(range(len(closing_price)))
	plt.plot(xaxis, closing_price)
	plt.title(symbol)
	plt.show()
	print(closing_price)

if __name__ == "__main__":
	main('MSFT')

