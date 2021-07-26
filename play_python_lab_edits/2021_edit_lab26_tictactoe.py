class Player():
    def __init__(self,token,name='player1'):
        self.token = token
        self.name = name
    def __str__(self):
        return self.token
    @staticmethod # doesn't require self!
    def make_human_sound():
        print('ughhhh')
class Board():
    def __init__(self, winner=''):
        self.winner = winner                                                                 ##### TODO CHANGE BOARD IN FINAL #####
        self.board = [  ' ', ' ', ' ',
                        ' ', ' ', ' ',
                        ' ', ' ', ' '   ]

    def __repr__(self):
        return f'Current Game Board: \n{self.board[0]} | {self.board[1]} | {self.board[2]}\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n{self.board[6]} | {self.board[7]} | {self.board[8]}'

    def move(self, position, player):
        if self.board[position-1] != ' ':
            return False
        else:
            self.board[position-1] = f'{player.token}' # places token
            return True

    def calc_winner(self,player):
            # ALL 9 POSSIBLE WINNING INDICES in if statement below, written on individual lines in order:
            # 012 # horizontal win1             # 345 # horizontal win2             # 678 # horizontal win3
            # 036 # vertical win1               # 147 # vertical win2               # 258 # vertical win3
            # 048 # diagonal win1/2             # 246 # diagonal win2/2

        if self.board[0] == self.board[1] == self.board[2] == player.token:   # horizontal
            return player.token
        elif self.board[3] == self.board[4] == self.board[5] == player.token: # horizontal
            return player.token
        elif self.board[6] == self.board[7] == self.board[8] == player.token: # horizontal
            return player.token
        elif self.board[0] == self.board[3] == self.board[6] == player.token: # vertical
            return player.token
        elif self.board[1] == self.board[4] == self.board[7] == player.token: # vertical
            return player.token
        elif self.board[2] == self.board[5] == self.board[8] == player.token: # vertical
            return player.token
        elif self.board[0] == self.board[4] == self.board[8] == player.token: # diagonal 
            return player.token
        elif self.board[2] == self.board[4] == self.board[6] == player.token: # diagonal 
            return player.token
        else:
            return False

        # This is the old way I had it written (uglier but only 3 really long lines)
        # Q Q NOTE QQ Q which one is better for memory purposes?

        # if ( self.board[0] == player and self.board[1] == player and self.board[2] == 'X') or ( self.board[3] == self.board[4] == self.board[5]  == 'X') or ( self.board[6] == self.board[7] == self.board[8]  == 'X') or ( 
        #     self.board[0] == self.board[3] == self.board[6]  == 'X') or ( self.board[1] == self.board[4] == self.board[7]  == 'X') or ( self.board[2] == self.board[5] == self.board[8]  == 'X') or ( 
        #     self.board[0] == self.board[4] == self.board[8]  == 'X') or ( self.board[2] == self.board[4] == self.board[6]  == 'X') :
        #     self.winner = self.board[0]
        #     return True

    def is_full(self):
        filled_positions = 0
        for i in range(9):
            if self.board[i] == 'X' or self.board[i] == 'O':
                filled_positions += 1
        if filled_positions == 9:
            return True
        else:
            return False

    def is_game_over(self,player):
        if self.calc_winner(player) == player.token:
            return True
        else:
            if self.is_full() == True:
                return True
            else:
                return False

board_indices = [           '0', '1', '2',
                            '3', '4', '5',
                            '6', '7', '8'   ] # INDICES ONLY for writing the game
helper_board = Board()
helper_board.board = [      '1', '2', '3',
                            '4', '5', '6',
                            '7', '8', '9'   ] # FOR HELPING USER 

