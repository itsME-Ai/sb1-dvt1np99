class MoveValidator:
    def is_valid_move(self, board, move):
        if not move:
            return False
            
        start_pos, end_pos = move
        
        # Check if positions are within board
        if not self._is_within_board(start_pos) or not self._is_within_board(end_pos):
            return False
        
        # Check if start position has a piece
        if not board.board[start_pos[0]][start_pos[1]]:
            return False
        
        # Check if end position doesn't have a piece of the same color
        start_piece = board.board[start_pos[0]][start_pos[1]]
        end_piece = board.board[end_pos[0]][end_pos[1]]
        
        if end_piece and start_piece[0] == end_piece[0]:  # Same color
            return False
            
        # Simplified validation - in a real implementation,
        # you would check specific rules for each piece type
        return True
    
    def _is_within_board(self, pos):
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8