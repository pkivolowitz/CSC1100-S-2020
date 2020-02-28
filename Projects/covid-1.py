import csv

def	GetCovidData(file_name):
	data = []
	with open(file_name) as file_object:
		reader = csv.reader(file_object)
		next(reader)
		for line in reader:
			data.append(line)
	return data

if __name__ == "__main__":
	covid_data = GetCovidData('02-27-2020.csv')
	print('Lines read:', len(covid_data))
	countries = { }
	for line in covid_data:
		country = line[1]
		if len(country) > 0:
			if country in countries:
				countries[country] += int(line[3])
			else:
				countries[country] = int(line[3])
	print(countries)
