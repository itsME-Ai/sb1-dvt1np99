class Board:
    def __init__(self):
        self.board = self._initial_board()
        self.piece_symbols = {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',  # White pieces
            'BK': '♚', 'BQ': '♛', 'BR': '♜', 'BB': '♝', 'BN': '♞', 'BP': '♟'  # Black pieces
        }
        
    def _initial_board(self):
        # Initialize standard chess board
        board = [['' for _ in range(8)] for _ in range(8)]
        # Set up pawns
        for i in range(8):
            board[1][i] = 'BP'  # Black pawns
            board[6][i] = 'WP'  # White pawns
        
        # Set up other pieces
        pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i in range(8):
            board[0][i] = 'B' + pieces[i]  # Black pieces
            board[7][i] = 'W' + pieces[i]  # White pieces
            
        return board
    
    def display(self):
        print('\n  a b c d e f g h')
        print('  ─────────────────')
        for i in range(8):
            print(f"{8-i}│", end=' ')
            for j in range(8):
                piece = self.board[i][j]
                if not piece:
                    # Alternate between light and dark squares
                    print('·' if (i + j) % 2 == 0 else '·', end=' ')
                else:
                    symbol = self.piece_symbols.get(piece[1:], piece[1])
                    if piece.startswith('W'):
                        print(symbol, end=' ')
                    else:
                        print(symbol, end=' ')
            print(f"│{8-i}")
        print('  ─────────────────')
        print('  a b c d e f g h\n')
    
    def get_state(self):
        return [row[:] for row in self.board]
    
    def make_move(self, move):
        start_pos, end_pos = move
        self.board[end_pos[0]][end_pos[1]] = self.board[start_pos[0]][start_pos[1]]
        self.board[start_pos[0]][start_pos[1]] = ''
    
    def is_game_over(self):
        # Check for checkmate, stalemate, or insufficient material
        # Simplified version for demonstration
        kings = sum(row.count('WK') + row.count('BK') for row in self.board)
        return kings != 2
    
    def get_winner(self):
        # Simplified winner determination
        white_king = any('WK' in row for row in self.board)
        black_king = any('BK' in row for row in self.board)
        
        if white_king and not black_king:
            return "White"
        elif black_king and not white_king:
            return "Black"
        return "Draw"