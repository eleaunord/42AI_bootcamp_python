import sys

def program(input_string) :

	result = input_string[::-1].swapcase()
	print(result)
	return 0

def main():
	args = sys.argv
	# print("number of arguments :", len(args) - 1)
	# print("arugments: ", sys.argv[1])

	if len(args) <= 1 : 
		print("usage : python3 exec.py <string(s) you want to write>")
		return 1
	input_string = " ".join(args[1:])
	# print(input_string)
	return (program(input_string))
	

if __name__ == "__main__":
	raise SystemExit(main())