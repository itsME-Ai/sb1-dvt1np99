import random
import time
import sys

class Player:
    def __init__(self, color):
        self.color = color
    
    def get_move(self, board):
        while True:
            try:
                move = input(f"\n{self.color}'s move (e.g., e2e4): ").lower().strip()
                if move == 'quit':
                    print("\nGame ended by player.")
                    sys.exit(0)
                    
                if len(move) != 4:
                    raise ValueError("Invalid move length")
                
                if not (move[0].isalpha() and move[2].isalpha() and 
                       move[1].isdigit() and move[3].isdigit()):
                    raise ValueError("Invalid move format")
                
                start = (8 - int(move[1]), ord(move[0]) - ord('a'))
                end = (8 - int(move[3]), ord(move[2]) - ord('a'))
                
                if not (0 <= start[0] <= 7 and 0 <= start[1] <= 7 and 
                       0 <= end[0] <= 7 and 0 <= end[1] <= 7):
                    raise ValueError("Move coordinates out of bounds")
                
                return (start, end)
            except (EOFError, KeyboardInterrupt):
                print("\nGame terminated by user")
                sys.exit(0)
            except ValueError as e:
                print(f"Invalid move: {str(e)}. Please use format 'e2e4' or type 'quit' to end game")
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Please try again")

class AIPlayer(Player):
    def __init__(self, color, history):
        super().__init__(color)
        self.history = history
        
    def get_move(self, board):
        try:
            print(f"\n{self.color} (AI) is thinking...", end='', flush=True)
            time.sleep(1)  # Simulate thinking
            
            # Get possible moves for all pieces of the AI's color
            possible_moves = self._get_possible_moves(board)
            
            # Use historical data to weight moves
            weighted_moves = self._weight_moves(possible_moves, board)
            
            # Select the best move
            if weighted_moves:
                move = max(weighted_moves, key=lambda x: x[1])[0]
            else:
                move = random.choice(possible_moves) if possible_moves else None
                
            if move:
                start, end = move
                print(f" plays {chr(ord('a') + start[1])}{8-start[0]}{chr(ord('a') + end[1])}{8-end[0]}")
            return move
            
        except Exception as e:
            print(f"\nAI error: {e}")
            return None
    
    def _get_possible_moves(self, board):
        moves = []
        for i in range(8):
            for j in range(8):
                if board.board[i][j].startswith(self.color[0]):
                    # Add all theoretically possible moves
                    # This is simplified - in a real implementation,
                    # you would check valid moves for each piece type
                    for x in range(8):
                        for y in range(8):
                            moves.append(((i, j), (x, y)))
        return moves
    
    def _weight_moves(self, moves, board):
        weighted_moves = []
        for move in moves:
            weight = 1.0
            
            # Increase weight based on historical success
            historical_success = self.history.get_move_success_rate(move)
            weight *= (1 + historical_success)
            
            # Add position-based weighting
            weight *= self._evaluate_position(move[1])
            
            weighted_moves.append((move, weight))
        
        return weighted_moves
    
    def _evaluate_position(self, pos):
        # Simple position evaluation - prefer center squares
        center_distance = abs(3.5 - pos[0]) + abs(3.5 - pos[1])
        return 1 / (1 + center_distance)