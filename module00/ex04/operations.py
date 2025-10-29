#!/usr/bin/env python3
import sys


def operations(a, b):
	print(f"Sum       : {a + b}")
	print(f"Difference: {a - b}")
	print(f"Product   : {a * b}")
	if (b != 0):
		print(f"Quotient  : {a / b}")
		print(f"Remainder : {a % b}")
	else:
		print("ERROR : division by zero")
		print("ERROR: modulo by zero")


def main():

	if len(sys.argv) > 3 or len(sys.argv) < 3:
		print("Error : must be two integers")
		return 1
	if len(sys.argv) == 1
		print("Usage : operations.py < 2 integers of your choice>")
		return 1

	try :
			a = int(sys.argv[1])
			b = int(sys.arv[2])
	except ValueError:
		print("ERROR : only integers accepted")
	
	operations(a,b)
	return 0


if __name__=="__main__":
	raise SystemExit(main())