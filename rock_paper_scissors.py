def rockpapperscissors():

    import random

    computer_win = 0
    user_win = 0
    options = ["rock","paper","scissors"]

    while True:
        user_input = input("enter (rock/paper/scissor or Q to quit)""\n:").lower()
        if user_input == "q":
            print("please condsider playing next time")
            break

        if user_input not in options:

            print("invalid input")
            continue

        random_number = random.randint(0,2)
        computer = options[random_number]
        print("computer picked", computer)

        if user_input == "rock" and computer == "scissors":
            print("you win!!")
            user_win +=1

        elif user_input == "paper" and computer == "rock":
            print("you win!!")
            user_win +=1

        elif user_input == "scissors" and computer == "paper":
            print("you win!!")
            user_win +=1

        else:
            print("computer wins!!")
            computer_win += 1

    print("computer won",computer_win,"time")
    print("you won",user_win,"time")
    print("GOOD BYE THANKS FOR PLAYING")

rockpapperscissors()
