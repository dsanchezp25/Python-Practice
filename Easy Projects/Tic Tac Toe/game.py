class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]   # 3x3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + '| '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0|1|2 etc
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for i in range(3)]
        for row in number_board:
            print('| ' + '| '.join(row) + ' |')

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0,'x'), (1,'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
