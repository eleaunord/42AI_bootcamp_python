
import random

def main():
	print("Welcome + rules\n")

	secret = random.randint(1, 99)
	#print(secret)
	count = 0

	while True : 
		guess = input("what's your guess ?\n").strip()
		


		if guess.lower() == "exit":
			print("bye")
			return

		try : 
			realguess = int(guess)
		except ValueError : 
			print("a nb please")
			continue
			count = count + 1
		#print(count)
		if realguess == secret: 
			
			if secret == 42:
				print("universe ref")
				
			print(f"congrats in {count} attempt{'s' if count > 1 else ''}")
			return
		if realguess < secret:
            print("too low")
        else:
            print("too high")
		


if __name__=="__main__":
	raise SystemExit(main())