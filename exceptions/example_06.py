# This example demonstrates causing one of several built-in exceptions.

import random

def main():

	for type_of_exception in range(4):
		try:
			if type_of_exception == 0:
				print('Demonstrating a TypeError')
				a = '2' + 2
			elif type_of_exception == 1:
				print('Demonstrating a ValueError')
				a = int('a')
			elif type_of_exception == 2:
				print('Demonstrating an IndexError')
				a = [ 1 ]
				print(a[99])
			elif type_of_exception == 3:
				print('Demonstrating a KeyError')
				a = { 'a': 17 }
				print(a['bad index'])
				
		except TypeError:
			print('A TypeError happened')
			print()
				
		except:
			print('A non-TypeError exception happened')
			print()

		finally:
			print('This is the finally block.')
			print('It could be used for cleaning up')
			print()

if __name__ == '__main__':
	main()
