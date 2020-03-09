#TicTacToe Exam
# Tomas,Leonardo Jr.,C.
"""
Instruction:
 Create a web app tic-tac-toe program using any of these languages (Python/Django),
 and database (SQLite). You don’t need
 to create a nice-looking UI. Just provide a way for 2 players to play tic-tac-toe.

You are NOT allowed to search for or copy any code from the Internet. You must write your code from scratch.
However, you are allowed to search for syntax of the programming language of your choice in w3schools.com or other reference sites.
1. You may identify the tic-tac-toe cells as numbers 1 to 9.
2. Player 1 will enter the cell number where he will place his token
3. A9fter that, Player 2 will enter the cell number where he will place his token
4. The application should check if there is a winner and display a message (e.g., “Player 1 wins!”)
5. Save the score in your preferred database. Show high score feature (web page showing player names and scores; from highest score to lowest score).

Instructions for Submission:
1.Take a video of the game being played with Player 1 winning. Then Player 2 winning. Then a draw.
2.Upload the video as an Unlisted Video on YouTube.
3.Put your code in a bitbucket, github, gitlab or any alternative git repository hosting.
4.Email the YouTube link and the repository URL to your code
5.Kindly send your exam to tech-exam@achievewb.com, art.ruado@achievewithoutborders.com,
and kenza.batac@achievewithoutborders.com
"""

theBoard ={'7': ' ', '8': ' ', '9': ' ',
           '4': ' ', '5': ' ', '6': ' ',
           '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

#for showing the board
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['6'] + '|' + board['5'] + '|' + board['4'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#main function for the game
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
                print("that place is already filled. \nMove to which place?")
                continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()
