import heapq  

from algorithms.BeliefState import beliefState 

def greedy(start, goal):

    def heuristic(state):
        return beliefState(state, goal)  # Gọi hàm beliefState để tính toán giá trị heuristic

    # Hàng đợi lưu các trạng thái cần duyệt
    priorityQueue = [(heuristic(start), start, [])] # Mỗi phần tử: heuristic giá trị + trạng thái hiện tại + đường đi đã đi qua
    visited = set()  # Lưu các trạng thái đã thăm

    # Thêm trạng thái ban đầu là đã thăm
    visited.add(tuple(tuple(row) for row in start))  # Chuyển trạng thái 2D thành tuple để sử dụng trong visited

    # Hướng di chuyển của ô trống
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Lặp cho đến khi hàng đợi trống.
    while priorityQueue:
        # Lấy trạng thái có heuristic thấp nhất (tốt nhất) từ hàng đợi
        _, current, path = heapq.heappop(priorityQueue)

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
                    # Thêm trạng thái mới vào hàng đợi với giá trị heuristic tính từ trạng thái mới
                    heapq.heappush(priorityQueue, (heuristic(newState), newState, path + [newState]))
                    visited.add(stateTuple) 

    # Không tìm thấy đường đi, trả về None
    return None