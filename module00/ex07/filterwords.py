
import sys
import string

def main():
	args = sys.argv
	if len(args) != 3:
		print("ERROR")
	if type(args[1]) != str :
		print("ERROR")
	try : 
		num = int(args[2])
	except ValueError : 
		print("ERROR")
		return

	# split string into words separated by spaces
	wordlist = args[1].split()

	# str.maketrans(chars_to_replace, replacement_chars, chars_to_delete)
	table = str.maketrans('', '', string.punctuation)
	# .translate : takes a string and returns a new string where chars have been replaced / delted according to a translation table
	clean_words = [w.translate(table) for w in words]
	result = [w for w in clean_words if len(w) > num and w != ""]
	print(result)

if __name__ == "__main__":
	raise SystemExit(main())