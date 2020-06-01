import argparse
from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

#Global variables

BOARDS =['debug', 'n00b', 'l33t','error'] #The variety of boards the user can choose from
MARGIN = 20 #Number of pixels around board
SIDE = 50 #Width of each cell
WIDTH = HEIGHT = MARGIN * 2 + SIDE # The width and height of the entire board


#Error exceptions
class SudokuError(Exception):

    #Future implementation

    pass #a null statement, no operation


#Game Logic

class SudokuBoard(object):
    #Board representation

    #Creating a private function that parses the board_file by creating a matrix or list of lists,
    #self.board is equal to the private function

    def __init__(self,board_file):
        self.board = self.__create_board(board_file)
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


class SudokuGame(object):
    #Incharge of storing ths status of the board and checking if the puzzle is complete

    def __init__(self,board_file):
        self.board_file =board_file
        self.start_puzzle = SudokuBoard(board_file).board

    #Setup for the users to play

    #initially set the game over flag to false and later charge to true once the puzzle is complete
    #We also create a copy to clear the board at the end of the game as well as check the answers against the start board

    def Start(self):
        self.game_over = False
        self.puzzle = []
        for i in range(9):
            self.puzzle.append([])
        for j in range(9):
            self.puzzle[i].append(self.start_puzzle[i][j])


#Checking the answers to see if the user won the puzzle, and check the board's row, columns  and each 3x3 square
    def check_win(self):
        for row in range(9):
            if not self.__check_row(row):
                return False
        for column in range(9):
            if not self.__check_column(column):
                return False
        for row in range(9):
            for column in range(9):
                if not self.__check_square(row, column):
                    return False
        self.game_over = True
        return True


    #Checking inputted numbers(helper functions)

    def __check_block(self,block):
        return set(block) == set(range(1,10))
    def __check_row(self,row):
        return set.__check_block(self.puzzle[row])
    def __check_column(self,column):
        return set.__check_block([self.puzzle[row][column] for row in range(9)])
    def __check_square(self,row,column):
        return self.__check_block(
            [
                self.puzzle[r][c]
                for r in range(row * 3, (row + 1) * 3)
                for c in range(column * 3, (column +1) * 3)




            ]
        )
#Check block returns true if the block passed in(row, column or square) is eqaul to set(range(1,10)). The set(range(1,10)) means only numbers 1 thru 9 are valid.
#If the block is padded in then False is returned

#Check row and column iterate over each row/column of the puzzle with the user's input and passes it to check_block. Check square does the same thing but not with with row
#and columns but a 3x3 square



#Implement GUI

#Represent the Sudoku UI

class SudokuUI(Frame):
    #Responsible for drawing the board and accpeting user input

    #For each new game we create a new UI, SudokuUI with a game and parent. Parent is the main window of the whole program

    def __init__(self,parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self,parent)

        self.row, self.col = 0, 0

        self.__initUI()


    def __initUI(self):
        self.parent.title("Sudoku")

        #self.pack is a frame attribute that organizes the frame's geometry relative to the parent. We wnat to fill the entire frame, so fill=both means both vert and horiz
        self.pack(fill= BOTH, expand = 1)
        #canvas is a general purpose widget so we can diplay the board.The global variables of width and height will help us setup tne canvas
        self.canvas = Canvas(self, width =WIDTH, height = HEIGHT)
        #A set pack where the entire square of the puzzle will fit in the space and will e pulled to the top part of the window
        self.canvas.pack(fill = BOTH, side = TOP)

        #We create a button attribbute using Button, giving it a text and a command when its pressed.
        clear_button = Button(self, text = "Clear answers", command = self.__clear_answers)

        #We set a pack for the button to fill the space, and sit at the bottom of the window
        clear_button.pack(fill = BOTH, side = Button)

        #Two helper functions
        self.__draw_grid()
        self.__draw_puzzle()



        #The first canvas bind is binding the Button-1 to a callback to cell_clicked. The Button-1 is a mouse click and refers to left click
        #When the user clicks on the puzzle with a single left click, the UI cell_clicked is called. The bind method passes in x and y location of the cursor
        #where cell_clicked will turn into cells of the puzzle
        #Key is used in the same fashion, where the __key_pressed will bind the key the user enters(number) to the method.
        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)


