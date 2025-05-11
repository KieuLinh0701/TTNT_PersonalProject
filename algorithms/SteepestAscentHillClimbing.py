from copy import deepcopy

# Hàm tính heuristic: số ô không đúng vị trí.
def calculate_misplaced_tiles(state, goal):
    return sum(
        1 for i in range(3) for j in range(3) if state[i][j] != 0 and state[i][j] != goal[i][j]
    )

# Hàm Steepest-Ascent Hill Climbing.
def steepestAscentHillClimbing(start, goal):
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

        # Tạo danh sách các trạng thái hàng xóm.
        neighbors = []
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

                # Nếu trạng thái mới chưa được thăm, thêm nó vào danh sách hàng xóm.
                if stateTuple not in visited:
                    neighbors.append((newState, calculate_misplaced_tiles(newState, goal)))

        # Nếu không có hàng xóm khả thi, không thể tiếp tục.
        if not neighbors:
            return None  # Không tìm thấy giải pháp.

        # Chọn trạng thái hàng xóm tốt nhất (heuristic nhỏ nhất).
        neighbors.sort(key=lambda x: x[1])  # Sắp xếp theo giá trị heuristic.
        best_neighbor = neighbors[0]

        # Nếu trạng thái hàng xóm tốt nhất không tốt hơn trạng thái hiện tại, dừng lại.
        if calculate_misplaced_tiles(current, goal) <= best_neighbor[1]:
            return None  # Kẹt tại cực đại cục bộ.

        # Cập nhật trạng thái hiện tại và đường đi.
        current = best_neighbor[0]
        path.append(current)
        visited.add(tuple(tuple(row) for row in current))