def main():

    print('Welcome to TIC-TAC-TOE v1.0!')

    # PLAYER_INITIALIZATION HERE # # originally had this as a function, but would have to return the players...
        
    player1 = Player('X',input(f'Enter name for player1: '))    # FOR TESTING : player1 = Player('X','Johnny!')
    print(f'{player1.name}, you have been assigned \"X\" as your token.')    
    player2 = Player('O',input(f'Please enter the name for player2: '))    # FOR TESTING : player2 = Player('O','computer42')
    print(f'{player2.name}, you have been assigned \"O\" as your token.')         

    board1 = Board() # create the game board   
    turn = 1 # turn % 1 is 1 for odd, player 1 moves, and 0 for even, player 2 moves
    next_player = player1 # first player. if this changes, need to change the if turn % 2 modulus statements to reverse them

    while True:             
        if turn % 2 == 0:
            next_player = player2
        else:
            next_player = player1        
        
        print(f'{next_player.name}, where will you place token {next_player.token}? Type \"help\" to see the game board, or \"exit\" to exit.')
        user_input = input()

        if user_input in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            user_input = int(user_input)
            if board1.move(user_input,next_player):
                print(f'Player \"{next_player.name}\" places \"{next_player.token}\" at position {int(user_input)}:')
                print('Current Game Board:')
                print(board1.__repr__())
                turn += 1    
            else:
                print(f'Position: {int(user_input)} is currently full! Please try again, type \"help\" to see the game board, or \"exit\" to exit.')
                print(board1.__repr__())
        elif user_input == 'help':
            print('Think of the board positions like an old phone keypad, numbered from top left to bottom right:')
            print(helper_board.__repr__())
            print('Current Game Board:')
            print(board1.__repr__())
        elif user_input == 'exit':
            break
        else:
            print(f'Invalid entry. Try again.')        

        if board1.is_game_over(next_player) == True:
            if board1.calc_winner(next_player) == 'X':
                print(f'Congratulations, {player1.name} won!')
            elif board1.calc_winner(next_player) == 'O':
                print(f'Congratulations, {player2.name} won!')
            else: # calc_winner = False, which means nobody won but the board is full anyway
                print('Board is full. Game over.')
                print('Boring outcome -- both players lost!')

            print('Play again, y/n?')
            user_input = input()
            if user_input == 'n':
                break
            else:
                board1 = Board()

# main()

##############################################################################

# # TEST MOVES
player1 = Player('X','Johnny!')
player2 = Player('O','computer42')
print(player1.make_human_sound())
board1 = Board()

board1.move(8,player1)
board1.move(5,player2)
# print('Current Game Board:')
print(board1.__repr__())
board1.move(3,player1)
board1.move(2,player2)
board1.move(1,player1)
board1.move(9,player2)
board1.move(4,player1)
board1.move(6,player2)
board1.move(7,player1) # X WINS
# print('Current Game Board:')
print(board1.__repr__())
print(board1.is_game_over(player1))
print(board1.calc_winner(player1))
# TODO review static methods@
# TODO review __magic__ methods
# 

# TEST BOARDS
    # test_board_blank = [    ' ', ' ', ' ',
    #                         ' ', ' ', ' ',
    #                         ' ', ' ', ' '   ]

    # test_board_1 = [        'X', 'O', 'O',
    #                         'X', 'O', 'X',
    #                         'O', 'X', 'O'   ] # FULL, NO WINNER

    # test_board_2 = [        'X', 'O', 'X',
    #                         'X', 'O', 'O',
    #                         'O', 'X', 'X'   ] # FULL, NO WINNER

    # test_board_3 = [        'X', 'X', 'X',
    #                         'O', 'O', 'X',
    #                         'X', 'O', 'O'   ] # X WINS

    # test_board_4 = [        'X', 'O', 'O',
    #                         'O', 'O', 'X',
    #                         'X', 'O', 'X'   ] # O WINS

    # test_board_5 = [        'X', 'O', 'O',
    #                         'O', ' ', 'X',
    #                         'X', 'O', 'X'   ] # NOT FULL


print('    >> PROGRAM ENDED <<    ')
##############################################################################
    
                                        # IN CASE I WANT LISTS OF LISTS:
                                        # self.board = [  [' '],[' '],[' '],
                                        #                 [' '],[' '],[' '],
                                        #                 [' '],[' '],[' ']   ]