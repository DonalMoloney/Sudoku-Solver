# Sudoku Game
# Developed by Donal Moloney
# Description: This is a Sudoku game implemented in Python using the Pygame library.
#              Players can solve Sudoku puzzles and select difficulty levels.
#              The game features a GUI interface with buttons and a rules popup.


import time
import pygame
import sudokum
from tkinter import messagebox


class Dropdown:
    """
    Represents a GUI Dropdown element.

    Attributes:
        pos_x, pos_y (int): Position of the dropdown.
        width, height (int): Dimensions of the dropdown and each item, respectively.
        options_list (list): List of available options.
        is_expanded (bool): True if expanded, False otherwise.
        current_index (int): Index of the selected option.
        color_scheme (tuple): RGB color of the dropdown.

    Args:
        pos_x, pos_y (int): Dropdown's position.
        width, height (int): Dropdown and item dimensions.
        options_list (list): Options for the dropdown.
        default_index (int, optional): Initial selected index. Defaults to 0.
    """

    def __init__(self, pos_x, pos_y, width, height, options_list, default_index=0):
        """
        Initialize the Dropdown with position, dimensions, options, and a default selection.

        Args:
            pos_x (int): X-coordinate of the dropdown's top-left corner.
            pos_y (int): Y-coordinate of the dropdown's top-left corner.
            width (int): Width of the dropdown.
            height (int): Height of each item in the dropdown.
            options_list (list): Options available for selection in the dropdown.
            default_index (int, optional): Index of the default selected option. Defaults to 0.
        """
        # Initializing the attributes of the Dropdown class
        self.pos_x = pos_x  # X position of the dropdown
        self.pos_y = pos_y  # Y position of the dropdown
        self.width = width  # Width of the dropdown
        self.height = height  # Height of each item in the dropdown
        self.options_list = options_list  # List of options in the dropdown
        self.is_expanded = False  # Boolean to check if dropdown is expanded
        self.current_index = default_index  # Index of the currently selected option
        self.color_scheme = (160, 160, 160)  # Color scheme of the dropdown

    def draw(self, window):
        """
        Render the dropdown on the provided window.

        Args:
            window (Surface): Pygame Surface to draw the dropdown on.
        """
        # Method to render the dropdown on the screen

        # Drawing the rectangle for the dropdown
        pygame.draw.rect(window, self.color_scheme, (self.pos_x, self.pos_y, self.width, self.height))

        # Setting the font style and rendering the label of the selected option
        font_style = pygame.font.SysFont('helvetica', 30)
        label = font_style.render(self.options_list[self.current_index], 1, (255, 255, 255))
        window.blit(label, (self.pos_x + 5, self.pos_y + 5))

        # If the dropdown is expanded, render all the options below the selected one
        if self.is_expanded:
            for index, option in enumerate(self.options_list):
                pygame.draw.rect(window, self.color_scheme,
                                 (self.pos_x, self.pos_y + (index + 1) * self.height, self.width, self.height))
                label = font_style.render(option, 1, (0, 0, 0))
                window.blit(label, (self.pos_x + 5, self.pos_y + 5 + (index + 1) * self.height))

    def click(self, position):
        """
        Handle a mouse click event. Expand/collapse the dropdown or select an option.

        Args:
            position (tuple): X and Y coordinates of the mouse click.

        Returns:
            str or None: The selected option's string if an option was clicked, None otherwise.
        """
        # Method to handle mouse clicks on the dropdown

        # If clicked within the bounds of the dropdown
        if self.pos_x < position[0] < self.pos_x + self.width:
            # If clicked on the dropdown when it is not expanded
            if self.pos_y < position[1] < self.pos_y + self.height and not self.is_expanded:
                self.is_expanded = not self.is_expanded
                return None
            # If clicked on an option in the dropdown when it is expanded
            elif self.pos_y + self.height < position[1] < self.pos_y + self.height * (
                    len(self.options_list) + 1) and self.is_expanded:
                # Calculating the index of the clicked option and updating the current index
                clicked_index = (position[1] - self.pos_y - self.height) // self.height
                self.current_index = clicked_index
                self.is_expanded = False
                return self.options_list[self.current_index]

    def get_selected_option(self):
        """
        Return the currently selected option from the dropdown.

        Returns:
            str: The selected option's string.
        """
        # Method to get the currently selected option
        return self.options_list[self.current_index]


