from copy import deepcopy
import random

# Hàm tính heuristic: số ô không đúng vị trí.
def calculate_misplaced_tiles(state, goal):
    return sum(
        1 for i in range(3) for j in range(3) if state[i][j] != 0 and state[i][j] != goal[i][j]
    )

# Hàm Stochastic Hill Climbing.
def stochasticHillClimbing(start, goal):
    current = start  # Trạng thái hiện tại.
    path = []  # Lưu đường đi.
    visited = set()  # Tập hợp các trạng thái đã thăm để tránh lặp lại.

    # Đánh dấu trạng thái bắt đầu là đã thăm.
    visited.add(tuple(tuple(row) for row in current))
    
    # Các hướng di chuyển của ô trống: lên, xuống, trái, phải.
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while True:
        # Nếu trạng thái hiện tại là trạng thái mục tiêu, trả về đường đi.
        if current == goal:
            return path

        # Tìm vị trí của ô trống (giá trị 0) trong ma trận.
        zeroX, zeroY = next(
            (i, j) for i in range(3) for j in range(3) if current[i][j] == 0
        )

        # Tạo danh sách các trạng thái hàng xóm tốt hơn trạng thái hiện tại.
        neighbors = []
        current_heuristic = calculate_misplaced_tiles(current, goal)

        for dx, dy in directions:
            newX, newY = zeroX + dx, zeroY + dy

            # Kiểm tra nếu vị trí mới nằm trong phạm vi của ma trận.
            if 0 <= newX < 3 and 0 <= newY < 3:
                # Tạo trạng thái mới bằng cách sao chép trạng thái hiện tại.
                newState = deepcopy(current)

                # Hoán đổi ô trống với ô ở vị trí mới.
                newState[zeroX][zeroY], newState[newX][newY] = (
                    newState[newX][newY],
                    newState[zeroX][zeroY],
                )

                # Biến trạng thái mới thành dạng tuple để kiểm tra visited.
                stateTuple = tuple(tuple(row) for row in newState)

                # Tính giá trị heuristic cho trạng thái hàng xóm.
                new_heuristic = calculate_misplaced_tiles(newState, goal)

                # Nếu trạng thái hàng xóm tốt hơn và chưa được thăm, thêm nó vào danh sách.
                if stateTuple not in visited and new_heuristic < current_heuristic:
                    neighbors.append((newState, new_heuristic))

        # Nếu không có hàng xóm nào tốt hơn, dừng lại.
        if not neighbors:
            return None  # Không tìm thấy giải pháp.

        # Chọn ngẫu nhiên một trạng thái hàng xóm tốt hơn từ danh sách.
        next_state = random.choice(neighbors)[0]

        # Cập nhật trạng thái hiện tại và đường đi.
        current = next_state
        path.append(current)
        visited.add(tuple(tuple(row) for row in current))