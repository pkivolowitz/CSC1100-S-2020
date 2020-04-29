# This program demonstrates both raising an exception AND
# having an exception percolating upward.

def OpenABadFile():
	bad_file_name = 'scooby_do_where_are_you.txt'
	try:
		file = open(bad_file_name)
		file.close()

	except OSError as err:
		# This essentially reformats the exception for passage upward
		raise Exception('A file was particularly naughty', err.filename)

def main():
	try:
		OpenABadFile()
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()