class Button:
    """
    A class representing a clickable button widget.

    Attributes:
    button_x (int): The x-coordinate of the button's top-left corner.
    button_y (int): The y-coordinate of the button's top-left corner.
    button_width (int): The width of the button.
    button_height (int): The height of the button.
    button_label (str): The text label displayed on the button.
    button_color (tuple): The RGB color of the button background.
    font_style (pygame.font.Font): The font style used for the button label.

    Methods:
    render(window: pygame.Surface) -> None:
        Renders the button on the specified window surface.

    click(position: tuple) -> bool:
        Checks if the button is clicked based on the given mouse position.

    """

    def __init__(self, button_x, button_y, button_width, button_height, button_label):
        """
        Initializes a Button instance.

        Args:
        button_x (int): The x-coordinate of the button's top-left corner.
        button_y (int): The y-coordinate of the button's top-left corner.
        button_width (int): The width of the button.
        button_height (int): The height of the button.
        button_label (str): The text label displayed on the button.

        Returns:
        None
        """
        self.button_x = button_x
        self.button_y = button_y
        self.button_width = button_width
        self.button_height = button_height
        self.button_label = button_label
        self.button_color = (160, 160, 160)
        self.font_style = pygame.font.SysFont('helvetica', 20)

    def draw(self, window):
        """
        Renders the button on the specified window surface.

        Args:
        window (pygame.Surface): The pygame surface to render the button on.

        Returns:
        None
        """
        pygame.draw.rect(window, self.button_color,
                         (self.button_x, self.button_y, self.button_width, self.button_height))
        label = self.font_style.render(self.button_label, 1, (255, 255, 255))
        window.blit(label, (self.button_x + (self.button_width - label.get_width()) // 2,
                            self.button_y + (self.button_height - label.get_height()) // 2))

    def click(self, position):
        """
        Checks if the button is clicked based on the given mouse position.

        Args:
        position (tuple): A tuple containing the x and y coordinates of the mouse position.

        Returns:
        bool: True if the button is clicked, False otherwise.
        """
        return self.button_x < position[0] < self.button_x + self.button_width and self.button_y < position[
            1] < self.button_y + self.button_height


class Popup:
    """
    A class representing a popup window with text content.

    Attributes:
    x (int): The x-coordinate of the top-left corner of the popup.
    y (int): The y-coordinate of the top-left corner of the popup.
    width (int): The width of the popup window.
    height (int): The height of the popup window.
    text (str): The text content loaded from a file.
    visible (bool): Flag indicating whether the popup is currently visible.

    Methods:
    load_text_from_file(file_path: str) -> str:
        Loads text content from a file and returns it as a string.

    draw(win: pygame.Surface) -> None:
        Draws the popup window on the specified pygame surface if it is visible.

    wrap_text(text: str, font: pygame.font.Font, max_width: int) -> List[str]:
        Wraps the given text to fit within a maximum width and returns a list of wrapped lines.

    toggle() -> None:
        Toggles the visibility state of the popup.

    """

    def __init__(self, x, y, width, height):
        """
        Initializes a Popup instance.

        Args:
        x (int): The x-coordinate of the top-left corner of the popup.
        y (int): The y-coordinate of the top-left corner of the popup.
        width (int): The width of the popup window.
        height (int): The height of the popup window.

        Returns:
        None
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = self.load_text_from_file("instructions.txt")
        self.visible = False

    def load_text_from_file(self, file_path):
        """
        Loads text content from a file and returns it as a string.

        Args:
        file_path (str): The path to the text file.

        Returns:
        str: The text content read from the file.
        """
        with open(file_path, "r") as file:
            return file.read()

    def draw(self, win):
        """
        Draws the popup window on the specified pygame surface if it is visible.

        Args:
        win (pygame.Surface): The pygame surface to draw the popup on.

        Returns:
        None
        """
        if self.visible:
            pygame.draw.rect(win, (200, 200, 200), (self.x, self.y, self.width, self.height))
            font = pygame.font.SysFont('helvetica', 19)
            wrapped_text = self.wrap_text(self.text, font, self.width - 10)
            y_offset = 10
            for line in wrapped_text:
                rendered_text = font.render(line, 1, (0, 0, 0))
                win.blit(rendered_text, (self.x + 5, self.y + y_offset))
                y_offset += rendered_text.get_height() + 5

    def wrap_text(self, text, font, max_width):
        """
        Wraps the given text to fit within a maximum width and returns a list of wrapped lines.

        Args:
        text (str): The text to wrap.
        font (pygame.font.Font): The font used for rendering the text.
        max_width (int): The maximum width for each wrapped line.

        Returns:
        List[str]: A list of wrapped lines.
        """
        lines = []
        paragraphs = text.split('\n')

        for paragraph in paragraphs:
            words = paragraph.split(' ')
            current_line = []

            while words:
                word = words.pop(0)
                if word:  # Check if word is not empty
                    tentative_line = ' '.join(current_line + [word])
                    if font.size(tentative_line)[0] <= max_width:
                        current_line.append(word)
                    else:
                        lines.append(' '.join(current_line))
                        current_line = [word]

            if current_line:
                lines.append(' '.join(current_line))

        return lines

    def toggle(self):
        """
        Toggles the visibility state of the popup.

        Returns:
        None
        """
        self.visible = not self.visible


class Grid:
    """
    A class representing a Sudoku puzzle grid and user interface.

    Attributes:
    board (list[list[int]]): A 2D list representing the Sudoku puzzle.
    rows (int): The number of rows in the Sudoku grid.
    cols (int): The number of columns in the Sudoku grid.
    width (int): The width of the Sudoku grid.
    height (int): The height of the Sudoku grid.
    win (pygame.Surface): The pygame surface for rendering.
    model (list[list[int]]): A copy of the Sudoku puzzle for solving.
    selected (tuple): The currently selected cell (row, col).
    new_puzzle_button (Button): A button to generate a new puzzle.
    difficulty_dropdown (Dropdown): A dropdown menu for puzzle difficulty.
    rules_popup (Popup): A popup window displaying game rules.
    help_button (Button): A button to display help or instructions.

    Methods:
    get_mask_rate(difficulty: str) -> float:
        Gets the mask rate based on the selected difficulty level.

    generate_new_puzzle() -> None:
        Generates a new Sudoku puzzle and updates the model.

    generate_board() -> None:
        Generates a new Sudoku board based on the mask rate.

    update_model() -> None:
        Updates the model to reflect the current state of the grid.

    place(val: int) -> bool:
        Places a numeric value in the selected cell and checks for validity.

    sketch(val: int) -> None:
        Sets a temporary value in the selected cell.

    draw() -> None:
        Draws the Sudoku grid and UI elements on the pygame surface.

    select(row: int, col: int) -> None:
        Selects a cell in the Sudoku grid.

    clear() -> None:
        Clears the temporary value in the selected cell.

    click(pos: tuple) -> tuple or None:
        Converts a click position to row and column indices.

    is_finished() -> bool:
        Checks if the Sudoku puzzle is completed.

    solve() -> bool:
        Solves the Sudoku puzzle using a backtracking algorithm.

    solve_gui() -> bool:
        Solves the Sudoku puzzle step by step and updates the GUI.
    """

    board = []  # Initialize an empty Sudoku board

    def __init__(self, rows, cols, width, height, win):
        """
        Initializes a Grid instance.

        Args:
        rows (int): The number of rows in the Sudoku grid.
        cols (int): The number of columns in the Sudoku grid.
        width (int): The width of the Sudoku grid.
        height (int): The height of the Sudoku grid.
        win (pygame.Surface): The pygame surface for rendering.

        Returns:
        None
        """
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.win = win
        self.model = None
        self.selected = None

        # Create UI elements
        self.new_puzzle_button = Button(10, 550, 170, 50, "New Puzzle")
        self.difficulty_dropdown = Dropdown(185, 550, 100, 50, ["Easy", "Medium", "Hard"], default_index=1)
        self.rules_popup = Popup(100, 100, 400, 420)
        self.help_button = Button(300, 550, 40, 40, "?")

        # Ensure mask_rate is initialized before generating the board
        self.mask_rate = self.get_mask_rate(self.difficulty_dropdown.get_selected_option())
        self.generate_board()

        # Initialize cubes after the board has been generated
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.update_model()

    def get_mask_rate(self, difficulty):
        """
        Gets the mask rate based on the selected difficulty level.

        Args:
        difficulty (str): The selected difficulty level ("Easy", "Medium", or "Hard").

        Returns:
        float: The mask rate for the Sudoku puzzle.
        """
        if difficulty == "Easy":
            return 0.1  # Example mask rate for easy difficulty
        elif difficulty == "Medium":
            return 0.3  # Example mask rate for medium difficulty
        elif difficulty == "Hard":
            return 0.5  # Example mask rate for hard difficulty

    def generate_new_puzzle(self):
        """
        Generates a new Sudoku puzzle and updates the model.

        Returns:
        None
        """
        self.generate_board()
        self.update_model()
        self.selected = None

    def generate_board(self):
        """
        Generates a new Sudoku board based on the mask rate.

        Returns:
        None
        """
        new_board = sudokum.generate(mask_rate=self.mask_rate)
        self.board = new_board  # will always be 9 x 9
        self.cubes = [[Cube(self.board[i][j], i, j, 540, 540) for j in range(9)] for i in range(9)]

    def update_model(self):
        """
        Updates the model to reflect the current state of the grid.

        Returns:
        None
        """
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        """
        Places a numeric value in the selected cell and checks for validity.

        Args:
        val (int): The numeric value to place in the cell.

        Returns:
        bool: True if the placement is valid, False otherwise.
        """
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row, col)) and self.solve():
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        """
        Sets a temporary value in the selected cell.

        Args:
        val (int): The temporary value to set in the cell.

        Returns:
        None
        """
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def select(self, row, col):
        """
        Selects a cell in the Sudoku grid.

        Args:
        row (int): The row index of the cell to select.
        col (int): The column index of the cell to select.

        Returns:
        None
        """
        # Reset all other selections
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        # Set the selected cell
        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        """
        Clears the temporary value in the selected cell.

        Returns:
        None
        """
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        """
        Converts a click position to row and column indices.

        Args:
        pos (tuple): The x and y coordinates of the click position.

        Returns:
        tuple or None: A tuple containing the row and column indices, or None if not within the grid.
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return int(y), int(x)
        else:
            return None

    def is_finished(self):
        """
        Checks if the Sudoku puzzle is completed.

        Returns:
        bool: True if the puzzle is completed, False otherwise.
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

    def solve(self):
        """
        Solves the Sudoku puzzle using a backtracking algorithm.

        Returns:
        bool: True if a solution is found, False otherwise.
        """
        find = find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.model, i, (row, col)):
                self.model[row][col] = i

                if self.solve():
                    return True

                self.model[row][col] = 0

        return False

    def solve_gui(self):
        """
        Solves the Sudoku puzzle step by step and updates the GUI.

        Returns:
        bool: True if a solution is found, False otherwise.
        """
        self.update_model()
        find = find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.model, i, (row, col)):
                self.model[row][col] = i
                self.cubes[row][col].set(i)
                self.cubes[row][col].draw_change(self.win, True)
                self.update_model()
                pygame.display.update()
                pygame.time.delay(100)

                if self.solve_gui():
                    return True

                self.model[row][col] = 0
                self.cubes[row][col].set(0)
                self.update_model()
                self.cubes[row][col].draw_change(self.win, False)
                pygame.display.update()
                pygame.time.delay(100)

        return False

    def draw(self):
        """
        Draws the Sudoku grid and UI elements on the pygame surface.

        Returns:
        None
        """

        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(self.win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(self.win)

        # Draw UI elements
        self.new_puzzle_button.draw(self.win)
        self.difficulty_dropdown.draw(self.win)
        self.help_button.draw(self.win)
        self.rules_popup.draw(self.win)


class Cube:
    """
    A class representing a single cell in a Sudoku puzzle grid.

    Attributes:
    rows (int): The number of rows in the Sudoku grid.
    cols (int): The number of columns in the Sudoku grid.
    value (int): The numeric value of the cell (0 for empty).
    temp (int): Temporary value used for user input before confirmation.
    row (int): The row index of the cell in the grid.
    col (int): The column index of the cell in the grid.
    width (int): The width of the Sudoku grid cell.
    height (int): The height of the Sudoku grid cell.
    selected (bool): Flag indicating whether the cell is currently selected.

    Methods:
    draw(win: pygame.Surface) -> None:
        Draws the cell on the specified pygame surface.

    draw_change(win: pygame.Surface, g: bool = True) -> None:
        Draws a changed cell appearance on the specified pygame surface.

    set(val: int) -> None:
        Sets the numeric value of the cell.

    set_temp(val: int) -> None:
        Sets the temporary value of the cell.

    """

    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        """
        Initializes a Cube instance.

        Args:
        value (int): The numeric value of the cell (0 for empty).
        row (int): The row index of the cell in the grid.
        col (int): The column index of the cell in the grid.
        width (int): The width of the Sudoku grid cell.
        height (int): The height of the Sudoku grid cell.

        Returns:
        None
        """
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        """
        Draws the cell on the specified pygame surface.

        Args:
        win (pygame.Surface): The pygame surface to draw the cell on.

        Returns:
        None
        """
        fnt = pygame.font.SysFont("helvetica", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))
        elif not (self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def draw_change(self, win, g=True):
        """
        Draws a changed cell appearance on the specified pygame surface.

        Args:
        win (pygame.Surface): The pygame surface to draw the cell on.
        g (bool, optional): Flag indicating whether to highlight the cell in green. Defaults to True.

        Returns:
        None
        """
        fnt = pygame.font.SysFont("helvetica", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(win, (255, 255, 255), (x, y, gap, gap), 0)

        text = fnt.render(str(self.value), 1, (0, 0, 0))
        win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(win, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        """
        Sets the numeric value of the cell.

        Args:
        val (int): The new numeric value to set for the cell.

        Returns:
        None
        """
        self.value = val

    def set_temp(self, val):
        """
        Sets the temporary value of the cell.

        Args:
        val (int): The temporary value to set for the cell.

        Returns:
        None
        """
        self.temp = val


def find_empty(bo):
    """
    Finds the first empty cell (cell with value 0) in the Sudoku grid.

    Args:
    bo (list[list[int]]): The Sudoku grid as a 2D list.

    Returns:
    tuple or None: A tuple containing the row and column indices of the empty cell, or None if no empty cells are found.
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def valid(bo, num, pos):
    """
    Checks if placing a number in a particular cell is a valid move according to Sudoku rules.

    Args:
    bo (list[list[int]]): The Sudoku grid as a 2D list.
    num (int): The number to be placed in the cell.
    pos (tuple): A tuple containing the row and column indices of the cell.

    Returns:
    bool: True if the placement is valid, False otherwise.
    """
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def redraw_window(win, board, time, strikes):
    """
    Redraws the game window with updated information.

    Args:
    win (pygame.Surface): The pygame surface for rendering.
    board (Grid): The Sudoku grid object to be drawn.
    time (int): The elapsed time in seconds.
    strikes (int): The number of strikes (incorrect moves) made.

    Returns:
    None
    """
    win.fill((255, 255, 255))  # Clear the window

    # Draw time
    fnt = pygame.font.SysFont("helvetica", 35)
    text = fnt.render("Time: " + format_time(time), 1, (0, 0, 0))
    win.blit(text, (540 - 180, 540))

    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))

    # Draw grid and board
    board.draw()


