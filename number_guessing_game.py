import random
print("""Welcome to the Number Guessing Game!
 Try to guess the number between 1 and 100.""")

random_number=random.randint(1,100)


i=0;
while(1):
  try:
    guess_number=int(input("Enter your guess: "))
    i+=1
    if random_number>guess_number:
        print("Too Low!")
    elif random_number<guess_number:
        print("Too High!")
    elif random_number==guess_number:
        print(f"Congratulations! You've guessed the number in {i} attempts.")
        break
  except ValueError:
            print("Invalid input! Please enter a valid integer.")
