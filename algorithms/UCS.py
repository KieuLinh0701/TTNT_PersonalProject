import heapq

# Thuật toán UCS (Uniform Cost Search)
def ucs(start, goal):
    priority_queue = [(0, start, [])]  # (cost, state, path)
    visited = set()
    visited.add(tuple(tuple(row) for row in start))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

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
                    heapq.heappush(priority_queue, (cost + 1, newState, path + [newState]))
                    visited.add(stateTuple)
    return None