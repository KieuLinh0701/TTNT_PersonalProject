from copy import deepcopy  # Thư viện để sao chép danh sách đa chiều.

# Hàm tìm kiếm sâu với giới hạn (Depth-Limited Search).
def depth_limited_search(current, goal, limit, path, visited):
    # Nếu trạng thái hiện tại là trạng thái mục tiêu, trả về đường đi.
    if current == goal:
        return path

    # Nếu vượt quá giới hạn độ sâu, dừng tìm kiếm tại nhánh này.
    if limit == 0:
        return None

    # Tìm vị trí của ô trống (giá trị 0) trong ma trận.
    zeroX, zeroY = next(
        (i, j) for i in range(3) for j in range(3) if current[i][j] == 0
    )

    # Các hướng di chuyển của ô trống: lên, xuống, trái, phải.
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Duyệt qua các hướng di chuyển.
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

            # Nếu trạng thái mới chưa được thăm, tiếp tục tìm kiếm đệ quy.
            if stateTuple not in visited:
                visited.add(stateTuple)
                result = depth_limited_search(newState, goal, limit - 1, path + [newState], visited)
                if result:
                    return result
                # Loại bỏ trạng thái khỏi visited sau khi quay lui.
                visited.remove(stateTuple)

    return None

# Hàm IDS để tìm đường từ trạng thái bắt đầu (start) đến trạng thái mục tiêu (goal).
def ids(start, goal):
    depth = 0  # Bắt đầu từ độ sâu 0.

    # Lặp tăng giới hạn độ sâu.
    while True:
        visited = set()  # Tập hợp các trạng thái đã thăm trong mỗi giới hạn.
        visited.add(tuple(tuple(row) for row in start))  # Đánh dấu trạng thái bắt đầu.
        result = depth_limited_search(start, goal, depth, [], visited)
        
        # Nếu tìm thấy kết quả, trả về đường đi.
        if result:
            return result

        # Tăng giới hạn độ sâu.
        depth += 1