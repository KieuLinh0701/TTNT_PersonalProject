def beliefState(state, goal):
    # Hàm tính toán khoảng cách Manhattan giữa trạng thái hiện tại và đích
    def heuristic(state, goal):
        flatGoal = [] # Làm phẳng trạng thái đích thành một danh sách 1 chiều
        for row in goal:
            for num in row:
                flatGoal.append(num)  

        # Kiểm tra xem các giá trị trong state có xuất hiện trong goal không
        for row in state:
            for val in row:
                if val != 0 and val not in flatGoal:  # Ô trống (0) không cần kiểm tra
                    raise ValueError(f"Giá trị {val} không tồn tại trong trạng thái đích (goal).")

        # Tính toán tổng khoảng cách Manhattan
        distance = 0
        for i in range(len(state)):  
            for j in range(len(state[i])):  
                val = state[i][j]  # Giá trị của ô tại vị trí (i, j)
                
                if val != 0:  # Không tính khoảng cách cho ô giá trị 0
                    # Tìm vị trí đích của giá trị val trong goal
                    for gi in range(len(goal)): 
                        for gj in range(len(goal[gi])):  
                            if goal[gi][gj] == val:  
                                gi, gj = gi, gj  
                                break
                    # Cộng khoảng cách Manhattan vào tổng
                    distance += abs(i - gi) + abs(j - gj)

        # Trả về tổng khoảng cách Manhattan
        return distance

    # Gọi hàm heuristic để tính toán và trả về kết quả
    return heuristic(state, goal)