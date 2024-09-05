#Name: Nafis Anwar
#U-Number: U2092-0991
#Description: This is the driver program of a trivia game that executes the program by importing and running the other modules

#import function
from TriviaQns import questionlist

#driver function 

def main():
    questions = questionlist()
    round_number = 0 
    score = [0, 0]

    for question in questions:
        
        #Determine Round
        if round_number %2 == 0:
            print('Question for the first player.')
            current_player = 0
        else:
            print('Question for the second player.')
            current_player = 1
        
        #Start game
        print(question)
        answer = int(input("Enter your solution (a number between 1 and 4): "))

        #Check answer
        if question.check_answer(answer):
            print('That is the correct answer. You earn a point')
            print()
            score[current_player] += 1

        else:
            print(f"That is incorrect. The correct answer is {question.corr_ans}")
            print()

        round_number += 1 
    
    #score determinator 

    print(f"The first player earned {score[0]} points")
    print(f"The second player earned {score[1]} points")

    if score[0]>score[1]:
        print(f'The first player wins!')
    elif score[0]<score[1]:
        print(f'The second player wins!')
    else:
        print('The game is a tie')

main()



