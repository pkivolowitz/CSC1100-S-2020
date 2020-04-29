
def main():
	bad_file_name = 'scooby_do_where_are_you.txt'
	try:
		file = open(bad_file_name)
		file.close()

	except OSError as err:
		# OSError has an additional member 'errno'
		print('An OSError happened - this is the error number:', err.errno)
		print('\nThis is the full string provided:')
		print(err)
		print('\nThis is the short error message:')
		print(err.strerror)
		print('\nThis is the name of the offending file:')
		print(err.filename)

if __name__ == '__main__':
	main()
