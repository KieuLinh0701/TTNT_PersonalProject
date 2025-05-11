""" 
THUẬT TOÁN TÌM KIẾM QUAY LUI
(Back Tracking)

Ý tưởng: 
❑ Dựa trên giải thuật tìm kiếm theo chiều sâu (depth-first search)
❑ Mỗi lần gán, chỉ làm việc (gán giá trị) cho một biến
❑ (Tìm kiếm bằng kiểm thử: mỗi lần gán xác định các giá trị cho tất
cả các biến)
"""

def solve8PuzzleBacktracking(startState, goalState):
    """
    Giải bài toán 8-puzzle bằng thuật toán quay lui.

    Args:
        startState: Trạng thái bắt đầu của trò chơi.
        goalState: Trạng thái đích của trò chơi.

    Returns:
        Một danh sách các trạng thái dẫn từ trạng thái bắt đầu đến trạng thái đích,
        hoặc None nếu không tìm thấy giải pháp.
    """

    def findEmptyTilePosition(state):
        """
        Tìm vị trí (hàng, cột) của ô trống (0) trong trạng thái bàn cờ.

        Args:
            state: Trạng thái bàn cờ.

        Returns:
            Một tuple (hàng, cột) là vị trí của ô trống, hoặc None nếu không tìm thấy.
        """
        for row in range(3):
            for col in range(3):
                if state[row][col] == 0:
                    return row, col
        return None

    def isGoalState(state):
        """
        Kiểm tra xem trạng thái hiện tại có phải là trạng thái đích không.

        Args:
            state: Trạng thái bàn cờ hiện tại.

        Returns:
            True nếu là trạng thái đích, False nếu không.
        """
        return state == goalState

    def getNextPossibleStates(state):
        """
        Tạo ra các trạng thái bàn cờ có thể từ trạng thái hiện tại bằng cách
        di chuyển ô trống lên, xuống, trái hoặc phải.

        Args:
            state: Trạng thái bàn cờ hiện tại.

        Returns:
            Một danh sách các trạng thái bàn cờ mới.
        """
        nextPossibleStates = []
        emptyRow, emptyCol = findEmptyTilePosition(state)
        if emptyRow is None:
            return []  # Không tìm thấy ô trống, không có trạng thái kế tiếp

        # Các dịch chuyển có thể: (deltaRow, deltaCol)
        possibleMoves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for deltaRow, deltaCol in possibleMoves:
            newRow, newCol = emptyRow + deltaRow, emptyCol + deltaCol
            if 0 <= newRow < 3 and 0 <= newCol < 3:  # Kiểm tra xem có nằm trong bàn cờ không
                newState = [list(row) for row in state]  # Tạo bản sao
                # Hoán đổi các ô
                newState[emptyRow][emptyCol], newState[newRow][newCol] = \
                    newState[newRow][newCol], newState[emptyRow][emptyCol]
                nextPossibleStates.append(newState)
        return nextPossibleStates

    def solve8PuzzleUtil(currentState, path):
        """
        Hàm đệ quy để tìm giải pháp cho bài toán 8-puzzle.

        Args:
            currentState: Trạng thái bàn cờ hiện tại.
            path: Danh sách các trạng thái đã đi qua để đến trạng thái hiện tại.

        Returns:
            Một danh sách các trạng thái dẫn từ trạng thái bắt đầu đến trạng thái đích,
            hoặc None nếu không tìm thấy giải pháp.
        """
        if isGoalState(currentState):
            return path + [currentState]  # Thêm trạng thái đích vào đường đi và trả về

        nextPossibleStates = getNextPossibleStates(currentState)
        for nextState in nextPossibleStates:
            # Kiểm tra xem trạng thái kế tiếp có lặp lại không để tránh vòng lặp
            if nextState not in path:
                newPath = path + [currentState]  # Tạo đường đi mới
                result = solve8PuzzleUtil(nextState, newPath)
                if result:
                    return result  # Nếu tìm thấy giải pháp, trả về
        return None  # Không tìm thấy giải pháp từ trạng thái hiện tại

    # Bắt đầu tìm kiếm từ trạng thái bắt đầu
    result = solve8PuzzleUtil(startState, [])
    if result:
        return result
    else:
        return None

# Ví dụ sử dụng
startState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goalState = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]

path = solve8PuzzleBacktracking(startState, goalState)
if path:
    print("Tìm thấy giải pháp:")
    for i, state in enumerate(path):
        print(f"Bước {i}:")
        for row in state:
            print(row)
else:
    print("Không tìm thấy giải pháp.")