def format_time(secs):
    """
    Formats a time duration in seconds as a string in the format 'hours minutes:seconds'.

    Args:
    secs (int): The time duration in seconds.

    Returns:
    str: The formatted time string.
    """
    seconds = secs % 60
    minutes = (secs // 60) % 60
    hours = (secs // 60) // 60

    formatted_time = f"{hours} {minutes}:{seconds}"
    return formatted_time


WINDOW_WIDTH, WINDOW_HEIGHT = 540, 770
GRID_SIZE = 9


def run_game():
    """
    Runs the Sudoku solver game. This function initializes the game window, handles user input events (keyboard and mouse),
    updates the game state, and redraws the window.

    Args: None

    Returns:
    None
    """
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sudoku Whiz")
    board = Grid(GRID_SIZE, GRID_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT - 230, win)
    start = time.time()
    strikes = 0
    run = True

    key_mapping = {
        pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3,
        pygame.K_4: 4, pygame.K_5: 5, pygame.K_6: 6,
        pygame.K_7: 7, pygame.K_8: 8, pygame.K_9: 9
    }

    while run:
        play_time = round(time.time() - start)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key in key_mapping:
                    key = key_mapping[event.key]
                elif event.key == pygame.K_DELETE:
                    board.clear()
                    key = None

                if event.key == pygame.K_SPACE:
                    board.solve_gui()

                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            messagebox.showinfo("Success", "You placed the number correctly!")
                        else:
                            messagebox.showinfo("Wrong", "Incorrect number!")
                            strikes += 1
                        key = None
                        if board.is_finished():
                            messagebox.showinfo("Game Over", "The puzzle is solved.")

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                difficulty = board.difficulty_dropdown.click(pygame.mouse.get_pos())
                if difficulty:
                    board.mask_rate = board.get_mask_rate(difficulty)
                    board.generate_new_puzzle()  # Generate a new puzzle with the new mask rate

                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None
                else:
                    if board.help_button.click(pygame.mouse.get_pos()):
                        board.rules_popup.toggle()
                    if board.new_puzzle_button.click(pos):
                        board.generate_new_puzzle()
                        start = time.time()
                        strikes = 0
                        redraw_window(win, board, play_time, strikes)  # Redraw the window

        if board.selected and key is not None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()


if __name__ == "__main__":
    pygame.font.init()
    run_game()
    pygame.quit()
