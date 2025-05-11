from collections import deque  # Import deque từ thư viện collections để sử dụng hàng đợi hiệu quả.

# Hàm BFS để tìm đường từ trạng thái bắt đầu (start) đến trạng thái mục tiêu (goal).
def bfs(start, goal):
    # Khởi tạo hàng đợi với trạng thái ban đầu và đường đi rỗng.
    queue = deque([(start, [])])
    visited = set()  # Tập hợp các trạng thái đã thăm để tránh lặp lại.
    
    # Đánh dấu trạng thái ban đầu là đã thăm.
    visited.add(tuple(tuple(row) for row in start))

    # Các hướng di chuyển của ô trống: lên, xuống, trái, phải.
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    # Vòng lặp cho đến khi hàng đợi trống.
    while queue:
        # Lấy trạng thái hiện tại và đường đi từ hàng đợi.
        current, path = queue.popleft()
        
        # Nếu trạng thái hiện tại là trạng thái mục tiêu, trả về đường đi.
        if current == goal:
            return path

        # Tìm vị trí của ô trống (giá trị 0) trong ma trận.
        zeroX, zeroY = next(
            (i, j) for i in range(3) for j in range(3) if current[i][j] == 0
        )

        # Thử di chuyển ô trống theo các hướng khả thi.
        for dx, dy in directions:
            newX, newY = zeroX + dx, zeroY + dy

            # Kiểm tra nếu vị trí mới nằm trong phạm vi của ma trận.
            if 0 <= newX < 3 and 0 <= newY < 3:
                # Tạo trạng thái mới bằng cách sao chép trạng thái hiện tại.
                newState = [row[:] for row in current]
                
                # Hoán đổi ô trống với ô ở vị trí mới.
                newState[zeroX][zeroY], newState[newX][newY] = (
                    newState[newX][newY],
                    newState[zeroX][zeroY],
                )

                # Biến trạng thái mới thành dạng tuple để có thể lưu trong tập hợp visited.
                stateTuple = tuple(tuple(row) for row in newState)
                
                # Nếu trạng thái mới chưa được thăm, thêm nó vào hàng đợi và đánh dấu đã thăm.
                if stateTuple not in visited:
                    queue.append((newState, path + [newState]))  # Thêm trạng thái mới và cập nhật đường đi.
                    visited.add(stateTuple)
    
    # Nếu không tìm thấy đường đi đến trạng thái mục tiêu, trả về None.
    return None