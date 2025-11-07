import string 


import sys
import string

#dictionnary morse code 

# sos.py
import sys

MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/"      # space becomes slash
}



def main():
	args = sys.argv
	if len(args) == 1:
		print("Usage : enter an argument")
		return
	text = " ".join(args[1:]).upper()
	print(text)
	answer = []
	for ch in text : 
		if ch in MORSE : 
			answer.append(MORSE[ch])
		else : 
			print("ERROR")
			return
	print(" ".join(answer))




if __name__ == "__main__":
	raise SystemExit(main())
