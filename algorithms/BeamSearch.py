# Import hàm beliefState từ file algorithms.BeliefState
from algorithms.BeliefState import beliefState

def beamSearch(start, goal, beamWidth=2):
    # Khởi tạo hàng đợi (queue) với trạng thái ban đầu và đường đi rỗng
    queue = [(start, [])]
    visited = set()  # Lưu các trạng thái đã thăm
    
    # Thêm trạng thái ban đầu là đã thăm
    visited.add(tuple(tuple(row) for row in start))

    # Hướng di chuyển của ô trống
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    # Lặp cho đến khi hàng đợi rỗng
    while queue:  
        # Sắp xếp hàng đợi theo giá trị beliefState 
        queue.sort(key=lambda x: beliefState(x[0], goal))

        queue = queue[:beamWidth] # Giữ lại tối đa `beamWidth` trạng thái tốt nhất

        # Hàng đợi mới cho các trạng thái lân cận
        nextQueue = []

        # Duyệt từng trạng thái hiện tại trong hàng đợi
        for current, path in queue:
            # Kiểm tra xem có phải trạng thái đích chưa, đúng thì trả về đường đi
            if current == goal:
                return path

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

                    # Kiểm tra xem trạng thái mới được thăm chưa, nếu chưa thêm vào hàng đợi và đánh dấu đã thăm
                    if stateTuple not in visited:
                        nextQueue.append((newState, path + [newState]))
                        visited.add(stateTuple)

        # Cập nhật hàng đợi với các trạng thái lân cận
        queue = nextQueue

    # Không tìm thấy đường đi, trả về None
    return None