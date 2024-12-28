# Playing a rock, paper and scissor game with computer
import random

print('Rock Paper Scissors Game')

while True:
    user = input('Enter the choice :').lower()         # to get user input
    
    while user not in ['rock', 'paper', 'scissors']:   
        print('Invalid choice. Try again.')
        user = input('Enter your choice : ').lower()

    computer = random.choice(['rock', 'paper', 'scissors'])   # computer's choice
    
    print(f'Computers choice: {computer}')
    
    if user == computer:
        print("It's a tie!")
        
    elif user == 'paper' and computer == 'rock':
        print('Paper covers rock! You win!')
        
    elif user == 'rock' and computer == 'scissors':
        print('Rock smashes scissors! You win!')
        
    elif user == 'scissors' and computer == 'paper':
        print('Scissors cuts paper! You win!')
        
    else:
        print('You lose. computer win!')

    play_again = input('\nDo you like to play again? (yes/no): ').lower()
    
    if play_again == 'yes':
        print('\nHurray! Lets play again!')

    elif play_again == 'no':
        print('Thank you for playing! See you next time')
        break
        
    else:
        print('Invalid choice!')
        break