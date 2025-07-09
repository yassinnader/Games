class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (a single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. Please choose a single letter.")


class Menu:
    def display_main_menu(self):
        print("Welcome to my X-O game!")
        print("1. Start game")
        print("2. Quit game")
        choice = input("Enter your choice (1 or 2): ")
        return choice
    
    def display_game_over_menu(self):
        menu_text = """
        Game over!
        1. Restart Game
        2. Quit Game
        Enter your choice (1 or 2): """
        choice = input(menu_text)
        return choice


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()
    
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0 

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for player in self.players:
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        self.board.reset_board()
        self.board.display_board()
        while True:
            current_player = self.players[self.current_player_index]
            while True:
                try:
                    choice = int(input(f"{current_player.name}, choose a position (1-9): "))
                    if 1 <= choice <= 9 and self.board.update_board(choice, current_player.symbol):
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 9.")
            self.board.display_board()
            if self.check_winner(current_player.symbol):
                print(f"Congratulations {current_player.name}! You won!")
                break
            if all(not cell.isdigit() for cell in self.board.board):
                print("It's a tie!")
                break
            self.current_player_index = 1 - self.current_player_index
        
        choice = self.menu.display_game_over_menu()
        if choice == "1":
            self.start_game()
        else:
            self.quit_game()

    def check_winner(self, symbol):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in winning_combinations:
            if all(self.board.board[i] == symbol for i in combo):
                return True
        return False

    def quit_game(self):
        print("Thank you for playing!")
        exit()


game = Game()
game.start_game()