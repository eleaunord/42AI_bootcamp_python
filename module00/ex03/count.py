#!/usr/bin/env python3

import sys
import string

def text_analyzer(single_string):
	#total nb of printable char
	i = 0
	nb = 0
	while i < len(single_string):
		if single_string[i].isprintable():
			nb = nb+1
		i += 1
	print(f"The text contains {nb} printable character(s).")

	# or nb_printable = sum(1 for c in single_string if c.isprintable())


	#nb of upper case


	i = 0
	nb_upp = 0
	while i < len(single_string):
		if single_string[i].isupper():
			nb_upp = nb_upp + 1
		i += 1
	print(f"- {nb_upp} upper letter(s)")

	#or nb_upper = sum(1 for c in single_string if c.isupper())

	#nb lower case
	i = 0
	nb_lower = 0
	while i < len(single_string):
		if single_string[i].islower():
			nb_lower = nb_lower + 1
		i += 1
	print(f"- {nb_lower} lower letter(s)")

	#or nb_lower = sum(1 for c in single_string if c.islower())

	#punctuation
	i = 0
	punc = 0
	while i < len(single_string):
		if single_string[i] in string.punctuation:
			punc = punc + 1
		i += 1
	print(f"- {punc} punctuation mark(s)")

	# or nb_punctuation = sum(1 for c in single_string if c in string.punctuation)

	#spaces
	i = 0
	spaces = 0
	while i < len(single_string):
		if single_string[i].isspace():
			spaces = spaces + 1
		i += 1
	print(f"- {spaces} space(s)")

	#or nb_spaces = sum(1 for c in single_string if c.isspace())

	

def main():

	if len(sys.argv) != 2 :
		print("Please enter a single string")
		return 1
	
	arg = sys.argv[1]

	if arg.lstrip('-').replace('.', '', 1).isdigit():
		print("Error : enter a string")
		return 1

	text_analyzer(arg)

if __name__ == "__main__":
    raise SystemExit(main())
