from board import Board
from player import Player, AIPlayer
from game_history import GameHistory
from move_validator import MoveValidator

class ChessGame:
    def __init__(self, mode="player_vs_ai"):
        self.board = Board()
        self.history = GameHistory()
        self.validator = MoveValidator()
        
        if mode == "player_vs_ai":
            self.white = Player("White")
            self.black = AIPlayer("Black", self.history)
        else:  # ai_vs_ai
            self.white = AIPlayer("White", self.history)
            self.black = AIPlayer("Black", self.history)
    
    def play(self):
        current_player = self.white
        while not self.board.is_game_over():
            self.board.display()
            move = current_player.get_move(self.board)
            
            if self.validator.is_valid_move(self.board, move):
                self.board.make_move(move)
                self.history.record_move(move, self.board.get_state())
                current_player = self.black if current_player == self.white else self.white
            
        self.history.save_game()
        self.board.display()
        print(f"Game Over! Winner: {self.board.get_winner()}")