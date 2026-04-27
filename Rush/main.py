
print("""Pawn (P):
. . . . . . .
. . . . . . .
. . X . X . .
. . . P . . .
. . . . . . .
. . . . . . .
. . . . . . .""")

print("""Bishop (B):
X . . . . . X
. X . . . X .
. . X . X . .
. . . B . . .
. . X . X . .
. X . . . X .
X . . . . . X""")

print("""Rook (R):
. . . X . . .
. . . X . . .
. . . X . . .
X X X R X X X
. . . X . . .
. . . X . . .
. . . X . . .""")

print("""Queen (Q)
X . . X . . X
. X . X . X .
. . X X X . .
X X X Q X X X
. . X X X . .
. X . X . X .
X . . X . . X""")

from checkmate import checkmate


def main():
    board = """\
R...
.K..
..P.
....\
"""

    checkmate(board)


if __name__ == "__main__":
    main()