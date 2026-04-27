from checkmate import checkmate


def show_piece_moves():
    print("""Pawn (P):
. . . . . . .
. . . . . . .
. . X . X . .
. . . P . . .
. . . . . . .
. . . . . . .
. . . . . . .
""")

    print("""Bishop (B):
X . . . . . X
. X . . . X .
. . X . X . .
. . . B . . .
. . X . X . .
. X . . . X .
X . . . . . X
""")

    print("""Rook (R):
. . . X . . .
. . . X . . .
. . . X . . .
X X X R X X X
. . . X . . .
. . . X . . .
. . . X . . .
""")

    print("""Queen (Q):
X . . X . . X
. X . X . X .
. . X X X . .
X X X Q X X X
. . X X X . .
. X . X . X .
X . . X . . X
""")


def main():
    show_piece_moves()

    board = """\
R...
.K..
..P.
....\
"""

    checkmate(board)


if __name__ == "__main__":
    main()