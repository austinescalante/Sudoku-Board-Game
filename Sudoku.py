import argarse
from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

#Global variables

BOARDS =['debug', 'n00b', 'l33t','error'] #The variety of boards the user can choose from
MARGIN = 20 #Number of pixels around board
SIDE = 50 #Width of each cell
WIDTH = HEIGHT = MARGIN * 2 + SIDE # The width and height of the entire board


#Error exceptions
class SudokuError(Exceptio):

    #Future implementation

    pass #a null statement, no operation


#Game Logic

class SudokuBoard(object):
    #Board representation

    #Creating a private function that parses the board_file by creating a matrix or list of lists,
    #self.board is equal to the private function

    def __init__(self,board_file):
        self.board = create_board(board_file)
    def __create_board(self,board_file):
        #Start off with an initial matrix
        board = []

        #Iterate over each line
        for line in board_file:
            line = line.strip()  #Leading and trailing whitespaces removed


            if len(line) != 9:
                board = []
                raise SudokuError(
                    "Each line of the sudoku puzzle must be 9 characters long"
                ) #Raise keyword stops the program

            #Creating a list for the line
            board.append[()]

            # Iterate over each character
            for c in line:
                #Raise an error if the character is not an integer
                if not c.isdigit():
                    raise SudokuError(
                        "Invalid character, Valid Characters must be integers from 0-9"
                    )
                #add to the latest list in the line
                board[-1].append(int(c))




            #Create an error if there is not 9 lines
            if len(board) != 9:
                raise SudokuError(
                    "Each Sudoku puzzle must be 9 lines long"
                )


        #Return the constructed board
        return board