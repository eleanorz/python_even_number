# This program extracts even numbers from an input array of other numbers

first_user_input = input("What number do you want to check?  ")

print type(first_user_input)
# if type(number) == string:
# 	pass "i am string"

numbers = [1,2,3,4,5,6,7]

if type(first_user_input) == int:
	first_user_input.append(number)
 	print "i am int"
elif type(first_user_input) == list:
	print "i am a list"
	print first_user_input
	numbers += first_user_input




def even_number(numbers):
	print numbers
	for number in numbers:
		if type(number) == int:
			if number%2 == 0:
				 print number

even_number(numbers)

# raw_input("exit")
