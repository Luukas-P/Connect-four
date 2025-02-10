"""
Game logic in this file.
"""

from tkinter import *
from tkinter import colorchooser, messagebox
import random


class Player:
    # A class that represents a player in the game, the class does not use the
    # .__ after self because we want to access the attributes in class ConnectFour
    def __init__(self, name, default_color=None):
        """
        Initialize the attributes of the class; name, color, score
        :param name: either player_1 or player_2
        :param default_color: None before being chosen from colorchooser
        """
        self.name = name
        self.color = default_color
        self.score = 0


class Board:
    # The class manages the game board, does not use .__ because the ConnectFour
    # needs to be able to access the attributes and methods of this class.
    def __init__(self, rows, columns, circle_size, canvas, switch_player):
        """
        Initialize the attributes of the class: rows, colums, piece_size,
        canvas widget, and a function for switching players
        :param rows: the amount of rows on the board
        :param columns: the amount of columns on the board
        :param circle_size: the size of the circle on the board
        :param canvas: the way to draw the circle on the board
        :param switch_player: allows to draw the right color pieces
        """
        self.rows = rows
        self.columns = columns
        self.circle_size = circle_size
        self.canvas = canvas
        self.switch_player = switch_player
        # the board is a 2d array, with the first list being rows and the second
        # list the columns of the board. The column elements are all initialized as
        # 0 which represent an empty cell
        self.board = [[0] * columns for _ in range(rows)]

    def draw_board(self, current_player):
        """
        Method to draw the game board
        :param current_player: allows to determine the color of the pieces
        """
        # Make the canvas blank before drawing anything on it
        self.canvas.delete("all")
        # Using loops draw all of the pieces on the board
        for row in range(self.rows):
            for col in range(self.columns):
                self.draw_piece(row, col, current_player)

    def draw_piece(self, row, col, current_player):
        """
        Method to draw a singular piece on the board
        :param row: the row the piece that is to be drawn
        :param col: the column the piece that is to be drawn
        :param current_player: the current player to determine piece color
        """
        player_color = current_player.color
        # Check if the content of the circle is owned by the player and if it is
        # the circles color is changed to the players color, otherwise the circle
        # is white
        if self.board[row][col] == current_player:
            piece_color = player_color
        else:
            piece_color = "white"

        # the coorinates which are used to draw the circle, the +5 and -10
        # are used to make it so that the circles have some room between each other
        x0 = col * self.circle_size + 7
        y0 = row * self.circle_size + 7
        x1 = x0 + self.circle_size - 10
        y1 = y0 + self.circle_size - 10

        # Using create_oval widget to draw the circles in the game
        self.canvas.create_oval(x0, y0, x1, y1, fill=piece_color, outline="Black")


