def backtrackingWithForwardChecking(startState, goalState):
    """
    Giải bài toán 8-puzzle bằng thuật toán quay lui với kiểm tra trước (Backtracking with Forward Checking).
    """

    def findEmptyTilePosition(state):
        for row in range(3):
            for col in range(3):
                if state[row][col] == 0:
                    return row, col
        return None

    def isGoalState(state):
        return state == goalState

    def getNextPossibleStates(state):
        nextPossibleStates = []
        emptyRow, emptyCol = findEmptyTilePosition(state)
        if emptyRow is None:
            return []
        possibleMoves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for deltaRow, deltaCol in possibleMoves:
            newRow, newCol = emptyRow + deltaRow, emptyCol + deltaCol
            if 0 <= newRow < 3 and 0 <= newCol < 3:
                newState = [list(row) for row in state]
                newState[emptyRow][emptyCol], newState[newRow][newCol] = \
                    newState[newRow][newCol], newState[emptyRow][emptyCol]
                nextPossibleStates.append(newState)
        return nextPossibleStates

    def isConsistent(state, goalState):
        """
        Kiểm tra tính nhất quán của trạng thái:
        Một trạng thái nhất quán nếu số lượng các mảnh không đúng vị trí không vượt quá một ngưỡng nhất định.
        """
        misplacedTiles = sum(
            1 for i in range(3) for j in range(3) if state[i][j] != 0 and state[i][j] != goalState[i][j]
        )
        return misplacedTiles <= 2  # Ngưỡng kiểm tra tùy chỉnh

    def solve8PuzzleUtil(currentState, path, visited):
        if isGoalState(currentState):
            return path  # Không thêm trạng thái hiện tại vào path
        nextPossibleStates = getNextPossibleStates(currentState)
        for nextState in nextPossibleStates:
            stateTuple = tuple(tuple(row) for row in nextState)
            if stateTuple not in visited and isConsistent(nextState, goalState):  # Kiểm tra trước
                visited.add(stateTuple)
                result = solve8PuzzleUtil(nextState, path + [nextState], visited)  # Chỉ thêm trạng thái tiếp theo
                if result:
                    return result
                visited.remove(stateTuple)
        return None
    
    # Bắt đầu tìm kiếm
    visited = set()
    visited.add(tuple(tuple(row) for row in startState))
    return solve8PuzzleUtil(startState, [], visited)