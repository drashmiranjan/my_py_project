# here we buit a game called Rock paper sessior
'''
-1 = sessior
1 = Rock
0 = paper
'''
computer = -1
your_choice = input("Enter your Choice: ")
choice_Dict = {
        "s": -1,
        "r": 1,
        "p":0,
}
reverse_Dict = {
        -1: "sessior",
        1: "rock",
        0: "paper",
}
you = choice_Dict[your_choice]

print(f"you chose {reverse_Dict[you]} and computer chose {reverse_Dict[computer]}")

if computer == you:
    print("match Draw..")

if ((computer + you) == -1 and (computer + you) == 1):
    print("you loss")
else:
    print("you won..")

# elif computer == -1 and you == 1: #computer + you = 2
        # Here the winner is the user
# like This if the sum of computer number and your number is -1 or 1 then you loss