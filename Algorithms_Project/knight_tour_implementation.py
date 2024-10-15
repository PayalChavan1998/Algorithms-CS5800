# Project Topic: Knight Tour's Problem Using Backtracking
# Summer 2024
# CS5800 Algorithms (Seattle)
# Team Members: Anjali Haryani, Mengyuan Liu, Payal Chavan, Yuexin Ma
# Date: 08/15/2024

'''
Given an (N * M) chessboard, determine if there exists a sequence of moves for a knight such that it visits every square on the board exactly once. 
If such a sequence exists, provide the sequence of moves. If no such sequence exists, return an error message.
'''

import time # This module provides various time-related functions.
import sys  # Import the sys module for system-specific parameters and functions

# Import necessary classes and functions from PyQt5.QtWidgets
from PyQt5.QtWidgets import (
    QApplication,  # The main application class
    QMainWindow,   # The main window class
    QGridLayout,   # Layout manager for arranging widgets in a grid
    QWidget,       # Base class for all UI objects
    QLabel,        # Widget for displaying text or images
    QVBoxLayout,   # arranges widgets vertically, one below the other
    QSpinBox,      # A widget that allows users to input an integer value by either typing or using up/down arrows
    QPushButton,   # A clickable button widget
    QCheckBox,     # A widget that represents a checkbox 
    QDialog,       # A base class for creating custom dialog windows
    QHBoxLayout,   # arranges widgets horizontally
    QMessageBox    # Dialog for showing messages to the user
)

# Import necessary classes and functions from PyQt5.QtCore
from PyQt5.QtCore import (
    Qt,    # Namespace for various identifiers used in Qt
    QTimer # Timer class for creating timers
)

# Class to handle the logic of the Knight's Tour
class KnightTour:
    def __init__(self, rows, cols, show_backtracking=False):
        # Store the dimensions of the chessboard
        self.rows = rows
        self.cols = cols
        self.show_backtracking = show_backtracking      # Indicates whether to show backtracking steps.
        self.path = []
        self.board = [[-1 for _ in range(cols)] for _ in range(rows)]       # Initialize the board with -1
        self.moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]       # Possible knight moves

    # Define a function to check if the move is valid
    def is_valid_move(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == -1

    # Recursive function to solve the Knight's Tour problem
    def solve(self, r, c, move_i, visualizer):    
        # Place the knight on the board and update the path
        self.board[r][c] = move_i
        self.path.append((r, c))
        if self.show_backtracking:
            visualizer.update_board(self.board, self.path, False)

        if move_i == self.rows * self.cols - 1:  # Base Case 
            return True     # All cells are visited

        # Exploring Moves
        for move in self.moves:
            next_r, next_c = r + move[0], c + move[1]

            # is_valid_move() method ensures the move is within the board boundaries and the cell is unvisited
            if self.is_valid_move(next_r, next_c) and self.solve(next_r, next_c, move_i + 1, visualizer):
                return True

        # Backtrack: reset cell and remove from path
        if self.show_backtracking:
            visualizer.update_board(self.board, self.path, True)
        self.board[r][c] = -1
        self.path.pop()
        return False

    # Start the knight's tour
    def start_tour(self, visualizer = None):
        if self.solve(0, 0, 0, visualizer):
            print("Solution found!")
            self.print_board()
            return True
        else:
            print("No solution exists.")
            QMessageBox.information(None, "Knight's Tour", "No path found")
            return False
    
    # Print the board
    def print_board(self):
        for row in self.board:
            print(' '.join(str(cell).zfill(2) for cell in row))

# Class to visualize the Knight's Tour using PyQt5 library
class KnightTourVisualizer(QMainWindow):
    def __init__(self, knight_tour: KnightTour):  # Initialize the visualization window
        super().__init__()
        self.knight_tour = knight_tour
        self.labels = [[QLabel(self) for _ in range(knight_tour.cols)] for _ in range(knight_tour.rows)]
        self.init_ui()

    # Initialize the UI
    def init_ui(self):
        # Set up the grid layout for labels representing board cells
        self.setWindowTitle('Knight\'s Tour Visualization')
        self.setGeometry(100, 100, 600, 600)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        self.originalStyle = "QLabel { border: 1px solid black; font-size: 24px;}"

        for i in range(self.knight_tour.rows):
            for j in range(self.knight_tour.cols):
                self.labels[i][j].setAlignment(Qt.AlignCenter)
                self.labels[i][j].setStyleSheet(self.originalStyle)
                self.grid_layout.addWidget(self.labels[i][j], i, j)

        # If not showing backtracking, use a timer for step-by-step visualization
        if not self.knight_tour.show_backtracking:
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_board_tour)
            self.move_i = 0
            self.timer.start(500)   # Update every 500 milliseconds

    # Update the board with the knight's moves
    def update_board(self, board, path, do_backtrack):
        # Update labels based on the current board state
        for i in range(self.knight_tour.rows):
            for j in range(self.knight_tour.cols):
                cell_value = board[i][j]
                if cell_value == -1:
                    self.labels[i][j].setText("")
                    self.labels[i][j].setStyleSheet(self.originalStyle)
                else:
                    self.labels[i][j].setStyleSheet("QLabel { background-color : grey; border: 1px solid black; font-size: 24px;}")
                    self.labels[i][j].setText(f"<b>{cell_value}</b>")

        if do_backtrack and path:
            last_r, last_c = path[-1]
            self.labels[last_r][last_c].setStyleSheet("QLabel { background-color : red; border: 1px solid black; font-size: 24px;}")
            QTimer.singleShot(600, lambda: self.reset_cell_color(last_r, last_c))

        QApplication.processEvents()
        wait_time = 0.6 if do_backtrack else 0.3
        time.sleep(wait_time)

    # Reset the cell color
    def reset_cell_color(self, r, c):
        self.labels[r][c].setStyleSheet(self.originalStyle)

    # Visualize the knight's path step by step
    def update_board_tour(self):
        if self.move_i < len(self.knight_tour.path):
            x, y = self.knight_tour.path[self.move_i]
            self.labels[x][y].setText(str(self.move_i))
            self.move_i += 1
        else:
            self.timer.stop()

