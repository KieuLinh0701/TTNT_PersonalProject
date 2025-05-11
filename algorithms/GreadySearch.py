import heapq

from algorithms.BeliefState import beliefState

# Thuật toán Greedy Search
def greedy(start, goal):
    def heuristic(state):
        # Gọi hàm belief_state đã được định nghĩa ngoài
        return beliefState(state, goal)

    priority_queue = [(heuristic(start), start, [])]  # (heuristic, state, path)
    visited = set()
    visited.add(tuple(tuple(row) for row in start))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Lên, xuống, trái, phải

    while priority_queue:
        _, current, path = heapq.heappop(priority_queue)

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
                    heapq.heappush(priority_queue, (heuristic(newState), newState, path + [newState]))
                    visited.add(stateTuple)
    return None