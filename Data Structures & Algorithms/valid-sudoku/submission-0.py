class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counts = Counter()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    # Add unique identifying tuple keys for row, col, and sub-box
                    counts[(r, val)] += 1
                    counts[(val, c)] += 1
                    counts[(r // 3, c // 3, val)] += 1
                    
                    # If any entry appears more than once, the board is invalid
                    if counts[(r, val)] > 1 or counts[(val, c)] > 1 or counts[(r // 3, c // 3, val)] > 1:
                        return False
                        
        return True