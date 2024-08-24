import random 

#dictionary to map input number into each items
number_to_item = {1: "scissor", 2: "paper", 3:"rock"}



#function to verify if the user input is validd
def verify_correct_entry(number):
    try:
        converted_number = int(number)
        if converted_number in range(1,4):
            return True
        else:
            return False
    except ValueError:
        return False
    

#function to display the result in a formatted manner after user have made their input
def display_result(computer, human, winner):

    if winner == None:
        return "game_tied"
    
    else:
        return f"computer chose {computer}, human chose {human}. \n {winner} is the winner"
    
#function to handle gameplay logic
def gameplay(computer_entry, human_entry):

    if computer_entry == human_entry:
        #winner variable is set to keep track of winner, if the winner is None, it means game is died
        winner = None
        return display_result(computer_entry, human_entry, winner)
    
    if human_entry == "scissor":
        if computer_entry == "paper":
            winner = "human"
        
        if computer_entry == "rock":
            winner = "computer"
        
    if human_entry == "paper":
        if computer_entry == "rock":
            winner = "human"
        
        if computer_entry == "scissor":
            winner = "computer"
        
    if human_entry == "rock":
        if computer_entry == "scissor":
            winner = "human"
        
        if computer_entry == "paper":
            winner = "computer"
        
    return display_result(computer_entry, human_entry, winner)
        
    

def main():
    #setting the start flag to True to start the game
    start = True
    while start:
        #generate a computer selection randomly
        computer_selection = number_to_item[random.randint(1,3)]
        
        #take input from the user and verify the input for correctness
        input_number = input("1: Scissor \n 2: paper \n 3:rock ")
        verification = verify_correct_entry(input_number)

        if verification == False:
            print("The entry is invalid, please enter the valid selection")
            continue

        #if verification is successful, run the gameplay logic
        else:
            human_select = number_to_item[int(input_number)]
            result = gameplay(computer_selection, human_select)
            print(result)


        #the game runs until the user decides they want to play no more, they can quit the game by pressing z
        quit = input("press Z to quit, anything else to continue playing").lower()

        if quit == 'z':
            start = False #sets the start flag to False

if __name__ == "__main__":
    main()





    


    