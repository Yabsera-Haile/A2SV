class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        queens = set(tuple(q) for q in queens)
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        result = []
        
        for move_x, move_y in moves:
            curr_x, curr_y = king
            
            while 0 <= curr_x < 8 and 0 <= curr_y < 8:
                curr_x += move_x
                curr_y += move_y
                if (curr_x, curr_y) in queens:
                    result.append([curr_x, curr_y])
                    break
                    
        return result


            
        