# Activity 4
player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")

player1_inp = input(player1 + ", do you want to choose rock, paper or scissors? ")
player2_inp = input(player2 + ", do you want to choose rock, paper or scissors? ")


if player1_inp == player2_inp:
    print("It's a tie!")
elif player1_inp == 'rock':
    if player2_inp == 'scissors':
        print("rock wins!")
    else:
        print("paper wins!")
elif player1_inp == 'scissors':
    if player2_inp == 'paper':
        print("scissors win!")
    else:
        print("rock wins!")
elif player1_inp == 'paper':
    if player2_inp == 'rock':
        print("paper wins!")
    else:
        print("scissors win!")
else:
    print("Value entered is not as rock, paper or scissors.")

# again asking to repeat the game
repeat = input("Do you want to play another round? Yes/No: ")
if(repeat == "yes"):
	pass
elif(repeat == "no"):
	 raise SystemExit
else:
    print("You entered an invalid option. Exiting now.")
raise SystemExit