class ConnectFour:
    # The main class of the game that ties it all together.
    def __init__(self, main_window):
        """
        Initialize the games attributes
        :param main_window: the main window of the game
        """
        self.__mainw = main_window
        self.__mainw.title("Connect Four")
        # Stops the changing of the window size
        self.__mainw.resizable(False, False)

        self.__rows = 6
        self.__columns = 7
        self.__circle_size = 70

        self.__players = [Player("Player 1"), Player("Player 2")]
        # make the starting player random
        starting_player = random.randint(0, 1)
        self.__current_player = self.__players[starting_player]
        self.__board = Board(self.__rows, self.__columns, self.__circle_size,
                             self.create_canvas(), self.switch_player)

        self.create_gui()

    def create_canvas(self):
        """
        Method to create the canvas
        :return: canvas
        """
        canvas = Canvas(self.__mainw, width=self.__columns * self.__circle_size,
                        height=self.__rows * self.__circle_size, bg="royal blue")
        canvas.grid(row=1, column=0, pady=10, columnspan=2)
        # Use bind to allow for dropping of pieces with left click on the screen
        canvas.bind("<Button-1>", self.drop_piece)
        return canvas

    def create_gui(self):
        """
        Method to create the graphical user intereface
        """
        # Score display on the top of the game board
        self.__score_label = Label(self.__mainw,
                                   text=f"{self.__players[0].name}: 0  "
                                   f"/  {self.__players[1].name}: 0",
                                   font=("Times New Roman", 18), bg="steel blue",
                                   fg="white")
        self.__score_label.grid(row=0, column=0, columnspan=2)

        # Menu (rules and quit)
        self.__menu_bar = Menu(self.__mainw)
        self.__mainw.config(menu=self.__menu_bar)

        self.__file_menu = Menu(self.__menu_bar, tearoff=0)
        self.__menu_bar.add_cascade(label="Rules / quit", menu=self.__file_menu)

        self.__file_menu.add_command(label="Rules", command=self.show_rules)
        self.__file_menu.add_command(label="Quit", command=self.__mainw.quit)

        # Player's color display frame
        self.__players_display = Frame(self.__mainw, bg="black")
        self.__players_display.grid(row=2, column=0, pady=5, columnspan=2)

        # Buttons for player 1 and 2 to choose a color
        self.__player1_button = Button(self.__mainw,
                                       text=f"{self.__players[0].name} Color",
                                       command=lambda: self.choose_color(1),
                                       font=("Helvetica", 12), bg="gold")
        self.__player1_button.grid(row=3, column=0, pady=5, padx=(0, 10))

        self.__player2_button = Button(self.__mainw,
                                       text=f"{self.__players[1].name} Color",
                                       command=lambda: self.choose_color(2),
                                       font=("Helvetica", 12), bg="gold")
        self.__player2_button.grid(row=3, column=1, pady=5, padx=(10, 0))

        # Color and name display
        self.__player1_name_label = Label(self.__players_display,
                                          text=self.__players[0].name,
                                          font=("Helvetica", 12), bg="black",
                                          fg="white")
        self.__player1_name_label.grid(row=0, column=0, padx=10)

        self.__player2_name_label = Label(self.__players_display,
                                          text=self.__players[1].name,
                                          font=("Helvetica", 12), bg="black",
                                          fg="white")
        self.__player2_name_label.grid(row=0, column=2, padx=10)

        # default color for color square is black
        # the white highlights allow for the color to be seen even if black
        self.__player1_square = Canvas(self.__players_display, width=20, height=20,
                                       bg="black", highlightthickness=1,
                                       highlightbackground="white")
        self.__player1_square.grid(row=0, column=1, padx=5)

        self.__player2_square = Canvas(self.__players_display, width=20, height=20,
                                       bg="black", highlightthickness=1,
                                       highlightbackground="white")
        self.__player2_square.grid(row=0, column=3, padx=5)

        # Draw initial game board
        self.draw_board()

    def switch_player(self):
        """
        Switches the player to the other one
        :return: current new player (1 -> 2 or 2 -> 1)
        """
        if self.__current_player == self.__players[0]:
            self.__current_player = self.__players[1]
        else:
            self.__current_player = self.__players[0]
        return self.__current_player

    def show_rules(self):
        """
        Shows the rules in a messagebox
        """
        rules_text = (
            "Connect Four Rules:\n"
            "1. The game is played on a 6x7 grid.\n"
            "2. Players take turns dropping their pieces from the top.\n"
            "3. The pieces occupy the lowest free space in the board \n" 
            "4. The goal is to connect four of their own "
            "discs vertically, horizontally, or diagonally.\n"
            "5. The first player to connect four discs in a row wins!\n"
        )
        messagebox.showinfo("Connect Four - Rules", rules_text)

    def draw_board(self):
        """
        Draws the current state of the game board using the class board
        """
        self.__board.draw_board(self.__current_player)

    def choose_color(self, player):
        """
         Allows the player to choose a color for their pieces using colorchooser.
        :param player: the player choosing the color
        """
        color = colorchooser.askcolor()[1]

        if player == 1:
            self.__players[0].color = color
        else:
            self.__players[1].color = color
        self.update_players_display()
        # Disable the buttons after both players have chosen colors.
        if self.__players[0].color and self.__players[1].color:
            self.__player1_button.config(state="disabled")
            self.__player2_button.config(state="disabled")
            # Messagebox to inform the player the game can begin
            messagebox.showinfo("Connect Four",
                                "Both players have chosen colors. "
                                "Let the game begin!")

    def drop_piece(self, event):
        """
        This method handles the dropping of the pieces and check if the game is won,
        a draw or continues switching the current player
        :param event: The event object containing mouse click information.
        """
        # prevents the game starting before a color is chosen. Uses a messagebox
        # to inform the player.
        if self.__players[0].color is None or self.__players[1].color is None:
            messagebox.showinfo("Connect Four",
                                "Both players need to choose colors first.")
            return

        # using the x-coordinate of the mouse click get the column that is clicked on
        col = event.x // self.__circle_size
        row = self.find_empty_row(col)

        if row is not None:
            # place the current player's piece on the board
            self.__board.board[row][col] = self.__current_player
            # draw the piece on the canvas
            self.__board.draw_piece(row, col, self.__current_player)
            # check winner based on current move
            if self.check_winner(row, col):
                if self.__current_player == self.__players[0]:
                    winner = self.__players[0].name
                else:
                    winner = self.__players[1].name

                messagebox.showinfo("Connect Four", f"{winner} wins!")
                self.update_scores(winner)
                self.reset_game()
            # check if the game is a draw
            elif self.is_board_full():
                messagebox.showinfo("Connect Four", "The game is a draw!")
                self.reset_game()
            # switch players if not a winning move or a draw
            else:
                self.switch_player()

    def find_empty_row(self, col):
        """
        Finds the lowest empty row in a given column that is determied by a mouse
        click.
        :param col: the column that is clicked on the board
        :return: None if column is full, otherwise the lowest free row
        """
        for row in range(self.__rows - 1, -1, -1):
            if 0 <= row < self.__rows and 0 <= col < self.__columns:
                if self.__board.board[row][col] == 0:
                    return row
        return None

    def is_board_full(self):
        """
        Check the wheahter the board is full by looking at the topmost row.
        :return: True if the first row of the board is True and if not False
        """
        return all(self.__board.board[0])

    def check_winner(self, row, col):
        """
        The method checks if the current move results in a win.
        :param row: the row a piece is placed
        :param col: the column a piece is placed
        :return: True if the player win and false if not.
        """
        # Check right, left, and diagonal pieces of the dropped piece
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for d_row, d_col in directions:
            count = 1
            # check left, right and diagonally up the board
            for number in range(1, 4):
                r, c = row + number * d_row, col + number * d_col
                if 0 <= r < self.__rows and 0 <= c < self.__columns and \
                        self.__board.board[r][c] == self.__current_player:
                    count += 1
                else:
                    break

            # check left right and diagonally down the board
            for number in range(1, 4):
                r, c = row - number * d_row, col - number * d_col
                if 0 <= r < self.__rows and 0 <= c < self.__columns and \
                        self.__board.board[r][c] == self.__current_player:
                    count += 1
                else:
                    break

            # if the game is won return True
            if count >= 4:
                return True
        # if the game is not won return False
        return False

    def update_scores(self, winner):
        """
        Updates the scoreboard depending on who the winner is.
        :param winner: check winner checks the winner and its saved under winner
        """
        if winner == self.__players[0].name:
            self.__players[0].score += 1
        else:
            self.__players[1].score += 1

        self.__score_label.config(
            text=f"{self.__players[0].name}: {self.__players[0].score}  "
                 f"  {self.__players[1].name}: {self.__players[1].score}")

    def update_players_display(self):
        """
        This method updates the color display after a player chooses their color
        """
        self.__player1_name_label.config(text=self.__players[0].name)
        self.__player2_name_label.config(text=self.__players[1].name)
        self.__player1_square.config(bg=self.__players[0].color)
        self.__player2_square.config(bg=self.__players[1].color)

    def reset_game(self):
        """
        Reset the game and choose a random player to start if the game is won or draw
        """
        self.__board.board = [[0] * self.__columns for _ in range(self.__rows)]
        starting_player = random.randint(0, 1)
        self.__current_player = self.__players[starting_player]
        self.update_players_display()
        self.draw_board()


def main():
    main_window = Tk()
    ConnectFour(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    main()
