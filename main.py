#Fixed Num guess game :]
import random 
play = input("Hello there !! would you like to play this game (yes/no): ")
if play == "yes":
    print("""Cool! 
          Let me explain how the game works!
          I picked a random number between 0-100 and you have to guess it """)
elif play == "no":
    print("thank you! have a good day")
    exit()
else:
    print("invalid choice! closing the game : ")
    exit()

#game logic part 

n = random.randint(1, 100)
max_g = 5 #maxium guesses 

print(f"I'm thinking of a number between 1 and 100")
print(f"You have {max_g} attempts to guess it")  
for guess in range(max_g):
    try:
        ui = input(f"Guesses left: {max_g - guess}\nGuess a number: ") #user input 
        a = int(ui)

        if a > n:
            print("Too high! Try a lower number")
        elif a < n:
            print("Too low! Try a higher number")
        else:
            print(f"\n🎉 Congratulations! You guessed the number {n} in {guess + 1} attempts")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer")

else:
    print(f"You've used all your attempts! The number was {n}")