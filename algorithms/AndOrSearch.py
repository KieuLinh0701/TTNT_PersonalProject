def AndOrSearch(state, goal, path=None, visited=None):
    if path is None:
        path = [state]  # Khởi tạo đường đi với trạng thái đầu tiên
    if visited is None:
        visited = set()  # Khởi tạo tập hợp lưu trữ các trạng thái đã thăm

    # Chuyển trạng thái hiện tại thành dạng tuple để lưu vào visited (dùng cho hash)
    state_tuple = tuple(tuple(row) for row in state)

    # Nếu trạng thái đã được thăm, bỏ qua
    if state_tuple in visited:
        return None

    # Đánh dấu trạng thái hiện tại là đã thăm
    visited.add(state_tuple)

    # Nếu đạt mục tiêu, trả về đường đi
    if state == goal:
        return path

    # Kiểm tra trạng thái không khả thi
    if isDeadEnd(state):
        return None

    actions = getActions(state)  # Lấy danh sách hành động có thể thực hiện
    for action in actions:
        result_state = applyAction(state, action)

        # Đệ quy với trạng thái mới, cập nhật đường đi và visited
        subplan = AndOrSearch(result_state, goal, path + [result_state], visited)

        if subplan is not None:
            return subplan  # Trả về kế hoạch đầu tiên tìm được

    # Nếu không tìm được kế hoạch khả thi
    return None

def isDeadEnd(state):
    # Giả sử trạng thái không có nút bế tắc (cần định nghĩa cụ thể nếu có)
    return False

def getActions(state):
    # Tìm vị trí của ô trống (giá trị 0)
    zeroX, zeroY = next(
        (i, j) for i in range(3) for j in range(3) if state[i][j] == 0
    )

    # Xác định các hành động hợp lệ
    actions = []
    if zeroX > 0: actions.append("up")    # Di chuyển lên
    if zeroX < 2: actions.append("down")  # Di chuyển xuống
    if zeroY > 0: actions.append("left")  # Di chuyển trái
    if zeroY < 2: actions.append("right") # Di chuyển phải

    return actions


def applyAction(state, action):
    import copy
    # Tìm vị trí của ô trống (giá trị 0)
    zeroX, zeroY = next(
        (i, j) for i in range(3) for j in range(3) if state[i][j] == 0
    )

    # Tạo trạng thái mới dựa trên hành động
    newState = copy.deepcopy(state)
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