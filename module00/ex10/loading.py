
from time import time, sleep

#while the loop runs the progress bar is printed on the same line
#must be an iterable that yields one element at a time
def ft_progress(listy):
	total = len(listy)
	start = time()

	for i, elem in enumerate(listy, start=1):
		elapsed = time() - start #how many seconds have passed since start, starting at 1
		eta = elapsed * (total - i) / i if i > 0 else 0
		#eta = estimated time of arrival
		#elapsed / i => average time per step so far
		#total - i => steps remaining
		#estimate time left = average time per step * steps remaiing
		percent = int(i * 100 / total)

		bar_len = 20
		done = int(bar_len * percent/100)
		bar = "="* done + ">" + " " *(bar_len - done - 1) # - 1 for >
		print (
			f"\rETA: {eta:5.2f}s [{percent:3d}%][{bar}]"
			f"{i}/{total} | elapsed time {elapsed:5.2f}s",
			end = ""
		)
		#eta:5.2f => float with 2 decimals, width 5
		#percent:3d => means use at least 3 characters for this number pad w/ spaces on the left if needed


		yield elem
	print() #newline

def main():

	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy): #ft_progress(listy) returns a generator
	#at each iteration ft_progress updates and prints the progress bar, then
	#the yield elem sends the current elem back to the loop 
	#and the function is paused until next iteration
		ret += (elem + 3) % 5 #stimulate work inside the looop
		sleep(0.01)
	print()
	print(ret)



if __name__=="__main__":
	raise SystemExit(main())