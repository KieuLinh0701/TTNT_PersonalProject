# Thuật toán IDA*
def idaStar(start, goal):
    def heuristic(state):
        # Hàm heuristic tính khoảng cách Manhattan
        return sum(
            abs(i - gi) + abs(j - gj)
            for i, row in enumerate(state)
            for j, val in enumerate(row)
            if val != 0
            for gi, grow in enumerate(goal)
            for gj, gval in enumerate(grow)
            if gval == val
        )

    def dfs_limited(state, g, threshold, path):
        f = g + heuristic(state)  # Tính f(n) = g(n) + h(n)
        if f > threshold:
            return f, None

        if state == goal:
            return f, path

        min_threshold = float('inf')
        zeroX, zeroY = next(
            (i, j) for i in range(3) for j in range(3) if state[i][j] == 0
        )

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            newX, newY = zeroX + dx, zeroY + dy

            if 0 <= newX < 3 and 0 <= newY < 3:
                newState = [row[:] for row in state]
                newState[zeroX][zeroY], newState[newX][newY] = (
                    newState[newX][newY],
                    newState[zeroX][zeroY],
                )

                if newState not in path:  # Tránh lặp trạng thái
                    result, solution = dfs_limited(newState, g + 1, threshold, path + [newState])
                    if solution is not None:
                        return result, solution
                    min_threshold = min(min_threshold, result)

        return min_threshold, None

    # Khởi tạo ngưỡng bằng giá trị heuristic của trạng thái bắt đầu
    threshold = heuristic(start)
    while True:
        result, solution = dfs_limited(start, 0, threshold, [start])
        if solution is not None:
            return solution
        if result == float('inf'):
            return None  # Không tìm thấy lời giải
        threshold = result