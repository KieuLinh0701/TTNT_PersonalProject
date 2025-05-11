import heapq

from algorithms.BeliefState import beliefState

# Thuật toán A* Search
def aStar(start, goal, use_belief_state=False):
    def heuristic(state):
        return sum(
            abs(i - gi) + abs(j - gj)
            for i, row in enumerate(state)
            for j, val in enumerate(row)
            if val != 0
            for gi, grow in enumerate(goal)
            for gj, gval in enumerate(grow)
            if gval == val
        )

    priority_queue = [(heuristic(start) if not use_belief_state else beliefState(start, goal), 0, start, [])]
    visited = set()
    visited.add(tuple(tuple(row) for row in start))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path

        zeroX, zeroY = next(
            (i, j) for i in range(len(current)) for j in range(len(current[0])) if current[i][j] == 0
        )

        for dx, dy in directions:
            newX, newY = zeroX + dx, zeroY + dy

            if 0 <= newX < len(current) and 0 <= newY < len(current[0]):
                newState = [row[:] for row in current]
                newState[zeroX][zeroY], newState[newX][newY] = (
                    newState[newX][newY],
                    newState[zeroX][zeroY],
                )

                stateTuple = tuple(tuple(row) for row in newState)
                if stateTuple not in visited:
                    new_g = g + 1
                    new_f = new_g + (beliefState(newState, goal) if use_belief_state else heuristic(newState))

                    heapq.heappush(priority_queue, (new_f, new_g, newState, path + [newState]))
                    visited.add(stateTuple)
    return None