import random

print("Enter 1 for Easy" + "\n" + "Enter 2 for Medium" + "\n" + "Enter 3 for Hard")

print(". . . . . . . . . . . . . . . . . . . . .")
chs = int(input("Enter difficulty level: "))

def easy():
  n = random.randint(1, 10)
  print("Dificulty: Easy" + "\n" +"You have 6 guesses.")
  guess = int(input("Enter a number from 1 to 10: "))
  while n != "guess":
    print
    if guess < n:
        print ("Low");
        guess = int(input("Enter a number from 1 to 10: "))
    elif guess > n:
        print ("guess is high");
        guess = int(input("Enter a number from 1 to 10: "))
    else:
        print ("You guessed it right!");
        print ("GAME OVER!!!");
        break;
    #print

def medium():
  n = random.randint(1, 20)
  print("Dificulty: Medium" + "\n" +"You have 4 guesses.")
  guess = int(input("Enter a number from 1 to 20: "))
  while n != "guess":
    print
    if guess < n:
        print ("guess is low");
        guess = int(input("Enter a number from 1 to 20: "))
    elif guess > n:
        print ("guess is high");
        guess = int(input("Enter a number from 1 to 20: "))
    else:
        print ("You guessed it right!");
        print ("GAME OVER!!!");
        break;
    #print

def hard():
  n = random.randint(1, 50)
  print("Dificulty: Hard" + "\n" +"You have 3 guesses.")
  guess = int(input("Enter a number from 1 to 50: "))

  while n != "guess":
    print
    if guess < n:
        print ("guess is low");
        guess = int(input("Enter a number from 1 to 50: "))
    elif guess > n:
        print ("guess is high");
        guess = int(input("Enter a number from 1 to 50: "))
    else:
        print ("You guessed it right!");
        print ("GAME OVER!!!");
        break;
    #print

if chs == 1:
  easy()
elif chs == 2:
  medium()
elif chs == 3:
  hard()