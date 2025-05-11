def beliefState(state, goal):
    """
    Hàm tính toán môi trường niềm tin cho trạng thái hiện tại.
    Ở đây, môi trường niềm tin là khoảng cách Manhattan.
    """
    def heuristic(state, goal):
        """
        Hàm heuristic tính khoảng cách Manhattan giữa trạng thái hiện tại và mục tiêu.
        """
        # Làm phẳng goal
        flat_goal = [num for row in goal for num in row]  # Flatten the goal

        # Kiểm tra giá trị hợp lệ
        for row in state:
            for val in row:
                if val != 0 and val not in flat_goal:
                    raise ValueError(f"Giá trị {val} không tồn tại trong trạng thái mục tiêu (goal).")

        distance = 0
        for i, row in enumerate(state):
            for j, val in enumerate(row):
                if val != 0:  # Không tính khoảng cách cho ô trống (0)
                    # Tìm vị trí mục tiêu của giá trị val
                    gi, gj = divmod(flat_goal.index(val), len(state))  # Vị trí của val trong goal
                    distance += abs(i - gi) + abs(j - gj)
        return distance

    return heuristic(state, goal)