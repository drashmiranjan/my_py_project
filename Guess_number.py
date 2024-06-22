import random
n = random.randint(1 , 100)
a = -1
guesses = 0

while (a != n):
    guesses +=1
    a = int(input("Guess the number between 1 to 100: "))
    if(a>n):
        print("Guess lower number..")
    else:
        print("Guedd higher number..")

print(f"Hurrew you guessed the number {n} in {guesses} attempt")