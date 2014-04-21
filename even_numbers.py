# This program extracts even numbers from an input array of other numbers

numbers = [1,2,3,4,5,6,7]

def even_number(numbers):
	print numbers
	for number in numbers:
		if number%2 == 0:
			print number

even_number(numbers)

raw_input("")

print 'hello world'