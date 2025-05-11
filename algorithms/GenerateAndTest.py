""" 
THUẬT TOÁN TÌM KIẾM BẰNG KIỂM THỬ
(Generate and Test)

Ý tưởng: 
❑ Sinh ra một khả năng (candidate) của lời giải
❑ Kiểm tra xem khả năng này có thực sự là một lời giải
"""

import random

def is_solvable(board):
    """Kiểm tra xem trạng thái ban đầu của trò chơi có giải được không."""
    inversions = 0
    flat_list = [num for row in board for num in row if num != 0]
    for i in range(len(flat_list)):
        for j in range(i + 1, len(flat_list)):
            if flat_list[i] > flat_list[j]:
                inversions += 1
    return inversions % 2 == 0

def get_random_neighbor(board):
    """Sinh ngẫu nhiên một trạng thái lân cận."""
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    empty_pos = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0][0]
    x, y = empty_pos
    possible_moves = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            possible_moves.append((nx, ny))
    if not possible_moves:
        return None  # Không có nước đi hợp lệ
    nx, ny = random.choice(possible_moves) # Chọn ngẫu nhiên
    new_board = [row[:] for row in board]
    new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
    return new_board

def generate_and_test(start, goal, max_iterations=10000):
    """Tìm kiếm lời giải bằng thuật toán Generate and Test."""
    current = start
    for _ in range(max_iterations):
        if current == goal:
            return [current]  # Trả về đường đi (chỉ có trạng thái cuối)
        current = get_random_neighbor(current)
        if current is None:
            return None # Không có trạng thái tiếp theo
    return None  # Không tìm thấy giải pháp sau số lần thử tối đa