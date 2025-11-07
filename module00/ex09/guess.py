
import random
import sys

def main():
	print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")

	#randint to get random nb
	secret = random.randint(1, 99)
	#print(secret)
	count = 1
	
	while True : 

		guess = input("Guess a nb btwn 1 and 99\n").strip()

		if guess.lower() == "exit":
			print("bye")
			return
		if not guess.isdigit():
			print("nope that's not a number")
			continue
		guess = int(guess)
		count = count + 1 

		if guess == secret : 
			if secret == 42:
				print("the universe and everything is 42")
			#print(f"You won in {attempts} attempt{'s' if attempts > 1 else ''}!")
			print(f"you won in {count} attempt{'s' if count > 1 else ''}!")
			return

		elif guess > secret:
			print("too high")
		else:
			print("too low")
	


if __name__ == "__main__":
	raise SystemExit(main())