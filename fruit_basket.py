
fruit_basket = ["apple", "pear", "strawberry", "pineapple", "orange"]

fruit_guess = ""
guess_correct = False

while(guess_correct is False):
	fruit_guess = input("Guess what fruit is in the basket.\n")
	if fruit_guess in fruit_basket:
		print ("Yes!")
		guess_correct = True
	else:
		fruit_guess = input("Try again! \n")
	

