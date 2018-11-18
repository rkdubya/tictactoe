

class Board(object):

    def __init__(self, p1 = 'person', p2 = 'computer'):
        self.p1 = p1
        self.p2 = p2
        self.squares = [' ']*9
        self.turn = 'X'

    def print_board(self):
        for i in range(3):
            v = 3*i
            print " %s | %s | %s " % (self.squares[v], self.squares[v + 1], self.squares[v + 2])
            if i < 2:
                print '-'*12

    def pick(self):
        player = self.p1 if self.turn == 'X' else self.p2
        q = raw_input("%s's turn. Pick a square (1 - 9)" % player)
        self.squares[int(q) - 1] = self.turn
        self.print_board()
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

if __name__ == '__main__':

    b = Board('Pete', 'Kaya')
    print "Player 1 is %s" % b.p1
    print "Player 2 is %s" % b.p2
    for i in range(9):
        b.pick()


