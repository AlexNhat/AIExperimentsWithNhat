def is_valid_move(board, x, y):
    # Kiểm tra xem nước đi (x, y) có hợp lệ trên bàn cờ hay không
    n = len(board)
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1


def get_valid_moves(board, x, y):
    # Trả về danh sách các nước đi hợp lệ từ vị trí (x, y) trên bàn cờ
    moves = [
        (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1),
        (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2)
    ]
    valid_moves = []
    for move in moves:
        nx, ny = move
        if is_valid_move(board, nx, ny):
            valid_moves.append(move)
    return valid_moves


def knight_tour(board, x, y, move_number):
    n = len(board)

    # Gán giá trị nước đi hiện tại
    board[x][y] = move_number

    # Nếu đã thăm hết các ô trên bàn cờ, trả về True (tìm được lời giải)
    if move_number == n * n:
        return True

    # Lấy danh sách các nước đi hợp lệ từ vị trí hiện tại
    valid_moves = get_valid_moves(board, x, y)

    # Duyệt qua từng nước đi tiếp theo
    for move in valid_moves:
        nx, ny = move
        if knight_tour(board, nx, ny, move_number + 1):
            return True

    # Nếu không tìm được lời giải, đánh dấu nước đi hiện tại là chưa thăm
    board[x][y] = -1
    return False


def solve_knight_tour(start_x, start_y):
    n = 5  # Kích thước bàn cờ

    # Khởi tạo bàn cờ với tất cả các ô chưa thăm (-1)
    board = [[-1 for _ in range(n)] for _ in range(n)]

    # Chạy thuật toán Backtracking
    if knight_tour(board, start_x, start_y, 1):
        # Nếu tìm được lời giải, in ra bàn cờ và trả về True
        for row in board:
            print(row)
        return True
    else:
        # Nếu không tìm được lời giải, trả về False
        return False


# Ví dụ: Vị trí ban đầu (0, 0)
print("Cách con mã đi hết bàn cờ 5*5")
print("Với vị trí [0,2]")
solve_knight_tour(0, 2)
