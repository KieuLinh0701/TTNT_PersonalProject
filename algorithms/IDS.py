# Hàm tìm kiếm sâu với giới hạn (Depth Limited Search).
def depthLimitedSearch(current, goal, limit, path, visited):
    # Kiểm tra xem có phải trạng thái đích chưa, đúng thì trả về đường đi
    if current == goal:
        return path

    # Nếu vượt quá giới hạn độ sâu, dừng tìm kiếm tại nhánh này.
    if limit == 0:
        return None
    
    # Hướng di chuyển của ô trống
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    # Tìm vị trí của ô giá trị 0
    zeroX, zeroY = next((i, j) for i in range(3) for j in range(3) if current[i][j] == 0)

    # Duyệt theo các hướng di chuyển có thể có của ô giá trị 0
    for dx, dy in directions:
        newX = zeroX + dx
        newY = zeroY + dy

        # Kiểm tra xem ô mới có nằm trong ma trận không
        if 0 <= newX < 3 and 0 <= newY < 3:
            # Tạo trạng thái mới
            newState = [row[:] for row in current]
            # Hoán đổi vị trí ô trống với ô ở tọa độ mới
            newState[zeroX][zeroY], newState[newX][newY] = newState[newX][newY], newState[zeroX][zeroY]

            # Chuyển trạng thái mới thành dạng tuple để lưu trữ
            stateTuple = tuple(tuple(row) for row in newState)

            # Kiểm tra xem trạng thái mới được thăm chưa, nếu chưa tiếp tục tìm kiếm đệ quy.
            if stateTuple not in visited:
                visited.add(stateTuple)  
                result = depthLimitedSearch(newState, goal, limit - 1, path + [newState], visited)
                if result:
                    return result
                # Loại bỏ trạng thái khỏi visited sau khi quay lui.
                visited.remove(stateTuple)

    # Không tìm thấy đường đi, trả về None
    return None


# Hàm IDS để tìm đường từ trạng thái bắt đầu (start) đến trạng thái mục tiêu (goal).
def ids(start, goal):
    depth = 0  # Bắt đầu từ độ sâu 0.

    # Lặp tăng giới hạn độ sâu.
    while True:
        visited = set() # Lưu các trạng thái đã thăm

        # Thêm trạng thái ban đầu là đã thăm
        visited.add(tuple(tuple(row) for row in start))

        # Gọi hàm tìm kiếm sâu với giới hạn.
        result = depthLimitedSearch(start, goal, depth, [], visited)

        # Nếu tìm thấy kết quả, trả về đường đi.
        if result:
            return result

        # Tăng giới hạn độ sâu để thử lại.
        depth += 1