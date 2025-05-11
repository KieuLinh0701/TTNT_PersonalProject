from algorithms.BeliefState import beliefState

def idaStar(start, goal):

    def heuristic(state):
        return beliefState(state, goal)  # Gọi hàm beliefState để tính toán giá trị heuristic

    # Hàm tìm kiếm sâu giới hạn theo ngưỡng threshold
    def dfsLimited(state, g, threshold, path):

        # Tính toán giá trị f(n) = g(n) + h(n)
        f = g + heuristic(state)

        # Kiểm tra xem giá trị f có vượt quá ngưỡng đúng thì trả về giá trị f
        if f > threshold:
            return f, None

        # Kiểm tra xem có phải trạng thái đích chưa, đúng thì trả về đường đi
        if state == goal:
            return f, path

        # Khởi tạo ngưỡng tối thiểu mới
        minThreshold = float('inf')

        # Tìm vị trí của ô giá trị 0
        zeroX, zeroY = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)

        # Hướng di chuyển của ô trống
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        # Duyệt theo các hướng di chuyển có thể có của ô giá trị 0
        for dx, dy in directions:
            newX = zeroX + dx
            newY = zeroY + dy

            # Kiểm tra xem ô mới có nằm trong ma trận không
            if 0 <= newX < 3 and 0 <= newY < 3:
                # Tạo trạng thái mới
                newState = [row[:] for row in state]
                # Hoán đổi vị trí ô trống với ô ở tọa độ mới
                newState[zeroX][zeroY], newState[newX][newY] = newState[newX][newY], newState[zeroX][zeroY]

                # Kiểm tra trạng thái mới có lặp lại hay không
                if newState not in path:  # Nếu chưa đi qua trạng thái này
                    # Gọi đệ quy với trạng thái mới
                    result, solution = dfsLimited(newState, g + 1, threshold, path + [newState])

                    # Nếu tìm thấy giải pháp, trả về ngay
                    if solution is not None:
                        return result, solution

                    # Cập nhật ngưỡng tối thiểu
                    minThreshold = min(minThreshold, result)

        # Trả về ngưỡng tối thiểu mới nếu không tìm thấy giải pháp
        return minThreshold, None

    # Bắt đầu thuật toán IDA* với ngưỡng bằng heuristic của trạng thái ban đầu
    threshold = heuristic(start)

    while True:
        # Gọi hàm tìm kiếm sâu giới hạn
        result, solution = dfsLimited(start, 0, threshold, [])

        # Nếu tìm thấy giải pháp, trả về
        if solution is not None:
            return solution

        # Nếu không tìm thấy và ngưỡng mới là vô cực, dừng lại
        if result == float('inf'):
            return None

        # Cập nhật ngưỡng cho vòng lặp tiếp theo
        threshold = result