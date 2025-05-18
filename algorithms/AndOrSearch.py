def AndOrSearch(state, goal, isAND=False, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    # Biểu diễn trạng thái để kiểm tra trạng thái đã thăm
    stateTuple = tuple(tuple(row) for row in state)
    if stateTuple in visited:
        return None

    # Đánh dấu trạng thái đã thăm
    visited.add(stateTuple)

    # Kiểm tra trạng thái đích
    if state == goal:
        return path  # Trả về path mà không thêm state (start) nữa

    # Sinh ra các hành động khả thi
    actions = getActions(state)

    if not isAND:  # Nút OR: Một hành động thành công là đủ
        for action in actions:
            resultState = applyAction(state, action)
            # Sửa chỗ gọi hàm ở đây:
            subplan = AndOrSearch(resultState, goal, True, path + [resultState], visited)  # Thêm resultState vào path
            if subplan:  # Nếu một hành động thành công, trả về kế hoạch
                return subplan

    else:  # Nút AND: Tất cả trạng thái con phải thành công
        allSubplans = []
        for action in actions:
            resultState = applyAction(state, action)
            # Sửa chỗ gọi hàm ở đây:
            subplan = AndOrSearch(resultState, goal, False, path + [resultState], visited)  # Thêm resultState vào path
            if subplan is None:  # Nếu một trạng thái con thất bại
                return None
            allSubplans.append(subplan)

        # Nếu tất cả trạng thái con đều thành công
        return path + [state] + [item for subplan in allSubplans for item in subplan]

    # Không tìm thấy giải pháp
    return None

def getActions(state):
    # Tìm vị trí của ô giá trị 0
    zeroX, zeroY = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)

    # Xác định các hành động hợp lệ
    actions = []
    if zeroX > 0: actions.append("up")   
    if zeroX < 2: actions.append("down") 
    if zeroY > 0: actions.append("left")  
    if zeroY < 2: actions.append("right") 

    return actions

def applyAction(state, action):
    # Tìm vị trí của ô giá trị 0
    zeroX, zeroY = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)

    # Tạo trạng thái mới
    newState = [row[:] for row in state]
    if action == "up" and zeroX > 0:
        newState[zeroX][zeroY], newState[zeroX - 1][zeroY] = newState[zeroX - 1][zeroY], newState[zeroX][zeroY]
    elif action == "down" and zeroX < 2:
        newState[zeroX][zeroY], newState[zeroX + 1][zeroY] = newState[zeroX + 1][zeroY], newState[zeroX][zeroY]
    elif action == "left" and zeroY > 0:
        newState[zeroX][zeroY], newState[zeroX][zeroY - 1] = newState[zeroX][zeroY - 1], newState[zeroX][zeroY]
    elif action == "right" and zeroY < 2:
        newState[zeroX][zeroY], newState[zeroX][zeroY + 1] = newState[zeroX][zeroY + 1], newState[zeroX][zeroY]

    return newState