import json
import time
import os

class GameHistory:
    def __init__(self):
        self.moves = []
        self.history = []
        self.load_history()
    
    def record_move(self, move, board_state):
        self.moves.append({
            'move': self._move_to_string(move),
            'board_state': board_state
        })
    
    def save_game(self):
        history_file = 'chess_history.json'
        
        # Load existing history
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                history = json.load(f)
        else:
            history = []
        
        # Add current game
        history.append({
            'moves': self.moves,
            'timestamp': time.time()
        })
        
        # Save updated history
        with open(history_file, 'w') as f:
            json.dump(history, f)
    
    def load_history(self):
        history_file = 'chess_history.json'
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                self.history = json.load(f)
        else:
            self.history = []
    
    def get_move_success_rate(self, move):
        move_str = self._move_to_string(move)
        total_occurrences = 0
        successful_occurrences = 0
        
        for game in self.history:
            for i, game_move in enumerate(game['moves']):
                if game_move['move'] == move_str:
                    total_occurrences += 1
                    # Consider a move successful if the game continues for at least 3 more moves
                    if len(game['moves']) > i + 3:
                        successful_occurrences += 1
        
        return successful_occurrences / total_occurrences if total_occurrences > 0 else 0
    
    def _move_to_string(self, move):
        start, end = move
        return f"{chr(ord('a') + start[1])}{8-start[0]}{chr(ord('a') + end[1])}{8-end[0]}"