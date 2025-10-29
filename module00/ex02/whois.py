
import sys

def whois(input_number) :

	if (input_number == 0) :
		print("I'm Zero.")

	elif (input_number % 2 != 0) :
		print("I'm Odd.")
	
	elif (input_number % 2 == 0) :
		print("I'm Even.")
	
	return 0


def main() -> int: #type int to hint what types are expected
	args = sys.argv
	# print(len(args))
	if len(args) != 2 :
		print("Error : python3 whois.py < 1 input number only>. ")
		return 1
	
	try :
		num = int(args[1])
		# print(f"argument is an int:{num}")
	except ValueError:
		print("Error : argument is not an integer")
		return 1

	return(whois(num))


#only run this block of code if the file was executed directly (no import count file elsewhere)
if __name__== "__main__":
	raise SystemExit(main()) #clean exit behavior