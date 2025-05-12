import copy

def AndOrSearch(state, goal, path=None, visited=None):
    if path is None:
        path = []  # Lưu đường đi với trạng thái đầu tiên
    if visited is None:
        visited = set()  # Lưu các trạng thái đã thăm

    # Chuyển trạng thái hiện tại thành dạng tuple để lưu vào visited (dùng cho hash)
    stateTuple = tuple(tuple(row) for row in state)

    # Nếu trạng thái đã được thăm, bỏ qua
    if stateTuple in visited:
        return None

    # Đánh dấu trạng thái hiện tại là đã thăm
    visited.add(stateTuple)

    # Kiểm tra xem có phải trạng thái đích chưa, đúng thì trả về đường đi
    if state == goal:
        return path + [state]

    # Kiểm tra trạng thái không khả thi
    if isDeadEnd(state):
        return None

    # Sinh ra các hành động khả thi
    actions = getActions(state)
    for action in actions:
        resultState = applyAction(state, action)

        # Đệ quy với trạng thái mới, cập nhật đường đi và visited
        subplan = AndOrSearch(resultState, goal, path + [state], visited)

        if subplan is not None:
            return subplan  # Trả về kế hoạch đầu tiên tìm được

    # Nếu không tìm được kế hoạch khả thi
    return None

def isDeadEnd(state):
    # Giả sử trạng thái không có nút bế tắc (cần định nghĩa cụ thể nếu có)
    return False

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
        # Di chuyển ô trống lên
        newState[zeroX][zeroY], newState[zeroX - 1][zeroY] = newState[zeroX - 1][zeroY], newState[zeroX][zeroY]
    elif action == "down" and zeroX < 2:
        # Di chuyển ô trống xuống
        newState[zeroX][zeroY], newState[zeroX + 1][zeroY] = newState[zeroX + 1][zeroY], newState[zeroX][zeroY]
    elif action == "left" and zeroY > 0:
        # Di chuyển ô trống sang trái
        newState[zeroX][zeroY], newState[zeroX][zeroY - 1] = newState[zeroX][zeroY - 1], newState[zeroX][zeroY]
    elif action == "right" and zeroY < 2:
        # Di chuyển ô trống sang phải
        newState[zeroX][zeroY], newState[zeroX][zeroY + 1] = newState[zeroX][zeroY + 1], newState[zeroX][zeroY]

    return newState