# Create a dialog for setting board dimensions
class InputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Knight's Tour Settings")
        self.show_backtracking = False
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Rows input
        rows_layout = QHBoxLayout()
        rows_label = QLabel("Rows:")
        self.rows_spinbox = QSpinBox()
        self.rows_spinbox.setRange(1, 20)
        self.rows_spinbox.setValue(3)
        rows_layout.addWidget(rows_label)
        rows_layout.addWidget(self.rows_spinbox)
        layout.addLayout(rows_layout)

        # Columns input
        cols_layout = QHBoxLayout()
        cols_label = QLabel("Columns:")
        self.cols_spinbox = QSpinBox()
        self.cols_spinbox.setRange(1, 20)
        self.cols_spinbox.setValue(4)
        cols_layout.addWidget(cols_label)
        cols_layout.addWidget(self.cols_spinbox)
        layout.addLayout(cols_layout)

        # Backtracking toggle
        self.backtracking_checkbox = QCheckBox("Show Backtracking")
        layout.addWidget(self.backtracking_checkbox)

        # OK and Cancel buttons
        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Set font size
        self.setStyleSheet("""
            QLabel, QSpinBox, QCheckBox, QPushButton {
                font-size: 24px;
            }
        """)

    def accept(self):
        # This method is called when the user clicks the "OK" button in the input dialog.
        # It retrieves the values from the input fields (rows, columns, and backtracking checkbox).
        self.rows = self.rows_spinbox.value()
        self.cols = self.cols_spinbox.value()
        self.show_backtracking = self.backtracking_checkbox.isChecked()
        super().accept()        # Call the base class accept method (closes the dialog)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = InputDialog()      # Create an instance of the InputDialog
    if dialog.exec_() == QDialog.Accepted:
        # If the user clicked "OK" in the dialog, retrieve the chosen values
        rows = dialog.rows
        cols = dialog.cols
        show_backtracking = dialog.show_backtracking

        # Print the chosen settings
        print("Running Knight's Tour with board size:", rows, "x", cols, " and show_backtracking:", show_backtracking)

        # Create a KnightTour instance with the chosen settings
        kt = KnightTour(rows, cols, show_backtracking)

        # Create a visualizer for the knight's tour
        visualizer = KnightTourVisualizer(kt)
        visualizer.show()

        # Start the knight's tour and check if a path was found
        path_found = kt.start_tour(visualizer)

        if not path_found:
            # close the KnightTourVisualizer window
            visualizer.close()

            # quit the application
            QApplication.quit()
            sys.exit()
        else:
            # wait till user closes the QMainWindow
            sys.exit(app.exec_())

