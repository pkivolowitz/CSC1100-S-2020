import datetime
import random

# Exceptions are "classes" - classes are bundles of user defined information
# (like message, time_stamp and random_number) and functions (like the
# special functions __init__ and __str__).
#
# __init__ is called to create or construct the instance of the class.
# __str__ is called when trying to evaluate a thing as a string.

class CustomException(Exception):
	def __init__(self, *args):
		if args:
			self.message = args[0]
		else:
			self.message = 'None'
		self.time_stamp = str(datetime.datetime.now())
		self.random_number = random.randint(10, 21)

	def __str__(self):
		if self.message:
			retval = 'Message: ' + self.message + ' '
		else:
			retval = 'Message: None '
		retval = retval + 'Time Stamp: ' + self.time_stamp + ' Random Number: ' + str(self.random_number)
		return retval

def OpenABadFile():
	bad_file_name = 'scooby_do_where_are_you.txt'
	try:
		file = open(bad_file_name)
		file.close()

	except OSError as err:
		# This essentially reformats the exception for passage upward
		raise CustomException('This is awkward')

def main():
	try:
		OpenABadFile()
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()
