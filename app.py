from flask import Flask, render_template
import random
app = Flask(__name__)

class Game:
    def __init__(self, is_computer_game):
        self.current_turn = 'X'
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.is_computer_game = is_computer_game
        
    def player_move(self, player, location):
        self.board[location // 3][location % 3] = player
        if self.current_turn == 'X':
            self.current_turn = 'O'
        else:
            self.current_turn = 'X'

    def is_valid_move(self, location):
        return self.board[location // 3][location % 3] == ''

    def has_player_won(self, player):
        return (self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player) or (self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player) or (self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player) or (self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player) or (self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player) or (self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player) or (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player) or (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player)

    def show_board(self):
        print(self.board) 

    def computer_move(self):
        moved = False
        while not moved:
            random_x = random.randint(0, 2)
            random_y = random.randint(0, 2)
            if self.board[random_x][random_y] == '':
                self.board[random_x][random_y] = self.current_turn
                moved = True
        if self.current_turn == 'X':
            self.current_turn = 'O'
        else:
            self.current_turn = 'X'
        
current_game = Game(False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start/<is_computer_game>')
def start(is_computer_game):
    global current_game 
    current_game = Game(True if is_computer_game == 'true' else False)
    print(current_game.is_computer_game)
    return []

@app.route('/move/<location>', methods=['GET', 'POST'])
def move(location):
    is_valid = current_game.is_valid_move(int(location))
    player_turn = current_game.current_turn
    if is_valid:
        current_game.player_move(current_game.current_turn, int(location))
    has_won = current_game.has_player_won(player_turn)
    first_has_won = has_won
    before_computer_board = []
    for line in current_game.board:
        before_computer_board.append(line[:])
    if current_game.is_computer_game:
        if not has_won:
            player_turn = current_game.current_turn
            current_game.computer_move()
            has_won = current_game.has_player_won(player_turn)

    return [is_valid, first_has_won, before_computer_board, current_game.current_turn, player_turn, current_game.board, has_won]   
  
