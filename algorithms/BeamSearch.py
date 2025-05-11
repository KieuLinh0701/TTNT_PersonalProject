from algorithms.BeliefState import beliefState

def beamSearch(start, goal, beam_width=2):
    # Mảng queue chứa các trạng thái và đường đi
    queue = [(start, [])]
    visited = set()
    visited.add(tuple(tuple(row) for row in start))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Lên, xuống, trái, phải

    while queue:
        # Sắp xếp queue theo giá trị belief_state (hàm belief_state đã có bên ngoài)
        queue.sort(key=lambda x: beliefState(x[0], goal))

        # Giữ lại beam_width phần tử có giá trị thấp nhất
        queue = queue[:beam_width]

        next_queue = []

        for current, path in queue:
            if current == goal:
                return path

            zeroX, zeroY = next(
                (i, j) for i in range(3) for j in range(3) if current[i][j] == 0
            )

            for dx, dy in directions:
                newX, newY = zeroX + dx, zeroY + dy

                if 0 <= newX < 3 and 0 <= newY < 3:
                    newState = [row[:] for row in current]
                    newState[zeroX][zeroY], newState[newX][newY] = (
                        newState[newX][newY],
                        newState[zeroX][zeroY],
                    )

                    stateTuple = tuple(tuple(row) for row in newState)
                    if stateTuple not in visited:
                        next_queue.append((newState, path + [newState]))
                        visited.add(stateTuple)

        # Cập nhật queue với các trạng thái lân cận đã duyệt
        queue = next_queue

    return None