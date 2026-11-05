# Ход Коня
class Knight:
    def __init__(self,horizontal,vertical,color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
    def get_char(self):
        return 'N'
    def can_move(self,horizontal,vertical):
        if self.horizontal > horizontal:
            res_h = ord(self.horizontal) - ord(horizontal)
        else:
            res_h = ord(horizontal) - ord(self.horizontal)
        if self.vertical > vertical:
            res_v = self.vertical - vertical
        else:
            res_v = vertical - self.vertical
        if 1 < res_v > 8 or 1 < res_h > 8:
            return False
        if res_v == 2 and res_h == 1:
            return True
        elif res_v == 1 and res_h == 2:
            return True
        else:
            return False
    def move_to(self,horizontal,vertical):
        if self.can_move(horizontal,vertical):
           self.horizontal = horizontal
           self.vertical = vertical
    def draw_board(self):
        board = [['.' for _ in range(8)] for _ in range(8)]
        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for f in files:
            for r in range(1, 9):
                if self.can_move(f, r):
                    row_idx = 8 - r
                    col_idx = ord(f) - ord('a')
                    board[row_idx][col_idx] = '*'
        knight_row = 8 - self.vertical
        knight_col = ord(self.horizontal) - ord('a')
        board[knight_row][knight_col] = self.get_char()
        for row in board:
            print(''.join(row))


# TEST_6:
knight = Knight('g', 7, 'black')
knight.draw_board()

# TEST_7:
knight = Knight('d', 8, 'white')
knight.draw_board()

# TEST_8:
knight = Knight('h', 1, 'black')
knight.draw_board()