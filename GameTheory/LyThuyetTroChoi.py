import pygame

# Set kích thước của bàn cờ
board_size = 8
square_size = 80  # Kích thước của mỗi ô trong pixel

# Khởi tạo Pygame
pygame.init()

# Tính toán kích thước của cửa sổ dựa trên kích thước bàn cờ và ô vuông
window_size = (board_size * square_size, board_size * square_size)

# Tạo cửa sổ trò chơi
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Chessboard")

# Tải hình ảnh quân hậu
queen_image = pygame.image.load("queen.png")
queen_image = pygame.transform.scale(queen_image, (square_size, square_size))

# Hàm để vẽ bàn cờ
def draw_chessboard():
    for row in range(board_size):
        for col in range(board_size):
            x = col * square_size
            y = row * square_size

            if (row + col) % 2 == 0:
                color = (255, 255, 255)  # Màu trắng
            else:
                color = (0, 0, 0)  # Màu đen

            pygame.draw.rect(window, color, (x, y, square_size, square_size))

# Hàm để vẽ các quân hậu trên bàn cờ
def draw_queens(queens):
    for queen in queens:
        x = queen * square_size
        y = queens.index(queen) * square_size
        window.blit(queen_image, (x, y))

# Hàm để kiểm tra xem có thể đặt một quân hậu tại vị trí đã cho hay không
def is_safe(queens, col):
    for i in range(len(queens)):
        if queens[i] == col or queens[i] + i == col + len(queens) or queens[i] - i == col - len(queens):
            return False
    return True

# Hàm đệ quy để đặt các quân hậu sử dụng thuật toán Backtracking
def place_queens(n, i, queens, solutions):
    if i == n:
        solutions.append(queens.copy())
        return

    for j in range(n):
        if is_safe(queens, j):
            queens.append(j)
            place_queens(n, i + 1, queens, solutions)
            queens.pop()

# Tìm tất cả các giải pháp để đặt 8 quân hậu
solutions = []
place_queens(board_size, 0, [], solutions)

# Chọn giải pháp có số ô không bị chiếm giữ là lớn nhất
max_unattacked = max(solutions, key=lambda s: board_size - len(s))

# Vòng lặp trò chơi
running = True
while running:
    # Xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vẽ bàn cờ
    draw_chessboard()

    # Vẽ các quân hậu trên bàn cờ
    draw_queens(max_unattacked)

    # Cập nhật hiển thị
    pygame.display.flip()

# Kết thúc Pygame
pygame.quit()
