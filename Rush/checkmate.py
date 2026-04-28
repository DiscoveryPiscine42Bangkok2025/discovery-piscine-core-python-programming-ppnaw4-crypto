def find_king(board):
    king_count = 0
    king_position = None

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "K":
                king_count += 1
                king_position = (i, j)

    if king_count != 1:
        return None

    return king_position


def check_pawn(board, x, y):
    rows = len(board)
    cols = len(board[0])


    for dx, dy in [(-1, -1), (-1, 1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < rows and 0 <= ny < cols:
            if board[nx][ny] == "P":
                return True

    return False


def check_rook(board, x, y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx = x
        ny = y

        while True:
            nx += dx
            ny += dy

            if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
                break

            piece = board[nx][ny]

            if piece != ".":
                if piece == "R" or piece == "Q":
                    return True
                break

    return False


def check_bishop(board, x, y):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dx, dy in directions:
        nx = x
        ny = y

        while True:
            nx += dx
            ny += dy

            if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
                break

            piece = board[nx][ny]

            if piece != ".":
                if piece == "B" or piece == "Q":
                    return True
                break

    return False


def checkmate(board_string):
    try:
        board = board_string.splitlines()

        if not board:
            print("Error")
            return

        size = len(board)

        for row in board:
            if len(row) != size:
                print("Error")
                return

        king_position = find_king(board)

        if king_position is None:
            print("Error")
            return

        x, y = king_position

        if (
            check_pawn(board, x, y)
            or check_rook(board, x, y)
            or check_bishop(board, x, y)
        ):
            print("Success")
        else:
            print("Fail")

    except Exception:
        print("Error")